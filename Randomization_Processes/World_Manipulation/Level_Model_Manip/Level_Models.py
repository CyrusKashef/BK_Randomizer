'''
Created on Dec 6, 2021

@author: Cyrus
'''

import mmap
from math import floor
from math import ceil
from Randomization_Processes.Common_Functions import leading_zeros

class Level_Model_Class():
    def __init__(self, file_dir, address, min_x=-8000, max_x=8000, min_z=-8000, max_z=8000):
        self._address = address
        self._file_dir = file_dir
        with open(f"{self._file_dir}Randomized_ROM/{address}-Decompressed.bin", "r+b") as level_model_file:
            self.mm = mmap.mmap(level_model_file.fileno(), 0)
        self._file_length = len(self.mm)
        self._geometry_layout_offset = None
        self._min_x = min_x
        self._max_x = max_x
        self._min_z = min_z
        self._max_z = max_z
    
    ########################
    ### COMMON FUNCTIONS ###
    ########################
    
    def leading_zeros(self, num, num_of_digits):
        '''Adds leading zeros to a string that's supposed to be a certain number of digits in length'''
        if(isinstance(num, int)):
            num = str(hex(num))[2:].upper()
        while (len(num) < num_of_digits):
            num = "0" + num
        return num
    
    def possible_negative(self, int_val):
        '''If value would be a negative hex value (greater than 0x8000), converts to negative. Otherwise returns initial value'''
        if(int_val > 0x8000):
            int_val = int_val - 0x10000
        return int_val
    
    ##############
    ### HEADER ###
    ##############

    def _grab_geometry_layout_offset(self):
        self._geometry_layout_offset = int(self.leading_zeros(self.mm[4], 2) +
                                           self.leading_zeros(self.mm[5], 2) +
                                           self.leading_zeros(self.mm[6], 2) +
                                           self.leading_zeros(self.mm[7], 2), 16)
        self._texture_setup_offset = int(self.leading_zeros(self.mm[8], 2) +
                                         self.leading_zeros(self.mm[9], 2), 16)
        self._geo_type = int(self.leading_zeros(self.mm[10], 2) +
                             self.leading_zeros(self.mm[11], 2), 16)
        self._display_list_setup_offset = int(self.leading_zeros(self.mm[12], 2) +
                                              self.leading_zeros(self.mm[13], 2) +
                                              self.leading_zeros(self.mm[14], 2) +
                                              self.leading_zeros(self.mm[15], 2), 16)
        self._vertex_store_setup_offset = int(self.leading_zeros(self.mm[16], 2) +
                                              self.leading_zeros(self.mm[17], 2) +
                                              self.leading_zeros(self.mm[18], 2) +
                                              self.leading_zeros(self.mm[19], 2), 16)
        self._animation_setup_offset = int(self.leading_zeros(self.mm[24], 2) +
                                           self.leading_zeros(self.mm[25], 2) +
                                           self.leading_zeros(self.mm[26], 2) +
                                           self.leading_zeros(self.mm[27], 2), 16)
        self._collision_setup_offset = int(self.leading_zeros(self.mm[28], 2) +
                                           self.leading_zeros(self.mm[29], 2) +
                                           self.leading_zeros(self.mm[30], 2) +
                                           self.leading_zeros(self.mm[31], 2), 16)
        self._effects_setup_end_address = int(self.leading_zeros(self.mm[32], 2) +
                                              self.leading_zeros(self.mm[29], 2) +
                                              self.leading_zeros(self.mm[33], 2) +
                                              self.leading_zeros(self.mm[34], 2), 16)
        self._effects_setup_offset = int(self.leading_zeros(self.mm[36], 2) +
                                         self.leading_zeros(self.mm[37], 2) +
                                         self.leading_zeros(self.mm[38], 2) +
                                         self.leading_zeros(self.mm[39], 2), 16)
        
    def _print_offsets(self):
        print(f"Geometry Layout Offset: {hex(self._geometry_layout_offset)}")
        print(f"Texture Setup Offset: {hex(self._texture_setup_offset)}")
        print(f"Display List Setup Offset: {hex(self._display_list_setup_offset)}")
        print(f"Vertex Store Setup Offset: {hex(self._vertex_store_setup_offset)}")
        print(f"Animation Setup Offset: {hex(self._animation_setup_offset)}")
        print(f"Collision Setup Offset: {hex(self._collision_setup_offset)}")
        print(f"Effects Setup Offset: {hex(self._effects_setup_offset)}")
    
    def _header_main(self):
        self._grab_geometry_layout_offset()
