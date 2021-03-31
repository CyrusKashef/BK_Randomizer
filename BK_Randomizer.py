'''
Created on Mar 1, 2021

@author: Cyrus
'''

###########################################################################
################################# IMPORTS #################################
###########################################################################

import mmap
import random
import os
import shutil
import tkinter.filedialog
import tkinter as tk
import logging
from logging.handlers import RotatingFileHandler

#####################################################################################
##################################### VARIABLES #####################################
#####################################################################################

tmp_folder = "EPPIIISA/"

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.DEBUG)
FORMAT = '[%(levelname)s] %(asctime)-15s - %(funcName)s: %(message)s'
# USER LOGGER
handler = RotatingFileHandler(os.getcwd() + "\Randomizer_Log_File.log", maxBytes=(10*1024), backupCount=0)
logger.addHandler(handler)
# DEV LOGGER
logging.basicConfig(format=FORMAT)

default_options = {
    "Rom": os.getcwd(),
    "Non-Flag": "2",
    "Flagged": "1",
    "Struct": "2",
    "Enemies": "3",
    }

#############################################################################################
####################################### SETUP ID LIST #######################################
#############################################################################################

setup_ids = {
    # Setup Location
        # Setup Address
        # Header -> GEDecompressor decompressed file's compressed characters that are different from the default compressed header
        # Footer -> GEDecompressor decompressed file's compressed characters that are different from the default compressed footer
        # Lead -> Compressed file's original header (grab first 10 hex from rom)
        # Tail -> Compressed file's original footer (grab from rom)
    "Spiral Mountain": [
        ("0x9780", # Main Area - 4C4680
            ["1F", "8B", "08", "08", "C0", "A9", "47", "60", "00", "0B", "34", "43", "34", "36", "38", "30", "2D", "41", "63", "74", "75", "61", "6C", "5F", "44", "65", "63", "6F", "6D", "70", "72", "65", "73", "73", "65", "64", "2E", "62", "69", "6E", "00"],
            ["F5", "0F", "4E", "05", "A0", "26", "00", "00"],
            ['11', '72', '00', '00', '26', 'A0'],
            ['AA', 'AA', 'AA'],
            ),
        ],
    "Mumbo's Mountain": [
        ("0x9788", # Main Area - 4C5A30
            ["1F", "8B", "08", "08", "C0", "A9", "47", "60", "00", "0B", "34", "43", "35", "41", "33", "30", "2D", "41", "63", "74", "75", "61", "6C", "5F", "44", "65", "63", "6F", "6D", "70", "72", "65", "73", "73", "65", "64", "2E", "62", "69", "6E", "00"],
            ["07", "D0", "9F", "9C", "10", "39", "00", "00"],
            ["11", "72", "00", "00", "39", "10"],
            []),
        ("0x97D8", # Ticker's Tower - 4CCD40
            ["1F", "8B", "08", "08", "8E", "D1", "50", "60", "00", "0B", "34", "43", "43", "44", "34", "30", "2D", "41", "63", "74", "75", "61", "6C", "5F", "44", "65", "63", "6F", "6D", "70", "72", "65", "73", "73", "65", "64", "2E", "62", "69", "6E", "00"],
            ["09", "CE", "33", "CD", "97", "07", "00", "00"],
            ["11", "72", "00", "00", "07", "97"],
            ["AA", "AA", "AA", "AA"]
            ),
        ("0x97E8", # Mumbo's Skull - 4CF158
            ["1F", "8B", "08", "08", "8E", "D1", "50", "60", "00", "0B", "34", "43", "46", "31", "35", "38", "2D", "41", "63", "74", "75", "61", "6C", "5F", "44", "65", "63", "6F", "6D", "70", "72", "65", "73", "73", "65", "64", "2E", "62", "69", "6E", "00"],
            ["57", "06", "86", "0A", "1B", "04", "00", "00"],
            ["11", "72", "00", "00", "04", "1B"],
            ["AA", "AA", "AA", "AA"]
            ),
        ],
####################################################
#     "Mad Monster Mansion": [
#         ("0x9850", # Main Area - 4D44D8
#         ["1F", "8B", "08", "08", "8F", "D1", "50", "60", "00", "0B", "34", "44", "34", "34", "44", "38", "2D", "41", "63", "74", "75", "61", "6C", "5F", "44", "65", "63", "6F", "6D", "70", "72", "65", "73", "73", "65", "64", "2E", "62", "69", "6E", "00"],
#         ["A9", "19", "C5", "C7", "51", "45", "00", "00"],
#         ["11", "72", "00", "00", "45", "51"],
#         ["AA", "AA", "AA", "AA"]
#         ),
#         ],
    }

###################################################################################
##################################### ID LIST #####################################
###################################################################################

jiggy_flag_list = [
    1, 2, 5, 6, # Mumbo's Mountain
    ]

obj_flagged_id_list = [
    "002D", # Mumbo Token
    "0046", # Jiggy
    "0047", # Empty Honeycomb
    ]

obj_no_flag_id_list = [
    "0029", # Orange
    "0049", # 1-Up
    "005E", # Yellow Jinjo
    "005F", # Orange Jinjo
    "0060", # Blue Jinjo
    "0061", # Purple Jinjo
    "0062", # Green Jinjo
    # Sometimes Structs
#     "0052", # Egg
#     "0129", # Red Feather
#     "0370", # Gold Feather
    ]

collectable_struct_id_list = [
    "164000B4", # Note B4
    "164000B5", # Note B5
    "164000B6", # Note B6
    "164000B7", # Note B7
    "165000A0", # Blue Egg A0
    "165000A2", # Blue Egg A2
#     "00E000DC", # Red Feather DC
#     "00E000DD", # Red Feather DD
#     "00E000DE", # Red Feather DE
#     "15F000DF", # Gold Feather DF
#     "15F000DC", # Gold Feather DC
#     "15F000DE", # Gold Feather DE
    ]

ground_enemy_id_list = [
    "0004", # Bull
    "0005", # Ticker
    "0006", # Grublin
    "0012", # Beehive
    "0067", # Grublin
    "00C7", # RIP Tombstone
    #"0120", # Slappa (Purple Slappa)
    "034E", # Skeleton
    "034F", # Mummy
    "0350", # Sea Grublin
    #"0367", # Gruntling
    #"0375", # Grublin Hood
    "037D", # Ice Cube
    #"03BF", # Gruntling 2
    #"03C0", # Gruntling 3
    ]

flying_enemy_id_list = [
    "00CA", # Tee-Hee
    "0134", # Dragon Fly
    #"036D", # Coliwobble
    "0380", # Beetle
    ]

wall_enemy_id_list = [
    "013B", # Floatsam
    "01CC", # Chompa
    "029F", # Big Clucker
    ]

