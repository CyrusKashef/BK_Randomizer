'''
Created on Aug 23, 2021

@author: Cyrus

##################
### GUI LAYOUT ###
##################

    #################################################
    #                                               #
    #                 VARIABLE_TEXT                 #
    #                                               #
    #  |-----------------------------------------|  #
    #  |//////////////////////                   |  #
    #  |-----------------------------------------|  #
    #                                               #
    #################################################

####################
### GUI FUNCTION ###
####################

VARIABLE TEXT:
1) Setup
2) Decompressing
3) Randomizing Worlds
4) Miscellaneous Options
5) Compressing
6) CRC Tool
7) Clean Up
8) Done, Close Window

###########################
### GUI ERRORS/WARNINGS ###
###########################

* Closing the progress bar window prematurely does not stop the process from attempting to finish.
* Closing the user gui will close this window, causing a crash. Process does not finish.
* If error occurs, progress bar remains frozen. Needs to be updated to alert the user a crash occured.

#########################
### USER GUI OVERVIEW ###
#########################

    ##########            #################               ##############################           #####################
   #          #          #                 #              #                            #  8 DONE   #                   #
  #  USER GUI  # -----> #  PROGRESSION GUI  # ----------> #   PROGRESS BAR WINDOW      # --------> # YOU CAN CLOSE NOW #
   #          #          #                 #              #                            #           #                   #
    ##########            #################               ##############################           #####################
                                  |                        ^   ^  ^  ^   ^   ^   ^   ^
                                  |                        |   |  |  |   |   |   |   |
                                  |   ###################  |   |  |  |   |   |   |   |
                                  |   #                 #  |   |  |  |   |   |   |   |
                                1 |-> # SETUP FUNCTIONS #--|   |  |  |   |   |   |   |
                                  |   #                 #      |  |  |   |   |   |   |
                                  |   ###################      |  |  |   |   |   |   |
                                  |                            |  |  |   |   |   |   |
                                  |       #################    |  |  |   |   |   |   |
                                  |       #               #    |  |  |   |   |   |   |
                                2 |-----> # DECOMPRESSING #    |  |  |   |   |   |   |
                                  |       #   FUNCTIONS   #----|  |  |   |   |   |   |
                                  |       #               #       |  |   |   |   |   |
                                  |       #################       |  |   |   |   |   |
                                  |                               |  |   |   |   |   |
                                  |           ###############     |  |   |   |   |   |
                                  |           #             #     |  |   |   |   |   |
                                  |           # RANDOMIZING #     |  |   |   |   |   |
                                3 |---------> #   WORLDS    #-----|  |   |   |   |   |
                                  |           #             #        |   |   |   |   |
                                  |           ###############        |   |   |   |   |
                                  |                                  |   |   |   |   |
                                  |               #################  |   |   |   |   |
                                  |               #               #  |   |   |   |   |
                                4 |-------------> # MISCELLANEOUS #--|   |   |   |   |
                                  |               #    OPTIONS    #      |   |   |   |
                                  |               #               #      |   |   |   |
                                  |               #################      |   |   |   |
                                  |                                      |   |   |   |
                                  |                   ###############    |   |   |   |
                                  |                   #             #    |   |   |   |
                                5 |-----------------> # RECALCULATE #----|   |   |   |
                                  |                   #  CHECKSUM   #        |   |   |
                                  |                   #             #        |   |   |
                                  |                   ###############        |   |   |
                                  |                                          |   |   |
                                  |                      ###############     |   |   |
                                  |                      #             #     |   |   |
                                  |                      # COMPRESSING #     |   |   |
                                6 |--------------------> #  FUNCTIONS  #-----|   |   |
                                  |                      #             #         |   |
                                  |                      ###############         |   |
                                  |                                              |   |
                                  |                          ############        |   |
                                  |                          #          #        |   |
                                7 |------------------------> # CRC TOOL #--------|   |
                                  |                          #          #            |
                                  |                          ############            |
                                  |                                                  |
                                  |                             ############         |
                                  |                             #          #         |
                                8 |---------------------------> # CLEAN UP #---------|
                                                                #          #
                                                                ############

'''

