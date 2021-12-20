'''
Created on Oct 31, 2021

@author: Cyrus

#################
### JSON FILE ###
#################

### FORMAT ###
{
    "ITEM_SHAPE_1": {
        "SHUFFLE_INTO_NEXT_GROUP_1": {
            "POINTER_ADDRESS_1": "ITEM_NAME_1",
            "POINTER_ADDRESS_2": "ITEM_NAME_2",
            "POINTER_ADDRESS_3": "ITEM_NAME_3"
        },
        "SHUFFLE_INTO_NEXT_GROUP_2": {
            "POINTER_ADDRESS_4": "ITEM_NAME_4",
            "POINTER_ADDRESS_5": "ITEM_NAME_5",
            "POINTER_ADDRESS_6": "ITEM_NAME_6"
        }
        ...
        "SHUFFLE_INTO_FIRST_GROUP": {
            "POINTER_ADDRESS_97": "ITEM_NAME_97",
            "POINTER_ADDRESS_98": "ITEM_NAME_98",
            "POINTER_ADDRESS_99": "ITEM_NAME_99"
        }
    },
    "ITEM_SHAPE_2": {
        "SHUFFLE_WITHIN_ITSELF": {
            "POINTER_ADDRESS_101": "ITEM_NAME_101",
            "POINTER_ADDRESS_102": "ITEM_NAME_102",
            "POINTER_ADDRESS_103": "ITEM_NAME_103"
        },
    },
}

### EXPLAINED ###
* Item shapes should generally match to have the models function as closely as possible to the original.
* Size does not affect the functionality of the model, but may make gameplay difficult if too big or too small.
* If you want two items to switch no matter what, put them in two seperate groups within a shape.
* If you want two categories to shuffle between each other (example, swap jinjos with baddies), put one category in one group and the other category in the other group. Groups must have the same number of items.
* If you want all items of the same shape to shuffle, place them all in one group.

### DOESNT WORK ###
* Sizes scale with original item, so things like trees and sexy Grunty don't shuffle well.
* Cannot swap Conga (0x7978) and Chimpy (0x7980) because Chimpy cannot throw oranges. You can get the "beating up Conga" jiggy, but you can't get the "orange pad" jiggy. Conga can become Chimpy though.
* Cannot swap Conga (0x7978) and Sir Slush (0x7A50) because Conga doesn't have a hat for it to be killed in Freezeezy Peak. Sir Slush can become Conga though.
* Slappa can be Grabba, but there's not slamming animation, so no Beak Buster killing. Maybe Wonderwing?
* Jinjonator or Stone cannot be swapped, game will freeze. Not sure which one crashed, needs testing.
* Mutie Snippets cannot be swapped with Snippets/Black Snippets; Clanker's won't load.

'''

#####################
### PYTHON IMPORT ###
#####################

from random import seed, shuffle, choice
from mmap import mmap

###################
### FILE IMPORT ###
###################

from Randomization_Processes.Common_Functions import get_address_endpoints, leading_zeros, read_json

##########################
### MODEL MANIP CLASS ###
##########################

class Swap_Models_Manipulation_Class():
    '''Swap models manipulation class'''
    def __init__(self, seed_val, file_dir, randomized_rom_path):
        '''Initializes the swap models manipulation class'''
        self._file_dir = file_dir
        self._randomized_rom_path = randomized_rom_path
        with open(self._randomized_rom_path, "rb") as file:
            self._file_bytes = file.read()
        self._seed_val = seed_val
        self._pointers_start = None
        self._pointers_end = None
        self._model_address_dict = {}
        self._model_dict = read_json(f"{self._file_dir}Randomization_Processes/Misc_Manipulation/Model_Data/Swappable_Models.json")
    
    def _grab_compressed_file(self, pointer_str):
        '''Uses the pointer to find the beginning and end of a model file and extracts it'''
        (address1, address2) = get_address_endpoints(self._file_bytes, pointer_str)
        with open(f"{self._file_dir}Randomized_ROM/{pointer_str[2:].lower()}-Compressed.bin", "w+b") as comp_file:
            for index in range(address1, address2):
                hex_string = str(hex(self._file_bytes[index]))[2:]
                if(len(hex_string) < 2):
                    hex_string = "0" + hex_string
                comp_file.write(bytes.fromhex(hex_string))
    
    def _place_compressed_files(self):
        '''Replaces the model pointers with the new model file'''
        for pointer in range(self._pointers_start, self._pointers_end + 0x08, 0x08):
#             print("~~~~")
            pointer_str = str(hex(pointer))
            pointer_dec = int(pointer_str[2:], 16)
            curr_pointer_file = self._model_address_dict[pointer_str]
            with open(f"{self._file_dir}Randomized_ROM\\{curr_pointer_file}", "r+b") as comp_file:
                pointer_content = comp_file.read()
            with open(f"{self._file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_{self._seed_val}.z64", "r+b") as rom_file:
                mm_rand_rom = mmap(rom_file.fileno(), 0)
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
        seed(a=self._seed_val)
        shuffle(original_list)
        return original_list
    
    def _model_manip_main(self):
        '''Runs through the functions of extracting, shuffling, and reinserting the model files'''
        for category in self._model_dict:
            for curr_set in self._model_dict[category]:
                for model in self._model_dict[category][curr_set]:
                    pointer = int(model[2:], 16)
                    if((not self._pointers_start) or (pointer < self._pointers_start)):
                        self._pointers_start = pointer
                    if((not self._pointers_end) or (pointer > self._pointers_end)):
                        self._pointers_end = pointer
        # Extract Compressed Files
        for pointer in range(self._pointers_start, self._pointers_end + 8, 8):
            pointer_str = str(hex(pointer))
            self._grab_compressed_file(pointer_str)
            self._model_address_dict[pointer_str.lower()] = f"{pointer_str[2:].lower()}-Compressed.bin"
        for category in self._model_dict:
            if("Replacements" in self._model_dict[category]):
                replacement_list = []
                for replacement_file in self._model_dict[category]["Replacements"]:
                    replacement_list.append(replacement_file)
                for original_file in self._model_dict[category]["Original"]:
                    seed(a=(self._seed_val + int(original_file[2:], 16)))
                    replacement_model = choice(replacement_list)
                    self._model_address_dict[original_file.lower()] = f"{replacement_model[2:].lower()}-Compressed.bin"
                    replacement_list.remove(replacement_model)
            else:
                swap_lists = {}
                set_counter = 0
                for curr_set in self._model_dict[category]:
                    swap_lists[set_counter] = []
                    for model in self._model_dict[category][curr_set]:
                        swap_lists[set_counter].append(f"{model[2:].lower()}-Compressed.bin")
                    swap_lists[set_counter] = self._shuffle_list(swap_lists[set_counter])
                    set_counter += 1
                # Assign New Files
                set_count = len(self._model_dict[category])
                set_counter = 0
                for curr_set in self._model_dict[category]:
                    model_count = 0
                    for model in self._model_dict[category][curr_set]:
                        if(set_count == (set_counter + 1)):
                            self._model_address_dict[model.lower()] = swap_lists[0][model_count]
                        else:
                            self._model_address_dict[model.lower()] = swap_lists[set_counter + 1][model_count]
                        model_count += 1
                    set_counter += 1
        # Replace Compressed Files Into ROM
        self._place_compressed_files()