jumping_enemy_id_list = [
#     "0069", # Yum Yum
#     "0133", # Ribbit
#     "030D", # TNT Box Part 2
    "036E", # Bawl
    "036F", # Topper
    ]

non_collect_struct_id_list = [
    ]

#####################################################################################
##################################### FUNCTIONS #####################################
#####################################################################################

######################
### MISC FUNCTIONS ###
######################

def leading_zeros(num_string, num_of_digits):
    if(num_of_digits <= len(num_string)):
        return num_string
    for add_zero in range(num_of_digits - len(num_string)):
        num_string = "0" + num_string
    return num_string

##############
### SET UP ###
##############

def split_dir_rom(rom_dir):
    '''Separates the directory to the rom with the name of the rom'''
    logger.info("Split Dir Rom")
    if("\\" in rom_dir):
        rom_file = rom_dir.split("\\")[-1]
    elif("/" in rom_dir):
        rom_file = rom_dir.split("/")[-1]
    else:
        logger.info("File Directory Unfamiliar Format?")
        logger.warning("File Directory Unfamiliar Format?")
    file_dir = rom_dir.replace(rom_file, "")
    #logger.debug(file_dir, rom_file)
    return (file_dir, rom_file)

def setup_tmp_folder(file_dir):
    """Creates temporary folder that'll be used to store bin files and the randomized ROM."""
    logger.info("Set Up Temporary Folder")
    if(not os.path.isdir(file_dir + tmp_folder)):
        os.mkdir(file_dir + tmp_folder)
    else:
        for filename in os.listdir(file_dir + tmp_folder):
            file_path = os.path.join(file_dir + tmp_folder, filename)
            try:
                if(os.path.isfile(file_path) or os.path.islink(file_path)):
                    os.unlink(file_path)
                elif(os.path.isdir(file_path)):
                    shutil.rmtree(file_path)
            except Exception as e:
                logger.error('Failed to delete %s. Reason: %s' % (file_path, e))

def seed(seed_val=None):
    """If seed was not provided, generates a seed value."""
    logger.info("Generate Seed")
    if((seed_val == None) or (seed_val == "")):
        seed_val = random.randint(10000000, 19940303)
    logger.debug("Seed: " + str(seed_val))
    return seed_val

def make_copy_of_rom(seed_val, file_dir, rom_file):
    """Creates a copy of the rom that will be used for randomization"""
    logger.info("Make Copy Of Rom")
    randomized_rom_file = file_dir + tmp_folder + "Banjo-Kazooie_Randomized_Seed_" + str(seed_val) + ".z64"
    shutil.copyfile(file_dir + rom_file, randomized_rom_file)

########################
### Parameter Window ###
########################

def verify_rom_and_gzip(rom_dir):
    '''Checks if ROM file ends in .z64 and is located in the folder with GZIP.EXE'''
    if(rom_dir == ""):
        error_msg = "Please provide the directory to the ROM."
        logger.error(error_msg)
        error_window(error_msg)
        return False
    (file_dir, rom_file) = split_dir_rom(rom_dir)
    rom_ext = rom_file.split(".")[-1]
    if(rom_ext != "z64"):
        error_msg = "Rom Extention is not allowed: " + rom_ext
        logger.error(error_msg)
        error_window(error_msg)
        return False
    gzip_location = file_dir + "GZIP.EXE"
    if(not os.path.exists(gzip_location)):
        error_msg = "GZIP.EXE Is Not In Folder"
        logger.error(error_msg)
        error_window(error_msg)
        return False
    return True

def verify_seed_val(seed_val):
    '''Verifies the seed value is either blank or only consists of digits'''
    if((not seed_val.isdigit()) and (seed_val != "")):
        error_msg = "Seed value is not allowed: '" + seed_val + "'"
        logger.error(error_msg)
        error_window(error_msg)
        return False
    return True

def error_window(error_msg):
    '''Brings up a GUI that displays an error message'''
    window = tk.Tk()
    window.geometry('350x50')
    # Title? Idk if this is even needed
    window.winfo_toplevel().title("Banjo Kazooie Randomizer")
    error_label = tk.Label(window, text=error_msg)
    error_label.config(anchor='center')
    error_label.pack()
    ok_btn = tk.Button(window, text='Doh!', command=window.destroy)
    ok_btn.config(anchor='center')
    ok_btn.pack()
    window.mainloop()

def parameter_gui():
    '''Creates a GUI where users give the directory of the ROM file, select options for the randomization, and optionally provide a seed value'''
    def verify_parameters():
        '''Runs verification functions for the ROM and the seed values given'''
        rom_gzip_bool = verify_rom_and_gzip(rom_file_entry.get())
        seed_bool = verify_seed_val(seed_var.get())
        if(rom_gzip_bool and seed_bool):
            window.destroy()
    
    def UploadAction():
        '''Opens a browser to select the ROM file ending in .z64'''
        cwd = os.getcwd()
        filename = tkinter.filedialog.askopenfilename(initialdir=cwd, title="Select A File", filetype =(("Rom Files","*.z64"),("all files","*.*")) )
        rom_file_entry.set(filename)
    
    window = tk.Tk()
    window.geometry('525x250')
    # Title? Idk if this is even needed
    window.winfo_toplevel().title("Banjo Kazooie Randomizer")
    # Select Rom File
    select_rom_button = tk.Button(window, text='Select Rom', command=UploadAction)
    select_rom_button.grid(row=0, column=0)
    rom_file_entry = tk.StringVar()
    rom_file_entry.set(default_options["Rom"])
    entry = tk.Entry(textvariable=rom_file_entry, state='readonly', width=50)
    entry.grid(row=1, column=0)
    # Seed Label And Entry
    seed_label = tk.Label(window, text='Would you like to insert a seed?')
    seed_label.grid(row=2, column=0)
    seed_var = tk.StringVar()
    seed_var.set("")
    seed_entry = tk.Entry(window, textvariable=seed_var)
    seed_entry.grid(row=3, column=0)
    # Select Rom
    # Radio Buttons For Non-Flag Object Options
    nf_obj_label = tk.Label(window, text='How Would You Like The Non-Flag Objects Randomized?')
    nf_obj_label.grid(row=4, column=0)
    nf_obj_var = tk.StringVar(window, default_options["Non-Flag"])
    nf_obj_options = {
        "None": "1",
        "Within World": "2",
        #"Completely": "3"
        }
    for (text, value) in nf_obj_options.items():
        nf_obj_select = tk.Radiobutton(window, text=text, variable=nf_obj_var, value=value, indicator=0)
        nf_obj_select.grid(row=4, column=value)
    # Radio Buttons For Flagged Objects Options
    f_obj_label = tk.Label(window, text='How Would You Like The Flagged Objects Randomized?')
    f_obj_label.grid(row=5, column=0)
    f_obj_var = tk.StringVar(window, default_options["Flagged"])
    f_obj_options = {
        "None": "1",
        "Within World": "2",
        #"Completely": "3"
        }
    for (text, value) in f_obj_options.items():
        f_obj_select = tk.Radiobutton(window, text=text, variable=f_obj_var, value=value, indicator=0)
        f_obj_select.grid(row=5, column=value)
    # Radio Buttons For Struct Options
    struct_label = tk.Label(window, text='How Would You Like The Notes/Eggs/Feathers Randomized?')
    struct_label.grid(row=6, column=0)
    struct_var = tk.StringVar(window, default_options["Struct"])
    struct_options = {
        "None": "1",
        "Within World": "2",
        #"Completely": "3"
        }
    for (text, value) in struct_options.items():
        struct_select = tk.Radiobutton(window, text=text, variable=struct_var, value=value, indicator=0)
        struct_select.grid(row=6, column=value)
    # Radio Buttons For Enemy Options
    enemy_label = tk.Label(window, text='How Would You Like The Enemies Randomized?')
    enemy_label.grid(row=7, column=0)
    enemy_var = tk.StringVar(window, default_options["Enemies"])
    enemy_options = {
        "None": "1",
        "Within World": "2",
        "Completely": "3"
        }
    for (text, value) in enemy_options.items():
        enemy_select = tk.Radiobutton(window, text=text, variable=enemy_var, value=value, indicator=0)
        enemy_select.grid(row=7, column=value)
    # Button To Start Randomization
    start_label = tk.Label(window, text='Once finished, click submit!')
    start_label.grid(row=8, column=0)
    sub_btn = tk.Button(window, text='Submit', command=verify_parameters)
    sub_btn.grid(row=9, column=0)
    
    window.mainloop()
    try:
        seed_val = int(seed_var.get())
    except ValueError:
        logger.debug("No Seed Value Was Given")
        seed_val = ""
    return (rom_file_entry.get(), seed_val, str(nf_obj_var.get()), str(f_obj_var.get()), str(struct_var.get()), str(enemy_var.get()))