######################
### PYTHON IMPORTS ###
######################

from random import seed, randint
import tkinter as tk
from tkinter import ttk
from tkinter import HORIZONTAL
import threading
import gc

####################
### FILE IMPORTS ###
####################

from Randomization_Processes.Setup_Functions import setup_tmp_folder, set_seed, make_copy_of_rom
from Randomization_Processes.Decompress_Functions import Decompressor
from Randomization_Processes.Compress_Functions import Compressor
from Randomization_Processes.World_Manipulation.World_Manipulation_Main import World_Manipulation_Class
from Randomization_Processes.Misc_Manipulation.Misc_Manipulation_Main import Misc_Manipulation_Class
# from Randomization_Processes.CRC_Tool import run_crc_calc
from Randomization_Processes.CRC_Tool import CRC_Calc_Class
from Randomization_Processes.Clean_Up import CleanUp
from Randomization_Processes.BK_Checksum import BK_Checksum_Class

#################
### GUI CLASS ###
#################

class Progression_GUI_Class():
    '''Progression GUI class'''
    def __init__(self, master):
        '''Initializes the Progress GUI'''
        self.master = master
        self.rom_path = self.master.rom_file_entry.get()
        if(master.app_window):
            self.progress_bar_window = tk.Toplevel(master.app_window)
        else:
            self.progress_bar_window = tk.Tk()
        self.progress_bar_window.winfo_toplevel().title("Banjo-Kazooie Randomizer Progress Bar")
