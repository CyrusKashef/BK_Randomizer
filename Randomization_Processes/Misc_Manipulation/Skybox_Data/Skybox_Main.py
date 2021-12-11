'''
Created on Oct 23, 2021

@author: Cyrus
'''

#####################
### PYTHON IMPORT ###
#####################

import random
import mmap

###################
### FILE IMPORT ###
###################

from ...Common_Functions import get_address_endpoints, leading_zeros, read_json

##########################
### SKYBOX MANIP CLASS ###
##########################

class Skybox_Manipulation():
    '''Skybox manipulation class'''
    def __init__(self, seed_val, file_dir, randomized_rom_path):
        '''Initializes the skybox manipulation class'''
        self._file_dir = file_dir
        self._randomized_rom_path = randomized_rom_path
        with open(self._randomized_rom_path, "rb") as file:
            self._file_bytes = file.read()
        self._seed_val = seed_val
        self._pointers_start = 0x9C80
        self._pointers_end = 0x9D00
        self._skybox_address_dict = {}
        self._skybox_dict = read_json(f"{self._file_dir}Randomization_Processes\\Misc_Manipulation\\Skybox_Data\\Skybox.json")
    
    def _grab_compressed_file(self, pointer_str):
        '''Uses the pointer to find the beginning and end of a skybox file and extracts it'''
        (address1, address2) = get_address_endpoints(self._file_bytes, pointer_str)
        with open(f"{self._file_dir}Randomized_ROM\\{pointer_str[2:]}-Compressed.bin", "w+b") as comp_file:
            for index in range(address1, address2):
                hex_string = str(hex(self._file_bytes[index]))[2:]
                if(len(hex_string) < 2):
                    hex_string = "0" + hex_string
                comp_file.write(bytes.fromhex(hex_string))
    
    def _place_compressed_files(self):
        '''Replaces the skybox pointers with the new skybox file'''
        for pointer in range(self._pointers_start, self._pointers_end + 0x08, 0x08):
#             print("~~~~")
            pointer_str = str(hex(pointer))
            pointer_dec = int(pointer_str[2:], 16)
            curr_pointer_file = self._skybox_address_dict[pointer_str]
            with open(f"{self._file_dir}Randomized_ROM\\{curr_pointer_file}", "r+b") as comp_file:
                pointer_content = comp_file.read()
            with open(f"{self._file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_{self._seed_val}.z64", "r+b") as rom_file:
                mm_rand_rom = mmap.mmap(rom_file.fileno(), 0)
#                 print(f"Pointer Str: {pointer_str}   Pointer File: {curr_pointer_file}")
                # Find The Pointer Start
                pointer_start = ""
                for offset in range(4):
                    pointer_start += leading_zeros(mm_rand_rom[pointer_dec + offset], 2)
                address_start = int("0x" + pointer_start, 16) + int("0x10CD0", 16)
#                 print(f"Start: {hex(address_start)}   End: {hex(address_start + len(pointer_content))}")
                curr_pointer_index = 0
                for index in range(address_start, address_start + len(pointer_content)):
                    mm_rand_rom[index] = pointer_content[curr_pointer_index]
                    curr_pointer_index += 1
                address_end = address_start + len(pointer_content) - int("0x10CD0", 16)
                address_end_hex = leading_zeros(address_end, 8)
                mm_rand_rom[pointer_dec + 8] = int(address_end_hex[:2], 16)
                mm_rand_rom[pointer_dec + 9] = int(address_end_hex[2:4], 16)
                mm_rand_rom[pointer_dec + 10] = int(address_end_hex[4:6], 16)
                mm_rand_rom[pointer_dec + 11] = int(address_end_hex[6:], 16)
#                 print(f"Address End Hex: {address_end_hex}")
        if((mm_rand_rom[self._pointers_end + 8] != 0x0) or
           (mm_rand_rom[self._pointers_end + 9] != 0x50) or
           (mm_rand_rom[self._pointers_end + 10] != 0x3F) or
           (mm_rand_rom[self._pointers_end + 11] != 0xA8)):
            print("Last Pointer Doesn't Match")
            print(hex(mm_rand_rom[self._pointers_end + 8]))
            print(hex(mm_rand_rom[self._pointers_end + 9]))
            print(hex(mm_rand_rom[self._pointers_end + 10]))
            print(hex(mm_rand_rom[self._pointers_end + 11]))
            raise SystemError
    
    def _shuffle_list(self, original_list):
        '''Shuffles a given list'''
        random.seed(a=self._seed_val)
        random.shuffle(original_list)
        return original_list
    
    def _skybox_manip_main(self):
        '''Runs through the functions of extracting, shuffling, and reinserting the skybox files'''
        # Main Categories
        skybox_categories = ["Sky", "Clouds"]
        pointer_dict = {}
        for category in self._skybox_dict:
            category_pointer_list = []
            # Extract Compressed Files
            pointer_dict[category] = []
            for pointer_str in self._skybox_dict[category]:
                self._grab_compressed_file(pointer_str)
                pointer_dict[category].append(f"{pointer_str[2:]}-Compressed.bin")
        for category in self._skybox_dict:
            # Shuffle Compressed Files
            category_pointer_list = []
            for item in pointer_dict[category]:
                category_pointer_list.append(item)
            if(category in skybox_categories):
                category_pointer_list = self._shuffle_list(category_pointer_list)
            # Assign New Files
            list_counter = 0
            for pointer_str in self._skybox_dict[category]:
                self._skybox_address_dict[pointer_str.lower()] = category_pointer_list[list_counter]
                list_counter += 1
        # Replace Compressed Files Into ROM
        self._place_compressed_files()