#####################
### Decompression ###
#####################

def get_file_bytes(file_dir, read_file):
    """Reads the contents of a hex file without using mmap"""
    logger.info("Get File Bytes")
    with open(file_dir + read_file, "rb") as file:
        file_bytes = file.read()
    return file_bytes

def get_address_endpoints(file_bytes, addr):
    """Goes to address (found in Banjo's Backpack) and address 8 bytes after to find the start and end of a setup file"""
    logger.info("Get Address Endpoints")
    byte_list = []
    for byte_num in range(16):
        byte_val = str(hex(file_bytes[int(addr, 16) + byte_num])[2:])
        if(len(str(byte_val)) < 2):
            byte_val = "0" + byte_val
        byte_list.append(byte_val)
    address1 = int("0x" + byte_list[0] + byte_list[1] + byte_list[2] + byte_list[3], 16) + int("0x10CD0", 16)
    address2 = int("0x" + byte_list[8] + byte_list[9] + byte_list[10] + byte_list[11], 16) + int("0x10CD0", 16)
    logger.debug("Address Start: " + str(hex(address1)))
    logger.debug("Address End: " + str(hex(address2)))
    return (address1, address2)

def verify_original_header(file_bytes, address):
    """Verifies the start of an address by looking for 11 72 00 00"""
    logger.info("Verify Original Header")
    if((file_bytes[address] != 17) or (file_bytes[address+1] != 114) or (file_bytes[address+2] != 0) or (file_bytes[address+3] != 0)):
        logger.error("Does Not Start With 11 72 00 00")
        error_window("Error During Randomization")
        exit(0)

def decompress_file(file_dir, compressed_file):
    """Decompresses the hex file that was extracted from the main ROM file"""
    logger.info("Decompress File")
    cmd = file_dir + "GZIP.EXE -dc " + file_dir + tmp_folder + compressed_file.upper() + "-Compressed.bin > " + file_dir + tmp_folder + compressed_file.upper() + "-Decompressed.bin"
    logger.debug(cmd)
    os.system(cmd)

def decompressor(file_dir, rom_file):
    """Extracts a chunk of hex values from the main ROM file into a new file and prepares the new file for decompression by providing the correct header and footer"""
    logger.info("Decompressor")
    # Get File Bytes
    file_bytes = get_file_bytes(file_dir, rom_file)
    address_dict = {}
    address_translator = {}
    for location_name in setup_ids:
        address_list = []
        for (addr, header, footer, lead, tail) in setup_ids[location_name]:
            # Get Address Endpoints
            (address1, address2) = get_address_endpoints(file_bytes, addr)
            verify_original_header(file_bytes, address1)
            # Write Compressed File
            compressed_file = str(hex(address1)[2:]).upper()
            address_translator[addr] = compressed_file
            with open(file_dir + tmp_folder + compressed_file + "-Compressed.bin", "w+b") as comp_file:
                # Write Header
                for hex_val in header:
                    comp_file.write(bytes.fromhex(hex_val))
                # Grab Middle
                for index in range(address1+6, address2-len(tail)):
                #for index in range(address1, address2-len(tail)):
                    hex_string = str(hex(file_bytes[index]))[2:]
                    if(len(hex_string) < 2):
                        hex_string = "0" + hex_string
                    comp_file.write(bytes.fromhex(hex_string))
                # Write Footer
                for hex_val in footer:
                    comp_file.write(bytes.fromhex(hex_val))
            # Decompress File
            decompress_file(file_dir, compressed_file)
            address_list.append(compressed_file)
        address_dict[location_name] = address_list
    return (address_dict, address_translator)

###################
### Compression ###
###################

def compress_file(file_dir, decompressed_file):
    """Compresses the hex file that was extracted from the main ROM file"""
    logger.info("Compress File")
    cmd = file_dir + "GZIP.EXE -c " + file_dir + tmp_folder + decompressed_file.upper() + "-Decompressed.bin > " + file_dir + tmp_folder + decompressed_file.upper() + "-New_Compressed.bin"
    logger.debug(cmd)
    os.system(cmd)