#         self.progress_bar_window.geometry("400x50")
        self.progress_bar_window.config(background="#F3E5AB")
        self.progress_bar_value = 0
        self._mumbo_error_message = "Please Check The ReadMe Under 'GUI Errors/Warnings' For Instructions"
        self.transform_cost_dict = {
                "Termite": 5,
                "Crocodile": 10,
                "Walrus": 15,
                "Pumpkin": 20,
                "Bee": 25
                }
    
    class App_Variable_Label():
        '''A text box that can altered after creation'''
        def __init__(self, window, label_text):
            '''Initializes variable label'''
            self.text = tk.StringVar()
            self.text.set(label_text)
            self.label = tk.Label(window, textvariable=self.text, background="#F3E5AB", font=("Arial", 12), padx=5, pady=5)

        def set_text(self, new_text):
            '''Changes the text'''
            self.text.set(new_text)

        def pack_label(self):
            '''Displays label'''
            self.label.pack()
    
    class App_ProgressBar():
        '''A progress bar'''
        def __init__(self, window, bar_length=390, bar_mode='determinate'):
            '''Initializes progress bar'''
            self.progressbar = ttk.Progressbar(window, style="bk.Horizontal.TProgressbar", orient=HORIZONTAL, length=bar_length, mode=bar_mode)
            self.progressbar.config(maximum=100)

        def update_bar(self, percentage):
            '''Updates progress bar percentage'''
            self.progressbar['value'] = percentage

        def pack_bar(self):
            '''Displays progress bar'''
            self.progressbar.pack(padx=5, pady=5)
    
    def _hidden_random_values(self):
        self.master.logger.info("Hidden Random Values")
        cheat_sheet = ""
        # Final Note Door
        if(self.master.final_note_door_value.get() == "?"):
            seed(a=(self.master.seed_value.get()))
            if(self.master.struct_var.get() == "All Notes"):
                self.master.final_note_door_val = randint(0, 2000)
            else:
                self.master.final_note_door_val = randint(0, 900)
            cheat_sheet += f"Final Note Door Val: {self.master.final_note_door_val}\n"
        else:
            self.master.final_note_door_val = int(self.master.final_note_door_value.get())
        self.master.logger.debug(f"Final Note Door Val: {self.master.final_note_door_val}")
        # Final Puzzle
        if(self.master.final_puzzle_value.get() == "?"):
            seed(a=(self.master.seed_value.get()))
            if(self.master.remove_floating_jiggies_var.get() == 1):
                self.master.final_puzzle_val = randint(0, 50)
            else:
                self.master.final_puzzle_val = randint(0, 99)
            cheat_sheet += f"Final Puzzle Val: {self.master.final_puzzle_val}\n"
        else:
            self.master.final_puzzle_val = int(self.master.final_puzzle_value.get())
        self.master.logger.debug(f"Final Puzzle Val: {self.master.final_puzzle_val}")
        ### CAPACITIES
        # Blue Egg Capacity
        if(self.master.before_blue_egg_carry_value.get() == "?"):
            self.master.before_blue_egg = randint(0, 255)
            cheat_sheet += f"Before Cheato Blue Egg: {self.master.before_blue_egg}\n"
        else:
            self.master.before_blue_egg = int(self.master.before_blue_egg_carry_value.get())
        self.master.logger.debug(f"Before Cheato Blue Egg: {self.master.before_blue_egg}")
        if(self.master.before_blue_egg_carry_value.get() == "?"):
            self.master.after_blue_egg = randint(32, 255)
            cheat_sheet += f"After Cheato Blue Egg: {self.master.after_blue_egg}\n"
        else:
            self.master.after_blue_egg = int(self.master.before_blue_egg_carry_value.get())
        self.master.logger.debug(f"After Cheato Blue Egg: {self.master.after_blue_egg}")
        # Red Feather Capacity
        if(self.master.before_red_feather_carry_value.get() == "?"):
            self.master.before_red_feather = randint(0, 255)
            cheat_sheet += f"Before Cheato Red Feather: {self.master.before_red_feather}\n"
        else:
            self.master.before_red_feather = int(self.master.before_red_feather_carry_value.get())
        self.master.logger.debug(f"Before Cheato Red Feather: {self.master.before_red_feather}")
        if(self.master.after_red_feather_carry_value.get() == "?"):
            self.master.after_red_feather = randint(8, 255)
            cheat_sheet += f"After Cheato Red Feather: {self.master.after_red_feather}\n"
        else:
            self.master.after_red_feather = int(self.master.after_red_feather_carry_value.get())
        self.master.logger.debug(f"After Cheato Red Feather: {self.master.after_red_feather}")
        # Gold Feather Capacity
        if(self.master.before_gold_feather_carry_value.get() == "?"):
            self.master.before_gold_feather = randint(0, 255)
            cheat_sheet += f"Before Cheato Gold Feather: {self.master.before_gold_feather}\n"
        else:
            self.master.before_gold_feather = int(self.master.before_gold_feather_carry_value.get())
        self.master.logger.debug(f"Before Cheato Gold Feather: {self.master.before_gold_feather}")
        if(self.master.after_gold_feather_carry_value.get() == "?"):
            self.master.after_gold_feather = randint(0, 255)
            cheat_sheet += f"After Cheato Gold Feather: {self.master.after_gold_feather}\n"
        else:
            self.master.after_gold_feather = int(self.master.after_gold_feather_carry_value.get())
        self.master.logger.debug(f"After Cheato Gold Feather: {self.master.after_gold_feather}")
        # Cheat Sheet
        with open(f"{self.master.cwd}Randomized_ROM/HIDDEN_VALUES_CHEAT_SHEET_{self.seed_val}.txt", "w+") as f:
            f.write(cheat_sheet)
    
    def _setup(self):
        '''Creates the randomized ROM folder with a copy of the original ROM file'''
        self.master.logger.info("Randomization Setup")
        setup_tmp_folder(self.master.cwd)
        self.seed_val = set_seed(self.master.seed_value.get())
        self._hidden_random_values()
        self.randomized_rom_path = make_copy_of_rom(self.seed_val, self.master.cwd, self.rom_path)
        gc.enable()
    
    def _decompress_main(self):
        '''Runs the decompression functions'''
        self.master.logger.info("Decompress Main")
        decompressor = Decompressor(self.master.cwd, self.randomized_rom_path)
        decompressor._decompress_main()
        del decompressor
    
    def _randomize_world(self):
        '''Runs the world manipulation functions, including world specific functions'''
        self.master.logger.info("Start Of Randomize World")
        try:
            self.pb_label.set_text("Mumbo Creating Worlds...")
            world_manip = World_Manipulation_Class(self.master, self.seed_val)
            world_manip._create_worlds()
        except Exception:
            self.master.logger.info("Creating Worlds Error")
            self.pb_label.set_text(f"Error Generating Worlds...\n{self._mumbo_error_message}")
            raise
        # Specificly needs to go first
        if(self.master.world_entrance_var.get() == "Bottles Shuffle"):
            try:
                self.pb_label.set_text("Bear And Bird Need Extra Lives...")
                world_manip._bottles_to_1_ups()
            except Exception:
                self.master.logger.info("Bottles To 1-Ups Error")
                self.pb_label.set_text(f"Error Preparing Bottles Shuffle...\n{self._mumbo_error_message}")
                raise
        # Dropdown Boxes
        try:
            self.pb_label.set_text("Mumbo Hut Filled With Notes, Eggs, & Feathers...")
            world_manip._structs_main()
        except Exception:
            self.master.logger.info("Structs Error")
            self.pb_label.set_text(f"Error Swapping Notes/Eggs/Feathers...\n{self._mumbo_error_message}")
            raise
        try:
            self.pb_label.set_text("Jinjos Are Good Friends Of Mumbo...")
            world_manip._non_flag_objects_main()
        except Exception:
            self.master.logger.info("Non-Flag Objects Error")
            self.pb_label.set_text(f"Error Moving Jinjos & Extra Lives...\n{self._mumbo_error_message}")
            raise
        try:
            self.pb_label.set_text("Me Summon Gold Statue To Kick Baddie Butt!...")
            world_manip._enemies_main()
        except Exception:
            self.master.logger.info("Enemies Error")
            self.pb_label.set_text(f"Error Moving Enemies...\n{self._mumbo_error_message}")
            raise
        try:
            self.pb_label.set_text("Mumbo Keep Token Or Two...")
            world_manip._flagged_objects_main()
        except Exception:
            self.master.logger.info("Flagged Objects Error")
            self.pb_label.set_text(f"Error Moving Jiggies/Tokens/Honeycombs...\n{self._mumbo_error_message}")
            raise
        try:
            self.pb_label.set_text("Mumbo Has Stronger Magic Than Note Door...")
            world_manip._note_doors_main(self.master.final_note_door_val)
        except Exception:
            self.master.logger.info("Note Doors Error")
            self.pb_label.set_text(f"Error Changing Note Doors...\n{self._mumbo_error_message}")
            raise
        # Checkboxes
        if(self.master.remove_magic_barriers_var.get() == 1):
            try:
                self.pb_label.set_text("Mumbo Make Good Transformation Spells...")
                world_manip._magic_barrier_main()
            except Exception:
                self.master.logger.info("Remove Magic Barriers Error")
                self.pb_label.set_text(f"Error Removing Magic Barriers...\n{self._mumbo_error_message}")
                raise
        if(self.master.skip_furnace_fun_var.get() == 1):
            try:
                self.pb_label.set_text("Furnace Fun No Fun...")
                world_manip._skip_furnace_fun()
            except Exception:
                self.master.logger.info("Skip Furnace Fun Error")
                self.pb_label.set_text(f"Error Skipping Furnace Fun...\n{self._mumbo_error_message}")
                raise
        if(self.master.hard_rings_var.get() == 1):
            try:
                self.pb_label.set_text("Mumbo Use Clanker For Parts...")
                world_manip._shuffle_clanker_rings()
            except Exception:
                self.master.logger.info("Shuffle Clanker's Rings Error")
                self.pb_label.set_text(f"Error Shuffling Clanker's Rings...\n{self._mumbo_error_message}")
                raise
        if(self.master.croctus_var.get() == 1):
            try:
                self.pb_label.set_text("Mumbo Need New Boots! Only Kidding...")
                world_manip._shuffle_croctus()
            except Exception:
                self.master.logger.info("Shuffle Croctus Error")
                self.pb_label.set_text(f"Error Shuffling Croctus...\n{self._mumbo_error_message}")
                raise
        if(self.master.mr_vile_var.get() == 1):
            try:
                self.pb_label.set_text("Mumbo Use Enlarge Spell...")
                world_manip._bigger_badder_mr_vile_main()
            except Exception:
                self.master.logger.info("Mr. Vile Error")
                self.pb_label.set_text(f"Error Changing Mr. Vile...\n{self._mumbo_error_message}")
                raise
        if(self.master.tiptup_choir_var.get() == 1):
            try:
                self.pb_label.set_text("Mumbo Sing Good, Too...")
                world_manip._tiptup_choir_main()
            except Exception:
                self.master.logger.info("Tiptup Choir Error")
                self.pb_label.set_text(f"Error Moving Tiptup Choir...\n{self._mumbo_error_message}")
                raise
        if(self.master.hard_races_var.get() == 1):
            try:
                self.pb_label.set_text("WAHAY!...")
                world_manip._boggy_race_flags_main()
            except Exception:
                self.master.logger.info("Boggy Race Error")
                self.pb_label.set_text(f"Error Adjusting Boggy Race...\n{self._mumbo_error_message}")
                raise
        if(self.master.ancient_ones_var.get() == 1):
            try:
                self.pb_label.set_text("Me Thought Ancient Ones Already Random?...")
                world_manip._shuffle_ancient_ones()
            except Exception:
                self.master.logger.info("Shuffle Ancient Ones Error")
                self.pb_label.set_text(f"Error Shuffling Ancient Ones...\n{self._mumbo_error_message}")
                raise
        if(self.master.maze_jinxy_heads_var.get() == 1):
            try:
                self.pb_label.set_text("Dum Dum Give Gum Gum...")
                world_manip._shuffle_jinxy_heads()
            except Exception:
                self.pb_label.set_text(f"Error Moving Jinxy Heads...\n{self._mumbo_error_message}")
                raise
        if(self.master.world_entrance_var.get() != "None"):
            try:
                self.pb_label.set_text("Mumbo Lost Way Back To Mountain...")
                self.transform_cost_dict = world_manip._world_order_warps_main()
            except Exception:
                self.master.logger.info("World Order Warps Error")
                self.pb_label.set_text(f"Error Shuffling World Order...\n{self._mumbo_error_message}")
                raise
        if(self.master.within_world_warps_var.get() != "None"):
            try:
                self.pb_label.set_text("Mumbo Lost Way Back To Skull...")
                world_manip._within_world_warps_main()
            except Exception:
                self.master.logger.info("Within World Warps Error")
                self.pb_label.set_text(f"Error Shuffling World Warps...\n{self._mumbo_error_message}")
                raise
        try:
            self.pb_label.set_text("Mumbo Make Cheat Sheet Hehe...")
            world_manip._generate_cheat_sheet()
        except Exception:
            self.master.logger.info("Cheat Sheet Error")
            self.pb_label.set_text(f"Error Making Cheat Sheet...\n{self._mumbo_error_message}")
            raise
        if(self.master.gruntilda_difficulty_var.get() > 0):
            try:
                self.pb_label.set_text("If Bear And Bird Lose, Mumbo Go Get Flower...")
                world_manip._harder_final_battle_main(self.master.gruntilda_difficulty_var.get())
