'''
Created on Dec 14, 2021

@author: Cyrus
'''

#####################
### PYTHON IMPORT ###
#####################

from random import seed, choice
from mmap import mmap
import json

###################
### FILE IMPORT ###
###################

from Randomization_Processes.Common_Functions import read_json

##############################
### PROPERTIES MANIP CLASS ###
##############################

class Properties_Manipulation_Class():
    '''Properties manipulation class'''
    def __init__(self, seed_val, file_dir, properties_dict, selected_json):
        '''Initializes the properties manipulation class'''
        self._file_dir = file_dir
        self._seed_val = seed_val
        self._properties_dict = properties_dict
        self._file_name = (selected_json.replace(" ", "_")).upper()
        asm_file_address_list = [
            "F19250", "F362EB", "F37F90", "F9CAE0", "FC4810", "FC6C0F",
            "FB24A0", "FB42D9", "FAE860", "FB1AEB", "FA3FD0", "FA5D96",
            "FB44E0", "FB9610", "FBEBE0", "FC3FEF", "FA9150", "FAE27E",
            "FA5F50", "FA8CE6", "FB9A30", "FBE5E2", "FD6190", "FDA2FF",
            "FC9150", "FCF698", "FD0420", "FD5A60", "FC6F20", "FC8AFC"
            ]
        self._asm_file_address_list = []
        for asm_file_address in asm_file_address_list:
            self._asm_file_address_list.append(f"{self._file_dir}Randomized_ROM/{asm_file_address}-Decompressed.bin")
        self._new_properties_cheat_sheet = {}
    
    def _choice_from_list(self, original_list, increment=0):
        '''PyDoc'''
        seed(a=(self._seed_val + increment))
        return choice(original_list)
    
    def _swap_properties_main(self):
        increment = 0
        for properties_category in self._properties_dict:
            for search_string in self._properties_dict[properties_category]["Original"]:
                new_property = self._choice_from_list(list(self._properties_dict[properties_category]["Selection"]), increment)
                increment += 1
                self._new_properties_cheat_sheet[self._properties_dict[properties_category]['Original'][search_string]] = self._properties_dict[properties_category]['Selection'][new_property]
#                 print(f"Enemy: {self._properties_dict[properties_category]['Original'][search_string]}    New Property: {self._properties_dict[properties_category]['Selection'][new_property]}")
                for asm_file_address in self._asm_file_address_list:
                    with open(asm_file_address, "r+b") as f:
                        mm = mmap(f.fileno(), 0)
                        item_index = mm.find(bytes.fromhex(search_string))
                        if(item_index > -1):
                            mm[item_index] = int(new_property[:2], 16)
                            mm[item_index + 1] = int(new_property[2:], 16)
                            break
    
    def _generate_cheat_sheet(self):
        cheat_sheet_file = f"{self._file_dir}Randomized_ROM/PROPERTIES_CHEAT_SHEET_{self._file_name}_{self._seed_val}.json"
        with open(cheat_sheet_file, "w+") as json_file: 
            json.dump(self._new_properties_cheat_sheet, json_file, indent=4)

