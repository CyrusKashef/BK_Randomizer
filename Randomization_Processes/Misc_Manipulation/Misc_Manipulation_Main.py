'''
Created on Oct 9, 2021

@author: Cyrus

'''

#####################
### PYTHON IMPORT ###
#####################

import mmap
import random

###################
### FILE IMPORT ###
###################

from .Model_Data.BK_Models import BK_Model
from .Model_Data.Swap_Models_Main import Swap_Models_Manipulation
from .Music_Data.Music_Main import Music_Manipulation
from .Skybox_Data.Skybox_Main import Skybox_Manipulation
from .Sprite_Data.Sprite_Main import Sprite_Manipulation
from .Speech_Data.Speech_Main import Speech_Manipulation
from .Animation_Data.Animation_Main import Swap_Animations_Manipulation
from ..Dicts_And_Lists.Misc_Dicts_And_Lists import gv_matching_puzzle_pictures
from .Game_Engine_Data.Game_Engine_Main import Game_Engine_Class

#################################
### MISCELLANEOUS MANIP CLASS ###
#################################

class misc_manipulation():
    '''Miscellaneous setting manipulation class'''
    def __init__(self, grandmaster, seed_val):
        '''Initializes the miscellaneous setting manipulation class'''
        self._grandmaster = grandmaster
        self._file_dir = grandmaster.cwd
        self._seed_val = seed_val
        self.world_abbreviations = {"Mumbo's Mountain": "MM", "Treasure Trove Cove": "TTC", "Clanker's Cavern": "CC",
                                    "Bubblegloop Swamp": "BGS", "Freezeezy Peak": "FP", "Gobi's Valley": "GV",
                                    "Mad Monster Mansion": "MMM", "Rusty Bucket Bay": "RBB", "Click Clock Wood": "CCW"}
        self.speech_manip = Speech_Manipulation(grandmaster, seed_val)
    
    #########################
    ### REQUIREMENTS TEXT ###
    #########################
    
    def _bottles_requirements_text(self, final_note_option, final_note_score, final_puzzle_option, final_puzzle_score):
        self.speech_manip._modify_bottles_unskippable_text(final_note_option, final_note_score, final_puzzle_option, final_puzzle_score)
        self.speech_manip._shorten_bottles_secret_game_text()
    
    ##################
    ### TTC OPTION ###
    ##################
    
    def _ttc_sandcastle_code(self):
        # Code: FB1AEB - FB24A0
        # 6B 6E 69 70 36 38 6E 33 36 36 34 6A
        # Texture: 0x10220 - 60FC30
        pass
    
    def _ttc_main(self):
        '''PyDoc'''
        # FA9150 - FB24A0
        pass
    
    #################
    ### GV OPTION ###
    #################
    
    def _gv_matching_puzzle_combination(self):
        '''PyDoc'''
        # FAE27E - FAE860
        # Every 8 bytes is one section of the matching puzzle
        #     COUNT PATRN ?? ?? ?? ??
        #     01 90 00 01 00 00 00 00
        with open(f"{self._file_dir}Randomized_ROM/FAE27E-Decompressed.bin", "r+b") as overlay_file:
            mm_overlay = mmap.mmap(overlay_file.fileno(), 0)
            index_start = mm_overlay.find(bytes.fromhex("0190000100000000"))
            selectable_values = []
            for index_val in range(16):
                selectable_values.append(mm_overlay[index_start + 3 + (8*index_val)])
            random.seed(a=self._seed_val)
            random.shuffle(selectable_values)
            for index_val in range(16):
                mm_overlay[index_start + 3 + (8*index_val)] = selectable_values[index_val]
        return selectable_values
    
    def _gv_matching_puzzle_textures(self, selectable_values):
        with open(f"{self._file_dir}Randomized_ROM/10248-Decompressed.bin", "r+b") as decomp_file:
            mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
            RGBA32_address_dict = {"Jinjo": (0x240, 0x1240), "Egg": (0x2E60, 0x3E60), "Kazooie": (0x4660, 0x5660), "Mumbo": (0xA6C0, 0xB6C0)}
            for texture in RGBA32_address_dict:
                for curr_index in range(RGBA32_address_dict[texture][0], RGBA32_address_dict[texture][1], 4):
                    if(mm_decomp[curr_index + 3] != 0):
                        mm_decomp[curr_index] = 0xFF
                        mm_decomp[curr_index + 1] = 0xFF
                        mm_decomp[curr_index + 2] = 0xFF
                        mm_decomp[curr_index + 3] = 0xFF
                    else:
                        mm_decomp[curr_index] = 0x0
                        mm_decomp[curr_index + 1] = 0x0
                        mm_decomp[curr_index + 2] = 0x0
                        mm_decomp[curr_index + 3] = 0x0
            RGBA16_address_dict = {"Note": (0x1240, 0x1E40), "Feather": (0x2660, 0x2E60), "Banjo": (0x3E60, 0x4660), "Honeycomb": (0x9EC0, 0xA6C0)}
            for texture in RGBA16_address_dict:
                for curr_index in range(RGBA16_address_dict[texture][0], RGBA16_address_dict[texture][1], 2):
                    if((mm_decomp[curr_index + 1] % 2) == 1):
                        mm_decomp[curr_index] = 0xFF
                        mm_decomp[curr_index + 1] = 0xFF
                    else:
                        mm_decomp[curr_index] = 0x0
                        mm_decomp[curr_index + 1] = 0x0
            for index in range(16):
                tile_index = 0x190 + index
                tile_value = selectable_values[index]
                new_color_red = 0xFF * ((tile_value >> 2) % 2)
                new_color_green = 0xFF * ((tile_value >> 1) % 2)
                new_color_blue = 0xFF * (tile_value % 2)
                for color_index in range(gv_matching_puzzle_pictures[tile_index], gv_matching_puzzle_pictures[tile_index] + 64, 16):
                    mm_decomp[color_index] = new_color_red
                    mm_decomp[color_index + 1] = new_color_green
                    mm_decomp[color_index + 2] = new_color_blue
    
    def _gv_cheat_sheet(self, selectable_values):
        '''PyDoc'''
        cheat_sheet_dict = {
            0: "___BLACK___", 1: "___BLUE____", 2: "___GREEN___", 3: "___CYAN____",
            4: "____RED____", 5: "__MAGENTA__", 6: "__YELLOW___", 7: "___WHITE___"
        }
        cheat_sheet_str = "| "
        for val1 in range(15, 11, -1):
            for val2 in range(4):
                cheat_sheet_str += f"{cheat_sheet_dict[selectable_values[val1 - (4 * val2)]]} | "
            if(val1 > 12):
                cheat_sheet_str += "\n| "
        with open(f"{self._file_dir}Randomized_ROM/MATCHING_PUZZLE_CHEAT_SHEET_{self._seed_val}.txt", "w+") as mp_cheat_sheet:
            mp_cheat_sheet.write(cheat_sheet_str)
    
    def _gv_puzzle_main(self):
        '''PyDoc'''
        # The count starts in the bottom right corner, bottom to top, then right to left, like so
        #  |--------|--------|--------|--------|
        #  |  019F  |  019B  |  0197  |  0193  |
        #  |  0007  |  0001  |  0004  |  0004  |
        #  |--------|--------|--------|--------|
        #  |  019E  |  019A  |  0196  |  0192  |
        #  |  0002  |  0006  |  0000  |  0003  |
        #  |--------|--------|--------|--------|
        #  |  019D  |  0199  |  0195  |  0191  |
        #  |  0005  |  0002  |  0007  |  0005  |
        #  |--------|--------|--------|--------|
        #  |  019C  |  0198  |  0194  |  0190  |
        #  |  0006  |  0000  |  0003  |  0001  |
        #  |--------|--------|--------|--------|
        selectable_values = self._gv_matching_puzzle_combination()
        self._gv_matching_puzzle_textures(selectable_values)
        if(self._grandmaster.cheat_sheet_var.get() == 1):
            self._gv_cheat_sheet(selectable_values)
    
    ##################
    ### RBB OPTION ###
    ##################
    
    def _rbb_code_texture(self, button_combo):
        '''Edits the texture of the side of the boat with the button combination'''
        with open(f"{self._file_dir}Randomized_ROM\\10418-Decompressed.bin", "r+b") as decomp_file:
            mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
            # Clears Number
            for index1 in range(0x1CD60, 0x1CF90, 0x20):
                for index2 in range(0x03, 0x10):
                    index = index1 + index2
                    mm_decomp[index] = 0x11
            for index1 in range(0x1CD70, 0x1CFA0, 0x20):
                for index2 in range(0x00, 0x0C):
                    index = index1 + index2
                    mm_decomp[index] = 0x11
        with open(f"{self._file_dir}Randomized_ROM\\10418-Decompressed.bin", "r+b") as decomp_file:
            mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
            index_list = [0x1CDE4, 0x1CDE8, 0x1CDEC, 0x1CDF0, 0x1CDF4, 0x1CDF8]
            for num in range(len(button_combo)):
                button_num = button_combo[num]
                index_start = index_list[num]
                if(button_num == 49):
                    num_structure = [(0,0), (1,0), (2,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (1,10), (0,10)]
                elif(button_num == 50):
                    num_structure = [(0,0), (1,0), (2,0), (0,1), (0,2), (0,3), (1,3), (1,4), (1,5), (2,5), (2,6), (2,7), (2,8), (2,9), (1,10), (0,9), (0,8)]
                elif(button_num == 51):
                    num_structure = [(0,0), (1,0), (2,1), (2,2), (2,3), (2,4), (2,6), (2,7), (2,8), (2,9), (1,5), (0,5), (1,10), (0,10)]
                for (x_offset, y_offset) in num_structure:
                    mm_decomp[index_start + x_offset + (32*y_offset)] = 2
    
    def _rbb_combination(self):
        '''Generates a new button combination'''
        # FBE5E2 - FBEBE0
        # Search for 33 31 32 31 31 31 00
        with open(f"{self._file_dir}Randomized_ROM/FBE5E2-Decompressed.bin", "r+b") as decomp_file:
            mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
            text_index_start = mm_decomp.find(bytes.fromhex("33313231313100"))
            random.seed(a=self._seed_val)
            button_combo = random.choices([49, 50, 51], k=6)
            for index in range(len(button_combo)):
                mm_decomp[text_index_start + index] = button_combo[index]
        return button_combo
    
    def _rbb_buttons_main(self):
        '''Handles the RBB RANDOM BUTTON COMBO functions'''
        button_combo = self._rbb_combination()
        self._rbb_code_texture(button_combo)

    ###########################
    ### MODELS AND TEXTURES ###
    ###########################
    
    def _bk_model(self, seed_val):
        '''Runs the functions for editing the Banjo Kazooie models'''
        bk_model_obj = BK_Model(self._file_dir, "7900", original_index_start=0xB138)
        bk_model_obj._main(
            banjo_fur=self._grandmaster.banjo_fur_var.get(),
            banjo_skin=self._grandmaster.banjo_skin_var.get(),
            banjo_feet=self._grandmaster.banjo_feet_var.get(),
            kazooie_primary=self._grandmaster.kazooie_primary_var.get(),
            kazooie_secondary=self._grandmaster.kazooie_secondary_var.get(),
            kazooie_wing_primary=self._grandmaster.kazooie_wing_primary_var.get(),
            kazooie_wing_secondary=self._grandmaster.kazooie_wing_secondary_var.get(),
            backpack=self._grandmaster.backpack_var.get(),
            wading_boots=self._grandmaster.wading_boots_var.get(),
            shorts_vertex=self._grandmaster.shorts_vertex_var.get(),
            shorts_texture=self._grandmaster.shorts_texture_var.get(),
            tooth_necklace=self._grandmaster.tooth_necklace_var.get()
            )
        bk_model_obj._only_low_poly_bk_model(seed_val)

    def _other_model_shuffle(self, seed_val, file_dir, randomized_rom_path):
        '''PyDoc'''
        swap_model_manip = Swap_Models_Manipulation(seed_val, file_dir, randomized_rom_path)
        swap_model_manip._model_manip_main()

    def _animation_shuffle(self, seed_val, file_dir, randomized_rom_path):
        '''PyDoc'''
        swap_animation_manip = Swap_Animations_Manipulation(seed_val, file_dir, randomized_rom_path)
        swap_animation_manip._animation_manip_main()

    ########################
    ### SOUNDS AND MUSIC ###
    ########################
    
    def _shuffle_music(self, seed_val, file_dir, randomized_rom_path, short_sounds_var, jingles_var, music_var, beta_sounds_var):
        '''Runs the functions for shuffling the music'''
        music_manip = Music_Manipulation(seed_val, file_dir, randomized_rom_path, short_sounds_var, jingles_var, music_var, beta_sounds_var)
        music_manip._music_manip_main()
    
    ################
    ### SKYBOXES ###
    ################
    
    def _shuffle_skyboxes(self, seed_val, file_dir, randomized_rom_path):
        '''Runs the functions for shuffling the skyboxes'''
        skybox_manip = Skybox_Manipulation(seed_val, file_dir, randomized_rom_path)
        skybox_manip._skybox_manip_main()
    
    ###############
    ### SPRITES ###
    ###############
    
    def _shuffle_sprites(self, seed_val, file_dir, randomized_rom_path):
        '''Runs the functions for shuffling the sprites'''
        sprite_manip = Sprite_Manipulation(seed_val, file_dir, randomized_rom_path)
        sprite_manip._sprite_manip_main()

    ###################
    ### GAME ENGINE ###
    ###################
    
    def _setup_game_engine_manip(self):
        game_engine_obj = Game_Engine_Class(self._file_dir)
        game_engine_obj._starting_moves()

    ########################
    ### EDIT OTHER TEXTS ###
    ########################
    
    def _edit_intro_cutscene_text_main(self):
        self.speech_manip._bottles_introduction_text()
        self.speech_manip._intro_cutscene_1()
        self.speech_manip._intro_cutscene_2()
        self.speech_manip._intro_cutscene_3()
        self.speech_manip._intro_cutscene_4()
        self.speech_manip._intro_cutscene_5()
        self.speech_manip._intro_cutscene_6()
        self.speech_manip._intro_cutscene_7()
        self.speech_manip._intro_cutscene_8()
        self.speech_manip._intro_cutscene_9()
        self.speech_manip._intro_cutscene_10()
        self.speech_manip._intro_cutscene_11()
        self.speech_manip._intro_cutscene_12()
        self.speech_manip._intro_cutscene_13()
        self.speech_manip._intro_cutscene_14()
        self.speech_manip._intro_cutscene_15()
        self.speech_manip._enter_lair_cutscene()
    
    def _edit_world_order_related_text_main(self):
        self.speech_manip._bottles_50_notes()
        self.speech_manip._bottles_enter_mm_moves()
        self.speech_manip._bottles_learned_mm_moves()
        self.speech_manip._bottles_enter_ttc_moves()
        self.speech_manip._bottles_learned_ttc_moves()
        self.speech_manip._bottles_enter_cc_moves()
        self.speech_manip._bottles_learned_cc_moves()
        self.speech_manip._bottles_enter_bgs_moves()
        self.speech_manip._bottles_learned_bgs_moves()
        self.speech_manip._bottles_enter_fp_moves()
        self.speech_manip._bottles_learned_fp_moves()
        self.speech_manip._bottles_enter_gv_moves()
        self.speech_manip._bottles_learned_gv_moves()
    
    def _edit_furnace_fun_questions_main(self):
        '''I probably won't implement this, since it seems everyone just wants to skip furnace fun'''
        pass