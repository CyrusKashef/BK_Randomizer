'''
Created on Aug 31, 2021

@author: Cyrus
'''

#####################
### PYTHON IMPORT ###
#####################

from mmap import mmap

###################
### FILE IMPORT ###
###################

from Randomization_Processes.Common_Functions import leading_zeros

###########################
### GENERIC MODEL CLASS ###
###########################

class Model():
    '''Generic model class'''
    def __init__(self, file_dir, address, original_index_start=0):
        '''Initializes generic model class'''
        self._file_dir = file_dir
        self.address = address
        self._create_mm()
        self.original_index_start = original_index_start
        self.original_index_end = len(self.mm)
    
    def _create_mm(self):
        '''Creates the currently used mmap for the model'''
        with open(f"{self._file_dir}Randomized_ROM/{self.address}-Decompressed.bin", "r+b") as f:
            self.mm = mmap(f.fileno(), 0)

    def _close_mm(self):
        self.mm.close()

    def _vertex_change_color(self, body_part, new_color):
        '''
        Changes the current vertex shading color to another color
        # 000008 - Black            FF0C0C - Red            09FF09 - Light Green    001C8C - Blue
        # 214508 - Swamp            31658C - Eastern Blue   4B9D09 - Green          52AA8C - Teal
        # 73EF8C - Verde            961109 - Red Brown      9C318C - Mauve          B95B09 - Burnt Orange
        # BD758C - Dark Pink        E0A709 - Gold           DEBA8C - Light Tan      FFEE09 - Yellow
        # 3165FF - Cosmos           438B7C - Turquoise      52AAFF - Sky Blue       73EFFF - Baby Blue
        # 9C31FF - Violet           AF567D - Salmon         BD75FF - Lavender       D09C7C - Dark Tan
        # DEBAFF - Light Pink       FFFFFF - White          FF00FF - Magenta        00FFFF - Cyan
        '''
        if(len(new_color) == 6):
            new_color_red = int(new_color[:2], 16)
            new_color_green = int(new_color[2:4], 16)
            new_color_blue = int(new_color[4:6], 16)
            new_color_alpha = 0xFF
        elif(len(new_color) == 8):
            new_color_red = int(new_color[:2], 16)
            new_color_green = int(new_color[2:4], 16)
            new_color_blue = int(new_color[4:6], 16)
            new_color_alpha = int(new_color[6:], 16)
        elif(int(new_color, 16) == 0):
            new_color_red = 0
            new_color_green = 0
            new_color_blue = 0
            new_color_alpha = 0
        else:
            print(f"Not 6/8 Digits For RRGGBBAA: {body_part} {new_color}")
            return
        for color_string in self.model_vertex_dict[body_part]:
            for item_index in range(self.original_index_start+4, self.original_index_end+4, 16):
                if((self.mm[item_index] == int(color_string[:2], 16)) and
                   (self.mm[item_index + 1] == int(color_string[2:4], 16)) and
                   (self.mm[item_index + 2] == int(color_string[4:6], 16)) and
                   (self.mm[item_index + 3] == int(color_string[6:], 16))):
                    self.mm[item_index] = new_color_red
                    self.mm[item_index + 1] = new_color_green
                    self.mm[item_index + 2] = new_color_blue
                    self.mm[item_index + 3] = new_color_alpha

    def _vertex_model_subsection_color_change(self, body_part, new_color):
        if(len(new_color) == 6):
            new_color_red = int(new_color[:2], 16)
            new_color_green = int(new_color[2:4], 16)
            new_color_blue = int(new_color[4:6], 16)
            new_color_alpha = 0xFF
        elif(len(new_color) == 8):
            new_color_red = int(new_color[:2], 16)
            new_color_green = int(new_color[2:4], 16)
            new_color_blue = int(new_color[4:6], 16)
            new_color_alpha = int(new_color[6:], 16)
        elif(int(new_color, 16) == 0):
            new_color_red = 0
            new_color_green = 0
            new_color_blue = 0
            new_color_alpha = 0
        else:
            print(f"Not 6/8 Digits For RRGGBBAA: {body_part} {new_color}")
            return
        for subsection in self.model_vertex_location_dict[body_part]:
            for item_index in range(subsection[0], subsection[1], 16):
                self.mm[item_index] = new_color_red
                self.mm[item_index + 1] = new_color_green
                self.mm[item_index + 2] = new_color_blue
                self.mm[item_index + 3] = new_color_alpha

    def _texture_change_color(self, texture_part, new_color):
        '''
        Changes the current texture color to another color
        # 0001 - Black           F841 - Red           0FE1 - Light Green   00D1 - Blue
        # 0301 - Swamp           2B11 - Eastern Blue  4CC1 - Green         4D51 - Teal
        # 6F71 - Verde           9081 - Red Brown     9191 - Mauve         B2C1 - Burnt Orange
        # B391 - Dark Pink       DD21 - Gold          D5B1 - Light Tan     FF41 - Yellow
        # 2B1F - Cosmos          444F - Turquoise     4D5F - Sky Blue      6F7F - Baby Blue
        # 919F - Violet          AAAF - Salmon        B39F - Lavender      CCCF - Dark Tan
        # D5BF - Light Pink      FFFF - White         F81F - Magenta       07FF - Cyan
        # 841F - Light Gray      420F - Dark Gray
        '''
        if(len(new_color) == 4):
            new_color_red_green = int(new_color[:2], 16)
            new_color_blue_alpha = int(new_color[2:], 16)
        elif(len(new_color) == 6):
            new_color = self._convert_32_to_16(f"{new_color}FF")
        elif(len(new_color) == 8):
            new_color = self._convert_32_to_16(new_color)
        elif(int(new_color, 16) == 0):
            new_color_red_green = 0
            new_color_blue_alpha = 0
        else:
            print(f"Incorrect Number Of Digits For RGBA: {texture_part} {new_color}")
            return
        for item_index in self.model_texture_dict[texture_part]:
            self.mm[item_index] = new_color_red_green
            self.mm[item_index + 1] = new_color_blue_alpha
    
    def _convert_32_to_16(self, _32_bit_color):
        red = int(_32_bit_color[0:2], 16)
        green = int(_32_bit_color[2:4], 16)
        blue = int(_32_bit_color[4:6], 16)
        alpha = int(_32_bit_color[6:8], 16)
        
        r = (red >> 3)
        g = (green >> 3)
        b = (blue >> 3)
        a = (alpha >> 7)
        _16_bit_color = (r << 11) | (g << 6) | (b << 1) | (a)
        return leading_zeros(_16_bit_color, 4)