def compressor(file_dir, location_setup, decompressed_file):
    """Prepares the hex file that was extracted from the main ROM file for compression by providing the correct header and footer"""
    logger.info("Compressor")
    (addr, header, footer, lead, tail) = location_setup
    # Compress File
    compress_file(file_dir, decompressed_file)
    # Get Length Of Original Compressed File
    with open(file_dir + tmp_folder + decompressed_file + "-New_Compressed.bin", "r+b") as comp_file:
        mm_comp = mmap.mmap(comp_file.fileno(), 0)
        comp_file_len = len(mm_comp)
        header_end = ""
        for header_val in header[-4:]:
            header_end += header_val
        header_end_index = mm_comp.find(bytes.fromhex(header_end)) + 4
        with open(file_dir + tmp_folder + decompressed_file + "-Randomized_Compressed.bin", "w+b") as new_comp_file:
            for hex_val in lead:
                new_comp_file.write(bytes.fromhex(hex_val))
            for index in range(header_end_index, comp_file_len-len(footer)):
                hex_string = str(hex(mm_comp[index]))[2:]
                if(len(hex_string) < 2):
                    hex_string = "0" + hex_string
                new_comp_file.write(bytes.fromhex(hex_string))
            for hex_val in tail:
                new_comp_file.write(bytes.fromhex(hex_val))

def insert_files_into_rom(seed_val, file_dir, file_address):
    """Replaces the values of the old ROM with the randomized values"""
    logger.info("Insert Files Into Rom")
    with open(file_dir + tmp_folder + file_address + "-Randomized_Compressed.bin", "rb") as setup_bin:
        setup_content = setup_bin.read()
    with open(file_dir + tmp_folder + "Banjo-Kazooie_Randomized_Seed_" + str(seed_val) + ".z64", "r+b") as rand_rom:
        setup_count = 0
        for index in range(int(file_address, 16), int(file_address, 16) + len(setup_content)):
            mm = mmap.mmap(rand_rom.fileno(), 0)
            mm[index] = setup_content[setup_count]
            setup_count += 1

def compress_files(seed_val, file_dir, address_translator):
    """Main function to compress the randomized, decompressed file"""
    logger.info("Compress Files")
    for location in setup_ids:
        for location_setup in setup_ids[location]:
            file_address = address_translator[location_setup[0]]
            compressor(file_dir, location_setup, file_address)
            insert_files_into_rom(seed_val, file_dir, file_address)

######################
### GET INDEX LIST ###
######################

def get_jiggy_flags(mm, lead, tail, start_val, end_val):
    '''For Jiggy Flags specifically, grabs a list of flag indices from pre-determined list of Jiggies'''
    flag_dict = []
    for mid_val in range(start_val, end_val): # Middle Value
        if(mid_val in jiggy_flag_list):
            hex_bytes = str(hex(mid_val))[2:]
            hex_bytes = leading_zeros(hex_bytes, 4)
            hex_string = lead + hex_bytes + "0000000000" + tail
            flag_index = mm.find(bytes.fromhex(hex_string))
            if(flag_index != -1):
                flag_dict.append(flag_index - 1)
            else:
    #             logger.warning("Match Not Found For " + str(hex_string))
                pass
    return flag_dict

def get_flags(mm, lead, tail, start_val, end_val):
    '''Grabs a list of flags indices'''
    flag_dict = []
    for mid_val in range(start_val, end_val): # Middle Value
        hex_bytes = str(hex(mid_val))[2:]
        hex_bytes = leading_zeros(hex_bytes, 4)
        hex_string = lead + hex_bytes + "0000000000" + tail
        flag_index = mm.find(bytes.fromhex(hex_string))
        if(flag_index != -1):
            flag_dict.append(flag_index - 1)
        else:
#             logger.warning("Match Not Found For " + str(hex_string))
            pass
    return flag_dict

def get_flag_index_list(mm):
    '''Locates the flags by index in the decompressed file'''
    jiggy_list = []
    empty_honeycomb_list = []
    mumbo_token_list = []
    for lead in ['14', '94']:
        logger.info("Jiggy Flags")
        jiggy_list_part = get_jiggy_flags(mm, lead, "00", 1, 80)
        for item in jiggy_list_part:
            jiggy_list.append(item)
        logger.info("Empty Honeycomb Flags")
        empty_honeycomb_list_part = get_flags(mm, lead, "64", 100, 122)
        for item in empty_honeycomb_list_part:
            empty_honeycomb_list.append(item)
        logger.info("Mumbo Token Flags")
        mumbo_token_list_part = get_flags(mm, lead, "64", 200, 315)
        for item in mumbo_token_list_part:
            mumbo_token_list.append(item)
    return (jiggy_list, empty_honeycomb_list, mumbo_token_list)

def get_object_index_list(mm, object_id, start=0):
    '''Locates the flagged objects by index in the decompressed file'''
    logger.info("Get Flagged Object Index List")
    object_index = mm.find(bytes.fromhex("190C" + object_id), start)
    if(object_index == -1):
        return []
    else:
        new_start = int(object_index) + 1
        object_list = get_object_index_list(mm, object_id, start=new_start)
    object_list.append(object_index)
    return object_list

def get_struct_index_list(mm, struct_id, start=0):
    '''Locates the structs by index in the decompressed file'''
    logger.info("Get Struct Index List")
    struct_index = mm.find(bytes.fromhex(struct_id), start)
    if(struct_index == -1):
        return []
    else:
        new_start = int(struct_index) + 1
        struct_list = get_struct_index_list(mm, struct_id, start=new_start)
    struct_list.append(struct_index)
    return struct_list

def get_enemy_index_list(mm, enemy_id, start=0):
    '''Locates the enemies by index in the decompressed file'''
    logger.info("Get Enemy Index List")
    enemy_index = mm.find(bytes.fromhex("190C" + enemy_id), start)
    if(enemy_index == -1):
        return []
    else:
        new_start = int(enemy_index) + 1
        enemy_list = get_enemy_index_list(mm, enemy_id, start=new_start)
    enemy_list.append(enemy_index)
    return enemy_list

########################
### OBTAIN LIST INFO ###
########################

