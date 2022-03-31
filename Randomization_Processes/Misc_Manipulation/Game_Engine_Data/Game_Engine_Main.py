'''
Created on Dec 10, 2021

@author: Cyrus
'''

#####################
### PYTHON IMPORT ###
#####################

import mmap
# import shutil
# import os

##########################
### PYTHON FILE IMPORT ###
##########################

from Randomization_Processes.Dicts_And_Lists.Game_Engine import start_level_ids
from Randomization_Processes.Common_Functions import leading_zeros
# from ...Common_Functions import apply_patch

#########################
### GAME ENGINE CLASS ###
#########################

class Game_Engine_Class():
    # F37F90 to F9CAE0
    # A lot of things change, might just not be worth it? IDK
    # 0C XX XX XX gets increased by 20E58
    #    Example: 0C 0E 40 3F -> 0C 10 4E 96
    def __init__(self, file_dir):
        self._file_dir = file_dir
#         self._patch_file()
        with open(f"{self._file_dir}Randomized_ROM/F37F90-Decompressed.bin", "r+b") as decomp_file:
            self.mm = mmap.mmap(decomp_file.fileno(), 0)

#     def _patch_file(self):
#         this_dir = f"{self._file_dir}Randomization_Processes/Misc_Manipulation/Game_Engine_Data/"
#         if(os.path.isfile(f"{this_dir}F37F90-Decompressed.bin")):
#             os.remove(f"{this_dir}F37F90-Decompressed.bin")
#         apply_patch(f"{self._file_dir}xdelta/", f"{self._file_dir}Randomized_ROM/F37F90-Decompressed.bin", f"{this_dir}F37F90-Patch.xdelta", f"{this_dir}F37F90-Decompressed.bin")
#         shutil.move(f"{this_dir}F37F90-Decompressed.bin", f"{self._file_dir}Randomized_ROM/F37F90-Decompressed.bin")

    def _starting_moves(self):
        # 0xE84E & 0xE84F
        # C3 A0 -> 0F 98
        self.mm[0xE84E] = 0x0F
        self.mm[0xE84F] = 0x98
    
    def _mumbo_transformations_costs(self, termite_cost=0, crocodile_cost=0, walrus_cost=0, pumpkin_cost=0, bee_cost=0):
        # 0x4A7E7 (Termite)
        # 0x4A7EF (Crocodile)
        # 0x4A7F7 (Walrus)
        # 0x4A7FF (Pumpkin)
        # 0x4A807 (Bee)
