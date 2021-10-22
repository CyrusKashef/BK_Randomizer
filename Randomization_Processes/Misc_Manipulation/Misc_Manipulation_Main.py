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

from ..Common_Functions import leading_zeros
from .Model_Data.Models_Main import ModelsMain
from .Music_Data.Music_Main import Music_Manipulation

#################################
### MISCELLANEOUS MANIP CLASS ###
#################################

class misc_manipulation():
    '''Miscellaneous setting manipulation class'''
    def __init__(self, file_dir, seed_val):
        '''Initializes the miscellaneous setting manipulation class'''
        self._file_dir = file_dir
        self._final_note_score = None
        self._final_puzzle_score = None
        self._seed_val = seed_val
    
    #####################
    ### FINAL OPTIONS ###
    #####################
    
    def _gruntildas_lair_requirements(self, final_note_option, final_note_score, final_puzzle_option, final_puzzle_score):
        '''Handles the FINAL NOTE DOOR and FINAL PUZZLE functions and calls the function to adjust Bottles text if needed'''
        # FCF698 - FD0420
        if(final_note_option):
            self._final_note_door(final_note_score)
        if(final_puzzle_option):
            self._final_world_puzzle(final_puzzle_score)
        if(final_note_option or final_puzzle_option):
            self._modify_bottles_unskippable_text()
    
    def _final_note_door(self, final_note_score):
        '''Sets the requirements of every note door to zero except for the note door proceeding the final battle'''
        # Find location of note doors
        # 00 32 00 B4 01 04 01 5E 01 C2 02 80 02 FD 03 2A 03 3C 03 4E 03 60 03 72
        # Every 2 are a note door
        # Edit each note door with zeros
        final_note_score = int(final_note_score)
        with open(f"{self._file_dir}Randomized_ROM\\FCF698-Decompressed.bin", "r+b") as decomp_file:
            mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
            #                                                      0 1 2 3 4 5 6 7 8 91011121314151617181920212223
            note_door_index_start = mm_decomp.find(bytes.fromhex("003200B40104015E01C2028002FD032A033C034E03600372"))
            for offset in range(14):
                mm_decomp[note_door_index_start + offset] = 0
            for offset in range(16, 24):
                mm_decomp[note_door_index_start + offset] = 0
            final_note_score_hex = leading_zeros(str(hex(final_note_score))[2:], 4)
            mm_decomp[note_door_index_start + 14] = int(final_note_score_hex[:2], 16)
            mm_decomp[note_door_index_start + 15] = int(final_note_score_hex[2:], 16)
        self._final_note_score = final_note_score
    
    def _final_world_puzzle(self, final_puzzle_score):
        '''Sets the requirements of every puzzle to zero except for the puzzle proceeding the final battle'''
        # Find location of world puzzles
        # 00 00 01 01 00 5D 02 02 00 5E 05 03 00 60 07 03 00 63 08 04 00 66 09 04 00 6A 0A 04 00 6E 0C 04 00 72 0F 04 00 76 19 05 00 7A 04 03
        # Every 4 is a note door, with the third value being the one you have to change
        final_puzzle_score = int(final_puzzle_score)
        with open(f"{self._file_dir}Randomized_ROM\\FCF698-Decompressed.bin", "r+b") as decomp_file:
            mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
            #                                                      0 1 2 3 4 5 6 7 8 910111213141516171819202122232425262728293031323334353637383940414243
            note_door_index_start = mm_decomp.find(bytes.fromhex("00000101005D0202005E0503006007030063080400660904006A0A04006E0C0400720F0400761905007A0403"))
            for offset in range(0, 37, 4):
                mm_decomp[note_door_index_start + offset + 2] = 0
            mm_decomp[note_door_index_start + 38] = final_puzzle_score
            honeycomb_puzzle_count = 100 - final_puzzle_score
            if(honeycomb_puzzle_count > 4):
                honeycomb_puzzle_count = 4
            mm_decomp[note_door_index_start + 42] = honeycomb_puzzle_count
        self._final_puzzle_score = final_puzzle_score
    
    def _modify_bottles_unskippable_text(self):
        '''Modifies the Bottles text at the beginning of the game'''
        # 5) Able to modify 5C9AF8/CF90.bin
        # (PRESS A IF YOU WANT ME TO TEACH YOU SOME BASIC MOVES, OR PRESS B IF YOU THINK YOU'RE ALREADY GOOD ENOUGH!)
        # "WELCOME TO BANJO KAZOOIE RANDOMIZER V. 0.7.6! THIS GENERATED SEED NEEDS 000 NOTES 000 JIGGIES" + also_add
        # "YOU'LL NEED 000 NOTES TO PASS THE FINAL NOTE DOOR! PRESS A FOR LESSONS OR PRESS B TO SKIP MY NOTES! HAHA!"
        # "YOU'LL NEED 000 JIGGIES TO PASS THE FINAL PUZZLE DOOR! PRESS B TO GO OR PRESS A IF YOU'RE PUZZLED!"
        # "WELCOME TO BANJO-KAZOOIE RANDOMIZER VERSION 0.7.6!!! HOPE YOU ENJOY THE GENERATED SEED!!" + also_add
        if((self._final_note_score != None) and (self._final_puzzle_score != None)):
            new_bottles_text = f"YOU WILL NEED {leading_zeros(str(self._final_note_score), 3)} NOTES AND {leading_zeros(str(self._final_puzzle_score), 3)} JIGGIES TO REACH THE TOP OF THE TOWER! PRESS B AND GET GOING!!!"
        elif(self._final_note_score != None):
            new_bottles_text = f"YOU'LL NEED {leading_zeros(str(self._final_note_score), 3)} NOTES TO PASS THE FINAL NOTE DOOR! PRESS A FOR LESSONS OR PRESS B TO SKIP MY NOTES! HAHA!"
        elif(self._final_puzzle_score != None):
            new_bottles_text = f"YOU'LL NEED {leading_zeros(str(self._final_puzzle_score), 3)} JIGGIES TO PASS THE FINAL PUZZLE DOOR! PRESS B TO GO OR PRESS A IF YOU'RE PUZZLED!"
        for extra_space in range(len(new_bottles_text), 105):
            new_bottles_text += " "
        with open(f"{self._file_dir}Randomized_ROM\\CF90-Decompressed.bin", "r+b") as decomp_file:
            mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
            text_index_start = mm_decomp.find(bytes.fromhex("50524553532041"))
            count = 0
            for char in new_bottles_text:
                mm_decomp[text_index_start + count] = ord(char)
                count += 1
            for index in range(text_index_start + len(new_bottles_text), len(mm_decomp)):
                mm_decomp[index] = mm_decomp[index]
    
    ##################
    ### TTC OPTION ###
    ##################
    
    def _ttc_main(self):
        '''PyDoc'''
        # FA9150 - FB24A0
        pass
    
    #################
    ### GV OPTION ###
    #################
    
    def _gv_main(self):
        '''PyDoc'''
        # FAE27E - FAE860
        pass
    
    ##################
    ### MMM OPTION ###
    ##################
    
    def _mmm_main(self):
        '''PyDoc'''
        # FA8CE6 - FA9150
        pass
    
    ##################
    ### RBB OPTION ###
    ##################
    
    def _rbb_buttons_main(self):
        '''Handles the RBB RANDOM BUTTON COMBO functions'''
        button_combo = self._rbb_combination()
        self._rbb_code_texture(button_combo)
    
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
        with open(f"{self._file_dir}Randomized_ROM\\FBE5E2-Decompressed.bin", "r+b") as decomp_file:
            mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
            text_index_start = mm_decomp.find(bytes.fromhex("33313231313100"))
            random.seed(a=self._seed_val)
            button_combo = random.choices([49, 50, 51], k=6)
            for index in range(len(button_combo)):
                mm_decomp[text_index_start + index] = button_combo[index]
        return button_combo

    ###########################
    ### MODELS AND TEXTURES ###
    ###########################
    
    def _bk_model(self, seed_val=None, banjo_fur_color=None, banjo_skin_color=None, banjo_toes_color=None, kazooie_feather_color=None, kazooie_spot_color=None, backpack_color=None, banjo_shorts_color=None):
        '''Runs the functions for editing the Banjo Kazooie models'''
        model_main = ModelsMain(self._file_dir)
        model_main._bk_model1(banjo_fur_color, banjo_skin_color, banjo_toes_color, kazooie_feather_color, kazooie_spot_color, backpack_color, banjo_shorts_color)
        model_main._only_bk_model1(seed_val)

    ########################
    ### SOUNDS AND MUSIC ###
    ########################
    
    def _shuffle_music(self, seed_val, file_dir, randomized_rom_path, short_sounds_var, jingles_var, music_var, beta_sounds_var):
        '''Runs the functions for shuffling the music'''
        music_manip = Music_Manipulation(seed_val, file_dir, randomized_rom_path, short_sounds_var, jingles_var, music_var, beta_sounds_var)
        music_manip._music_manip_main()

    ###################
    ### DOESNT WORK ###
    ###################
    
    def _abilities_setup(self):
        '''PyDoc'''
        # F37F90 - F9CAE0
        pass