#         self._print_offsets()
    
    #######################
    ### GEOMETRY LAYOUT ###
    #######################
    
    def _SORT(self):
        print("SORT")
        return 4
    
    def _BONE(self):
        print("BONE")
        return 4
    
    def _LOAD_DL(self):
        print("LOAD_DL")
        return 4
    
    def _SKINNING(self):
        print("SKINNING")
        return 4
    
    def _LOD(self):
        print("LOD")
        return 4
    
    def _REFERENCE_POINT(self):
        print("REFERENCE_POINT")
        return 4
    
    def _SELECTOR(self):
        print("SELECTOR")
        return 4
    
    def _DRAW_DISTANCE(self):
        print("DRAW_DISTANCE")
        return 4
    
    def _geometry_layout_main(self):
        known_sort_commands_dict = {
            0x1: self._SORT, 0x2: self._BONE,            0x3: self._LOAD_DL,  0x5: self._SKINNING,
            0x8: self._LOD,  0xA: self._REFERENCE_POINT, 0xC: self._SELECTOR, 0xD: self._DRAW_DISTANCE,
            }
        curr_index = self._geometry_layout_offset
        while(curr_index < self._file_length):
            if((self.mm[curr_index] == 0) and (self.mm[curr_index + 1] == 0) and (self.mm[curr_index + 2] == 0) and (self.mm[curr_index + 3] in known_sort_commands_dict)):
                command = self.mm[curr_index + 3]
                index_add = known_sort_commands_dict[command]()
                curr_index += index_add
            else:
                #print(f"{self.leading_zeros(self.mm[curr_index], 2)} {self.leading_zeros(self.mm[curr_index + 1], 2)} {self.leading_zeros(self.mm[curr_index + 2], 2)} {self.leading_zeros(self.mm[curr_index + 3], 2)}")
                curr_index += 4
    
    #####################
    ### TEXTURE SETUP ###
    #####################
    
    ##########################
    ### DISPLAY LIST SETUP ###
    ##########################
    
    ##########################
    ### VERTEX STORE SETUP ###
    ##########################
    
    def _vertex_header(self):
        self._vertex_draw_distance_negative_coords_a = int(self.leading_zeros(self.mm[self._vertex_store_setup_offset], 2) +
                                                           self.leading_zeros(self.mm[self._vertex_store_setup_offset + 1], 2), 16)
        self._vertex_draw_distance_negative_coords_b = int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + 2], 2) +
                                                           self.leading_zeros(self.mm[self._vertex_store_setup_offset + 3], 2), 16)
        self._vertex_draw_distance_negative_coords_c = int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + 4], 2) +
                                                           self.leading_zeros(self.mm[self._vertex_store_setup_offset + 5], 2), 16)
        self._vertex_draw_distance_positive_coords_d = int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + 6], 2) +
                                                           self.leading_zeros(self.mm[self._vertex_store_setup_offset + 7], 2), 16)
        self._vertex_draw_distance_positive_coords_e = int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + 8], 2) +
                                                           self.leading_zeros(self.mm[self._vertex_store_setup_offset + 9], 2), 16)
        self._vertex_draw_distance_positive_coords_f = int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + 10], 2) +
                                                           self.leading_zeros(self.mm[self._vertex_store_setup_offset + 11], 2), 16)
        self._object_coordinate_range_g = int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + 12], 2) +
                                              self.leading_zeros(self.mm[self._vertex_store_setup_offset + 13], 2), 16)
        self._object_coordinate_range_h = int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + 14], 2) +
                                              self.leading_zeros(self.mm[self._vertex_store_setup_offset + 15], 2), 16)
        self._collision_range_objects = int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + 16], 2) +
                                            self.leading_zeros(self.mm[self._vertex_store_setup_offset + 17], 2), 16)
        self._collision_range_banjo = int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + 18], 2) +
                                          self.leading_zeros(self.mm[self._vertex_store_setup_offset + 19], 2), 16)
        self._vertex_count_times_two = int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + 20], 2) +
                                           self.leading_zeros(self.mm[self._vertex_store_setup_offset + 21], 2), 16)
