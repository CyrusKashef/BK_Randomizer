'''
Created on Aug 30, 2021

@author: Cyrus
'''

########################
### PYTHON FUNCTIONS ###
########################

import mmap
import random

####################
### FILE IMPORTS ###
####################

from ..Dicts_And_Lists import Sequences

########################
### SETUP FILE CLASS ###
########################

class SetupFile():
    '''Generic setup file class'''
    def __init__(self, setup_address, cwd, setup_name=None):
        '''Initializes the setup file class'''
        self.cwd = f"{cwd}Randomized_ROM/"
        self.setup_name = setup_name
        self.setup_address = int(setup_address, 16)
        self.struct_index_list = []
        self.struct_info_list = []
        self.non_flag_object_index_list = []
        self.non_flag_object_info_list = []
        self.flagged_object_index_list = []
        self.flagged_object_info_list = []
        self.ground_enemy_index_list = []
        self.ground_enemy_info_list = []
        self.wall_enemy_index_list = []
        self.wall_enemy_info_list = []
        self.flying_enemy_index_list = []
        self.flying_enemy_info_list = []
        self.warp_index_list = []
        self.warp_info_list = []
        self.bottles_index_list = []
        self.bottles_info_list = []
        with open(f"{self.cwd}{setup_address}-Decompressed.bin", "r+b") as f:
            self.mm = mmap.mmap(f.fileno(), 0)
        if(self.setup_address == "97B0"):
            self.adjust_ttc_oob_egg()
        self.note_count = 0
        self.jiggy_counts = 0
        self.empty_honeycomb_count = 0
    
    def _locate_item_index(self, item_search_string, item_type=None, seed=None):
        '''Finds the index of every item type, then run the functions to pull their information'''
        item_index = 0
        item_list = []
        while(item_index > -1):
            item_index = self.mm.find(bytes.fromhex(item_search_string), item_index)
            if(item_index > -1):
                item_list.append(item_index)
                item_index = item_index + 1
        if(len(item_list) > 0):
            if(item_type == "Struct"):
                self.struct_index_list += item_list
                self._obtain_struct_parameters(item_list)
            elif(item_type == "No_Flagged_Object"):
                self.non_flag_object_index_list += item_list
                self._obtain_object_parameters(item_list, "No_Flagged_Object")
            elif(item_type == "Ground_Enemy"):
                self.ground_enemy_index_list += item_list
                self._obtain_object_parameters(item_list, "Ground_Enemy")
            elif(item_type == "Wall_Enemy"):
                self.wall_enemy_index_list += item_list
                self._obtain_object_parameters(item_list, "Wall_Enemy")
            elif(item_type == "Flying_Enemy"):
                self.flying_enemy_index_list += item_list
                self._obtain_object_parameters(item_list, "Flying_Enemy")
            elif(item_type == "Note_Door"):
                self._remove_object(item_list)
            elif(item_type == "Magic_Barrier"):
                self._remove_object(item_list)
            elif(item_type == "Warp"):
                self.warp_index_list += item_list
                self._obtain_object_parameters(item_list, "Warp")
            elif(item_type == "Bottles_Mound"):
                self.bottles_index_list += item_list
                self._obtain_object_parameters(item_list, "Bottles_Mound")
        return item_list
    
    def _obtain_struct_parameters(self, item_list):
        '''Grabs the necessary information for a struct'''
        # Index 0 - ID 1
        # Index 1 - ID 2
        # Index 2 - Unknown
        # Index 3 - Unknown
        # Index 10 - Size
        for struct_index in item_list:
            self.struct_info_list.append({
                "Obj_ID1": self.mm[struct_index],
                "Obj_ID2": self.mm[struct_index+1],
                "Unknown1": 0,
                "Unknown2": 160,
                "Size": self.mm[struct_index+10],
                })
    
    def _set_struct(self, struct_index, struct_info):
        '''Overwrites the previous struct info with new info'''
        self.mm[struct_index] = struct_info["Obj_ID1"]
        self.mm[struct_index+1] = struct_info["Obj_ID2"]
        self.mm[struct_index+2] = struct_info["Unknown1"]
        self.mm[struct_index+3] = struct_info["Unknown2"]
        self.mm[struct_index+10] = struct_info["Size"]
    
    def _obtain_object_parameters(self, item_list, item_type):
        '''Grabs the necessary information for an object'''
        # Index 0 - Object Script 1
        # Index 1 - Object Script 2
        # Index 2 - ID 1
        # Index 3 - ID 2
        if(item_type == "No_Flagged_Object"):
            for object_index in item_list:
                self.non_flag_object_info_list.append({
                    "Script1": self.mm[object_index],
                    "Script2": self.mm[object_index+1],
                    "Obj_ID1": self.mm[object_index+2],
                    "Obj_ID2": self.mm[object_index+3],
                    })
        elif(item_type == "Ground_Enemy"):
            for object_index in item_list:
                self.ground_enemy_info_list.append({
                    "Script1": self.mm[object_index],
                    "Script2": self.mm[object_index+1],
                    "Obj_ID1": self.mm[object_index+2],
                    "Obj_ID2": self.mm[object_index+3],
                    })
        elif(item_type == "Wall_Enemy"):
            for object_index in item_list:
                self.wall_enemy_info_list.append({
                    "Script1": self.mm[object_index],
                    "Script2": self.mm[object_index+1],
                    "Obj_ID1": self.mm[object_index+2],
                    "Obj_ID2": self.mm[object_index+3],
                    })
        elif(item_type == "Flying_Enemy"):
            for object_index in item_list:
                self.flying_enemy_info_list.append({
                    "Script1": self.mm[object_index],
                    "Script2": self.mm[object_index+1],
                    "Obj_ID1": self.mm[object_index+2],
                    "Obj_ID2": self.mm[object_index+3],
                    })
        elif(item_type == "Warp"):
            for object_index in item_list:
                self.warp_info_list.append({
                    "Obj_ID1": self.mm[object_index+8],
                    "Obj_ID2": self.mm[object_index+9],
                    })
        elif(item_type == "Bottles_Mound"):
            for object_index in item_list:
                self.bottles_info_list.append({
                    "Script1": self.mm[object_index],
                    "Script2": self.mm[object_index+1],
                    "Obj_ID1": self.mm[object_index+2],
                    "Obj_ID2": self.mm[object_index+3],
                    })
    
    def _set_object(self, object_index, object_info):
        '''Overwrites the previous object info with new info'''
        self.mm[object_index] = object_info["Script1"]
        self.mm[object_index+1] = object_info["Script2"]
        self.mm[object_index+2] = object_info["Obj_ID1"]
        self.mm[object_index+3] = object_info["Obj_ID2"]
        if((object_info["Script1"] == 0x19) and (object_info["Script2"] == 0x0C) and 
           (object_info["Obj_ID1"] == 0x02) and (object_info["Obj_ID2"] == 0x89)):
            rot_val = self.mm[object_index + 6]
            if(rot_val >= 45):
                self.mm[object_index + 6] = rot_val - 45
            else:
                self.mm[object_index + 6] = rot_val + 135
    
    def _locate_flagged_object_index(self, object_search_string, flag_search_string):
        '''Finds the index of a flagged object and its flag, then run the functions to pull their information'''
        object_index = self.mm.find(bytes.fromhex(object_search_string))
        flag_index = self.mm.find(bytes.fromhex(flag_search_string))
        if((object_index != -1) and (flag_index != -1)):
            self.flagged_object_index_list.append((object_index, flag_index))
            self._obtain_flagged_object_parameters(object_index, flag_index)
    
    def _obtain_flagged_object_parameters(self, object_index, flag_index):
        '''Grabs the necessary information for a flagged object and its flag'''
        # Index 6 - Script 1
        # Index 7 - Script 2
        # Index 8 - ID 1
        # Index 9 - ID 2
        # Index 10 - Unknown
        # Index 11 - Unknown
        # Index 12 - Unknown (Rotation 1?)
        # Index 13 - Rotation
        # Index 14 - Size 1
        # Index 15 - Size 2
        self.flagged_object_info_list.append(({
            "Script1": self.mm[object_index+6],
            "Script2": self.mm[object_index+7],
            "Obj_ID1": self.mm[object_index+8],
            "Obj_ID2": self.mm[object_index+9],
            "Unknown10": self.mm[object_index+10],
            "Unknown11": self.mm[object_index+11],
            "Rotation1": self.mm[object_index+12],
            "Rotation2": self.mm[object_index+13],
            "Size1": self.mm[object_index+14],
            "Size2": self.mm[object_index+15],
            },
        # Index 6 - Radius
        # Index 7 - IDK 8
        # Index 8 - ID 1
        # Index 9 - ID 2
        # Index 10 - Unknown
        # Index 11 - Unknown
        # Index 12 - Unknown
        # Index 13 - Unknown
        # Index 14 - Unknown
        # Index 15 - Unknown
        {
            "Radius": self.mm[flag_index+6],
            "Unknown7": self.mm[flag_index+7],
            "Obj_ID1": self.mm[flag_index+8],
            "Obj_ID2": self.mm[flag_index+9],
            "Unknown10": self.mm[flag_index+10],
            "Unknown11": self.mm[flag_index+11],
            "Unknown12": self.mm[flag_index+12],
            "Unknown13": self.mm[flag_index+13],
            "Unknown14": self.mm[flag_index+14],
            "Unknown15": self.mm[flag_index+15],
            }))
    
    def _set_flagged_object(self, object_index, obj_info, flag_index, flag_info):
        '''Overwrites the previous flagged object info and flag info with new info'''
        # OBJECT
        self.mm[object_index+6] = obj_info["Script1"]
        self.mm[object_index+7] = obj_info["Script2"]
        self.mm[object_index+8] = obj_info["Obj_ID1"]
        self.mm[object_index+9] = obj_info["Obj_ID2"]
        self.mm[object_index+10] = obj_info["Unknown10"]
        self.mm[object_index+11] = obj_info["Unknown11"]
        self.mm[object_index+12] = obj_info["Rotation1"]
        self.mm[object_index+13] = obj_info["Rotation2"]
        self.mm[object_index+14] = obj_info["Size1"]
        self.mm[object_index+15] = obj_info["Size2"]
        # FLAG
        self.mm[flag_index+6] = flag_info["Radius"]
        self.mm[flag_index+7] = flag_info["Unknown7"]
        self.mm[flag_index+8] = flag_info["Obj_ID1"]
        self.mm[flag_index+9] = flag_info["Obj_ID2"]
        self.mm[flag_index+10] = flag_info["Unknown10"]
        self.mm[flag_index+11] = flag_info["Unknown11"]
        self.mm[flag_index+12] = flag_info["Unknown12"]
        self.mm[flag_index+13] = flag_info["Unknown13"]
        self.mm[flag_index+14] = flag_info["Unknown14"]
        self.mm[flag_index+15] = flag_info["Unknown15"]

    def _locate_sequence_index(self, item_search_string, item_type="EPPIIISA"):
        '''Finds the index of every sequence item type, then run the functions to pull their information'''
        item_index = self.mm.find(bytes.fromhex(item_search_string))
        if(item_index != -1):
            use_this = True
            if(item_type == "Clanker_Rings"):
                use_this = self._skip_non_ring(item_index)
            if(use_this):
                self.sequence_index_list.append(item_index)
                self._obtain_sequence_parameters(item_index)

    def _obtain_sequence_parameters(self, item_index):
        '''Grabs the necessary information for a sequence object'''
        # Index 0 - Object Script 1
        # Index 1 - Object Script 2
        # Index 2 - ID 1
        # Index 3 - ID 2
        self.sequence_info_list.append({
            "Script1": self.mm[item_index],
            "Script2": self.mm[item_index+1],
            "Obj_ID1": self.mm[item_index+2],
            "Obj_ID2": self.mm[item_index+3],
            }
        )

    def _set_sequence(self, sequence_index, sequence_info):
        '''Overwrites the previous sequence object info with new info'''
        # SEQUENCE
        self.mm[sequence_index] = sequence_info["Script1"]
        self.mm[sequence_index+1] = sequence_info["Script2"]
        self.mm[sequence_index+2] = sequence_info["Obj_ID1"]
        self.mm[sequence_index+3] = sequence_info["Obj_ID2"]
    
    def _locate_sequence_tuple_index(self, item_search_tuple):
        '''Finds the index of every sequence pair item type, then run the functions to pull their information'''
        item_index1 = self.mm.find(bytes.fromhex(item_search_tuple[0]))
        item_index2 = self.mm.find(bytes.fromhex(item_search_tuple[1]))
        if((item_index1 != -1) and (item_index2 != -1)):
            self.sequence_index_list.append((item_index1, item_index2))
            self._obtain_sequence_tuple_parameters(item_index1, item_index2)

    def _obtain_sequence_tuple_parameters(self, item_index1, item_index2):
        '''Grabs the necessary information for a sequence pair object'''
        # Index 0 - Object Script 1
        # Index 1 - Object Script 2
        # Index 2 - ID 1
        # Index 3 - ID 2
        self.sequence_info_list.append(({
            "X_LOC1": self.mm[item_index1-6],
            "X_LOC2": self.mm[item_index1-5],
            "Y_LOC1": self.mm[item_index1-4],
            "Y_LOC2": self.mm[item_index1-3],
            "Z_LOC1": self.mm[item_index1-2],
            "Z_LOC2": self.mm[item_index1-1],
            "Script1": self.mm[item_index1],
            "Script2": self.mm[item_index1+1],
            "Obj_ID1": self.mm[item_index1+2],
            "Obj_ID2": self.mm[item_index1+3],
            },
            {
            "X_LOC1": self.mm[item_index2-6],
            "X_LOC2": self.mm[item_index2-5],
            "Y_LOC1": self.mm[item_index2-4],
            "Y_LOC2": self.mm[item_index2-3],
            "Z_LOC1": self.mm[item_index2-2],
            "Z_LOC2": self.mm[item_index2-1],
            "Script1": self.mm[item_index2],
            "Script2": self.mm[item_index2+1],
            "Obj_ID1": self.mm[item_index2+2],
            "Obj_ID2": self.mm[item_index2+3],
            })
        )
        
    def _set_sequence_tuple(self, item_index1, item_info1, item_index2, item_info2):
        '''Overwrites the previous sequence pair object info with new info'''
        # Item 1
        self.mm[item_index1-6] = item_info1["X_LOC1"]
        self.mm[item_index1-5] = item_info1["X_LOC2"]
        self.mm[item_index1-4] = item_info1["Y_LOC1"]
        self.mm[item_index1-3] = item_info1["Y_LOC2"]
        self.mm[item_index1-2] = item_info1["Z_LOC1"]
        self.mm[item_index1-1] = item_info1["Z_LOC2"]
        self.mm[item_index1]   = item_info1["Script1"]
        self.mm[item_index1+1] = item_info1["Script2"]
        self.mm[item_index1+2] = item_info1["Obj_ID1"]
        self.mm[item_index1+3] = item_info1["Obj_ID2"]
        # Item 2
        self.mm[item_index2-6] = item_info2["X_LOC1"]
        self.mm[item_index2-5] = item_info2["X_LOC2"]
        self.mm[item_index2-4] = item_info2["Y_LOC1"]
        self.mm[item_index2-3] = item_info2["Y_LOC2"]
        self.mm[item_index2-2] = item_info2["Z_LOC1"]
        self.mm[item_index2-1] = item_info2["Z_LOC2"]
        self.mm[item_index2]   = item_info2["Script1"]
        self.mm[item_index2+1] = item_info2["Script2"]
        self.mm[item_index2+2] = item_info2["Obj_ID1"]
        self.mm[item_index2+3] = item_info2["Obj_ID2"]

    def _locate_camera_sequence_index(self, object_search_string, camera_search_string):
        '''Finds the index of every sequence item with its associated camera, then run the functions to pull their information'''
        object_index = self.mm.find(bytes.fromhex(object_search_string))
        camera_index = self.mm.find(bytes.fromhex(camera_search_string))
        if((object_index != -1) and (camera_index != -1)):
            self.sequence_index_list.append((object_index, camera_index))
            self._obtain_camera_sequence_parameters(object_index, camera_index)

    def _obtain_camera_sequence_parameters(self, sequence_index, camera_index):
        '''Grabs the necessary information for a sequence object and its camera'''
        # Index 0 - Object Script 1
        # Index 1 - Object Script 2
        # Index 2 - ID 1
        # Index 3 - ID 2
        self.sequence_info_list.append(({
            "Script1": self.mm[sequence_index],
            "Script2": self.mm[sequence_index+1],
            "Obj_ID1": self.mm[sequence_index+2],
            "Obj_ID2": self.mm[sequence_index+3],
            },
        # Index 2 - ID 1
            {
            "Camera_ID": self.mm[camera_index+2],
            }
            )
        )
        
    def _set_camera_sequence(self, sequence_index, sequence_info, camera_index, camera_info):
        '''Overwrites the previous sequence object and its camera info with new info'''
        # SEQUENCE
        self.mm[sequence_index] = sequence_info["Script1"]
        self.mm[sequence_index+1] = sequence_info["Script2"]
        self.mm[sequence_index+2] = sequence_info["Obj_ID1"]
        self.mm[sequence_index+3] = sequence_info["Obj_ID2"]
        # CAMERA
        self.mm[camera_index+2] = camera_info["Camera_ID"]
    
    def _replace_object_parameters(self, item_list, replace_list, seed=0):
        '''Overwrites the previous object info with randomly selected info from a list'''
        for item_index in item_list:
            random.seed(a=(seed + self.setup_address))
            replace_choice = random.choice(replace_list)
            self.mm[item_index] = int(replace_choice[:2], 16)
            self.mm[item_index+1] = int(replace_choice[2:4], 16)
            self.mm[item_index+2] = int(replace_choice[4:6], 16)
            self.mm[item_index+3] = int(replace_choice[6:], 16)
    
    def _replace_each_object_parameters(self, search_string_list, replacement_list):
        '''PyDoc'''
        for index_num in range(len(search_string_list)):
            self._edit_object(search_string_list[index_num],
                              replacement_list[index_num])
    
    def _replace_all_in_area(self, search_string, replace_list):
        '''PyDoc'''
        item_index = self._locate_item_index(search_string)
        if(item_index):
            for item_index_start in item_index:
                self._edit_object_index(item_index_start, replace_list)
    
    def _remove_object(self, item_list):
        '''Replaces note doors with an object that doesn't seem to do anything'''
        for item_index in item_list:
            self.mm[item_index] = 0x19
            self.mm[item_index+1] = 0xC
            self.mm[item_index+2] = 0x2
            self.mm[item_index+3] = 0x68
            self.mm[item_index+9] = 0x1
    
    ######################
    ### MISC FUNCTIONS ###
    ######################

    def _edit_object(self, item_search_string, replacement_dict):
        '''Takes specific parameters of an object and replaces them with the info from a dictionary'''
        item_index = self.mm.find(bytes.fromhex(item_search_string))
        if(item_index > -1):
            for index_add in replacement_dict:
                self.mm[item_index + index_add] = replacement_dict[index_add]
            return True
        return False

    def _edit_object_index(self, item_index_start, replacement_dict):
        '''Takes specific parameters of an object and replaces them with the info from a dictionary'''
        for index_add in replacement_dict:
            self.mm[item_index_start + index_add] = replacement_dict[index_add]
    
    def _does_string_exist(self, item_search_string):
        item_index = self.mm.find(bytes.fromhex(item_search_string))
        if(item_index >= 0):
            return True
        return False

    def adjust_ttc_oob_egg(self):
        '''Moves the out of bounds egg in TTC slightly higher'''
        ttc_egg_index = self.mm.find(bytes.fromhex("F078041E06D6"))
        self.mm[ttc_egg_index+2] = 4
        self.mm[ttc_egg_index+3] = 166
    
    def adjust_ttc_lighthouse_token(self):
        '''PyDoc'''
        pass
    
    def _skip_non_ring(self, item_index):
        '''Skips a string pattern that looks like a Clanker ring'''
        if(self.mm[item_index - 1] == 119):
            print("Skipping Non-Ring")
            return False
        return True