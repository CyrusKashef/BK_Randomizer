'''
Created on Aug 24, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

import mmap
import subprocess
import os

####################
### FILE IMPORTS ###
####################

from .Dicts_And_Lists.Setups import setup_ids
from .Dicts_And_Lists.Misc_Dicts_And_Lists import other_setup_pointer_list, skip_these_setup_pointer_list
from .Common_Functions import leading_zeros, get_address_endpoints

#################
### FUNCTIONS ###
#################

def verify_pointers(seed_val, file_dir):
    '''Checks that all setup files point to a setup starting with 11 72 and is on an 8n byte'''
    #logger.info("Verifying Pointer")
    with open(f"{file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_" + str(seed_val) + ".z64", "r+b") as rand_rom:
        mm_rand_rom = mmap.mmap(rand_rom.fileno(), 0)
        #logger.debug("Modified Pointer List")
        for location in setup_ids:
            for file_pointer in setup_ids[location]:
                pointer_start_1 = str(hex(mm_rand_rom[int(file_pointer[0][2:], 16)]))[2:]
                pointer_start_1 = leading_zeros(pointer_start_1, 2)
                pointer_start_2 = str(hex(mm_rand_rom[int(file_pointer[0][2:], 16) + 1]))[2:]
                pointer_start_2 = leading_zeros(pointer_start_2, 2)
                pointer_start_3 = str(hex(mm_rand_rom[int(file_pointer[0][2:], 16) + 2]))[2:]
                pointer_start_3 = leading_zeros(pointer_start_3, 2)
                pointer_start_4 = str(hex(mm_rand_rom[int(file_pointer[0][2:], 16) + 3]))[2:]
                pointer_start_4 = leading_zeros(pointer_start_4, 2)
                pointer_start = int(pointer_start_1 + pointer_start_2 + pointer_start_3 + pointer_start_4, 16)
                header_start = pointer_start + 68816 # decimal 68816 -> hex 10CD0
                if((mm_rand_rom[header_start] != 17) or (mm_rand_rom[header_start + 1] != 114)):
                    #logger.error("Invalid Header At Hex Index: " + file_pointer[0] + " , " + str(hex(header_start)))
                    #error_window("Bad Seed (" + str(seed_val) + "), Try Another")
                    raise SystemExit
                elif(((header_start % 8) != 0)):
                    #logger.error("Invalid Index Start At Hex Index: " + file_pointer[0] + " , " + str(hex(header_start)))
                    #error_window("Bad Seed (" + str(seed_val) + "), Try Another")
                    raise SystemExit
        #logger.debug("Misc Pointer List")
        for file_pointer in other_setup_pointer_list:
            pointer_start_1 = str(hex(mm_rand_rom[int(file_pointer, 16)]))[2:]
            pointer_start_1 = leading_zeros(pointer_start_1, 2)
            pointer_start_2 = str(hex(mm_rand_rom[int(file_pointer, 16) + 1]))[2:]
            pointer_start_2 = leading_zeros(pointer_start_2, 2)
            pointer_start_3 = str(hex(mm_rand_rom[int(file_pointer, 16) + 2]))[2:]
            pointer_start_3 = leading_zeros(pointer_start_3, 2)
            pointer_start_4 = str(hex(mm_rand_rom[int(file_pointer, 16) + 3]))[2:]
            pointer_start_4 = leading_zeros(pointer_start_4, 2)
            pointer_start = int(pointer_start_1 + pointer_start_2 + pointer_start_3 + pointer_start_4, 16)
            header_start = pointer_start + 68816 # decimal 68816 -> hex 10CD0
            if((mm_rand_rom[header_start] != 17) or (mm_rand_rom[header_start + 1] != 114)):
                #logger.error("Invalid Header At Decimal Index: " + str(file_pointer))
                #error_window("Bad Seed (" + str(seed_val) + "), Try Another")
                raise SystemExit
            elif(((header_start % 8) != 0)):
                #logger.error("Invalid Index Start At Hex Index: " + str(file_pointer))
                #error_window("Bad Seed (" + str(seed_val) + "), Try Another")
                raise SystemExit

def compress_file(file_dir, decompressed_file):
    """Compresses the hex file that was extracted from the main ROM file"""
    #logger.info("Compress File")
    cmd = f"{file_dir}GZIP.EXE -c " + f"{file_dir}Randomized_ROM\\" + decompressed_file.upper() + "-Decompressed.bin > " + f"{file_dir}Randomized_ROM\\" + decompressed_file.upper() + "-New_Compressed.bin"
#     #logger.debug(cmd)
    subprocess.Popen(cmd.split(),shell=True).communicate()

def compressor(file_dir, location_setup):
    """Prepares the hex file that was extracted from the main ROM file for compression by providing the correct header and footer"""
    #logger.info("Compressor")
    (addr, header, footer, lead, tail) = location_setup
    # Decomp Size
    file_pointer = addr[2:]
    with open(f"{file_dir}Randomized_ROM\\{file_pointer}-Decompressed.bin", "r+b") as rand_comp_file:
        mm_decomp = mmap.mmap(rand_comp_file.fileno(), 0)
        decomp_len = str(hex(len(mm_decomp)))[2:]
        decomp_len = leading_zeros(decomp_len, 8)
    # Compress File
    compress_file(file_dir, file_pointer)
    # Get Length Of Original Compressed File
    with open(f"{file_dir}Randomized_ROM\\{file_pointer}-New_Compressed.bin", "r+b") as comp_file:
        mm_comp = mmap.mmap(comp_file.fileno(), 0)
        comp_file_len = len(mm_comp)
        header_end = ""
        for header_val in header[-4:]:
            header_end += header_val
        header_end_index = mm_comp.find(bytes.fromhex(header_end)) + 4
        with open(f"{file_dir}Randomized_ROM\\{file_pointer}-Randomized_Compressed.bin", "w+b") as new_comp_file:
            new_comp_file.write(bytes.fromhex("1172"))
            new_comp_file.write(bytes.fromhex(decomp_len))
            new_comp_len = 6
            for index in range(header_end_index, comp_file_len-len(footer)):
                hex_string = str(hex(mm_comp[index]))[2:]
                hex_string = leading_zeros(hex_string, 2)
                new_comp_file.write(bytes.fromhex(hex_string))
                new_comp_len += 1
            if((new_comp_len % 8) != 0):
                needs_padding = 8 - (new_comp_len % 8)
                for index in range(new_comp_len, new_comp_len + needs_padding):
                    new_comp_file.write(bytes.fromhex("AA"))
    return addr

def remove_unknown_object(file_dir, index_hex_str):
    '''THIS FUNCTION IS NOT IN USE! Removes the object with the id 0268.'''
    #-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
    # Cm Voxel No SO X1 X2 Y1 Y2 Z1 Z2 S1 S2 O1 O2 .. .. .. .. Ro Si .. .. .. E1 E2 E3
    # 01 03 0A 01 0B FA 47 01 6E FB E8 19 0C 02 68 00 00 00 00 00 64 11 40 00 40 08 00
    unknown_object_count = 0
    with open(f"{file_dir}Randomized_ROM\\" + index_hex_str + "-Decompressed.bin", "r+b") as rand_decomp_file:
        still_searching = True
        start_index = 0
        while(still_searching):
            mm_rand_decomp = mmap.mmap(rand_decomp_file.fileno(), 0)
            mm_rand_decomp_len = len(mm_rand_decomp)
            search_index = mm_rand_decomp.find(bytes.fromhex("190C0268"), start_index)
            if(search_index == -1):
                still_searching = False
#             elif((mm_rand_decomp[search_index - 12] == 0) and (mm_rand_decomp[search_index - 11] == 1) and (mm_rand_decomp[search_index - 10] == 3) and
#                  (mm_rand_decomp[search_index - 9] == 10) and (mm_rand_decomp[search_index - 7] == 11) and (mm_rand_decomp[search_index + 13] == 1) and 
#                  (mm_rand_decomp[search_index + 14] == 1)):
            elif((mm_rand_decomp[search_index - 11] == 1) and (mm_rand_decomp[search_index - 10] == 3) and (mm_rand_decomp[search_index - 9] == 10) and
                 (mm_rand_decomp[search_index - 7] == 11) and (mm_rand_decomp[search_index + 13] == 1) and (mm_rand_decomp[search_index + 14] == 1)):
                mm_rand_decomp[search_index - 12] = 1
                unknown_object_count += 1
                for index in range(search_index, mm_rand_decomp_len-15):
                    mm_rand_decomp[index - 11] = mm_rand_decomp[index + 15]
                mm_rand_decomp.size(mm_rand_decomp_len - 26)
            else:
                start_index = search_index + 1
    print(f"Unknown Object Count: {str(unknown_object_count)}")

def extract_unchanged_setup(seed_val, file_dir, addr):
    '''For every setup file not randomized, pull it out of the ROM into a compressed file.'''
    randomized_rom_path = f"{file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_{str(seed_val)}.z64"
    with open(randomized_rom_path, "rb") as file:
        file_bytes = file.read()
    (address1, address2) = get_address_endpoints(file_bytes, addr)
    with open(f"{file_dir}Randomized_ROM\\{addr}-Randomized_Compressed.bin", "w+b") as comp_file:
        for index in range(address1, address2):
            hex_string = str(hex(file_bytes[index]))[2:]
            if(len(hex_string) < 2):
                hex_string = "0" + hex_string
            comp_file.write(bytes.fromhex(hex_string))

def skip_this_setup(mm_rand_rom, index_dec):
    '''Move the next pointer to the current pointer's location, making the pointer size zero.'''
    for offset in range(4):
        mm_rand_rom[index_dec + offset + 8] = mm_rand_rom[index_dec + offset]

