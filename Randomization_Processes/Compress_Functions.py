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

from .Dicts_And_Lists.Setups import setup_ids, speech_file_ids, asm_setup_ids, texture_setup_ids, level_model_ids
from .Dicts_And_Lists.Misc_Dicts_And_Lists import skip_these_setup_pointer_list, furnace_fun_questions_pointer_list
from .Common_Functions import leading_zeros, get_address_endpoints

########################
### COMPRESSOR CLASS ###
########################

class Compressor():
    '''Compressor class'''
    def __init__(self, master, seed_val, file_dir):
        '''Initializes compressor class'''
        self.master = master
        self._seed_val = seed_val
        self._file_dir = file_dir

    def _extract_unchanged_setup(self, addr):
        '''For every setup file not randomized, pull it out of the ROM into a compressed file.'''
        with open(f"{self._file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_{self._seed_val}.z64", "rb") as file:
            file_bytes = file.read()
        (address1, address2) = get_address_endpoints(file_bytes, addr)
        with open(f"{self._file_dir}Randomized_ROM\\{addr}-Randomized_Compressed.bin", "w+b") as comp_file:
            for index in range(address1, address2):
                hex_string = str(hex(file_bytes[index]))[2:]
                if(len(hex_string) < 2):
                    hex_string = "0" + hex_string
                comp_file.write(bytes.fromhex(hex_string))

    def _compress_file(self, file_name):
        """Compresses the hex file that was extracted from the main ROM file"""
        cmd = f"{self._file_dir}GZIP.EXE -c {self._file_dir}Randomized_ROM\\{file_name.upper()}-Decompressed.bin > {self._file_dir}Randomized_ROM\\{file_name.upper()}-New_Compressed.bin"
        subprocess.Popen(cmd.split(),shell=True).communicate()
    
    def _post_compress_operations(self, file_name, header, footer, decomp_len, padding_text="AA"):
        with open(f"{self._file_dir}Randomized_ROM/{file_name}-New_Compressed.bin", "r+b") as comp_file:
            mm_comp = mmap.mmap(comp_file.fileno(), 0)
            comp_file_len = len(mm_comp)
            header_end = ""
            for header_val in header[-4:]:
                header_end += header_val
            header_end_index = mm_comp.find(bytes.fromhex(header_end)) + 4
            with open(f"{self._file_dir}Randomized_ROM/{file_name}-Randomized_Compressed.bin", "w+b") as new_comp_file:
                new_comp_file.write(bytes.fromhex("1172"))
                new_comp_file.write(bytes.fromhex(decomp_len))
                new_comp_len = 6
                for index in range(header_end_index, comp_file_len-len(footer)):
                    hex_string = leading_zeros(mm_comp[index], 2)
                    new_comp_file.write(bytes.fromhex(hex_string))
                    new_comp_len += 1
                if((new_comp_len % 8) != 0):
                    needs_padding = 8 - (new_comp_len % 8)
                    for index in range(new_comp_len, new_comp_len + needs_padding):
                        new_comp_file.write(bytes.fromhex(padding_text))
    
    def _insert_into_rom_by_pointer(self, setup_pointer_start, setup_pointer_end, additional_skip_these_pointer_list=[]):
        for index_dec in range(setup_pointer_start, setup_pointer_end + 1, 8):
            with open(f"{self._file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_{self._seed_val}.z64", "r+b") as bk_rom:
                mm_bk_rom = mmap.mmap(bk_rom.fileno(), 0)
                index_hex_str = str(hex(index_dec))[2:]
                if(index_hex_str in additional_skip_these_pointer_list):
                    self.skip_this_setup(mm_bk_rom, index_dec)
                else:
                    with open(f"{self._file_dir}Randomized_ROM\\{index_hex_str}-Randomized_Compressed.bin", "r+b") as setup_bin:
                        setup_content = setup_bin.read()
                        # Find The Pointer Start
                        pointer_start = ""
                        for offset in range(4):
                            pointer_start += leading_zeros(mm_bk_rom[index_dec + offset], 2)
                        address_start = int("0x" + pointer_start, 16) + int("0x10CD0", 16)
                        # Place It Where The Pointer Start Points To
                        setup_count = 0
                        for index in range(address_start, address_start + len(setup_content)):
                            mm_bk_rom[index] = setup_content[setup_count]
                            setup_count += 1
                        # Calculate Where The Pointer Ends And Put That As The Next Pointer Start
                        if(index_dec != setup_pointer_end):
                            address_end = address_start + len(setup_content) - int("0x10CD0", 16)
                            address_end_hex = leading_zeros(address_end, 8)
                            mm_bk_rom[index_dec + 8] = int(address_end_hex[:2], 16)
                            mm_bk_rom[index_dec + 9] = int(address_end_hex[2:4], 16)
                            mm_bk_rom[index_dec + 10] = int(address_end_hex[4:6], 16)
                            mm_bk_rom[index_dec + 11] = int(address_end_hex[6:], 16)
        # After The Last File Is Placed, Replace Bytes With AA Until Next Pointer Start
        pointer_start = ""
        for offset in range(4):
            pointer_start += leading_zeros(mm_bk_rom[setup_pointer_end + 8 + offset], 2)
        address_next_start = int(f"0x{pointer_start}", 16) + int("0x10CD0", 16)
        with open(f"{self._file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_{self._seed_val}.z64", "r+b") as bk_rom:
            mm_bk_rom = mmap.mmap(bk_rom.fileno(), 0)
            for index in range(address_start + len(setup_content), address_next_start):
                mm_bk_rom[index] = 0xAA
    
    def _insert_into_rom_by_location(self, section_dict):
        for subsection in section_dict:
            if((subsection == "Rusty_Bucket_Bay_Overlay") and (self.master.buttons_var.get() == 0)):
                pass
            elif((subsection == "Gobis_Valley_Overlay") and (self.master.matching_puzzle_var.get() == 0)):
                pass
            else:
                print(f"Subsection: {subsection}")
                for subsection_info in section_dict[subsection]:
                    with open(f"{self._file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_{self._seed_val}.z64", "r+b") as bk_rom:
                        mm_bk_rom = mmap.mmap(bk_rom.fileno(), 0)
                        file_name = subsection_info[0].split(",")[0]
                        address_start = int(file_name, 16)
                        with open(f"{self._file_dir}Randomized_ROM\\{file_name}-Randomized_Compressed.bin", "r+b") as setup_bin:
                            setup_content = setup_bin.read()
                            # Place It Where The Pointer Start Points To
                            setup_count = 0
                            for index in range(address_start, address_start + len(setup_content)):
                                mm_bk_rom[index] = setup_content[setup_count]
                                setup_count += 1
    
    def _verify_pointer_header(self, setup_pointer_start, setup_pointer_end):
        with open(f"{self._file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_{self._seed_val}.z64", "r+b") as bk_rom:
            mm_bk_rom = mmap.mmap(bk_rom.fileno(), 0)
            for pointer_index in range(setup_pointer_start, setup_pointer_end + 1, 8):
                address_start = int((leading_zeros(mm_bk_rom[pointer_index], 2) +
                                     leading_zeros(mm_bk_rom[pointer_index + 1], 2) +
                                     leading_zeros(mm_bk_rom[pointer_index + 2], 2) +
                                     leading_zeros(mm_bk_rom[pointer_index + 3], 2)), 16) + 0x10CD0
                if((mm_bk_rom[address_start] != 0x11) or (mm_bk_rom[address_start + 1] != 0x72)):
                    print(f"Pointer {hex(pointer_index)}: Header At Address {hex(address_start)} Does Not Start With 11 72")
                    raise SystemExit

    def _subection_compression_main(self, file_name, header, footer, padding_text="AA"):
        # Decomp Size
        if(file_name.startswith("0x")):
            file_name = file_name[2:]
        else:
            file_name = file_name.split(",")[0]
        with open(f"{self._file_dir}Randomized_ROM\\{file_name}-Decompressed.bin", "r+b") as rand_comp_file:
            mm_decomp = mmap.mmap(rand_comp_file.fileno(), 0)
            decomp_len = leading_zeros(len(mm_decomp), 8)
        # Compress File
        self._compress_file(file_name)
        self._post_compress_operations(file_name, header, footer, decomp_len, padding_text)

    def _section_compression_main(self, section_dict, setup_pointer_start=None, setup_pointer_end=None, additional_skip_these_pointer_list=[]):
        # Check every pointer within the start and end
        # If a section was not extracted to be randomized,
        #    extract it now to reinsert when things get shifted
        if((not setup_pointer_start) and (not setup_pointer_end)):
            for subsection in section_dict:
                for subsection_info in section_dict[subsection]:
                    curr_pointer = int(subsection_info[0][2:], 16)
                    if((not setup_pointer_start) and (not setup_pointer_end)):
                        setup_pointer_start = curr_pointer
                    elif(curr_pointer < setup_pointer_start):
                        setup_pointer_start = curr_pointer
                    elif(curr_pointer > setup_pointer_end):
                        setup_pointer_end = curr_pointer
        file_list = os.listdir(f"{self._file_dir}Randomized_ROM/")
        for index_dec in range(setup_pointer_start, setup_pointer_end + 1, 8):
            index_hex_str = str(hex(index_dec))[2:]
            if((index_hex_str + "-Decompressed.bin") not in file_list):
                self._extract_unchanged_setup(index_hex_str)
        # For every modified file,
        #     Compress it and reformat it to prepare for insertion
        for subsection in section_dict:
            for subsection_info in section_dict[subsection]:
                self._subection_compression_main(file_name=subsection_info[0],
                                                 header=subsection_info[1],
                                                 footer=subsection_info[2])
        # Insert the files and verify the pointers are correct
        self._insert_into_rom_by_pointer(setup_pointer_start, setup_pointer_end, additional_skip_these_pointer_list)
        self._verify_pointer_header(setup_pointer_start, setup_pointer_end)
    
    def _location_compression_main(self, section_dict):
        # For every modified file,
        #     Compress it and reformat it to prepare for insertion
        for subsection in section_dict:
            if((subsection == "Rusty_Bucket_Bay_Overlay") and (self.master.buttons_var.get() == 0)):
                pass
            elif((subsection == "Gobis_Valley_Overlay") and (self.master.matching_puzzle_var.get() == 0)):
                pass
            else:
                for subsection_info in section_dict[subsection]:
                    self._subection_compression_main(file_name=subsection_info[0],
                                                     header=subsection_info[1],
                                                     footer=subsection_info[2],
                                                     padding_text="00")
        self._insert_into_rom_by_location(section_dict)

    def _main(self):
        print("Setups")
        self._section_compression_main(setup_ids, 0x9780, 0x9C40, skip_these_setup_pointer_list) # Setups
        print("Intro & Lair Cutscene")
        self._section_compression_main(speech_file_ids, 0xD150, 0xD1C8) # Intro & Lair Cutscene
        print("Bottles Intro")
        self._section_compression_main(speech_file_ids, 0xCE30, 0xCE30) # Bottles Intro
        print("Bottles Tutorial Confirm")
        self._section_compression_main(speech_file_ids, 0xCF90, 0xCF98) # Bottles Tutorial Confirm & Secret Game Text
        print("Bottles Move Texts")
        self._section_compression_main(speech_file_ids, 0xAFD0, 0xDA00) # Bottles Move Texts
        if(self.master.skip_furnace_fun_var.get() == 1):
            print("Brentilda Hints")
#             self._section_compression_main(speech_file_ids, 0xE2B0, 0xE3A0) # Brentilda Hints
            self._section_compression_main(speech_file_ids, 0xE2B0, 0xFFB8, furnace_fun_questions_pointer_list) # Brentilda Hints & Furnace Fun & Whatever Is In Between
        print("BK Models Through Note Doors")
        self._section_compression_main(texture_setup_ids, 0x7900, 0x8320) # Note Doors
        if(self.master.world_entrance_var.get() != "None"):
            print("Level Sign")
            self._section_compression_main(texture_setup_ids, 0x89B0, 0x89B0) # Level Sign
        if(self.master.matching_puzzle_var.get() == 1):
            print("GV Matching Puzzle")
            self._section_compression_main(texture_setup_ids, 0x10248, 0x10248) # GV Matching Puzzle
        if(self.master.buttons_var.get() == 1):
            print("RBB Boat 1")
            self._section_compression_main(texture_setup_ids, 0x10418, 0x10418) # RBB Boat 1
        if(self.master.gruntilda_difficulty_var.get() > 0):
            self._section_compression_main(level_model_ids, 0x10678, 0x10678) # Final Battle Area 1
        print("ASM")
        self._location_compression_main(asm_setup_ids)