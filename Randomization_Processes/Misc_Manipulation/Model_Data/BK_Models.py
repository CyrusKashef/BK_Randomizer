'''
Created on Sep 4, 2021

@author: Cyrus
'''

#####################
### PYTHON IMPORT ###
#####################

import mmap
import shutil

###################
### FILE IMPORT ###
###################

# from .Generic_Models import Model
from Randomization_Processes.Misc_Manipulation.Model_Data import Generic_Models

######################
### BK MODEL CLASS ###
######################
 
class BK_Model(Generic_Models.Model):
    def _bk_model_low_poly(self):
        self.model_vertex_dict = {
            "Banjo_Fur": ["270E00FF", "411700FF", "632501FF", "833203FF", "AE4707FF", "BA7F4BFF", "CC560BFF", "FA6F12FF", "F6B400FF"],
            "Banjo_Skin": ["FFBE97FF", "FFEAB4FF", "995447FF", "C66E5CFF", "EB836DFF", "FFA385FF", "45251FFF", "66372FFF", "995447FF"],
#             "Banjo_Nose": ["000000FF"], # Half of the nose is a texture lmao
#             "Banjo_Mouth": ["A31036FF"],
#             "Banjo_Tooth_Necklace": ["FFFFFFFF"], # Shares value with several textures
            "Kazooie_Primary": ["880000FF", "D00000FF", "FF3300FF", "FF3452FF", "FF5F00FF", "520000FF", "2D0032FF", "4F4F4FFF"],
            "Kazooie_Secondary": ["FFFF9FFF", "923900FF", "C74700FF", "FEA131FF", "FF7425FF", "FF8900FF", "FFC700FF", "FFCF3DFF", "3C0D22FF", "801F4BFF", "B32C69FF", "662300FF"],
            "Backpack": ["001A4EFF", "002268FF", "003092FF", "004AE0FF", "2B71FFFF", "558DFFFF", "7FA9FFFF"],
            "Wading_Boots": ["131912FF", "21311EFF", "364F32FF", "5C8754FF"],
            "Shorts_Vertex": ["CE8700FF", "EAEA00FF", "FFFF28FF", "BA5500FF", "874708FF"],
#             "Running_Shoes": ["383838FF", "DBDBDBFF"], # Running Shoes Have So Many Textures DX
#             "Both_Eyes": ["7A7A7AFF", "A7A7A7FF"],
#             "Unknown": ["202020FF"],
            }
        self.model_texture_dict = {
            "Banjo_Feet": [0x5F0, 0x5F4, 0x5F6, 0x5F8, 0x5FA, 0x5FC, 0x600, 0x602, 0x604, 0x606, 0x608, 0x60A, 0x60C, 0x60E,
                           0xF10, 0xF14, 0xF16, 0xF18, 0xF1A, 0xF1C, 0xF1E, 0xF20, 0xF22, 0xF24, 0xF26, 0xF2A, 0xF2C, 0xF2E],
            "Kazooie_Wing_Primary": [0x1570, 0x1574, 0x157A, 0x157C, 0x157E, 0x1582, 0x1584, 0x1586, 0x1588, 0x158A],
            "Kazooie_Wing_Secondary": [0x1576, 0x1578, 0x1580, 0x158C],
            "Shorts_Texture": [0xAD0, 0xAD6, 0xADA, 0xADC, 0xADE, 0xAE0, 0xAE2, 0xAE4, 0xAE6, 0xAE8, 0xAEA, 0xAEC, 0xAEE,
                             0xCF0, 0xCF2, 0xCF6, 0xCF8, 0xCFA, 0xCFC, 0xCFE, 0xD00, 0xD04, 0xD06, 0xD0A, 0xD0E],
            # Running Shoes Have So Many Parts DX This Isn't Even All Of It
#             "Running_Shoes_White": [0x1E90, 0x1E9A, 0x1EAC,
#                                     0x1C10, 0x1C1A, 0x1C1E, 0x1C24],
#             "Running_Shoes_Red": [0x1E92, 0x1E94, 0x1E96, 0x1E98, 0x1E9C, 0x1E9E, 0x1EA0, 0x1EA2, 0x1EA4, 0x1EA6, 0x1EA8, 0x1EAA, 0x1EAE],
            }
        self.model_vertex_location_dict = {
            # 7A7A7AFF, FFFFFFFF, 383838FF
            "Tooth_Necklace": [(0xEBBC, 0xEC5C)]
            }
    
    def _only_low_poly_bk_model(self, seed_val):
        '''Copys the low poly model for Banjo-Kazooie and replaces the high poly model'''
        shutil.copy(f"{self._file_dir}Randomized_ROM/7900-Decompressed.bin", f"{self._file_dir}Randomized_ROM/7908-Decompressed.bin")
        with open(f"{self._file_dir}Randomized_ROM/Banjo-Kazooie_Randomized_Seed_{seed_val}.z64", "r+b") as rand_rom:
            mm_rand_rom = mmap.mmap(rand_rom.fileno(), 0)
            # 18D800 + 10CD0 = 19E4D0
            mm_rand_rom[30984] = 0
            mm_rand_rom[30985] = 24
            mm_rand_rom[30986] = 216
            mm_rand_rom[30987] = 0
            mm_rand_rom.close()

    def _main(self, banjo_fur="", banjo_skin="", banjo_feet="",
                    kazooie_primary="", kazooie_secondary="", kazooie_wing_primary="", kazooie_wing_secondary="",
                    backpack="", wading_boots="", shorts_vertex="", shorts_texture="", tooth_necklace=""):
        # DEFINE MODEL
        self._bk_model_low_poly()
        # EDIT BANJO VERTEX
        if(len(banjo_fur) > 0):
            self._vertex_change_color("Banjo_Fur", banjo_fur)
        if(len(banjo_skin) > 0):
            self._vertex_change_color("Banjo_Skin", banjo_skin)