#         print(f"Collision Range Objects: {hex(self._collision_range_objects)}")
#         print(f"Collision Range Banjo: {hex(self._collision_range_banjo)}")
    
    def _vertices_info(self):
        self._vertex_dict = {}
        for count in range(self._vertex_count_times_two):
            vertex_offset = count * 16
            self._vertex_dict[count] = {
                "X": self.possible_negative(int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 24], 2) +
                                                self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 25], 2), 16)),
                "Y": self.possible_negative(int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 26], 2) +
                                                self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 27], 2), 16)),
                "Z": self.possible_negative(int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 28], 2) +
                                                self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 29], 2), 16)),
                "U": self.possible_negative(int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 32], 2) +
                                                self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 33], 2), 16)),
                "V": self.possible_negative(int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 34], 2) +
                                                self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 35], 2), 16)),
                "R": self.possible_negative(int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 36], 2) +
                                                self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 37], 2), 16)),
                "G": self.possible_negative(int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 38], 2) +
                                                self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 39], 2), 16)),
                "B": self.possible_negative(int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 40], 2) +
                                                self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 41], 2), 16)),
                "A": self.possible_negative(int(self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 42], 2) +
                                                self.leading_zeros(self.mm[self._vertex_store_setup_offset + vertex_offset + 43], 2), 16)),
                }
    
    #######################
    ### ANIMATION SETUP ###
    #######################
    
    ######################
    ### COLLSION SETUP ###
    ######################
    
    def _collision_header(self):
        self._collision_info_start = (int(self.leading_zeros(self.mm[self._collision_setup_offset + 16], 2) +
                                          self.leading_zeros(self.mm[self._collision_setup_offset + 17], 2), 16) * 4) + self._collision_setup_offset + 24
#         print(f"Collision Info Start: {hex(self._collision_info_start)}")
    
    def _collision_info(self):
        self._collision_dict = {}
        vertext_dict_len = len(self._vertex_dict)
#         print(f"Vertex Dict Length: {hex(vertext_dict_len)}")
        count = 0
        for curr_index in range(self._collision_info_start, self._geometry_layout_offset, 12):
            curr_info = {
                "Tri_Index_1": int(self.leading_zeros(self.mm[curr_index], 2) +
                                   self.leading_zeros(self.mm[curr_index + 1], 2), 16),
                "Tri_Index_2": int(self.leading_zeros(self.mm[curr_index + 2], 2) +
                                   self.leading_zeros(self.mm[curr_index + 3], 2), 16),
                "Tri_Index_3": int(self.leading_zeros(self.mm[curr_index + 4], 2) +
                                   self.leading_zeros(self.mm[curr_index + 5], 2), 16),
                "Byte1": self.mm[curr_index + 6],
                "Byte2": self.mm[curr_index + 7],
                "Byte3": self.mm[curr_index + 8],
                "Byte4": self.mm[curr_index + 9],
                "Byte5": self.mm[curr_index + 10],
                "Byte6": self.mm[curr_index + 11],
                }
            if((curr_info["Tri_Index_1"] == curr_info["Tri_Index_2"]) or
               (curr_info["Tri_Index_2"] == curr_info["Tri_Index_3"]) or
               (curr_info["Tri_Index_1"] == curr_info["Tri_Index_3"]) or
               (curr_info["Tri_Index_1"] >= vertext_dict_len) or 
               (curr_info["Tri_Index_2"] >= vertext_dict_len) or 
               (curr_info["Tri_Index_3"] >= vertext_dict_len)):
                pass
            else:
                self._collision_dict[count] = curr_info
            count += 1
    
    #####################
    ### EFFECTS SETUP ###
    #####################

    ##############################
    ### COLLISION MANIPULATION ###
    ##############################
    
    def _collision_height(self):
#         print("Collision Height")
        self._collision_height_dict = {}
        for item in self._collision_dict:
            min_x = 0xFFFF
            max_x = -0xFFFF
            min_z = 0xFFFF
            max_z = -0xFFFF
            max_y = -0xFFFF
            for tri in ["Tri_Index_1", "Tri_Index_2", "Tri_Index_3"]:
                tri_index = self._collision_dict[item][tri]
                curr_x = self.possible_negative(self._vertex_dict[tri_index]["X"])
                curr_y = self.possible_negative(self._vertex_dict[tri_index]["Y"])
                curr_z = self.possible_negative(self._vertex_dict[tri_index]["Z"])
                min_x = min(curr_x, min_x)
                max_x = max(curr_x, max_x)
                if(curr_y < 6900):
                    max_y = max(curr_y, max_y)
                min_z = min(curr_z, min_z)
                max_z = max(curr_z, max_z)
            if(max_y > -500):
                for curr_x in range(max(floor(min_x/100)*100, self._min_x), min(ceil(max_x/100)*100, self._max_x), 100):
                    for curr_z in range(max(floor(min_z/100)*100, self._min_z), min(ceil(max_z/100)*100, self._max_z), 100):
                        if((curr_x, curr_z) not in self._collision_height_dict):
                            self._collision_height_dict[(curr_x, curr_z)] = max_y
                        elif(curr_y > self._collision_height_dict[(curr_x, curr_z)]):
                            self._collision_height_dict[(curr_x, curr_z)] = max_y
    
    def _find_collision_height(self):
        self._header_main()
        self._vertex_header()
        self._vertices_info()
        self._collision_header()
        self._collision_info()
        self._collision_height()
    
    def _grab_floors(self):
        self._header_main()
        self._vertex_header()
        self._vertices_info()
        self._collision_header()
        self._collision_info()
        floor_dict = {}
        for count in self._collision_dict:
            curr_info = self._collision_dict[count]
            floor_info = (curr_info["Byte1"], curr_info["Byte2"], curr_info["Byte3"], curr_info["Byte4"], curr_info["Byte5"], curr_info["Byte6"])
            if(floor_info not in floor_dict):
                floor_dict[floor_info] = 1
            else:
                floor_dict[floor_info] += 1
