'''
Created on Oct 14, 2021

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

from ...Dicts_And_Lists.Model_Dict import model_dict
from .Generic_Models import Model

##########################
### MODELS MANIP CLASS ###
##########################

class ModelsMain():
    '''Models manipulation class'''
    def __init__(self, file_dir):
        '''Initializes the models manipulation class'''
        self._file_dir = file_dir
        
    def _bk_model1(self, banjo_fur_color, banjo_skin_color, banjo_toes_color, kazooie_feather_color, kazooie_spot_color, backpack_color, banjo_shorts_color):
        '''Grabs the parameters for the Banjo-Kazooie model colors'''
        bk1 = Model(self._file_dir, "7900")
        model_dict["BK_Model1"]["Banjo_Fur"]["New_Color"] = banjo_fur_color
        model_dict["BK_Model1"]["Banjo_Skin"]["New_Color"] = banjo_skin_color
        model_dict["BK_Model1"]["Banjo_Toes"]["New_Color"] = banjo_toes_color
        model_dict["BK_Model1"]["Kazooie_Feathers"]["New_Color"] = kazooie_feather_color
        model_dict["BK_Model1"]["Kazooie_Spots"]["New_Color"] = kazooie_spot_color
        model_dict["BK_Model1"]["Backpack"]["New_Color"] = backpack_color
        model_dict["BK_Model1"]["Banjo_Shorts"]["New_Color"] = banjo_shorts_color
        bk1._main(model_dict["BK_Model1"])
    
    def _only_bk_model1(self, seed_val):
        '''Copys the low poly model for Banjo-Kazooie and replaces the high poly model'''
        shutil.copy(f"{self._file_dir}Randomized_ROM\\7900-Decompressed.bin", f"{self._file_dir}Randomized_ROM\\7908-Decompressed.bin")
        with open(f"{self._file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_{seed_val}.z64", "r+b") as rand_rom:
            mm_rand_rom = mmap.mmap(rand_rom.fileno(), 0)
            # 18D800 + 10CD0 = 19E4D0
            mm_rand_rom[30984] = 0
            mm_rand_rom[30985] = 24
            mm_rand_rom[30986] = 216
            mm_rand_rom[30987] = 0
            mm_rand_rom.close()