def obtain_flag_list_info(mm, flag_index_list):
    '''Gathers all of the information about the flag into a list'''
    logger.info("Obtain Flag List Info")
    #X-Loc  Y-Loc  Z-Loc  script   ID     --   --   --   --   rot.  size  --    --
    #0E48   0153   1998   190C     0049   00   00   00   00   00    64    0C    10
    flag_location_list = []
    for flag_index in flag_index_list:
        flag_dict = {}
        flag_dict["Index"] = flag_index
        hex_x1 = leading_zeros(str(hex(mm[flag_index - 6]))[2:].upper(), 2)
        hex_x2 = leading_zeros(str(hex(mm[flag_index - 5]))[2:].upper(), 2)
        flag_dict["Hex_X"] = hex_x1 + hex_x2
        hex_y1 = leading_zeros(str(hex(mm[flag_index - 4]))[2:].upper(), 2)
        hex_y2 = leading_zeros(str(hex(mm[flag_index - 3]))[2:].upper(), 2)
        flag_dict["Hex_Y"] = hex_y1 + hex_y2
        hex_z1 = leading_zeros(str(hex(mm[flag_index - 2]))[2:].upper(), 2)
        hex_z2 = leading_zeros(str(hex(mm[flag_index - 1]))[2:].upper(), 2)
        flag_dict["Hex_Z"] = hex_z1 + hex_z2
        flag_dict["Script1"] = mm[flag_index]
        flag_dict["Script2"] = mm[flag_index + 1]
        flag_dict["Obj_ID1"] = mm[flag_index + 2]
        flag_dict["Obj_ID2"] = mm[flag_index + 3]
        flag_dict["IDK1"] = mm[flag_index + 4]
        flag_dict["IDK2"] = mm[flag_index + 5]
        flag_dict["IDK3"] = mm[flag_index + 6]
        flag_dict["IDK4"] = mm[flag_index + 7]
        flag_dict["Rotation"] = mm[flag_index + 8]
        flag_dict["Size"] = mm[flag_index + 9]
        flag_dict["IDK5"] = mm[flag_index + 10]
        flag_dict["IDK6"] = mm[flag_index + 11]
        flag_location_list.append(flag_dict)
    return flag_location_list

def obtain_flagged_object_list_info(mm, obj_index_list):
    '''Gathers all of the information about the flagged object into a list'''
    logger.info("Obtain Flagged Object List Info")
    #X-Loc  Y-Loc  Z-Loc  script   ID     --   --   --   --   rot.  size  --    --
    #0E48   0153   1998   190C     0049   00   00   00   00   00    64    0C    10
    object_location_list = []
    for object_index in obj_index_list:
        object_dict = {}
        object_dict["Index"] = object_index
        hex_x1 = leading_zeros(str(hex(mm[object_index - 6]))[2:].upper(), 2)
        hex_x2 = leading_zeros(str(hex(mm[object_index - 5]))[2:].upper(), 2)
        object_dict["Hex_X"] = hex_x1 + hex_x2
        hex_y1 = leading_zeros(str(hex(mm[object_index - 4]))[2:].upper(), 2)
        hex_y2 = leading_zeros(str(hex(mm[object_index - 3]))[2:].upper(), 2)
        object_dict["Hex_Y"] = hex_y1 + hex_y2
        hex_z1 = leading_zeros(str(hex(mm[object_index - 2]))[2:].upper(), 2)
        hex_z2 = leading_zeros(str(hex(mm[object_index - 1]))[2:].upper(), 2)
        object_dict["Hex_Z"] = hex_z1 + hex_z2
        object_dict["Script1"] = mm[object_index]
        object_dict["Script2"] = mm[object_index + 1]
        object_dict["Obj_ID1"] = mm[object_index + 2]
        object_dict["Obj_ID2"] = mm[object_index + 3]
#         object_dict["Rotation"] = mm[object_index + 8]
#         object_dict["Size"] = mm[object_index + 9]
        object_location_list.append(object_dict)
    return object_location_list

def obtain_no_flag_object_list_info(mm, no_flag_obj_index_list):
    '''Gathers all of the information about the non-flag object into a list'''
    logger.info("Obtain Non-Flag Object List Info")
    #X-Loc  Y-Loc  Z-Loc  script   ID     --   --   --   --   rot.  size  --    --
    #0E48   0153   1998   190C     0049   00   00   00   00   00    64    0C    10
    object_location_list = []
    for object_index in no_flag_obj_index_list:
        object_dict = {}
#         object_dict["Hex_X1"] = mm[object_index - 6]
#         object_dict["Hex_X2"] = mm[object_index - 5]
#         object_dict["Hex_Y1"] = mm[object_index - 4]
#         object_dict["Hex_Y2"] = mm[object_index - 3]
#         object_dict["Hex_Z1"] = mm[object_index - 2]
#         object_dict["Hex_Z2"] = mm[object_index - 1]
        object_dict["Script1"] = mm[object_index]
        object_dict["Script2"] = mm[object_index + 1]
        object_dict["Obj_ID1"] = mm[object_index + 2]
        object_dict["Obj_ID2"] = mm[object_index + 3]
#         object_dict["Rotation"] = mm[object_index + 8]
#         object_dict["Size"] = mm[object_index + 9]
        object_location_list.append(object_dict)
    return object_location_list

def obtain_struct_list_info(mm, struct_list_index_list):
    '''Gathers all of the information about the struct into a list'''
    logger.info("Obtain Struct List Info")
    #obj id  ????  x-loc  y-loc  z-loc  size  ??
    #1640    00B6  FA12   03C4   02C2   19    80
    struct_location_list = []
    for struct_index in struct_list_index_list:
        struct_dict = {}
        struct_dict["Obj_ID1"] = mm[struct_index]
        struct_dict["Obj_ID2"] = mm[struct_index + 1]
        struct_dict["IDK1"] = mm[struct_index + 2]
        struct_dict["IDK2"] = mm[struct_index + 3]
#         struct_dict["Hex_X1"] = mm[struct_index + 4]
#         struct_dict["Hex_X2"] = mm[struct_index + 5]
#         struct_dict["Hex_Y1"] = mm[struct_index + 6]
#         struct_dict["Hex_Y2"] = mm[struct_index + 7]
#         struct_dict["Hex_Z1"] = mm[struct_index + 8]
#         struct_dict["Hex_Z2"] = mm[struct_index + 9]
#         struct_dict["Size"] = mm[struct_index + 10]
#         struct_dict["IDK3"] = mm[struct_index + 11]
        struct_location_list.append(struct_dict)
    return struct_location_list

def obtain_enemy_list_info(mm, enemy_index_list):
    '''Gathers all of the information about the enemy into a list'''
    logger.info("Obtain Enemy List Info")
    #X-Loc  Y-Loc  Z-Loc  script   ID     --   --   --   --   rot.  size  --    --
    #0E48   0153   1998   190C     0049   00   00   00   00   00    64    0C    10
    enemy_location_list = []
    for enemy_index in enemy_index_list:
        enemy_dict = {}
#         enemy_dict["Hex_X1"] = mm[enemy_index - 6]
#         enemy_dict["Hex_X2"] = mm[enemy_index - 5]
#         enemy_dict["Hex_Y1"] = mm[enemy_index - 4]
#         enemy_dict["Hex_Y2"] = mm[enemy_index - 3]
#         enemy_dict["Hex_Z1"] = mm[enemy_index - 2]
#         enemy_dict["Hex_Z2"] = mm[enemy_index - 1]
#         enemy_dict["Script1"] = mm[enemy_index]
#         enemy_dict["Script2"] = mm[enemy_index + 1]
        enemy_dict["Obj_ID1"] = mm[enemy_index + 2]
        enemy_dict["Obj_ID2"] = mm[enemy_index + 3]