#                 world_manip._return_of_furnace_fun()
            except Exception:
                self.master.logger.info("Harder Final Battle Error")
                self.pb_label.set_text(f"Error Adjusting Final Battle...\n{self._mumbo_error_message}")
                raise
        if(self.master.final_puzzle_var.get() == 1):
            try:
                self.pb_label.set_text(f"Mumbo Make Traveling Easier...")
                world_manip._final_world_puzzle(self.master.final_puzzle_val)
            except Exception:
                self.master.logger.info("Final World Puzzle Error")
                self.pb_label.set_text(f"Error Making Worlds Open...\n{self._mumbo_error_message}")
                raise
        if(self.master.scattered_structs_var.get() == 1):
            try:
                self.pb_label.set_text(f"Mumbo Better Shaman Than SM64 Modders...")
                world_manip._scattered_structs_main()
            except Exception:
                self.master.logger.info("Scattered Struct Error")
                self.pb_label.set_text(f"Error Scattering Notes...\n{self._mumbo_error_message}")
                raise
        if(self.master.ccw_open_var.get() == 1):
            try:
                self.pb_label.set_text(f"Be Vewy Vewy Quiet...")
                if(self.master.ccw_var.get() == "Season"):
                    world_manip._ccw_open_seasons_by_season()
                elif(self.master.ccw_var.get() == "Within World"):
                    world_manip._ccw_open_seasons_within_world()
            except Exception:
                self.master.logger.info("CCW Open Seasons Error")
                self.pb_label.set_text(f"Error CCW Open Seasons...\n{self._mumbo_error_message}")
        del world_manip
        self.master.logger.info("End of Randomize World")
    
    def _misc_options(self):
        '''Runs all non-world functions, such as overlays, models, and speeches'''
        self.master.logger.info("Start of Misc Options")
        try:
            self.pb_label.set_text(f"Mumbo Want To Edit Other Things...")
            misc_manip = Misc_Manipulation_Class(self.master, self.seed_val)
        except Exception:
            self.warning_label.set_text("Uh-Oh...")
            self.pb_label.set_text(f"Error Making Manipulation Class...\n{self._mumbo_error_message}")
            raise
        try:
            self.pb_label.set_text("Mumbo Make Bottles Say Silly Words...")
            misc_manip._bottles_requirements_text(self.master.final_note_door_var.get(), self.master.final_note_door_val,
                                              self.master.final_puzzle_var.get(), self.master.final_puzzle_val)
        except Exception:
            self.warning_label.set_text("Uh-Oh...")
            self.pb_label.set_text(f"Error Adjusting Note & Jiggy Requirement...\n{self._mumbo_error_message}")
            raise
        if(self.master.buttons_var.get() == 1):
            try:
                self.pb_label.set_text("Uh, Mumbo Forgot Code...")
                misc_manip._rbb_buttons_main()
            except Exception:
                self.warning_label.set_text("Uh-Oh...")
                self.pb_label.set_text(f"Error Randomizing RBB Code...\n{self._mumbo_error_message}")
                raise
        if(self.master.motzand_keys_var.get() == 1):
            try:
                self.pb_label.set_text("Magic To Mumbo's Ears...")
                misc_manip._motzand_keys_main()
            except Exception:
                self.warning_label.set_text("Uh-Oh...")
                self.pb_label.set_text(f"Error Randomizing Motzand's Song...\n{self._mumbo_error_message}")
                raise
        if(self.master.matching_puzzle_var.get() == 1):
            try:
                self.pb_label.set_text("Mumbo No So Good At Puzzles...")
                misc_manip._gv_puzzle_main()
            except Exception:
                self.warning_label.set_text("Uh-Oh...")
                self.pb_label.set_text(f"Error Shuffling Matching Puzzle...\n{self._mumbo_error_message}")
                raise
        if(self.master.bk_model_var.get() != "Default"):
            try:
                self.pb_label.set_text("Stand On Skull And Press B To See Mighty Mumbo Magic...")
                misc_manip._bk_model(seed_val=self.seed_val)
            except Exception:
                self.warning_label.set_text("Uh-Oh...")
                self.pb_label.set_text(f"Error Adjusting BK's Colors...\n{self._mumbo_error_message}")
                raise
        customization_option = False
        for custom_count, custom_name in enumerate(self.master.map_config_checkbox_dict):
            if(self.master.map_config_checkbox_dict[custom_name].get() == 2):
                seed(a=(self.seed_val + custom_count))
                self.master.map_config_checkbox_dict[custom_name].set(randint(0, 1))
            if(self.master.map_config_checkbox_dict[custom_name].get() == 1):
                customization_option = True
        try:
            self.pb_label.set_text("Hut Music Best Music...")
            misc_manip._shuffle_music(self.seed_val, self.master.cwd, self.rom_path)
        except Exception:
            self.pb_label.set_text(f"Error Shuffling Sounds/Jingles/Music...\n{self._mumbo_error_message}")
            raise
        if(customization_option):
            try:
                self.pb_label.set_text("Banjo Must Stand Still Or Spell Go All Funny...\n(Takes Longer The More Options You Selected)")
                misc_manip._models_animations_properties(self.seed_val, self.master.cwd, self.rom_path)
            except Exception:
                self.warning_label.set_text("Uh-Oh...")
                self.pb_label.set_text(f"Error Swapping Models/Animations/Properties...\n{self._mumbo_error_message}")
                raise
        if((self.master.before_blue_egg_carry_value.get() != 100) or (self.master.after_blue_egg_carry_value.get() != 200) or
           (self.master.before_red_feather_carry_value.get() != 50) or (self.master.after_red_feather_carry_value.get() != 100) or
           (self.master.before_gold_feather_carry_value.get() != 10) or (self.master.after_gold_feather_carry_value.get() != 20)):
            try:
                self.pb_label.set_text("Mumbo Adjusting Powerful Spells...")
                misc_manip._adjust_sandcastle_speeches()
            except Exception:
                self.warning_label.set_text("Uh-Oh...")
                self.pb_label.set_text(f"Error Adjusting Carrying Capacity...\n{self._mumbo_error_message}")
                raise
        try:
            self.pb_label.set_text("Mumbo Hide Easter Egg...")
            misc_manip._edit_cutscenes_text_main()
            if(self.master.skip_furnace_fun_var.get() == 1):
                misc_manip._gruntildas_lair_speeches_main()
        except Exception:
            self.warning_label.set_text("Uh-Oh...")
            self.pb_label.set_text(f"Error Placing Easter Eggs...\n{self._mumbo_error_message}")
            raise
        if(self.master.skip_furnace_fun_var.get() == 1):
            try:
                self.pb_label.set_text("Uh-Oh, Need Room In ROM...")
                misc_manip._edit_world_order_related_text_main()
            except Exception:
                self.warning_label.set_text("Uh-Oh...")
                self.pb_label.set_text(f"Error Removing Furnace Fun...\n{self._mumbo_error_message}")
                raise
        try:
            self.pb_label.set_text("Mumbo's Motors Now In Business...")
            misc_manip._setup_game_engine_manip(self.transform_cost_dict)
        except Exception:
            self.warning_label.set_text("Uh-Oh...")
            self.pb_label.set_text(f"Error Adjusting Game Engine...\n{self._mumbo_error_message}")
            raise
        del misc_manip
        self.master.logger.info("End of Misc Options")
    
    def _perform_checksum(self):
        '''Runs the checksum functions'''
        self.master.logger.info("Performing Checksum")
        bk_checksum_obj = BK_Checksum_Class(self.master.cwd, self.seed_val)
        bk_checksum_obj._main()
        del bk_checksum_obj
        self.master.logger.info("Checksum Complete")
    
    def _compress_main(self):
        '''Runs the compression functions'''
        self.master.logger.info("Compressing Main Start")
        compressor = Compressor(self.master, self.seed_val, self.master.cwd)
        compressor._main()
        del compressor
        self.master.logger.info("Compression Main End")
    
    def _crc_calc(self):
        '''Runs the CRC functions'''
        self.master.logger.info("Running CRC Functions")
        crc_calc_obj = CRC_Calc_Class(self.master.cwd, self.seed_val)
        crc_calc_obj.calculate_crc()
        crc_calc_obj.set_crc()
        del crc_calc_obj
        self.master.logger.info("CRC Functions Complete")

    def _clean_up(self):
        '''Runs the cleanup functions, if enabled'''
        self.master.logger.info("Cleaning Up")
        if(self.master.remove_files_var.get() == 1):
            clean_up = CleanUp(self.master.cwd)
            clean_up._remove_bin_files()
            del clean_up
        gc.collect()
        self.master.logger.info("Cleaning Up Complete")

    def _randomization_process(self):
        '''
        Runs through the setup, decompression, world manipulation, misc settings, compression, crc tool, and clean up functions in that order.
        Updates the progress bar after every function runs. Update values are arbitrary.
        '''
        self.master.logger.info("Setting Up...")
        self.pb_label.set_text("Setting up...")
        self._setup()
        self.progress_bar.update_bar(5)
        try:
            self.pb_label.set_text("Mumbo Extracting Parts Of Game...")
            self._decompress_main()
        except Exception:
            self.warning_label.set_text("Uh-Oh...")
            self.pb_label.set_text(f"Error Decompressing ROM...\n{self._mumbo_error_message}")
            raise
        self.progress_bar.update_bar(20)
        self.pb_label.set_text("Worlds Need Some Work...")
        self._randomize_world()
        self.progress_bar.update_bar(40)
        self.pb_label.set_text("Mumbo Adding These Too...")
        self._misc_options()
        self.progress_bar.update_bar(60)
        self.pb_label.set_text("Bear And Bird No Need This...")
        try:
            self._perform_checksum()
        except Exception:
            self.warning_label.set_text("Uh-Oh...")
            self.pb_label.set_text(f"Error Correcting Checksums...\n{self._mumbo_error_message}")
            raise
        self.progress_bar.update_bar(65)
        try:
            self.pb_label.set_text("Hope This Works... *Eekum Bookum Eekum Bookum*\n(May Take A Minute Or Two)")
            self._compress_main()
        except Exception:
            self.warning_label.set_text("Uh-Oh...")
            self.pb_label.set_text(f"Error Compressing Files...\n{self._mumbo_error_message}")
            raise
        self.progress_bar.update_bar(85)
        try:
            self.pb_label.set_text("Mumbo Turn Bear Into Dinosaur...")
            self._crc_calc()
        except Exception:
            self.warning_label.set_text("Uh-Oh...")
            self.pb_label.set_text(f"Error Recalculating CRC...\n{self._mumbo_error_message}")
            raise
        self.progress_bar.update_bar(95)
        try:
            self.pb_label.set_text("Changed Mind! T-Rex Spell Too Good For This Playthrough!")
            self._clean_up()
        except Exception:
            self.warning_label.set_text("Uh-Oh...")
            self.pb_label.set_text(f"Error Cleaning Up...\n{self._mumbo_error_message}")
            raise
        self.progress_bar.update_bar(100)
        self.warning_label.set_text("Oomenacka!")
        self.pb_label.set_text(f"Mumbo Spell Done! Let Player Close Window!")
        self.master.logger.info("##### Randomized ROM Creation Complete! #####")

    def update_mumbo_gif(self, ind):
        '''Updates The Gif Frame'''
        frame = self.frames[ind]
        ind += 1
        if ind == self.frame_count:
            ind = 0
        self.mumbo_talking_label.configure(image=frame)
        self.mumbo_talking_label.after(60, self.update_mumbo_gif, ind)

    def _main(self):
        '''Creates the progress bar gui and runs the main functions with threading'''
        ########################
        ### PROGRESS BAR GUI ###
        ########################
        # Label
        self.warning_label = self.App_Variable_Label(window=self.progress_bar_window, label_text="Bear And Bird Cannot Close Window.\nMust Complete ROM Transformation.\nHope This Works...")
        self.warning_label.pack_label()
        # Mumbo Jumbo Talking
        self.frame_count = 10
        self.frames = [tk.PhotoImage(master=self.progress_bar_window, file=(f"{self.master.cwd}Pictures/Mumbo_Jumbo_Speaking.gif"), format = 'gif -index %i' %(i)) for i in range(self.frame_count)]
        self.mumbo_talking_label = tk.Label(self.progress_bar_window, background="#F3E5AB")
        self.mumbo_talking_label.pack()
        # Variable Label
        self.pb_label = self.App_Variable_Label(window=self.progress_bar_window, label_text="Progress Bar")
        self.pb_label.pack_label()
        # Progress Bar
        self.progress_bar = self.App_ProgressBar(self.progress_bar_window)
        self.progress_bar.pack_bar()
        # Threading
        x = threading.Thread(target=self._randomization_process)
        x.start()
        ##########################
        ### GUI WINDOW OPTIONS ###
        ##########################
        ### Close Window ##
        self.progress_bar_window.protocol("WM_DELETE_WINDOW", self.progress_bar_window.destroy)
        ### Update Window ###
        self.progress_bar_window.after(0, self.update_mumbo_gif, 0)
        ### Main Loop ###
        self.progress_bar_window.mainloop()