#         for transform_index in range(0x4A7E7, 0x4A808, 8):
#             self.mm[transform_index] = 0
        self.mm[0x4A7E7] = termite_cost
        self.mm[0x4A7EF] = crocodile_cost
        self.mm[0x4A7F7] = walrus_cost
        self.mm[0x4A7FF] = pumpkin_cost
        self.mm[0x4A807] = bee_cost
    
    def _jiggies_per_world(self, jiggy_count):
        # One single value for every world?
        # 0x8AC5F
        self.mm[0x8AC5F] = jiggy_count
    
    def _empty_honeycombs_per_world(self, e_honeycomb_count):
        # 0x8ACAB
        self.mm[0x8ACAB] = e_honeycomb_count
    
    def _empty_honeycombs_for_sm(self, e_honeycomb_count):
        # 0x8ACAF
        self.mm[0x8ACAF] = e_honeycomb_count
    
    def _blue_egg_limit(self, count_before_cheato, count_after_cheato=None):
        # 0xBF21F Before Cheato
        # 0xBF217 After Cheato
        self.mm[0xBF21F] = count_before_cheato
        if(count_after_cheato):
            self.mm[0xBF217] = count_after_cheato
        else:
            count_after_cheato = min(count_before_cheato*2, 0xFF)
            self.mm[0xBF217] = count_after_cheato
    
    def _red_feather_limit(self, count_before_cheato, count_after_cheato=None):
        # 0xBF23F Before Cheato
        # 0xBF237 After Cheato
        self.mm[0xBF23F] = count_before_cheato
        if(count_after_cheato):
            self.mm[0xBF237] = count_after_cheato
        else:
            count_after_cheato = min(count_before_cheato*2, 0xFF)
            self.mm[0xBF237] = count_after_cheato
        
    def _gold_feather_limit(self, count_before_cheato, count_after_cheato=None):
        # 0xBF25B Before Cheato
        # 0xBF257 After Cheato
        self.mm[0xBF25B] = count_before_cheato
        if(count_after_cheato):
            self.mm[0xBF257] = count_after_cheato
        else:
            count_after_cheato = min(count_before_cheato*2, 0xFF)
            self.mm[0xBF257] = count_after_cheato
    
    def _new_game_start_level(self, new_start_level_name, skip_intro_cutscene=False):
        # 0x3E17B - Intro Cutscene
        # 0x986FA - New Game Start
        # starting pointer = 0x9778
        # new_start_level_id = (level_pointer - starting pointer) // 8
        # new_start_level_id = Game_Engine[new_start_level_name]
        self.mm[0x986FA] = start_level_ids[new_start_level_name]
        if(skip_intro_cutscene):
            self.mm[0x3E17B] = start_level_ids[new_start_level_name]
    
    def _load_game_start_level(self, load_game_start_level_name):
        # 0x98BAE - Load Game Start
        # starting pointer = 0x9778
        # new_start_level_id = (level_pointer - starting pointer) // 8
        # new_start_level_id = Game_Engine[new_start_level_name]
        self.mm[0x98BAE] = start_level_ids[load_game_start_level_name]
    
    def _starting_lives(self, life_count):
        # 0xBF51A & 0xBF51B
        # Default is 3 lives
        # 24 18 00 [03]
        life_count_str = leading_zeros(life_count, 4)
        self.mm[0xBF51A] = int(life_count_str[:2], 16)
        self.mm[0xBF51B] = int(life_count_str[2:], 16)
    
    def _starting_health(self, health_val):
        # Starting Health
        # 24 0E 00 [05]
        life_count_str = leading_zeros(health_val, 4)
        self.mm[0xBF516] = int(life_count_str[:2], 16)
        self.mm[0xBF517] = int(life_count_str[2:], 16)
    
    def _start_double_health(self):
        ## Double Health (I Think?)
        # 24 03 00 02 24 03 00 [01]
        self.mm[0xBF14F] = 0x02
    
    def _max_health(self):
        ## Lower Health Total?
        # 00 03 20 [C0]
        self.mm[0xBF157] = 0x00

    def _open_df(self, offset: str):
        return open(f"{self._file_dir}Randomized_ROM/{offset}-Decompressed.bin", "r+b")

    def _patch_ttc_yumyum_crashfix(self):
        """
        Fixes a vanilla bug: when a yumyum in TTC tries to eat a sprite in a cube,
        the game treats it as an actor, derefs an invalid pointer, and segfaults.

        Added by @wed, with <3
        """
        ovl_ttc        = "FAE860"
        ovl_core2_data = "F9CAE0"

        with self._open_df(ovl_ttc) as f:
            m = mmap.mmap(f.fileno(), 0)

            # Set hook in yumyum eat update func
            m.seek(0xC90)
            m.write((0x080DDDD0).to_bytes(4, "big"))

        with self._open_df(ovl_core2_data) as f:
            m = mmap.mmap(f.fileno(), 0)

            # Write fix handler over vanilla debug strings
            m.seek(0x141B0)
            m.write((0x1100000D000000008D0A0000000A4E0234010080552100083C098000012A4826).to_bytes(32, "big"))
            m.write((0x3C0100400121482A1120000300000000080E1C2200000000080E1C2800000000).to_bytes(32, "big"))

    def _patch_antiantitamper(self):
        """
        Try and patch out some vanilla antitamper checks so Jiggly doesn't have
        to fix his checksum code. :^)

        Added by @wed, with </3
        """
        ovl_core1_text = "F19250"
        ovl_core2_text = "F37F90"
        ovl_sm         = "FC4810"
        ovl_mm         = "FB24A0"
        ovl_cc         = "FA3FD0"
        ovl_bgs        = "FB44E0"
        ovl_gv         = "FA9150"

        with self._open_df(ovl_core2_text) as f:
            m = mmap.mmap(f.fileno(), 0)

            m[0xADF44] = 0x00
            m[0xADF45] = 0x00
            m[0xADF46] = 0x00
            m[0xADF47] = 0x00
            m[0x7E83C] = 0x10
            m[0x7E83D] = 0x00

        with self._open_df(ovl_core1_text) as f:
            m = mmap.mmap(f.fileno(), 0)

            m[0x10A1C] = 0x00
            m[0x10A1D] = 0x00
            m[0x10A1E] = 0x00
            m[0x10A1F] = 0x00
            m[0x10A30] = 0x10
            m[0x10A31] = 0x00

        with self._open_df(ovl_sm) as f:
            m = mmap.mmap(f.fileno(), 0)

            m[0x1D4]  = 0x10
            m[0x1D5]  = 0x00
            m[0x1EC]  = 0x10
            m[0x1ED]  = 0x00
            m[0x204]  = 0x10
            m[0x205]  = 0x00
            m[0x3FA4] = 0x00
            m[0x3FA5] = 0x00
            m[0x3FA6] = 0x00
            m[0x3FA7] = 0x00

        with self._open_df(ovl_mm) as f:
            m = mmap.mmap(f.fileno(), 0)

            m[0x1B7C] = 0x10
            m[0x1B7D] = 0x00

        with self._open_df(ovl_cc) as f:
            m = mmap.mmap(f.fileno(), 0)

            m[0x1984] = 0x10
            m[0x1985] = 0x00

        with self._open_df(ovl_bgs) as f:
            m = mmap.mmap(f.fileno(), 0)

            m[0x86C0] = 0x10
            m[0x86C1] = 0x00

        with self._open_df(ovl_gv) as f:
            m = mmap.mmap(f.fileno(), 0)

            m[0x3B8C] = 0x10
            m[0x3B8D] = 0x00

