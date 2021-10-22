'''
Created on Aug 31, 2021

@author: Cyrus
'''

#####################
### PYTHON IMPORT ###
#####################

import mmap

###########################
### GENERIC MODEL CLASS ###
###########################

class Model():
    '''Generic model class'''
    def __init__(self, file_dir, address):
        '''Initializes generic model class'''
        self._file_dir = file_dir
        self.address = address
    
    def _create_mm(self):
        '''Creates the currently used mmap for the model'''
        with open(f"{self._file_dir}Randomized_ROM\\{self.address}-Decompressed.bin", "r+b") as f:
            self.mm = mmap.mmap(f.fileno(), 0)

    def _sort_rgb_colors(self, rgb_list):
        '''Sorts the low, medium, and high values of an rgb list'''
        rgb_list.sort()
        if(rgb_list[0] > 85):
            rgb_list[0] = 85
        if(rgb_list[1] < 85):
            rgb_list[1] = 85
        elif(rgb_list[1] > 170):
            rgb_list[1] = 170
        if(rgb_list[2] < 170):
            rgb_list[2] = 170
        return rgb_list


    def _adjust_colors(self, model_dict):
        '''
        Changes the current vertex shading color to another color based on its previous color in order to maintain shading
        # Colors! 1=Low, 2=Med, 3=High
        # 111 - Black            112 - Navy           113 - Blue
        # 121 - Swamp            122 - Avery          123 - Cosmos
        # 131 - Green            132 - Emerald        133 - Teal
        # 211 - Rust             212 - Purple         213 - Violet
        # 221 - Shit             222 - Gray           223 - Lavender
        # 231 - Lime2            232 - Lime           233 - Turquoise
        # 311 - Red              312 - Pink           313 - Magenta
        # 321 - Brown            322 - Amber          323 - Magenta2
        # 331 - Yellow           332 - Gold           333 - White
        '''
        for body_part in model_dict:
            model_list = model_dict[body_part]["Model_List"]
            color = model_dict[body_part]["New_Color"]
            if((not model_list) or (not color)):
                continue
            if(color.lower() == "black"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = low
                            self.mm[index+0x0D] = low
                            self.mm[index+0x0E] = low
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "navy"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = low
                            self.mm[index+0x0D] = low
                            self.mm[index+0x0E] = med
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "blue"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = low
                            self.mm[index+0x0D] = low
                            self.mm[index+0x0E] = high
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "swamp"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = low
                            self.mm[index+0x0D] = med
                            self.mm[index+0x0E] = low
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "avery"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = low
                            self.mm[index+0x0D] = med
                            self.mm[index+0x0E] = med
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "cosmos"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = low
                            self.mm[index+0x0D] = med
                            self.mm[index+0x0E] = high
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "green"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = low
                            self.mm[index+0x0D] = high
                            self.mm[index+0x0E] = low
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "emerald"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = low
                            self.mm[index+0x0D] = high
                            self.mm[index+0x0E] = med
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "teal"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = low
                            self.mm[index+0x0D] = high
                            self.mm[index+0x0E] = high
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "rust"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = med
                            self.mm[index+0x0D] = low
                            self.mm[index+0x0E] = low
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "purple"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = med
                            self.mm[index+0x0D] = low
                            self.mm[index+0x0E] = med
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "violet"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = med
                            self.mm[index+0x0D] = low
                            self.mm[index+0x0E] = high
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "shit"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = med
                            self.mm[index+0x0D] = med
                            self.mm[index+0x0E] = low
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "gray"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = med
                            self.mm[index+0x0D] = med
                            self.mm[index+0x0E] = med
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "lavender"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = med
                            self.mm[index+0x0D] = med
                            self.mm[index+0x0E] = high
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "lime2"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = med
                            self.mm[index+0x0D] = high
                            self.mm[index+0x0E] = low
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "lime"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = med
                            self.mm[index+0x0D] = high
                            self.mm[index+0x0E] = med
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "turquoise"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = med
                            self.mm[index+0x0D] = high
                            self.mm[index+0x0E] = high
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "red"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = high
                            self.mm[index+0x0D] = low
                            self.mm[index+0x0E] = low
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "pink"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = high
                            self.mm[index+0x0D] = low
                            self.mm[index+0x0E] = med
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "magenta"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = high
                            self.mm[index+0x0D] = low
                            self.mm[index+0x0E] = high
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "brown"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = high
                            self.mm[index+0x0D] = med
                            self.mm[index+0x0E] = low
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "amber"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = high
                            self.mm[index+0x0D] = med
                            self.mm[index+0x0E] = med
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "magenta2"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = high
                            self.mm[index+0x0D] = med
                            self.mm[index+0x0E] = high
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "yellow"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = high
                            self.mm[index+0x0D] = high
                            self.mm[index+0x0E] = low
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "gold"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = high
                            self.mm[index+0x0D] = high
                            self.mm[index+0x0E] = med
                            self.mm[index+0x0F] = 0xFE
            elif(color.lower() == "white"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.mm[index+0x0C] = high
                            self.mm[index+0x0D] = high
                            self.mm[index+0x0E] = high
                            self.mm[index+0x0F] = 0xFE


    def _adjust_textures(self, model_dict):
        '''
        Changes the current texture color to another color; NOT based on its previous color
        # Colors! 1=Low, 2=Med, 3=High
        # 0001 - Black            008F - Navy           0031 - Blue
        # 0301 - Swamp            0211 - Avery          0331 - Cosmos
        # 0F0F - Green            0F8F - Emerald        0FFF - Teal
        # 0501 - Rust             801F - Purple         0631 - Violet
        # 8401 - Shit             841F - Gray           52B1 - Lavender
        # 8F0F - Lime2            5F21 - Lime           5F37 - Turquoise
        # F001 - Red              F2E1 - Pink           F0FF - Magenta
        # CB0F - Brown            E3A1 - Amber          E2BF - Magenta2
        # FF0F - Yellow           A54F - Gold           FFFF - White
        '''
        for body_part in model_dict:
            if("Texture" in model_dict[body_part]):
                color = model_dict[body_part]["New_Color"]
                if(not color):
                    continue
                if(color.lower() == "black"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x00
                            self.mm[byte_index+1] = 0x01
                elif(color.lower() == "navy"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x00
                            self.mm[byte_index+1] = 0x8F
                elif(color.lower() == "blue"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x00
                            self.mm[byte_index+1] = 0x31
                elif(color.lower() == "swamp"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x03
                            self.mm[byte_index+1] = 0x01
                elif(color.lower() == "avery"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x02
                            self.mm[byte_index+1] = 0x11
                elif(color.lower() == "cosmos"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x03
                            self.mm[byte_index+1] = 0x31
                elif(color.lower() == "green"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x0F
                            self.mm[byte_index+1] = 0x0F
                elif(color.lower() == "emerald"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x0F
                            self.mm[byte_index+1] = 0x8F
                elif(color.lower() == "teal"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x0F
                            self.mm[byte_index+1] = 0xFF
                elif(color.lower() == "rust"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x50
                            self.mm[byte_index+1] = 0x01
                elif(color.lower() == "purple"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x80
                            self.mm[byte_index+1] = 0x1F
                elif(color.lower() == "violet"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x60
                            self.mm[byte_index+1] = 0x31
                elif(color.lower() == "shit"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x84
                            self.mm[byte_index+1] = 0x01
                elif(color.lower() == "gray"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x84
                            self.mm[byte_index+1] = 0x1F
                elif(color.lower() == "lavender"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x52
                            self.mm[byte_index+1] = 0xB1
                elif(color.lower() == "lime2"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x8F
                            self.mm[byte_index+1] = 0x0F
                elif(color.lower() == "lime"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x5F # 0x8F8F
                            self.mm[byte_index+1] = 0x21 # 5F21
                elif(color.lower() == "turquoise"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0x5F
                            self.mm[byte_index+1] = 0x37
                elif(color.lower() == "red"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0xF0
                            self.mm[byte_index+1] = 0x01
                elif(color.lower() == "pink"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0xF2
                            self.mm[byte_index+1] = 0xE1
                elif(color.lower() == "magenta"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0xF0
                            self.mm[byte_index+1] = 0xFF
                elif(color.lower() == "brown"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0xCB
                            self.mm[byte_index+1] = 0x0F
                elif(color.lower() == "amber"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0xE3
                            self.mm[byte_index+1] = 0xA1
                elif(color.lower() == "magenta2"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0xE2
                            self.mm[byte_index+1] = 0xBF
                elif(color.lower() == "yellow"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0xFF
                            self.mm[byte_index+1] = 0x0F
                elif(color.lower() == "gold"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0xA5 #0xFF
                            self.mm[byte_index+1] = 0x4F #0x8F
                elif(color.lower() == "white"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.mm[byte_index] = 0xFF
                            self.mm[byte_index+1] = 0XFF

    def _main(self, model_dict):
        '''Runs through the process of changing the colors of a model based on the given dictionary'''
        self._create_mm()
        try:
            self._adjust_colors(model_dict)
            self._adjust_textures(model_dict)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.mm.close()