#         for item in sorted(floor_dict):
#             if(floor_dict[item] > 1):
#                 print(f"FLOOR BYTES: {self.leading_zeros(item[0], 2)} {self.leading_zeros(item[1], 2)} {self.leading_zeros(item[2], 2)} {self.leading_zeros(item[3], 2)} {self.leading_zeros(item[4], 2)} {self.leading_zeros(item[5], 2)} | COUNT: {floor_dict[item]}")
#             print(f"FLOOR BYTES: {self.leading_zeros(item[0], 2)} {self.leading_zeros(item[1], 2)} {self.leading_zeros(item[2], 2)} {self.leading_zeros(item[3], 2)} {self.leading_zeros(item[4], 2)} {self.leading_zeros(item[5], 2)} | COUNT: {floor_dict[item]}")

    def _change_floor_type_by_type(self, orignal_bytes, new_bytes):
        for curr_index in range(self._collision_info_start, self._geometry_layout_offset, 12):
            Byte1 = self.mm[curr_index + 6]
            Byte2 = self.mm[curr_index + 7]
            Byte3 = self.mm[curr_index + 8]
            Byte4 = self.mm[curr_index + 9]
            Byte5 = self.mm[curr_index + 10]
            Byte6 = self.mm[curr_index + 11]
            if([Byte1, Byte2, Byte3, Byte4, Byte5, Byte6] == orignal_bytes):
                self.mm[curr_index + 6] = new_bytes[0]
                self.mm[curr_index + 7] = new_bytes[1]
                self.mm[curr_index + 8] = new_bytes[2]
                self.mm[curr_index + 9] = new_bytes[3]
                self.mm[curr_index + 10] = new_bytes[4]
                self.mm[curr_index + 11] = new_bytes[5]

    def _change_floor_type_by_vert(self, vert_condition, new_bytes):
        for curr_index in range(self._collision_info_start, self._geometry_layout_offset, 12):
            Vert1 = int(leading_zeros(self.mm[curr_index], 2) + leading_zeros(self.mm[curr_index + 1], 2), 16)
            Vert2 = int(leading_zeros(self.mm[curr_index + 2], 2) + leading_zeros(self.mm[curr_index + 3], 2), 16)
            Vert3 = int(leading_zeros(self.mm[curr_index + 4], 2) + leading_zeros(self.mm[curr_index + 5], 2), 16)
            if(vert_condition(Vert1, Vert2, Vert3)):
                self.mm[curr_index + 6] = new_bytes[0]
                self.mm[curr_index + 7] = new_bytes[1]
                self.mm[curr_index + 8] = new_bytes[2]
                self.mm[curr_index + 9] = new_bytes[3]
                self.mm[curr_index + 10] = new_bytes[4]
                self.mm[curr_index + 11] = new_bytes[5]

def display_collisions(collision_height_list):
    print("Display Collisions")
    import matplotlib.pyplot as plt
    from mpl_toolkits import mplot3d
    import numpy as np
    ax = plt.axes(projection='3d')
    collision_height_dict_1 = collision_height_list[0]
    for (x, z) in collision_height_dict_1:
        y = collision_height_dict_1[(x, z)]
        if(len(collision_height_list) > 1):
            for collision_height_dict in collision_height_list[1:]:
                if((x, z) in collision_height_dict) :
                    if(collision_height_dict[(x, z)] > y):
                        y = collision_height_dict[(x, z)]
        ax.scatter(x, z, y)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
    plt.show()

if __name__ == '__main__':
    print("Treasure Trove Cove")
    level_model_obj = Level_Model_Class("C:/Users/Cyrus/eclipse-workspace/BK_Rando_v2.0/", "101F0")
    level_model_obj._find_collision_height()
    print(sorted(level_model_obj._collision_height_dict))
#     display_collisions([level_model_obj._collision_height_dict])