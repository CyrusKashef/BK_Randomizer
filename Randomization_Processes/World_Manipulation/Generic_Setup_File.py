'''
Created on Aug 30, 2021

@author: Cyrus
'''

import mmap

class SetupFile():
    def __init__(self, setup_address, setup_name=None):
        self.cwd = r"C:\\Users\\Cyrus\\eclipse-workspace\\BK_Rando_v2.0\\Randomized_ROM\\"
        self.setup_name = setup_name
        self.setup_address = setup_address
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
        with open(f"{self.cwd}{setup_address}-Decompressed.bin", "r+b") as f:
            self.mm = mmap.mmap(f.fileno(), 0)
    
    def _locate_item_index(self, item_search_string, item_type):
        item_index = 0
        item_list = []
        while(item_index > -1):
            item_index = self.mm.find(bytes.fromhex(item_search_string), item_index)
            if(item_index > -1):
                item_list.append(item_index)
                item_index = item_index + 1
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
    
    def _obtain_struct_parameters(self, item_list):
        # Index 0 - ID 1
        # Index 1 - ID 2
        # Index 2 - Unknown
        # Index 3 - Unknown
        # Index 10 - Size
        for struct_index in item_list:
            self.struct_info_list.append({
                "Obj_ID1": self.mm[struct_index],
                "Obj_ID2": self.mm[struct_index+1],
                "Unknown1": self.mm[struct_index+2],
                "Unknown2": self.mm[struct_index+3],
                "Size": self.mm[struct_index+10],
                })
    
    def _set_struct(self, struct_index, struct_info):
        self.mm[struct_index] = struct_info["Obj_ID1"]
        self.mm[struct_index+1] = struct_info["Obj_ID2"]
        self.mm[struct_index+2] = struct_info["Unknown1"]
        self.mm[struct_index+3] = struct_info["Unknown2"]
        self.mm[struct_index+10] = struct_info["Size"]
    
    def _obtain_object_parameters(self, item_list, item_type):
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
    
    def _set_object(self, object_index, object_info):
        self.mm[object_index] = object_info["Script1"]
        self.mm[object_index+1] = object_info["Script2"]
        self.mm[object_index+2] = object_info["Obj_ID1"]
        self.mm[object_index+3] = object_info["Obj_ID2"]
    
    def _locate_flagged_object_index(self, object_search_string, flag_search_string):
        object_index = self.mm.find(bytes.fromhex(object_search_string))
        flag_index = self.mm.find(bytes.fromhex(flag_search_string))
        if((object_index != -1) and (flag_index != -1)):
            self.flagged_object_index_list.append((object_index, flag_index))
            self._obtain_flagged_object_parameters(object_index, flag_index)
    
    def _obtain_flagged_object_parameters(self, object_index, flag_index):
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
    
    def _obtain_camera_parameters(self, camera_index):
        # Index 2 - ID 1
        pass