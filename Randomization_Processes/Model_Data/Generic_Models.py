'''
Created on Aug 31, 2021

@author: Cyrus
'''

import mmap
import shutil

class Model():
    def __init__(self, file_dir, address):
        self.dir = file_dir
        self.address = address
        self.original_file = f"{self.dir}{self.address}.bin"
    
    def _create_mm(self):
        with open(self.original_file, "r+b") as f:
            self.mm = mmap.mmap(f.fileno(), 0)
    
    def _make_copy(self, additional_name="Adjusted"):
        self.new_file = f"{self.dir}{self.address}_{additional_name}.bin"
        shutil.copyfile(self.original_file, self.new_file)
        with open(self.new_file, "r+b") as f:
            self.new_mm = mmap.mmap(f.fileno(), 0)

    def _sort_rgb_colors(self, rgb_list):
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

    # Colors! 1=Low, 2=Med, 3=High
    # 111 - Black            112 - Navy           113 - Blue
    # 121 - Swamp            122 - Avery          123 - Cosmos
    # 131 - Green            132 - Emerald        133 - Teal
    # 211 - Rust             212 - Purple         213 - Violet
    # 221 - Shit             222 - Gray           223 - Lavender
    # 231 - Lime2            232 - Lime           233 - Turquoise
    # 311 - Red              312 - Pink           313 - Magenta
    # 321 - Brown (Default)  322 - Amber          323 - Magenta2
    # 331 - Yellow           332 - Gold           333 - White
    def _adjust_colors(self, model_dict):
        for body_part in model_dict:
            model_list = model_dict[body_part]["Model_List"]
            color = model_dict[body_part]["New_Color"]
            if(color.lower() == "black"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = low
                            self.new_mm[index+0x0D] = low
                            self.new_mm[index+0x0E] = low
            elif(color.lower() == "navy"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = low
                            self.new_mm[index+0x0D] = low
                            self.new_mm[index+0x0E] = med
            elif(color.lower() == "blue"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = low
                            self.new_mm[index+0x0D] = low
                            self.new_mm[index+0x0E] = high
            elif(color.lower() == "swamp"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = low
                            self.new_mm[index+0x0D] = med
                            self.new_mm[index+0x0E] = low
            elif(color.lower() == "avery"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = low
                            self.new_mm[index+0x0D] = med
                            self.new_mm[index+0x0E] = med
            elif(color.lower() == "cosmos"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = low
                            self.new_mm[index+0x0D] = med
                            self.new_mm[index+0x0E] = high
            elif(color.lower() == "green"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = low
                            self.new_mm[index+0x0D] = high
                            self.new_mm[index+0x0E] = low
            elif(color.lower() == "emerald"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = low
                            self.new_mm[index+0x0D] = high
                            self.new_mm[index+0x0E] = med
            elif(color.lower() == "teal"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = low
                            self.new_mm[index+0x0D] = high
                            self.new_mm[index+0x0E] = high
            elif(color.lower() == "rust"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = med
                            self.new_mm[index+0x0D] = low
                            self.new_mm[index+0x0E] = low
            elif(color.lower() == "purple"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = med
                            self.new_mm[index+0x0D] = low
                            self.new_mm[index+0x0E] = med
            elif(color.lower() == "violet"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = med
                            self.new_mm[index+0x0D] = low
                            self.new_mm[index+0x0E] = high
            elif(color.lower() == "shit"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = med
                            self.new_mm[index+0x0D] = med
                            self.new_mm[index+0x0E] = low
            elif(color.lower() == "gray"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = med
                            self.new_mm[index+0x0D] = med
                            self.new_mm[index+0x0E] = med
            elif(color.lower() == "lavendar"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = med
                            self.new_mm[index+0x0D] = med
                            self.new_mm[index+0x0E] = high
            elif(color.lower() == "lime2"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = med
                            self.new_mm[index+0x0D] = high
                            self.new_mm[index+0x0E] = low
            elif(color.lower() == "lime"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = med
                            self.new_mm[index+0x0D] = high
                            self.new_mm[index+0x0E] = med
            elif(color.lower() == "turquiose"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = med
                            self.new_mm[index+0x0D] = high
                            self.new_mm[index+0x0E] = high
            elif(color.lower() == "red"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = high
                            self.new_mm[index+0x0D] = low
                            self.new_mm[index+0x0E] = low
            elif(color.lower() == "pink"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = high
                            self.new_mm[index+0x0D] = low
                            self.new_mm[index+0x0E] = med
            elif(color.lower() == "magenta"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = high
                            self.new_mm[index+0x0D] = low
                            self.new_mm[index+0x0E] = high
            elif(color.lower() == "brown"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = high
                            self.new_mm[index+0x0D] = med
                            self.new_mm[index+0x0E] = low
            elif(color.lower() == "amber"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = high
                            self.new_mm[index+0x0D] = med
                            self.new_mm[index+0x0E] = med
            elif(color.lower() == "magenta2"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = high
                            self.new_mm[index+0x0D] = med
                            self.new_mm[index+0x0E] = high
            elif(color.lower() == "yellow"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = high
                            self.new_mm[index+0x0D] = high
                            self.new_mm[index+0x0E] = low
            elif(color.lower() == "gold"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = high
                            self.new_mm[index+0x0D] = high
                            self.new_mm[index+0x0E] = med
            elif(color.lower() == "white"):
                for (index_start, index_end) in model_list:
                    for index in range(index_start, index_end + 0x10, 0x10):
                        red = self.mm[index+0x0C]
                        green = self.mm[index+0x0D]
                        blue = self.mm[index+0x0E]
                        alpha = self.mm[index+0x0F]
                        if(model_dict[body_part]["Color_Check"](red, green, blue, alpha)):
                            (low, med, high) = self._sort_rgb_colors([red, green, blue])
                            self.new_mm[index+0x0C] = high
                            self.new_mm[index+0x0D] = high
                            self.new_mm[index+0x0E] = high

    def _adjust_textures(self, model_dict):
        for body_part in model_dict:
            if("Texture" in model_dict[body_part]):
                color = model_dict[body_part]["New_Color"]
                if(color.lower() == "black"): # Fix This 010F Best?
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x01
                            self.new_mm[byte_index+1] = 0x0F
                elif(color.lower() == "navy"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x00
                            self.new_mm[byte_index+1] = 0x8F
                elif(color.lower() == "blue"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x00
                            self.new_mm[byte_index+1] = 0xFF
                elif(color.lower() == "swamp"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x03
                            self.new_mm[byte_index+1] = 0x0F
                elif(color.lower() == "avery"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x03
                            self.new_mm[byte_index+1] = 0x0F
                elif(color.lower() == "cosmos"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x08
                            self.new_mm[byte_index+1] = 0xFF
                elif(color.lower() == "green"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x0F
                            self.new_mm[byte_index+1] = 0x0F
                elif(color.lower() == "emerald"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x0F
                            self.new_mm[byte_index+1] = 0x8F
                elif(color.lower() == "teal"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x0F
                            self.new_mm[byte_index+1] = 0xFF
                elif(color.lower() == "rust"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x80
                            self.new_mm[byte_index+1] = 0x0F
                elif(color.lower() == "purple"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x80
                            self.new_mm[byte_index+1] = 0x9F
                elif(color.lower() == "violet"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x80
                            self.new_mm[byte_index+1] = 0xFF
                elif(color.lower() == "shit"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x5C
                            self.new_mm[byte_index+1] = 0x1F
                elif(color.lower() == "gray"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x4A
                            self.new_mm[byte_index+1] = 0x0F
                elif(color.lower() == "lavendar"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x88
                            self.new_mm[byte_index+1] = 0xFF
                elif(color.lower() == "lime2"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x8F
                            self.new_mm[byte_index+1] = 0x0F
                elif(color.lower() == "lime"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x8F
                            self.new_mm[byte_index+1] = 0x8F
                elif(color.lower() == "turquiose"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0x8F
                            self.new_mm[byte_index+1] = 0xFF
                elif(color.lower() == "red"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0xF0
                            self.new_mm[byte_index+1] = 0x0F
                elif(color.lower() == "pink"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0xC0
                            self.new_mm[byte_index+1] = 0x8F
                elif(color.lower() == "magenta"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0xF0
                            self.new_mm[byte_index+1] = 0xFF
                elif(color.lower() == "brown"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0xCB
                            self.new_mm[byte_index+1] = 0x0F
                elif(color.lower() == "amber"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0xCA
                            self.new_mm[byte_index+1] = 0x0F
                elif(color.lower() == "magenta2"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0xF8
                            self.new_mm[byte_index+1] = 0xFF
                elif(color.lower() == "yellow"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0xFF
                            self.new_mm[byte_index+1] = 0x0F
                elif(color.lower() == "gold"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0xFF
                            self.new_mm[byte_index+1] = 0x8F
                elif(color.lower() == "white"):
                    for part in model_dict[body_part]["Texture"]:
                        for byte_index in model_dict[body_part]["Texture"][part]["Map"]:
                            self.new_mm[byte_index] = 0xFF
                            self.new_mm[byte_index+1] = 0XFF

    def _main(self, model_dict, custom_name=None):
        if(not custom_name):
            custom_name = "New"
        self._create_mm()
        try:
            self._make_copy(additional_name=custom_name)
        except Exception as e:
            print(f"Error 1: {e}")
        else:
            try:
                self._adjust_colors(model_dict)
                self._adjust_textures(model_dict)
            except Exception as e:
                print(f"Error 2: {e}")
            finally:
                self.new_mm.close()
        finally:
            self.mm.close()