#         self._vertex_change_color("Banjo_Mouth", "A200FFFE")
        # EDIT BANJO TEXTURE
        if(len(banjo_feet) > 0):
            self._texture_change_color("Banjo_Feet", banjo_feet)
        # EDIT KAZOOIE VERTEX
        if(len(kazooie_primary) > 0):
            self._vertex_change_color("Kazooie_Primary", kazooie_primary)
        if(len(kazooie_secondary) > 0):
            self._vertex_change_color("Kazooie_Secondary", kazooie_secondary)
        # EDIT KAZOOIE TEXTURE
        if(len(kazooie_wing_primary) > 0):
            self._texture_change_color("Kazooie_Wing_Primary", kazooie_wing_primary)
        if(len(kazooie_wing_secondary) > 0):
            self._texture_change_color("Kazooie_Wing_Secondary", kazooie_wing_secondary)
        # EDIT OTHER VERTEX
        if(len(backpack) > 0):
            self._vertex_change_color("Backpack", backpack)
        if(len(wading_boots) > 0):
            self._vertex_change_color("Wading_Boots", wading_boots)
        if(len(shorts_vertex) > 0):
            self._vertex_change_color("Shorts_Vertex", shorts_vertex)
        if(len(tooth_necklace) > 0):
            self._vertex_model_subsection_color_change("Tooth_Necklace", tooth_necklace)
        # EDIT OTHER TEXTURE
        if(len(shorts_texture) > 0):
            self._texture_change_color("Shorts_Texture", shorts_texture)
        # CLOSE MM
        self._close_mm()

if __name__ == '__main__':
    print("Start")
    shutil.copy(f"C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/temp/197E38/197E38-Decompressed.bin", f"C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/temp/197E38/Randomized_ROM/197E38-Decompressed.bin")
    bk_model = BK_Model(f"C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/temp/197E38/", "197E38", original_index_start=0xB138)
    bk_model._main(
        banjo_fur="000008",
        banjo_skin="818181",
        banjo_feet="841F",
        kazooie_primary="818181",
        kazooie_secondary="FFFFFF",
        kazooie_wing_primary="841F",
        kazooie_wing_secondary="FFFF",
        backpack="818181",
        wading_boots="818181",
        shorts_vertex="000008",
        shorts_texture="0001",
        tooth_necklace="FF0C0C"
        )
    print("Done")