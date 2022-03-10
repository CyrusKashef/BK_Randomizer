'''
Created on Nov 15, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

from mmap import mmap

####################
### FILE IMPORTS ###
####################

from Randomization_Processes.Common_Functions import leading_zeros

#####################
### TEXTURE CLASS ###
#####################

class Texture_Class():
    def __init__(self, file_dir, address, seed_val=0):
        self._file_dir = file_dir
        self._address = address
        self._seed_val = seed_val
        with open(f"{self._file_dir}Randomized_ROM\\{self._address}-Decompressed.bin", "r+b") as decomp_file:
#         with open(f"{self._file_dir}{self._address}-Decompressed.bin", "r+b") as decomp_file:
            self.mm = mmap(decomp_file.fileno(), 0)
    
    def _extract_header_info(self):
        self._texture_setup_offset = int(leading_zeros(self.mm[8], 2) + leading_zeros(self.mm[9], 2), 16)
        self._texture_count = self.mm[self._texture_setup_offset + 5]
        self._textures_offset = self._texture_setup_offset + (0x10 * self._texture_count) + 0x8
    
    def _extract_texture_setup_info(self):
        self._texture_list = []
        texture_count = 0
        for text_header_index in range(self._texture_setup_offset + 8, self._texture_setup_offset + 8 + (self._texture_count*16), 16):
            self._texture_list.append({
                "Texture_Start": int(leading_zeros(self.mm[text_header_index], 2) + 
                                     leading_zeros(self.mm[text_header_index + 1], 2) + 
                                     leading_zeros(self.mm[text_header_index + 2], 2) + 
                                     leading_zeros(self.mm[text_header_index + 3], 2), 16)
                                + self._textures_offset,
                "Texture_Type": self.mm[text_header_index + 5],
                "X_Length": self.mm[text_header_index + 8],
                "Y_Length": self.mm[text_header_index + 9],
                })
            with open(f"{self._file_dir}Randomized_ROM\\{self._address}-Texture_{leading_zeros(str(texture_count), 3)}.bin", "w+b") as texture_file:
                for index in range(self._texture_list[-1]["Texture_Start"], self._texture_list[-1]["Texture_Start"] + (self._texture_list[-1]["X_Length"] * self._texture_list[-1]["Y_Length"])//2 + 0x20):
                    texture_file.write(bytes.fromhex(leading_zeros(self.mm[index], 2)))
            texture_count += 1
    
    def _rearrange_textures(self, new_order_dict):
        texture_count = 0
        next_texture_start = 0
        for text_header_index in range(self._texture_setup_offset + 8, self._texture_setup_offset + 8 + (self._texture_count*16), 16):
            if(texture_count in new_order_dict):
                curr_info = self._texture_list[new_order_dict[texture_count]]
                image_num = leading_zeros(str(new_order_dict[texture_count]), 3)
            else:
                curr_info = self._texture_list[texture_count]
                image_num = leading_zeros(str(texture_count), 3)
            texture_start = leading_zeros(next_texture_start, 8)
            self.mm[text_header_index] = int(texture_start[:2], 16)
            self.mm[text_header_index + 1] = int(texture_start[2:4], 16)
            self.mm[text_header_index + 2] = int(texture_start[4:6], 16)
            self.mm[text_header_index + 3] = int(texture_start[6:], 16)
            self.mm[text_header_index + 5] = curr_info["Texture_Type"]
            self.mm[text_header_index + 8] = curr_info["X_Length"]
            self.mm[text_header_index + 9] = curr_info["Y_Length"]
            next_texture_start = next_texture_start + (curr_info["X_Length"] * curr_info["Y_Length"])//2 + 0x20
            with open(f"{self._file_dir}Randomized_ROM/{self._address}-Texture_{image_num}.bin", "r+b") as texture_file:
                mm_texture = mmap(texture_file.fileno(), 0)
                index_count = 0
                for index in range(self._texture_list[texture_count]["Texture_Start"], self._texture_list[texture_count]["Texture_Start"] + (curr_info["X_Length"] * curr_info["Y_Length"])//2 + 0x20):
                    self.mm[index] = mm_texture[index_count]
                    index_count += 1
            texture_count += 1
    
    def _flip_texture(self, rgba_index_list, x_axis=True, y_axis=True):
        if(x_axis):
            for rgba_index in rgba_index_list:
                v_value = 0x10000 - int(leading_zeros(self.mm[rgba_index + 0xA], 2) + leading_zeros(self.mm[rgba_index + 0xB], 2), 16)
                if(v_value == 0x10000):
                    v_str = "0000"
                else:
                    v_str = leading_zeros(v_value, 4)
                self.mm[rgba_index + 0xA] = int(v_str[:2], 16)
                self.mm[rgba_index + 0xB] = int(v_str[2:], 16)
#                 self.mm[rgba_index + 0xC] = 0
#                 self.mm[rgba_index + 0xD] = 0
#                 self.mm[rgba_index + 0xE] = 0
        if(y_axis):
            for rgba_index in rgba_index_list:
                v_value = 0x10000 - int(leading_zeros(self.mm[rgba_index + 0x8], 2) + leading_zeros(self.mm[rgba_index + 0x9], 2), 16)
                if(v_value == 0x10000):
                    v_str = "0000"
                else:
                    v_str = leading_zeros(v_value, 4)
                self.mm[rgba_index + 0x8] = int(v_str[:2], 16)
                self.mm[rgba_index + 0x9] = int(v_str[2:], 16)
        

if __name__ == '__main__':
    pass