#         enemy_dict["Rotation"] = mm[enemy_index + 8]
#         enemy_dict["Size"] = mm[enemy_index + 9]
        enemy_location_list.append(enemy_dict)
    return enemy_location_list

##################
### INDEX MAIN ###
##################

def create_mmap(file_dir, address):
    '''Creates an mmap that can read and write to a hex file'''
    logger.info("Create MMap")
    with open(file_dir + tmp_folder + address + "-Decompressed.bin", "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
    return mm

def generic_get_lists(mm, id_list):
    '''For each type of id list, runs the functions that grabs the list of objects and locations'''
    logger.info("Generic Get Lists")
    index_list = []
    for obj_id in id_list:
        if((id_list == obj_no_flag_id_list) or (id_list == obj_flagged_id_list)):
            object_list = get_object_index_list(mm, obj_id)
        elif(id_list == collectable_struct_id_list):
            object_list = get_struct_index_list(mm, obj_id)
        elif((id_list == ground_enemy_id_list) or
             (id_list == flying_enemy_id_list) or
             (id_list == wall_enemy_id_list) or
             (id_list == jumping_enemy_id_list)):
            object_list = get_enemy_index_list(mm, obj_id)
        else:
            logger.error("Invalid ID List")
            error_window("Error During Randomization")
            exit(0)
        for item in object_list:
            index_list.append(item)
    if(id_list == obj_no_flag_id_list):
        location_list = obtain_no_flag_object_list_info(mm, index_list)
    elif(id_list == obj_flagged_id_list):
        location_list = obtain_flagged_object_list_info(mm, index_list)
    elif(id_list == collectable_struct_id_list):
        location_list = obtain_struct_list_info(mm, index_list)
    elif((id_list == ground_enemy_id_list) or
         (id_list == flying_enemy_id_list) or
         (id_list == wall_enemy_id_list) or
         (id_list == jumping_enemy_id_list)):
        location_list = obtain_enemy_list_info(mm, index_list)
    else:
        logger.error("Invalid ID List")
        error_window("Error During Randomization")
        exit(0)
    return (index_list, location_list)

def find_closest_flag(target_hex_x, target_hex_y, target_hex_z, compiled_list):
    '''For every flagged object, tries to find the closest flag'''
    score_dict = {}
    for item_dict in compiled_list:
        suspect_index = item_dict["Index"]
        suspect_hex_x = item_dict["Hex_X"]
        suspect_hex_y = item_dict["Hex_Y"]
        suspect_hex_z = item_dict["Hex_Z"]
        x_delta = int(str(target_hex_x), 16) - int(str(suspect_hex_x), 16)
        y_delta = int(str(target_hex_y), 16) - int(str(suspect_hex_y), 16)
        z_delta = int(str(target_hex_z), 16) - int(str(suspect_hex_z), 16)
        score = abs(x_delta) + abs(y_delta) + abs(z_delta)
        score_dict[score] = suspect_index
    best_score = min(score_dict.keys())
    return score_dict[best_score]

def match_obj_and_flag(flagged_object_location_list, jiggy_flag_location_list, empty_honeycomb_flag_location_list, mumbo_token_flag_location_list):
    '''Main function for matching flagged objects with their flag'''
    logger.info("Match Object And Flag")
    compiled_list = []
    closest_flag_dict = {}
    for item_dict in jiggy_flag_location_list:
        compiled_list.append(item_dict)
    for item_dict in empty_honeycomb_flag_location_list:
        compiled_list.append(item_dict)
    for item_dict in mumbo_token_flag_location_list:
        compiled_list.append(item_dict)
    for flagged_object_dict in flagged_object_location_list:
        target_hex_x = flagged_object_dict["Hex_X"]
        target_hex_y = flagged_object_dict["Hex_Y"]
        target_hex_z = flagged_object_dict["Hex_Z"]
        closet_flag_index = find_closest_flag(target_hex_x, target_hex_y, target_hex_z, compiled_list)
        closest_flag_dict[flagged_object_dict["Index"]] = closet_flag_index
    return closest_flag_dict

def get_index_main(file_dir, address_dict, seed_val, non_flag_option, flagged_option, struct_option, enemy_option):
    '''For every location, grabs all of the non-flags, flagged, struct, and enemy indices and information, randomizes the lists, and assigns the new values'''
    logger.info("Get Index Main")
    for location in address_dict:
        address_index_dict = {}
        flagged_obj_index_dict = {}
        address_flagged_object_location_list = []
        address_no_flag_object_location_list = []
        address_struct_location_list = []
        address_ground_enemy_location_list = []
        address_flying_enemy_location_list = []
        address_wall_enemy_location_list = []
        address_jumping_enemy_location_list = []
        location_jiggy_dict = {}
        location_empty_honeycomb_dict = {}
        location_mumbo_token_dict = {}
        for address in address_dict[location]:
            address_index_dict[address] = {}
            flagged_obj_index_dict[address] = {}
            mm = create_mmap(file_dir, address)
            # Flagged Objects
            if(flagged_option != "1"):
                logger.info("Get Flagged Objects Index")
                (flagged_obj_index_list, flagged_object_location_list) = generic_get_lists(mm, obj_flagged_id_list)
                for item in flagged_object_location_list:
                    address_flagged_object_location_list.append(item)
                address_index_dict[address]["Flagged_Objects"] = flagged_obj_index_list
                logger.info("Get Flag Indices")
                (jiggy_index_list, empty_honeycomb_index_list, mumbo_token_index_list) = get_flag_index_list(mm)
                jiggy_flag_location_list = obtain_flag_list_info(mm, jiggy_index_list)
                empty_honeycomb_flag_location_list = obtain_flag_list_info(mm, empty_honeycomb_index_list)
                mumbo_token_flag_location_list = obtain_flag_list_info(mm, mumbo_token_index_list)
                flagged_obj_index_dict[address]["Closest_Flag"] = match_obj_and_flag(flagged_object_location_list, jiggy_flag_location_list, empty_honeycomb_flag_location_list, mumbo_token_flag_location_list)
                for item in jiggy_flag_location_list:
                    location_jiggy_dict[(address, item["Index"])] = item
                for item in empty_honeycomb_flag_location_list:
                    location_empty_honeycomb_dict[(address, item["Index"])] = item
                for item in mumbo_token_flag_location_list:
                    location_mumbo_token_dict[(address, item["Index"])] = item
            # No Flag Objects
            if(non_flag_option != "1"):
                logger.info("Get Non-Flag Objects Index")
                (no_flag_obj_index_list, no_flag_object_location_list) = generic_get_lists(mm, obj_no_flag_id_list)
                for item in no_flag_object_location_list:
                    address_no_flag_object_location_list.append(item)
                address_index_dict[address]["No_Flag_Objects"] = no_flag_obj_index_list
            # Structs
            if(struct_option != "1"):
                logger.info("Get Structs Index")
                (struct_index_list, struct_location_list) = generic_get_lists(mm, collectable_struct_id_list)
                for item in struct_location_list:
                    address_struct_location_list.append(item)
                address_index_dict[address]["Structs"] = struct_index_list
            # Grounded Enemies
            if(enemy_option != "1"):
                logger.info("Get Grounded Enemies Index")
                (ground_enemy_index_list, ground_enemy_location_list) = generic_get_lists(mm, ground_enemy_id_list)
                for item in ground_enemy_location_list:
                    address_ground_enemy_location_list.append(item)
                address_index_dict[address]["Grounded_Enemies"] = ground_enemy_index_list
                # Flying Enemies
                logger.info("Get Flying Enemies Index")
                (flying_enemy_index_list, flying_enemy_location_list) = generic_get_lists(mm, flying_enemy_id_list)
                for item in flying_enemy_location_list:
                    address_flying_enemy_location_list.append(item)
                address_index_dict[address]["Flying_Enemies"] = flying_enemy_index_list
                # Wall Enemies
                logger.info("Get Wall Enemies Index")
                (wall_enemy_index_list, wall_enemy_location_list) = generic_get_lists(mm, wall_enemy_id_list)
                for item in wall_enemy_location_list:
                    address_wall_enemy_location_list.append(item)
                address_index_dict[address]["Wall_Enemies"] = wall_enemy_index_list
                # Jumping Enemies
                logger.info("Get Jumping Enemies Index")
                (jumping_enemy_index_list, jumping_enemy_location_list) = generic_get_lists(mm, jumping_enemy_id_list)
                for item in jumping_enemy_location_list:
                    address_jumping_enemy_location_list.append(item)
                address_index_dict[address]["Jumping_Enemies"] = jumping_enemy_index_list

        ### Randomize The Lists
        logger.info("Randomizing Lists Section")
        if(flagged_option != "1"):
            address_flagged_object_location_list = randomize_list(seed_val, address_flagged_object_location_list)
        if(non_flag_option != "1"):
            address_no_flag_object_location_list = randomize_list(seed_val, address_no_flag_object_location_list)
        if(struct_option != "1"):
            address_struct_location_list = randomize_list(seed_val, address_struct_location_list)
        if(enemy_option != "1"):
            address_ground_enemy_location_list = randomize_list(seed_val, address_ground_enemy_location_list)
            address_flying_enemy_location_list = randomize_list(seed_val, address_flying_enemy_location_list)
            address_wall_enemy_location_list = randomize_list(seed_val, address_wall_enemy_location_list)
            address_jumping_enemy_location_list = randomize_list(seed_val, address_jumping_enemy_location_list)
        
        ### Move Everything
        logger.info("Moving Object/Structs/Enemies Section")
        for address in address_dict[location]:
            logger.debug(address)
            mm = create_mmap(file_dir, address)
            # Flagged Objects
            if(flagged_option == "1"):
                logger.info("Flagged Objects Randomization Off")
            elif(flagged_option == "2"):
                (address_flagged_object_location_list,
                 location_jiggy_dict,
                 location_empty_honeycomb_dict,
                 location_mumbo_token_dict) = move_flagged_objects(mm,
                                                                   address_index_dict[address]["Flagged_Objects"],
                                                                   address_flagged_object_location_list,
                                                                   flagged_obj_index_dict[address]["Closest_Flag"],
                                                                   location_jiggy_dict,
                                                                   location_empty_honeycomb_dict,
                                                                   location_mumbo_token_dict)
            # No Flag Objects
            if(non_flag_option == "1"):
                logger.info("Non-Flag Objects Randomization Off")
            elif(non_flag_option == "2"):
                #move_no_flag_objects(mm, address_index_dict[address]["No_Flag_Objects"], address_no_flag_object_location_list)
                address_no_flag_object_location_list = move_no_flag_objects(mm, address_index_dict[address]["No_Flag_Objects"], address_no_flag_object_location_list)
            # Structs
            if(struct_option == "1"):
                logger.info("Struct Randomization Off")
            elif(struct_option == "2"):
                #move_structs(mm, address_index_dict[address]["Structs"], address_struct_location_list)
                address_struct_location_list = move_structs(mm, address_index_dict[address]["Structs"], address_struct_location_list)
            # Enemies
            if(enemy_option == "1"):
                logger.info("Enemy Randomization Off")
            elif(enemy_option == "2"):
                # Grounded Enemies
                address_ground_enemy_location_list = move_local_enemies(mm, address_index_dict[address]["Grounded_Enemies"], address_ground_enemy_location_list)
                # Flying Enemies
                address_flying_enemy_location_list = move_local_enemies(mm, address_index_dict[address]["Flying_Enemies"], address_flying_enemy_location_list)
                # Wall Enemies
                address_wall_enemy_location_list = move_local_enemies(mm, address_index_dict[address]["Wall_Enemies"], address_wall_enemy_location_list)
                # Jumping Enemies
                address_jumping_enemy_location_list = move_local_enemies(mm, address_index_dict[address]["Jumping_Enemies"], address_jumping_enemy_location_list)
            elif(enemy_option == "3"):
                # Grounded Enemies
                move_randomized_enemies(mm, seed_val, address_index_dict[address]["Grounded_Enemies"], ground_enemy_id_list)
                # Flying Enemies
                move_randomized_enemies(mm, seed_val, address_index_dict[address]["Flying_Enemies"], flying_enemy_id_list)
                # Wall Enemies
                move_randomized_enemies(mm, seed_val, address_index_dict[address]["Wall_Enemies"], wall_enemy_id_list)
                # Jumping Enemies
                move_randomized_enemies(mm, seed_val, address_index_dict[address]["Jumping_Enemies"], jumping_enemy_id_list)

#################
### RANDOMIZE ###
#################

def randomize_list(seed_val, original_list):
    '''Shuffles a given list based on the seed value'''
    logger.info("Randomize List")
    random.seed(a=seed_val)
    random.shuffle(original_list)
    return original_list

def move_flagged_objects(mm, obj_index_list, object_location_list, flag_indices_dict, jiggy_dict, empty_honeycomb_dict, mumbo_token_dict):
    '''For each object, assign it a new script and object id based on randomized list'''
    logger.info("Move Flagged Objects")
    for object_index in obj_index_list:
        mm[object_index] = object_location_list[0]["Script1"]
        mm[object_index + 1] = object_location_list[0]["Script2"]
        mm[object_index + 2] = object_location_list[0]["Obj_ID1"]
        mm[object_index + 3] = object_location_list[0]["Obj_ID2"]
        closest_index = flag_indices_dict[object_index]
        if(object_location_list[0]["Obj_ID2"] == 45): # Mumbo Token
            use_this_flag_key = list(mumbo_token_dict.keys())[0]
            use_this_flag_value = mumbo_token_dict[use_this_flag_key]
            mumbo_token_dict.pop(use_this_flag_key, None)
        elif(object_location_list[0]["Obj_ID2"] == 71): # Empty Honeycomb
            use_this_flag_key = list(empty_honeycomb_dict.keys())[0]
            use_this_flag_value = empty_honeycomb_dict[use_this_flag_key]
            empty_honeycomb_dict.pop(use_this_flag_key, None)
        elif(object_location_list[0]["Obj_ID2"] == 70): # Jiggy
            use_this_flag_key = list(jiggy_dict.keys())[0]
            use_this_flag_value = jiggy_dict[use_this_flag_key]
            jiggy_dict.pop(use_this_flag_key, None)
        mm[closest_index] = use_this_flag_value["Script1"]
        mm[closest_index + 1] = use_this_flag_value["Script2"]
        mm[closest_index + 2] = use_this_flag_value["Obj_ID1"]
        mm[closest_index + 3] = use_this_flag_value["Obj_ID2"]
        mm[closest_index + 4] = use_this_flag_value["IDK1"]
        mm[closest_index + 5] = use_this_flag_value["IDK2"]
        mm[closest_index + 6] = use_this_flag_value["IDK3"]
        mm[closest_index + 7] = use_this_flag_value["IDK4"]
        mm[closest_index + 8] = use_this_flag_value["Rotation"]
        mm[closest_index + 9] = use_this_flag_value["Size"]
        mm[closest_index + 10] = use_this_flag_value["IDK5"]
        mm[closest_index + 11] = use_this_flag_value["IDK6"]
        object_location_list.pop(0)
    return (object_location_list, jiggy_dict, empty_honeycomb_dict, mumbo_token_dict)

def move_no_flag_objects(mm, obj_index_list, object_location_list):
    '''For each object, assign it a new script and object id based on randomized list'''
    logger.info("Move Non-Flag Objects")
    for object_index in obj_index_list:
        mm[object_index] = object_location_list[0]["Script1"]
        mm[object_index + 1] = object_location_list[0]["Script2"]
        mm[object_index + 2] = object_location_list[0]["Obj_ID1"]
        mm[object_index + 3] = object_location_list[0]["Obj_ID2"]
        object_location_list.pop(0)
    return object_location_list

def move_structs(mm, struct_index_list, struct_location_list):
    '''For each struct, assign it a new script and object id based on randomized list'''
    logger.info("Move Local Structs")
    for struct_index in struct_index_list:
        mm[struct_index] = struct_location_list[0]["Obj_ID1"]
        mm[struct_index + 1] = struct_location_list[0]["Obj_ID2"]
        mm[struct_index + 2] = 0 #struct_location_list[struct_count]["IDK1"]
        mm[struct_index + 3] = 160 #struct_location_list[struct_count]["IDK2"]
        struct_location_list.pop(0)
    return struct_location_list

def move_local_enemies(mm, enemy_index_list, enemy_location_list):
    '''For each enemy, assign it a new script and object id based on randomized list'''
    logger.info("Move Local Enemies")
    for enemy_index in enemy_index_list:
#         mm[enemy_index] = enemy_location_list[enemy_count]["Script1"]
#         mm[enemy_index + 1] = enemy_location_list[enemy_count]["Script2"]
        mm[enemy_index + 2] = enemy_location_list[0]["Obj_ID1"]
        mm[enemy_index + 3] = enemy_location_list[0]["Obj_ID2"]
        enemy_location_list.pop(0)
    return enemy_location_list

def move_randomized_enemies(mm, seed_val, enemy_index_list, enemy_id_list):
    '''For each enemy, randomly assign it a new script and object id within the id list'''
    logger.info("Move Completely Randomized Enemies")
    seed_count = 0
    for enemy_index in enemy_index_list:
        random.seed(a=(seed_val+seed_count))
        enemy_obj_id = random.choice(enemy_id_list)
        mm[enemy_index + 2] = int(enemy_obj_id[:2], 16)
        mm[enemy_index + 3] = int(enemy_obj_id[2:], 16)
        seed_count += 1

################
### CLEAN UP ###
################

def remove_bin_files(file_dir):
    """Removes compressed and decompressed bin files created during the randomization"""
    logger.info("Remove Bin Files")
    for filename in os.listdir(file_dir + tmp_folder):
        file_path = os.path.join(file_dir + tmp_folder, filename)
        try:
            if((os.path.isfile(file_path) or os.path.islink(file_path)) and file_path.endswith("ompressed.bin")):
                os.unlink(file_path)
            elif(os.path.isdir(file_path)):
                shutil.rmtree(file_path)
        except Exception as e:
            logger.warning('Failed to delete %s. Reason: %s' % (file_path, e))

def done_window(seed_val):
    '''Displays a window to inform the user that the randomization is complete'''
    window = tk.Tk()
    window.geometry('3000x50')
    # Title
    window.winfo_toplevel().title("Banjo Kazooie Randomizer")
    done_label = tk.Label(window, text='The Randomizer Is Complete! Seed: ' + str(seed_val))
    done_label.config(anchor='center')
    done_label.pack()
    ok_btn = tk.Button(window, text='Guh-Huh!', command=window.destroy)
    ok_btn.config(anchor='center')
    done_label.pack()
    window.mainloop()

############
### MAIN ###
############

def main():
    """Goes through the steps of asking for parameters in a gui, setting up the folder, making a copy of the rom, decompressing the addresses, randomizing, compressing the files, and cleaning up"""
    logger.info("Main")
    ### Set Up ###
    (rom_dir, seed_val, non_flag_option, flagged_option, struct_option, enemy_option) = parameter_gui()
    (file_dir, rom_file) = split_dir_rom(rom_dir)
    setup_tmp_folder(file_dir)
    seed_val = seed(seed_val)
    make_copy_of_rom(seed_val, file_dir, rom_file)
    ### Decompress ROM ###
    (address_dict, address_translator) = decompressor(file_dir, rom_file)
    ### Randomize Indexes ###
    get_index_main(file_dir, address_dict, seed_val, non_flag_option, flagged_option, struct_option, enemy_option)
    ### Compress ROM ###
    compress_files(seed_val, file_dir, address_translator)
    ### Clean Up ###
    remove_bin_files(file_dir)
    ### Done ###
    done_window(seed_val)

##########################################################################################
####################################### TEST CASES #######################################
##########################################################################################

logger.info("########## Start ##########")
main()
logger.info("########## Done ##########")
