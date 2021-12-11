'''
Created on Dec 5, 2021

@author: Cyrus
'''

'''
Created on Oct 31, 2021

@author: Cyrus

#################
### JSON FILE ###
#################

### FORMAT ###
{
    "ANIMATION_DESCRIPTION_1": {
        "SHUFFLE_INTO_NEXT_GROUP_1": {
            "POINTER_ADDRESS_1": "ANIMATION_1",
            "POINTER_ADDRESS_2": "ANIMATION_2",
            "POINTER_ADDRESS_3": "ANIMATION_3"
        },
        "SHUFFLE_INTO_NEXT_GROUP_2": {
            "POINTER_ADDRESS_4": "ANIMATION_4",
            "POINTER_ADDRESS_5": "ANIMATION_5",
            "POINTER_ADDRESS_6": "ANIMATION_6"
        }
        ...
        "SHUFFLE_INTO_FIRST_GROUP": {
            "POINTER_ADDRESS_97": "ANIMATION_97",
            "POINTER_ADDRESS_98": "ANIMATION_98",
            "POINTER_ADDRESS_99": "ANIMATION_99"
        }
    },
    "ANIMATION_DESCRIPTION_2": {
        "SHUFFLE_WITHIN_ITSELF": {
            "POINTER_ADDRESS_101": "ANIMATION_101",
            "POINTER_ADDRESS_102": "ANIMATION_102",
            "POINTER_ADDRESS_103": "ANIMATION_103"
        },
    },
}

### EXPLAINED ###

### DOESNT WORK ###

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

#############################
### ANIMATION MANIP CLASS ###
#############################

class Swap_Animations_Manipulation():
    '''Swap animations manipulation class'''
    def __init__(self, seed_val, file_dir, randomized_rom_path):
        '''Initializes the swap animations manipulation class'''
        self._file_dir = file_dir
        self._randomized_rom_path = randomized_rom_path
        with open(self._randomized_rom_path, "rb") as file:
            self._file_bytes = file.read()
        self._seed_val = seed_val
        self._pointers_start = None
        self._pointers_end = None
        self._animation_address_dict = {}
        self._animation_dict = read_json(f"{self._file_dir}Randomization_Processes/Misc_Manipulation/Animation_Data/Swappable_Animations.json")
    
    def _grab_compressed_file(self, pointer_str):
        '''Uses the pointer to find the beginning and end of a animation file and extracts it'''
        (address1, address2) = get_address_endpoints(self._file_bytes, pointer_str)
        with open(f"{self._file_dir}Randomized_ROM/{pointer_str[2:].lower()}-Compressed.bin", "w+b") as comp_file:
            for index in range(address1, address2):
                hex_string = str(hex(self._file_bytes[index]))[2:]
                if(len(hex_string) < 2):
                    hex_string = "0" + hex_string
                comp_file.write(bytes.fromhex(hex_string))
    
    def _place_compressed_files(self):
        '''Replaces the animation pointers with the new animation file'''
        for pointer in range(self._pointers_start, self._pointers_end + 0x08, 0x08):
#             print("~~~~")
            pointer_str = str(hex(pointer))
            pointer_dec = int(pointer_str[2:], 16)
            curr_pointer_file = self._animation_address_dict[pointer_str]
            with open(f"{self._file_dir}Randomized_ROM/{curr_pointer_file}", "r+b") as comp_file:
                pointer_content = comp_file.read()
            with open(f"{self._file_dir}Randomized_ROM/Banjo-Kazooie_Randomized_Seed_{self._seed_val}.z64", "r+b") as rom_file:
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
                if(pointer < self._pointers_end):
                    address_end = address_start + len(pointer_content) - int("0x10CD0", 16)
                    address_end_hex = leading_zeros(address_end, 8)
                    mm_rand_rom[pointer_dec + 8] = int(address_end_hex[:2], 16)
                    mm_rand_rom[pointer_dec + 9] = int(address_end_hex[2:4], 16)
                    mm_rand_rom[pointer_dec + 10] = int(address_end_hex[4:6], 16)
                    mm_rand_rom[pointer_dec + 11] = int(address_end_hex[6:], 16)
    #                 print(f"Address End Hex: {address_end_hex}")
    
    def _shuffle_list(self, original_list):
        '''Shuffles a given list'''
        random.seed(a=self._seed_val)
        random.shuffle(original_list)
        return original_list
    
    def _animation_manip_main(self):
        '''Runs through the functions of extracting, shuffling, and reinserting the animation files'''
        for category in self._animation_dict:
            for curr_set in self._animation_dict[category]:
                for animation in self._animation_dict[category][curr_set]:
                    pointer = int(animation[2:], 16)
                    if((not self._pointers_start) or (pointer < self._pointers_start)):
                        self._pointers_start = pointer
                    if((not self._pointers_end) or (pointer > self._pointers_end)):
                        self._pointers_end = pointer
        # Extract Compressed Files
        for pointer in range(self._pointers_start, self._pointers_end + 8, 8):
            pointer_str = str(hex(pointer))
            self._grab_compressed_file(pointer_str)
            self._animation_address_dict[pointer_str.lower()] = f"{pointer_str[2:].lower()}-Compressed.bin"
        for category in self._animation_dict:
            if("Replacements" in self._animation_dict[category]):
                replacement_list = []
                for replacement_file in self._animation_dict[category]["Replacements"]:
                    replacement_list.append(replacement_file)
                for original_file in self._animation_dict[category]["Original"]:
                    random.seed(a=(self._seed_val + int(original_file[2:], 16)))
                    replacement_animation = random.choice(replacement_list)
                    self._animation_address_dict[original_file.lower()] = f"{replacement_animation[2:].lower()}-Compressed.bin"
                    replacement_list.remove(replacement_animation)
            else:
                swap_lists = {}
                set_counter = 0
                for curr_set in self._animation_dict[category]:
                    swap_lists[set_counter] = []
                    for animation in self._animation_dict[category][curr_set]:
                        swap_lists[set_counter].append(f"{animation[2:].lower()}-Compressed.bin")
                    swap_lists[set_counter] = self._shuffle_list(swap_lists[set_counter])
                    set_counter += 1
                # Assign New Files
                set_count = len(self._animation_dict[category])
                set_counter = 0
                for curr_set in self._animation_dict[category]:
                    animation_count = 0
                    for animation in self._animation_dict[category][curr_set]:
                        if(set_count == (set_counter + 1)):
                            self._animation_address_dict[animation.lower()] = swap_lists[0][animation_count]
                        else:
                            self._animation_address_dict[animation.lower()] = swap_lists[set_counter + 1][animation_count]
                        animation_count += 1
                    set_counter += 1
        # Replace Compressed Files Into ROM
        self._place_compressed_files()