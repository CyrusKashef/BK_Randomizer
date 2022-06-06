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

    def _starting_moves(self):
        '''Starts the player with all of the moves, and hits some other flags'''
        # 0xE84E & 0xE84F
        # C3 A0 -> 0F 98
        self.mm[0xE84E] = 0x0F
        self.mm[0xE84F] = 0x98
    
    def _mumbo_transformations_costs(self, termite_cost=0, crocodile_cost=0, walrus_cost=0, pumpkin_cost=0, bee_cost=0):
        '''Sets the cost of transformations'''
        # 0x4A7E7 (Termite)
        # 0x4A7EF (Crocodile)
        # 0x4A7F7 (Walrus)
        # 0x4A7FF (Pumpkin)
        # 0x4A807 (Bee)
        self.mm[0x4A7E7] = termite_cost
        self.mm[0x4A7EF] = crocodile_cost
        self.mm[0x4A7F7] = walrus_cost
        self.mm[0x4A7FF] = pumpkin_cost
        self.mm[0x4A807] = bee_cost
    
    def _jiggies_per_world(self, jiggy_count):
        '''Unused'''
        # One single value for every world?
        # 0x8AC5F
        self.mm[0x8AC5F] = jiggy_count
    
    def _empty_honeycombs_per_world(self, e_honeycomb_count):
        '''Unused'''
        # 0x8ACAB
        self.mm[0x8ACAB] = e_honeycomb_count
    
    def _empty_honeycombs_for_sm(self, e_honeycomb_count):
        '''Unused'''
        # 0x8ACAF
        self.mm[0x8ACAF] = e_honeycomb_count
    
    def _blue_egg_limit(self, count_before_cheato, count_after_cheato=None):
        '''Sets the blue egg capacity before and after Cheato'''
        # 0xBF21F Before Cheato
        # 0xBF217 After Cheato
        self.mm[0xBF21F] = count_before_cheato
        if(count_after_cheato):
            self.mm[0xBF217] = count_after_cheato
        else:
            count_after_cheato = min(count_before_cheato*2, 0xFF)
            self.mm[0xBF217] = count_after_cheato
    
    def _red_feather_limit(self, count_before_cheato, count_after_cheato=None):
        '''Sets the red feather capacity before and after Cheato'''
        # 0xBF23F Before Cheato
        # 0xBF237 After Cheato
        self.mm[0xBF23F] = count_before_cheato
        if(count_after_cheato):
            self.mm[0xBF237] = count_after_cheato
        else:
            count_after_cheato = min(count_before_cheato*2, 0xFF)
            self.mm[0xBF237] = count_after_cheato
        
    def _gold_feather_limit(self, count_before_cheato, count_after_cheato=None):
        '''Sets the gold feather capacity before and after Cheato'''
        # 0xBF25B Before Cheato
        # 0xBF257 After Cheato
        self.mm[0xBF25B] = count_before_cheato
        if(count_after_cheato):
            self.mm[0xBF257] = count_after_cheato
        else:
            count_after_cheato = min(count_before_cheato*2, 0xFF)
            self.mm[0xBF257] = count_after_cheato
    
    def _new_game_start_level(self, new_start_level_name, skip_intro_cutscene=False):
        '''Instead of the intro cutscene into Spiral Mountain, this is where the player will start the game'''
        # 0x3E17B - Intro Cutscene
        # 0x986FA - New Game Start
        # starting pointer = 0x9778
        # new_start_level_id = (level_pointer - starting pointer) // 8
        # new_start_level_id = Game_Engine[new_start_level_name]
        self.mm[0x986FA] = start_level_ids[new_start_level_name]
        if(skip_intro_cutscene):
            self.mm[0x3E17B] = start_level_ids[new_start_level_name]
    
    def _load_game_start_level(self, load_game_start_level_name):
        '''After watching the Gruntilda Lair cutscene, this is where the player will start on loading the game'''
        # 0x98BAE - Load Game Start
        # starting pointer = 0x9778
        # new_start_level_id = (level_pointer - starting pointer) // 8
        # new_start_level_id = Game_Engine[new_start_level_name]
        self.mm[0x98BAE] = start_level_ids[load_game_start_level_name]
    
    def _starting_lives(self, life_count):
        '''Sets the starting life count'''
        # 0xBF51A & 0xBF51B
        # Default is 3 lives
        # 24 18 00 [03]
        life_count_str = leading_zeros(life_count, 4)
        self.mm[0xBF51A] = int(life_count_str[:2], 16)
        self.mm[0xBF51B] = int(life_count_str[2:], 16)
    
    def _starting_health(self, health_val):
        '''Sets how much health the player has to begin with; Unused'''
        # Starting Health
        # 24 0E 00 [05]
        life_count_str = leading_zeros(health_val, 4)
        self.mm[0xBF516] = int(life_count_str[:2], 16)
        self.mm[0xBF517] = int(life_count_str[2:], 16)
    
    def _start_double_health(self):
        '''Doesn't Work'''
        ## Double Health (I Think?)
        # 24 03 00 02 24 03 00 [01]
        self.mm[0xBF14F] = 0x02
    
    def _max_health(self, health_val="Normal Health"):
        '''Sets the maximum health to zero, one, two, four, or normal health'''
        ## Lower Health Total?
        # 00 03 20 [C0]
        # XX11 = 0x30/0x70/0xF0 = Crash
        # XX01 = 0x10/0x50/0x90/0xD0 = Don't Touch Anything/Pausing Loses Life
        # XX10 = 0x00/0x20/0x60/0xA0/0xE0 = 1 Health
        # 0100 = 0x40 = 2 Health
        # 1000 = 0x80 = 4 Health
        # 1100 = 0xC0 = 5 Health
        if(health_val == "Zero Health (Unbeatable)"):
            self.mm[0xBF157] = 0x10
        elif(health_val == "One Health Only"):
            self.mm[0xBF157] = 0x00
        elif(health_val == "Two Health Only"):
            self.mm[0xBF157] = 0x40
        elif(health_val == "Four Health Only"):
            self.mm[0xBF157] = 0x80
        elif(health_val == "Normal Health"):
            self.mm[0xBF157] = 0xC0

    def _open_df(self, offset: str):
        return open(f"{self._file_dir}Randomized_ROM/{offset}-Decompressed.bin", "r+b")

    def _patch_ttc_yumyum_crashfix(self):
        """
        Fixes a vanilla bug: when a yumyum in TTC tries to eat a sprite in a cube,
        the game treats it as an actor, derefs an invalid pointer, and segfaults.

        Added by @wed, with <3
        """
        ovl_ttc        = "FAE860"
        ovl_core1_text = "F19250"
        ovl_core2_data = "F9CAE0"

        with self._open_df(ovl_ttc) as f:
            m = mmap.mmap(f.fileno(), 0)

            # Set hook in yumyum eat update func
            m.seek(0xC90)
            m.write((0x08096C05).to_bytes(4, "big"))

        with self._open_df(ovl_core1_text) as f:
            m = mmap.mmap(f.fileno(), 0)

            # Write fix handler over vanilla debug strings
            m.seek(0x1D5EC)
            m.write((0x03E0000800000000).to_bytes(8, "big"))
            m.write((0x1100000D000000008D0A0000000A4E0234010080552100083C098000012A4826).to_bytes(32, "big"))
            m.write((0x3C0100400121482A1120000300000000080E1C2200000000080E1C2800000000).to_bytes(32, "big"))

    def _patch_antiantitamper(self, core1_at=True, core2_at=True, sm_at=True,
                              mm_at=True, ttc_at=True, cc_at=True,
                              bgs_at=True, fp_at=True, gv_at=True,
                              mmm_at=True, rbb_at=True, ccw_at=True):
        """
        Try and patch out some vanilla antitamper checks so Jiggly doesn't have
        to fix his checksum code. :^)

        Added by @wed, with </3
        """
        ovl_core1_text = "F19250"
        ovl_core2_text = "F37F90"
        ovl_sm         = "FC4810"
        ovl_mm         = "FB24A0"
        ovl_ttc        = "FAE860"
        ovl_cc         = "FA3FD0"
        ovl_bgs        = "FB44E0"
        ovl_gv         = "FA9150"
        ovl_mmm        = "FA5F50"
        
        if(core1_at):
            with self._open_df(ovl_core1_text) as f:
                m = mmap.mmap(f.fileno(), 0)
                m[0x10A1C] = 0x00
                m[0x10A1D] = 0x00
                m[0x10A1E] = 0x00
                m[0x10A1F] = 0x00
                m[0x10A30] = 0x10
                m[0x10A31] = 0x00

        if(sm_at):
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

        if(mm_at):
            with self._open_df(ovl_mm) as f:
                m = mmap.mmap(f.fileno(), 0)
                m[0x1B7C] = 0x10
                m[0x1B7D] = 0x00

        if(ttc_at):
            with self._open_df(ovl_ttc) as f:
                m = mmap.mmap(f.fileno(), 0)
                m[0x31B4] = 0x00
                m[0x31B5] = 0x00
                m[0x31B6] = 0x00
                m[0x31B7] = 0x00

        if(cc_at):
            with self._open_df(ovl_cc) as f:
                m = mmap.mmap(f.fileno(), 0)
                m[0x1984] = 0x10
                m[0x1985] = 0x00

        if(bgs_at):
            with self._open_df(ovl_bgs) as f:
                m = mmap.mmap(f.fileno(), 0)
                m[0x86C0] = 0x10
                m[0x86C1] = 0x00

        if(gv_at):
            with self._open_df(ovl_gv) as f:
                m = mmap.mmap(f.fileno(), 0)
                m[0x3B8C] = 0x10
                m[0x3B8D] = 0x00

        if(mmm_at):
            with self._open_df(ovl_mmm) as f:
                m = mmap.mmap(f.fileno(), 0)
                m[0x4830] = 0x10
                m[0x4831] = 0x00