def insert_file_into_rom(seed_val, file_dir):
    '''Inserts a compressed file back into the ROM.'''
    setup_pointer_start = 38784
    setup_pointer_end = 40000
    # For every compressed file in numerical order,
    for index_dec in range(setup_pointer_start, setup_pointer_end+1, 8):
        with open(f"{file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_{str(seed_val)}.z64", "r+b") as rand_rom:
            mm_rand_rom = mmap.mmap(rand_rom.fileno(), 0)
            index_hex_str = str(hex(index_dec))[2:]
            if(index_hex_str in skip_these_setup_pointer_list):
                skip_this_setup(mm_rand_rom, index_dec)
            else:
                with open(f"{file_dir}Randomized_ROM\\{index_hex_str}-Randomized_Compressed.bin", "r+b") as setup_bin:
                    setup_content = setup_bin.read()
                    # Find The Pointer Start
                    pointer_start = ""
                    for offset in range(4):
                        pointer_start += leading_zeros(str(hex(mm_rand_rom[index_dec + offset]))[2:], 2)
                    address_start = int("0x" + pointer_start, 16) + int("0x10CD0", 16)
                    # Place It Where The Pointer Start Points To
                    setup_count = 0
                    for index in range(address_start, address_start + len(setup_content)):
                        mm_rand_rom[index] = setup_content[setup_count]
                        setup_count += 1
                    # Calculate Where The Pointer Ends And Put That As The Next Pointer Start
                    if(index_dec != setup_pointer_end):
                        address_end = address_start + len(setup_content) - int("0x10CD0", 16)
                        address_end_hex = leading_zeros(str(hex(address_end))[2:], 8)
                        mm_rand_rom[index_dec + 8] = int(address_end_hex[:2], 16)
                        mm_rand_rom[index_dec + 9] = int(address_end_hex[2:4], 16)
                        mm_rand_rom[index_dec + 10] = int(address_end_hex[4:6], 16)
                        mm_rand_rom[index_dec + 11] = int(address_end_hex[6:], 16)
    # After The Last File Is Placed, Replace Bytes With AA Until Next Pointer Start
    pointer_start = ""
    for offset in range(4):
        pointer_start += leading_zeros(str(hex(mm_rand_rom[setup_pointer_end + 8 + offset]))[2:], 2)
    address_next_start = int(f"0x{pointer_start}", 16) + int("0x10CD0", 16)
    with open(f"{file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_{str(seed_val)}.z64", "r+b") as rand_rom:
        mm_rand_rom = mmap.mmap(rand_rom.fileno(), 0)
        for index in range(address_start + len(setup_content), address_next_start):
            mm_rand_rom[index] = 170

def reinsert_setup_files(seed_val, file_dir):
    '''The entire procedure for placing all of the randomized compressed setups back into the ROM file.'''
    # For every set up pointer, check if it's already a compressed file
    setup_pointer_start = 38784
    setup_pointer_end = 40000
    file_list = os.listdir(f"{file_dir}Randomized_ROM\\")
    for index_dec in range(setup_pointer_start, setup_pointer_end+1, 8):
        index_hex_str = str(hex(index_dec))[2:]
        if((index_hex_str + "-Decompressed.bin") in file_list):
            #remove_unknown_object(file_dir, index_hex_str)
            pass
        else:
            extract_unchanged_setup(seed_val, file_dir, index_hex_str)
    # Compress every decompressed file
    #logger.info("Compress Files")
    for location in setup_ids:
        for location_setup in setup_ids[location]:
            compressor(file_dir, location_setup)
    insert_file_into_rom(seed_val, file_dir)
    verify_pointers(seed_val, file_dir)