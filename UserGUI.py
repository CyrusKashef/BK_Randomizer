'''
Created on Aug 21, 2021

@author: Cyrus

##################
### GUI LAYOUT ###
##################

    ############################################################################################################
    #                                                                 |                                        #
    #                                                                 |    Gruntilda's Lair                    #
    #                                                                 |    [] Final Note Door Only             #
    #    ROM_DIR: ______________________________________              |    Note Lower Bounds _____ Min 0       #
    #                                                                 |    Note Upper Bounds _____ Max 900*    #
    #    [Select_ROM] SEED:   __________________________              |    *2000 Only For 'All Notes' Feature  #
    #                                                                 |                                        #
    #                                                                 |    [] Final Puzzle Only                #
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|    Jiggy Lower Bounds _____ Min 0      #
    #                                                                 |    Jiggy Upper Bounds _____ Max 99     #
    #    [Load_Config]   [Save_Config]   [Read_Me]        [Submit]    |                                        #
    #                                                                 |    [] Skip Furnace Fun                 #
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|    [] Remove Magic Barriers            #
    #                                                                 |                                        #
    #    Jiggies/Empty Honeycombs/Mumbo Tokens ----> {Options}        |    Mumbo's Mountain                    #
    #    [] Include Abnormalities   [] Include Potential Soft-Locks   |    [] Include Flowers                  #
    #                                                                 |                                        #
    #    Jinjos/1-Ups/Misc Objects ----------------> {Options}        |    Treasure Trove Cove                 #
    #    [] Include Abnormalities (May Include Eggs)                  |    [] Scattered Notes                  #
    #                                                                 |                                        #
    #    Notes/Blue Eggs/Red Feathers/Gold Feathers  {Options}        |    Clanker's Cavern                    #
    #                                                                 |    [] Reordered Rings                  #
    #    World Entrances (Includes Randomized Moves) {Options}        |                                        #
    #    [] Move Bottles Locations                                    |    Bubblegloop Swamp                   #
    #                                                                 |    [] Shuffled Croctus                 #
    #    Within The World Warps -------------------> {Options}        |    [] Bigger, Badder Mr. Vile          #
    #                                                                 |    [] Tiptup Choir                     #
    #    Ground/Wall/Flying Enemies ---------------> {Options}        |                                        #
    #    [] Include Beta Enemy [] Include Soft-Locks                  |    Freezeezy Peak                      #
    #                                                                 |    [] Hard Races                       #
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|                                        #
    #                                                                 |    Gobi's Valley                       #
    #    Banjo-Kazooie Model Color ----------------> {Options}        |    [] Ancient Ones                     #
    #                                                                 |    [] Maze Jinxy Heads                 #
    #    Enemy Model Color ------------------------> {Options}        |    [] Matching Puzzle                  #
    #                                                                 |                                        #
    #    Sound Sounds/Fanfare & Jingles/Looped Music                  |    Mad Monster Mansion                 #
    #    [] Shuffle Sounds   [] Shuffle Jingles   [] Shuffle Music    |    [] Tricky Enemies                   #
    #    [] Include Beta Sounds                                       |    [] Tricky Objects                   #
    #                                                                 |                                        #
    #    Sprites/Textures                                             |    Rusty Bucket Bay                    #
    #    [] Shuffle Skyboxes   [] Shuffle Talking Sprites             |    [] Random Button Combo              #
    #                                                                 |                                        #
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|    Click Clock Wood                    #
    #                                                                 |    {Options}                           #
    #    [] Create Cheat Sheet   [] Remove Extra Files                |                                        #
    #                                                                 |                                        #
    ############################################################################################################

###########################
### GUI ERRORS/WARNINGS ###
###########################

* ROM directory cannot include spaces. This is because GZIP.EXE uses the command prompt and treats spaces as new inputs. Avoid using special characters as well.
* ROM file must be a Banjo-Kazooie ROM v1.0 NTSC (.z64). Other formats are currently not supported. Randomizer may work on top of other BK mods, but not guaranteed.
* Seed, upper bounds, and lower bounds must be positive integers.
* GZIP.EXE and CRC Tool must be in their original locations with the BK ROM in the root folder.

#########################
### USER GUI OVERVIEW ###
#########################

                                                ###
  #######        ############                ###   ###          #####################
 #       #       #          #   SUBMIT    ###         ###   NO  #                   #
#  START  # ---> # User GUI # ---------> #     ERROR?    # ---> # ProgressionGUI.py #
 #       #   |   #          #             ###         ###       #                   #
  #######    |   ############                ###   ###          #####################
             |        ^                         ###                      |
             |        |                          | YES                   |
             |        |                          V                       |
             |        |                   ################               |
             |        |                   #              #               |
             |        |-------------------# Error Window #               |
             |                            #              #               |
             |                            ################               |
             |                                                           |
             |         ###                                               |         ###
             |      ###   ###                  #######                   |      ###   ###                  #######
             |   ###         ###   PRESSED    #       #                  |   ###         ###   PRESSED    #       #
             |--#     CLOSE?    # ---------> #   END   #                 |--#     CLOSE?    # ---------> #   END   #
                 ###         ###      |       #       #                      ###         ###              #       #
                    ###   ###         |        #######                          ###   ###                  #######
                       ###            |                                            ###                        ^
                                      |                                                                       |
                                      |-----------------------------------------------------------------------|

'''

tool_tips_dict = {
    "ROM": {
        "SELECT_ROM_FILE": "Select the Banjo-Kazooie NTSC (.z64) v1.0 ROM File.",
        },
    "SEED": {
        "RANDOM_SEED_BUTTON": "Click the button to generate a random seed.",
        },
    "FLAGGED_OBJECTS": {
        "FRAME":
            "NONE:\n"+
            "    Skips the setting.\n" +
            "SHUFFLE WORLD:\n" +
            "    Takes all items of that set and swaps the Object IDs\n" +
            "    within the world (with the exception of Click Clock\n" +
            "    Wood unless the feature is turned on).\n" +
            "SHUFFLE GAME:\n" +
            "    Takes all items of that set and swaps the Object IDs\n" +
            "    within the game (overrides the Click Clock Wood feature).\n" +
            "    Recommended using FINAL NOTE DOOR feature.\n" +
            "FLAGGED_OBJECT_ABNORMALITIES: Includes Flagged Objects that\n" +
            "    cause weird glitches, but not ones that would break the game.\n" +
            "INCLUDE_POTENTIAL_SOFTLOCKS: Includes Flagged Objects that will\n" +
            "    probably prevent 100%-ing the game. Still playable, though.",
        },
    "NON_FLAGGED_OBJECTS": {
        "FRAME":
            "NONE:\n"+
            "    Skips the setting.\n" +
            "SHUFFLE WORLD:\n" +
            "    Takes all items of that set and swaps the Object IDs\n" +
            "    within the world (with the exception of Click Clock\n" +
            "    Wood unless the feature is turned on).\n" +
            "SHUFFLE GAME:\n" +
            "    Takes all items of that set and swaps the Object IDs\n" +
            "    within the game (overrides the Click Clock Wood feature).\n" +
            "    Recommended using FINAL NOTE DOOR feature.\n" +
            "INCLUDE_ABNORMALITIES: Includes eggs and feathers that are\n" +
            "    coded like objects.",
        },
    "STRUCTS": {
        "FRAME":
            "NONE:\n"+
            "    Skips the setting.\n" +
            "SHUFFLE WORLD:\n" +
            "    Takes all items of that set and swaps the Object IDs\n" +
            "    within the world (with the exception of Click Clock\n" +
            "    Wood unless the feature is turned on).\n" +
            "SHUFFLE GAME:\n" +
            "    Takes all items of that set and swaps the Object IDs\n" +
            "    within the game (overrides the Click Clock Wood feature).\n" +
            "    Recommended using FINAL NOTE DOOR feature.\n" +
            "RANDOMIZE:\n"+
            "    For every item in the world, randomly assign a new Object ID.\n" +
            "    Recommended using FINAL NOTE DOOR feature.\n" +
            "ALL NOTES:\n" +
            "    All eggs and feathers become notes. Brentildas are replaced\n" +
            "    with egg and feather refills. The refill at that Brentilda\n" +
            "    location is random.",
        },
    "WORLD_ENTRANCES": {
        "FRAME":
            "NONE:\n" +
            "    Skips the setting.\n" +
            "BASIC SHUFFLE:\n" +
            "    All worlds, except Mumbo's Mountain, are shuffled. Mumbo's\n" +
            "    Mountain will give the needed moves to progress the lair.\n" +
            "BOTTLES SHUFFLE:\n" +
            "    All worlds, including Mumbo's Mountain, are shuffled. Bottles\n" +
            "    mounds are shuffled with 1-Up locations to promote more\n" +
            "    exploration. Logic may not work if worlds are opened out of order.",
        },
    "WITHIN_WORLD_WARPS": {
        "FRAME": 
            "NONE:\n" +
            "    Skips the setting.\n" +
            "SHUFFLE:\n" +
            "    Shuffles the warps that are within the world."
        },
    "ENEMIES": {
        "FRAME":
            "NONE:\n"+
            "    Skips the setting.\n" +
            "SHUFFLE WORLD:\n" +
            "    Takes all items of that set and swaps the Object IDs\n" +
            "    within the world (with the exception of Click Clock\n" +
            "    Wood unless the feature is turned on).\n" +
            "SHUFFLE GAME:\n" +
            "    Takes all items of that set and swaps the Object IDs\n" +
            "    within the game (overrides the Click Clock Wood feature).\n" +
            "    Recommended using FINAL NOTE DOOR feature.\n" +
            "RANDOMIZE:\n"+
            "    For every item in the world, randomly assign a new Object ID.\n" +
            "    Recommended using FINAL NOTE DOOR feature.\n" +
            "ALL TOUGHIES:\n"+
            "    All ground enemies become Bigbutts. All flying enemies become\n" +
            "    Bees. All wall enemies become Flotsams (or vents if included).\n"+
            "BETA_ENEMIES: Unused enemies that are coded into the game but\n" +
            "    aren't used.",#\n" +
            #"INCLUDE_SOFTLOCKS: Shuffles/randomizes unkillable enemies.\n" +
            #"    May block/prevent collectables.",
        },
    "BK_COLOR": {
        "FRAME": "Change BK's colors to presets",
        },
    "MODELS_AND_ANIMATIONS": {
        "MODELS": "Swaps, shuffles, and randomizes some models.",
        "ANIMATIONS": "Swaps, shuffles, and randomizes some animations.",
        },
    "SOUNDS_MUSIC": {
        "SHUFFLE_SOUNDS": "Shuffles short sounds, like ones for eggs, notes, and feathers.",
        "SHUFFLE_JINGLES": "Shuffles jingles that last a few seconds.",
        "SHUFFLE_MUSIC": "Shuffles music for levels and minigames.",
        "INCLUDE_BETA_SOUNDS": "Shuffles the other categories with unused versions.",
        },
    "SPRITES_TEXTURES": {
        "SHUFFLE_SKYBOXES": "Shuffles the skyboxes, including clouds/thunderstorms.",
        "SHUFFLE_TALKING_SPRITES": "Shuffles the talking sprites (not the voices).",
        },
    "MISC_OPTIONS": {
        "CREATE_CHEAT_SHEET": "Writes a JSON file that gives a hint for the location of each Jiggy,\n" +
                              "the location of empty honeycombs, and how many notes are in each room.",
        "REMOVE_EXTRA_FILES": "Removes the compressed and decompressed files extrated from the ROM.\n" +
                              "Useful for BK modders or debugging an issue.",
        "TOOL_TIPS": "Hover over a feature to get an explanation of what it does."
        },
    "LOAD_CONFIG": "Reads a JSON file to configure the settings automatically.",
    "SAVE_CONFIG": "Writes a JSON file for future use. See LOAD CONFIG.",
    "OPEN_README": "Opens the README.txt file.",
    "SUBMIT": "Runs the randomizer with the current features,\n" +
              "barring everything is set correctly.",
    "GRUNTILDAS_LAIR": {
        "FINAL_NOTE_DOOR": "The 810 note door's note requirement can be altered to any\n" +
                           "value within the lower and upper bounds, inclusively. The\n" +
                           "lower bound's minimum is 0; the upper bound's maximum is 900\n" +
                           "unless the feature 'ALL NOTES' is selected, which will extend\n" +
                           "the maximum to 2000. All other note doors are removed.",
        "RANDOM_NOTE_BUTTON": "Turns on the final note door feature and\n" +
                              "randomly selects a note value",
        "FINAL_PUZZLE": "The door leading to the final boss fight's Jiggy requirement\n" +
                        "can be altered to any value within the lower and upper bounds,\n" +
                        "inclusively. The lower bound's minimum is 0; the upper bound's\n" +
                        "maximum is 99. The number of Jiggies required for red honeycombs\n" +
                        "is 100 - Jiggies Needed, minimum being 1, maximum being 4. All\n" +
                        "world puzzles are complete by default, meaning worlds are\n" +
                        "automatically opened.",
        "RANDOM_JIGGY_BUTTON": "Turns on the final puzzle door feature and\n" +
                               "randomly selects a jiggy value",
        "SKIP_FURNACE_FUN_AND_BRENTILDA": "Places a warp on the first square of Furnace Fun\n" +
                                          "that leads to the next area. Brentilda's texts are\n" +
                                          "replace with hints about the randomizer.",
        "NO_DETRANSFORMATIONS": "Removes all detransformation barriers in the lair.",
        "HARDER_FINAL_BATTLE": "Uses one of three variations of the final battle,\n" +
                               "each ranging in difficulty from easiest (1) to\n" +
                               "hardest (3). Zero turns the features off."
        },
    "MUMBOS_MOUNTAIN": {
        "INCLUDE_FLOWERS": "If the notes/eggs/feathers feature is not set to\n" +
                           "'None', the flowers in the level will be included."
        },
    "TREASURE_TROVE_COVE": {
        "SCATTERED_STRUCTS": "Notes are scattered across the level,\n" +
                             "both in the water and in the air."
        },
    "CLANKERS_CAVERN": {
        "SHUFFLE_CLANKER_RING_ORDER": "Clanker's ring order is shuffled.",
        },
    "BUBBLEGLOOP_SWAMP": {
        "SHUFFLE_CROCTUS_ORDER": "Croctus spawn order is shuffled.",
        "MR_VILE_BIGGER_BADDER_CROCODILE": "Mr. Vile is noticeably bigger.",
        "TIPTUP_CHOIR_NO_ASSIGNED_SEATS": "Choir memembers are scattered across the room,\n" +
                                          "only revealing their heads.",
        },
    "FREEZEEZY_PEAK": {
        "BOGGY_RACES_MOVED_FLAGS": "Flag poles for the Boggy race are either tighter left, tighter right,\n" +
                                   "lowered to the floor to make harder to see, or rotated.",
        },
    "GOBIS_VALLEY": {
        "SHUFFLED_ANCIENT_ONES_ORDER": "Ancient Ones order is shuffled.",
        "SHUFFLE_MAZE_JINXY_HEADS_ORDER": "Jinxy heads to raise King Sandybutt's Tomb order is shuffled.",
        },
    "MAD_MONSTER_MANSION": {
        "POTS_ARE_LIT": "Flower pots are shuffled with the fire pain objects.",
        },
    "RUSTY_BUCKET_BAY": {
        "RANDOMIZED_BUTTON_COMBO": "Generates a random 6-digit combination of 1s, 2s, and 3s for the\n" +
                                   "whistle buttons and places the code over the original code spot.",
        },
    "CLICK_CLOCK_WOOD": {
        "SHUFFLE_BY": "SEASON: All shuffling happens within each seasons/lobby area,\n" +
                      "        making it easier for players to track what they are missing.\n" +
                      "WORLD: All shuffling happens throughout the level.",
        },
    }


######################
### PYTHON IMPORTS ###
######################

import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
import os
import json
import random

####################
### FILE IMPORTS ###
####################

from ProgressionGUI import Progression_GUI
from Randomization_Processes.Common_Functions import read_json, space_in_directory, leading_zeros

#################
### VARIABLES ###
#################

BK_RANDO_VERSION = "2.0"

#################
### GUI CLASS ###
#################

def Error_GUI(error_msg):
    '''Brings up a GUI that displays an error message'''
    error_window = tk.Tk()
    error_msg = error_msg
    error_window.winfo_toplevel().title("Banjo-Kazooie Randomizer Error")
    error_label = tk.Label(error_window, text=error_msg)
    error_label.config(anchor='center')
    error_label.pack()
    ok_btn = tk.Button(error_window, text='Doh!', command=error_window.destroy)
    ok_btn.config(anchor='center')
    ok_btn.pack()
    error_window.mainloop()

class User_GUI():
    '''Creates a GUI where users give the directory of the ROM file, select options for the randomization, and optionally provide a seed value'''
    def __init__(self):
        '''Creates the Tkinter GUI'''
        self.cwd = os.getcwd() + "\\"
        self.app_window = tk.Tk()
        self.app_window.winfo_toplevel().title(f"Banjo-Kazooie Randomizer v{BK_RANDO_VERSION}")
        self.padx = 3
        self.pady = 1
    
    def _select_rom_file(self):
        '''Opens a browser to select the ROM file ending in .z64'''
        filename = tkinter.filedialog.askopenfilename(initialdir=self.cwd, title="Select The BK ROM File", filetype =(("Rom Files","*.z64"),("all files","*.*")) )
        if(" " in filename):
            filename = space_in_directory(filename)
        self.rom_file_entry.set(filename)
    
    def _random_seed(self):
        '''Randomly selects a seed'''
        self.seed_value.set(str(random.randint(10000000, 19940303)))
    
    def _random_note_value(self):
        '''Randomly selects a note value'''
        self.final_note_door_var.set("Final Note Door Only")
        if(self.struct_var.get() == "All Notes"):
            self.final_note_door_value.set(str(random.randint(0, 2000)))
        else:
            self.final_note_door_value.set(str(random.randint(0, 900)))
    
    def _random_puzzle_value(self):
        '''Randomly selects a puzzle value'''
        self.final_puzzle_var.set(1)
        self.final_puzzle_value.set(str(random.randint(0, 99)))
    
    class CreateToolTip(object):
        '''Create a tooltip for a given widget'''
        def __init__(self, widget, master, text='widget info'):
            self.widget = widget
            self.master = master
            self.text = text
            self.widget.bind("<Enter>", self.enter)
            self.widget.bind("<Leave>", self.close)
    
        def enter(self, event=None):
            try:
                if(self.master.tool_tips_var.get() == 1):
                    x = y = 0
                    x, y, cx, cy = self.widget.bbox("insert")
                    x += self.widget.winfo_rootx() + 25
                    y += self.widget.winfo_rooty() + 20
                    # creates a toplevel window
                    self.tw = tk.Toplevel(self.widget)
                    # Leaves only the label and removes the app window
                    self.tw.wm_overrideredirect(True)
                    self.tw.wm_geometry("+%d+%d" % (x, y))
                    label = tk.Label(self.tw, text=self.text, justify='left',
                                   background='white', relief='solid', borderwidth=1,
                                   font=("times", "10", "normal"))
                    label.pack(ipadx=1)
            except AttributeError:
                pass
    
        def close(self, event=None):
            try:
                if self.tw:
                    self.tw.destroy()
            except Exception:
                pass
    
    def _random_bk_model_preset(self):
        key_list = []
        for key in self.bk_model_json:
            key_list.append(key)
        random_bk_model = random.choice(key_list)
        self.bk_model_var.set(random_bk_model)
    
    def _random_hex(self, digit_len):
        max_num = "F" * digit_len
        random_hex_val = leading_zeros(random.randint(0, int(max_num, 16)), digit_len).upper()
        if(digit_len == 4):
            choices = [str(hex(num))[2:].upper() for num in range(0x1, 0xF, 0x2)]
            new_end_val = random.choice(choices)
            random_hex_val = random_hex_val[:-1] + new_end_val
        elif(digit_len == 6):
            random_hex_val = random_hex_val + "FF"
        return random_hex_val
    
    def _random_bk_model_colors(self):
        self.bk_model_var.set("Custom")
        self.banjo_fur_var.set(self._random_hex(6))
        self.tooth_necklace_var.set(self._random_hex(6))
        self.banjo_skin_var.set(self._random_hex(6))
        self.banjo_feet_var.set(self._random_hex(4))
        self.kazooie_primary_var.set(self._random_hex(6))
        self.kazooie_secondary_var.set(self._random_hex(6))
        self.kazooie_wing_primary_var.set(self._random_hex(4))
        self.kazooie_wing_secondary_var.set(self._random_hex(4))
        self.backpack_var.set(self._random_hex(6))
        self.wading_boots_var.set(self._random_hex(6))
        self.shorts_vertex_var.set(self._random_hex(6))
        self.shorts_texture_var.set(self._random_hex(4))
    
    def _update_bk_model(self, *args):
        '''PyDoc'''
        bk_model_preset = self.bk_model_var.get()
        if(bk_model_preset in self.bk_model_json):
            self.banjo_fur_var.set(self.bk_model_json[bk_model_preset]["Banjo_Fur"])
            self.tooth_necklace_var.set(self.bk_model_json[bk_model_preset]["Tooth_Necklace"])
            self.banjo_skin_var.set(self.bk_model_json[bk_model_preset]["Banjo_Skin"])
            self.banjo_feet_var.set(self.bk_model_json[bk_model_preset]["Banjo_Feet"])
            self.kazooie_primary_var.set(self.bk_model_json[bk_model_preset]["Kazooie_Primary"])
            self.kazooie_secondary_var.set(self.bk_model_json[bk_model_preset]["Kazooie_Secondary"])
            self.kazooie_wing_primary_var.set(self.bk_model_json[bk_model_preset]["Kazooie_Wing_Primary"])
            self.kazooie_wing_secondary_var.set(self.bk_model_json[bk_model_preset]["Kazooie_Wing_Secondary"])
            self.backpack_var.set(self.bk_model_json[bk_model_preset]["Backpack"])
            self.wading_boots_var.set(self.bk_model_json[bk_model_preset]["Wading_Boots"])
            self.shorts_vertex_var.set(self.bk_model_json[bk_model_preset]["Shorts_Vertex"])
            self.shorts_texture_var.set(self.bk_model_json[bk_model_preset]["Shorts_Texture"])
    
    def _set_recommended_defaults(self, *args):
        '''Sets the recommended defaults for first time users or when an error occurs with a loaded json file'''
        ### ROM and Seed ###
        # ROM
        self.rom_file_entry.set(self.cwd)
        # Seed
        self.seed_value.set("")
        ### General Settings ###
        # Flagged Objects
        self.flagged_object_var.set("Shuffle (World)")
        self.flagged_object_abnormalities_var.set(0)
        self.flagged_object_softlock_var.set(0)
        # Non-Flagged Objects
        self.non_flagged_object_var.set("Shuffle (World)")
        self.non_flagged_object_abnormalities_var.set(0)
        # Structs
        self.struct_var.set("Shuffle (World)")
        self.final_note_door_var.set("Scaling Note Doors")
        self.final_note_door_value.set(810)
        # World Entrances
        self.world_entrance_var.set("Basic Shuffle")
        # Within World Warps
        self.within_world_warps_var.set("Shuffle By World")
        # Enemies
        self.enemies_var.set("Randomize")
        self.enemies_beta_var.set(0)
        ### Aesthetic Settings ###
        # BK Model
        self.bk_model_var.set("Default")
        self.banjo_fur_var.set(self.bk_model_json[self.bk_model_var.get()]["Banjo_Fur"])
        self.tooth_necklace_var.set(self.bk_model_json[self.bk_model_var.get()]["Tooth_Necklace"])
        self.banjo_skin_var.set(self.bk_model_json[self.bk_model_var.get()]["Banjo_Skin"])
        self.banjo_feet_var.set(self.bk_model_json[self.bk_model_var.get()]["Banjo_Feet"])
        self.kazooie_primary_var.set(self.bk_model_json[self.bk_model_var.get()]["Kazooie_Primary"])
        self.kazooie_secondary_var.set(self.bk_model_json[self.bk_model_var.get()]["Kazooie_Secondary"])
        self.kazooie_wing_primary_var.set(self.bk_model_json[self.bk_model_var.get()]["Kazooie_Wing_Primary"])
        self.kazooie_wing_secondary_var.set(self.bk_model_json[self.bk_model_var.get()]["Kazooie_Wing_Secondary"])
        self.backpack_var.set(self.bk_model_json[self.bk_model_var.get()]["Backpack"])
        self.wading_boots_var.set(self.bk_model_json[self.bk_model_var.get()]["Wading_Boots"])
        self.shorts_vertex_var.set(self.bk_model_json[self.bk_model_var.get()]["Shorts_Vertex"])
        self.shorts_texture_var.set(self.bk_model_json[self.bk_model_var.get()]["Shorts_Texture"])
        # Enemy Models
        self.other_model_var.set(0)
        self.animation_var.set(0)
        # Sounds/Music
        self.short_sounds_var.set(0)
        self.jingles_var.set(0)
        self.music_var.set(0)
        self.beta_sounds_var.set(0)
        # Sprites/Textures
        self.skybox_var.set(0)
        self.talking_sprite_var.set(0)
        ### Misc Settings ###
        self.cheat_sheet_var.set(1)
        self.remove_files_var.set(1)
        self.tool_tips_var.set(0)
        ### World Specific ###
        # Gruntilda's Lair
        self.final_puzzle_var.set(0)
        self.final_puzzle_value.set(0)
        self.skip_furnace_fun_var.set(0)
        self.remove_magic_barriers_var.set(0)
        self.gruntilda_difficulty_var.set(0)
        # Mumbo's Mountain
        self.flowers_var.set(0)
        # Treasure Trove Cove
        self.scattered_structs_var.set(0)
        # Clanker's Cavern
        self.hard_rings_var.set(0)
        # Bubblegloop Swamp
        self.croctus_var.set(0)
        self.mr_vile_var.set(0)
        self.tiptup_choir_var.set(0)
        # Freezeezy Peak
        self.hard_races_var.set(0)
        # Gobi's Valley
        self.ancient_ones_var.set(0)
        self.maze_jinxy_heads_var.set(0)
        self.matching_puzzle_var.set(0)
        # Mad Monster Mansion
        self.lit_pots_var.set(0)
        # Rusty Bucket Bay
        self.buttons_var.set(0)
        # Click Clock Wood
        self.ccw_var.set("By Season")
    
    def _load_configuration(self, button_press=True):
        '''Opens a chosen JSON file and sets the parameters to match those'''
        if(button_press):
            config_default_dir = f"{self.cwd}Configurations\\"
            filename = tkinter.filedialog.askopenfilename(initialdir=config_default_dir, title="Select A JSON Config File", filetypes =(("Json Files","*.json"),("all files","*.*")))
        else:
            filename = self.cwd + "Configurations\\Last_Used_Configuration.json"
        with open(filename, "r") as json_file:
            json_data = json.load(json_file)
        ### ROM and Seed ###
        # ROM
        self.rom_file_entry.set(json_data["ROM_File"])
        # Seed
        self.seed_value.set(json_data["Seed"])
        ### General Settings ###
        # Flagged Objects
        self.flagged_object_var.set(json_data["Flagged_Objects_Option"])
        self.flagged_object_abnormalities_var.set(json_data["Flagged_Objects_Abnormalities"])
        self.flagged_object_softlock_var.set(json_data["Flagged_Objects_Softlock"])
        # Non-Flagged Objects
        self.non_flagged_object_var.set(json_data["Non_Flagged_Objects_Option"])
        self.non_flagged_object_abnormalities_var.set(json_data["Non_Flagged_Objects_Abnormalities"])
        # Structs
        self.struct_var.set(json_data["Struct_Option"])
        # World Entrances
        self.world_entrance_var.set(json_data["World_Entrance_Option"])
        # Within World Warps
        self.within_world_warps_var.set(json_data["Within_World_Warps_Option"])
        # Enemies
        self.enemies_var.set(json_data["Enemies_Option"])
        self.enemies_beta_var.set(json_data["Enemies_Beta"])
        ### Aesthetic Settings ###
        # BK Model
        self.bk_model_var.set(json_data["BK_Model_Option"])
        self.banjo_fur_var.set(json_data["Banjo_Fur"])
        self.tooth_necklace_var.set(json_data["Tooth_Necklace"])
        self.banjo_skin_var.set(json_data["Banjo_Skin"])
        self.banjo_feet_var.set(json_data["Banjo_Feet"])
        self.kazooie_primary_var.set(json_data["Kazooie_Primary"])
        self.kazooie_secondary_var.set(json_data["Kazooie_Secondary"])
        self.kazooie_wing_primary_var.set(json_data["Kazooie_Wing_Primary"])
        self.kazooie_wing_secondary_var.set(json_data["Kazooie_Wing_Secondary"])
        self.backpack_var.set(json_data["Backpack"])
        self.wading_boots_var.set(json_data["Wading_Boots"])
        self.shorts_vertex_var.set(json_data["Shorts_Vertex"])
        self.shorts_texture_var.set(json_data["Shorts_Texture"])
        # Enemy Models
        self.other_model_var.set(json_data["Other_Model_Option"])
        self.animation_var.set(json_data["Animation_Option"])
        # Sounds/Music
        self.short_sounds_var.set(json_data["Short_Sound_Option"])
        self.jingles_var.set(json_data["Jingle_Option"])
        self.music_var.set(json_data["Music_Option"])
        self.beta_sounds_var.set(json_data["Beta_Sounds"])
        # Sprites/Textures
        self.skybox_var.set(json_data["Skybox_Option"])
        self.talking_sprite_var.set(json_data["Talking_Sprite_Option"])
        ### Misc Settings ###
        self.cheat_sheet_var.set(json_data["Cheat_Sheet"])
        self.remove_files_var.set(json_data["Remove_Files"])
        self.tool_tips_var.set(json_data["Tool_Tips"])
        ### World Specific ###
        # Gruntilda's Lair
        self.final_note_door_var.set(json_data["Final_Note_Door"])
        self.final_note_door_value.set(json_data["Final_Note_Door_Value"])
        self.final_puzzle_var.set(json_data["Final_Puzzle"])
        self.final_puzzle_value.set(json_data["Final_Puzzle_Value"])
        self.skip_furnace_fun_var.set(json_data["Furnace_Fun_Skip"])
        self.remove_magic_barriers_var.set(json_data["Remove_Magic_Barriers"])
        self.gruntilda_difficulty_var.set(json_data["Final_Battle_Difficulty"])
        # Mumbo's Mountain
        self.flowers_var.set(json_data["MM_Flowers"])
        # Treasure Trove Cove
        self.scattered_structs_var.set(json_data["Scattered_Notes_Eggs_Feathers"])
        # Clanker's Cavern
        self.hard_rings_var.set(json_data["CC_Hard_Rings"])
        # Bubblegloop Swamp
        self.croctus_var.set(json_data["BGS_Croctus"])
        self.mr_vile_var.set(json_data["BGS_Mr_Vile"])
        self.tiptup_choir_var.set(json_data["BGS_Tiptup_Choir"])
        # Freezeezy Peak
        self.hard_races_var.set(json_data["FP_Hard_Races"])
        # Gobi's Valley
        self.ancient_ones_var.set(json_data["GV_Ancient_Ones"])
        self.maze_jinxy_heads_var.set(json_data["GV_Maze_Jinxy_Heads"])
        self.matching_puzzle_var.set(json_data["GV_Matching_Puzzle"])
        # Mad Monster Mansion
        self.lit_pots_var.set(json_data["MMM_Lit_Pots"])
        # Rusty Bucket Bay
        self.buttons_var.set(json_data["RBB_Buttons"])
        # Click Clock Wood
        self.ccw_var.set(json_data["CCW_Option"])
    
    def _save_current_configuration(self, button_press=True):
        '''Writes the current configuration to a JSON file'''
        current_config = {
            ### ROM and Seed ###
            # ROM
            "ROM_File": self.rom_file_entry.get(),
            # Seed
            "Seed": self.seed_value.get(),
            ### General Settings ###
            # Flagged Objects
            "Flagged_Objects_Option": self.flagged_object_var.get(),
            "Flagged_Objects_Abnormalities": self.flagged_object_abnormalities_var.get(),
            "Flagged_Objects_Softlock": self.flagged_object_softlock_var.get(),
            # Non-Flagged Objects
            "Non_Flagged_Objects_Option": self.non_flagged_object_var.get(),
            "Non_Flagged_Objects_Abnormalities": self.non_flagged_object_abnormalities_var.get(),
            # Structs
            "Struct_Option": self.struct_var.get(),
            # World Entrances
            "World_Entrance_Option": self.world_entrance_var.get(),
            # Within World Warps
            "Within_World_Warps_Option": self.within_world_warps_var.get(),
            # Enemies
            "Enemies_Option": self.enemies_var.get(),
            "Enemies_Beta": self.enemies_beta_var.get(),
            ### Aesthetic Settings ###
            # BK Model
            "BK_Model_Option": self.bk_model_var.get(),
            "Banjo_Fur": self.banjo_fur_var.get(),
            "Tooth_Necklace": self.tooth_necklace_var.get(),
            "Banjo_Skin": self.banjo_skin_var.get(),
            "Banjo_Feet": self.banjo_feet_var.get(),
            "Kazooie_Primary": self.kazooie_primary_var.get(),
            "Kazooie_Secondary": self.kazooie_secondary_var.get(),
            "Kazooie_Wing_Primary": self.kazooie_wing_primary_var.get(),
            "Kazooie_Wing_Secondary": self.kazooie_wing_secondary_var.get(),
            "Backpack": self.backpack_var.get(),
            "Wading_Boots": self.wading_boots_var.get(),
            "Shorts_Vertex": self.shorts_vertex_var.get(),
            "Shorts_Texture": self.shorts_texture_var.get(),
            # Enemy Models
            "Other_Model_Option" : self.other_model_var.get(),
            "Animation_Option" : self.animation_var.get(),
            # Sounds/Music
            "Short_Sound_Option": self.short_sounds_var.get(),
            "Jingle_Option": self.jingles_var.get(),
            "Music_Option": self.music_var.get(),
            "Beta_Sounds": self.beta_sounds_var.get(),
            # Sprites/Textures
            "Skybox_Option": self.skybox_var.get(),
            "Talking_Sprite_Option": self.talking_sprite_var.get(),
            ### Misc Settings ###
            "Cheat_Sheet": self.cheat_sheet_var.get(),
            "Remove_Files": self.remove_files_var.get(),
            "Tool_Tips": self.tool_tips_var.get(),
            ### World Specific ###
            # Gruntilda's Lair
            "Final_Note_Door": self.final_note_door_var.get(),
            "Final_Note_Door_Value": self.final_note_door_value.get(),
            "Final_Puzzle": self.final_puzzle_var.get(),
            "Final_Puzzle_Value": self.final_puzzle_value.get(),
            "Furnace_Fun_Skip": self.skip_furnace_fun_var.get(),
            "Remove_Magic_Barriers": self.remove_magic_barriers_var.get(),
            "Final_Battle_Difficulty": self.gruntilda_difficulty_var.get(),
            # Mumbo's Mountain
            "MM_Flowers": self.flowers_var.get(),
            # Treasure Trove Cove
            "Scattered_Notes_Eggs_Feathers": self.scattered_structs_var.get(),
            # Clanker's Cavern
            "CC_Hard_Rings": self.hard_rings_var.get(),
            # Bubblegloop Swamp
            "BGS_Croctus": self.croctus_var.get(),
            "BGS_Mr_Vile": self.mr_vile_var.get(),
            "BGS_Tiptup_Choir": self.tiptup_choir_var.get(),
            # Freezeezy Peak
            "FP_Hard_Races": self.hard_races_var.get(),
            # Gobi's Valley
            "GV_Ancient_Ones": self.ancient_ones_var.get(),
            "GV_Maze_Jinxy_Heads": self.maze_jinxy_heads_var.get(),
            "GV_Matching_Puzzle": self.matching_puzzle_var.get(),
            # Mad Monster Mansion
            "MMM_Lit_Pots": self.lit_pots_var.get(),
            # Rusty Bucket Bay
            "RBB_Buttons": self.buttons_var.get(),
            # Click Clock Wood
            "CCW_Option": self.ccw_var.get(),
            }
        if(button_press):
            try:
                json_file = tkinter.filedialog.asksaveasfile(filetypes=(("Json Files","*.json"),("all files","*.*")), defaultextension=json)
                json.dump(current_config, json_file, indent=4)
            except Exception:
                pass # log something here?
        else:
            config_file = self.cwd + "Configurations\\Last_Used_Configuration.json"
            with open(config_file, "w+") as json_file: 
                json.dump(current_config, json_file, indent=4)
    
    def _open_readme_file(self):
        '''Lmao if someone actually uses this button instead of being a typical end user, bless their heart'''
        readme_file = f"{self.cwd}ReadMe.txt"
        os.startfile(readme_file)
    
    def _check_rom_directory(self):
        '''Checks if ROM file ends in .z64 and is located in the folder with GZIP.EXE'''
        rom_path = self.rom_file_entry.get()
        if((rom_path == "") or (not os.path.isfile(rom_path))):
            Error_GUI("Please provide the directory to the ROM.")
            return False
        if("\\" in rom_path):
            rom_file = rom_path.split("\\")[-1]
        elif("/" in rom_path):
            rom_file = rom_path.split("/")[-1]
        else:
            Error_GUI("Unknown Directory?")
        file_dir = rom_path.replace(rom_file, "")
        if(" " in file_dir):
            Error_GUI("There's a space (' ') in the directory path. Please remove the space and try again.")
            return False
        if(" " in rom_file):
            Error_GUI("There's a space (' ') in the rom file name. Please remove the space and try again.")
            return False
        rom_ext = rom_file.split(".")[-1]
        if(rom_ext not in ["z64"]):
            Error_GUI(f"Rom Extention is not allowed: {rom_ext}")
            return False
        return True
    
    def _check_seed_value(self):
        '''Verifies the seed value is either blank or only consists of digits'''
        seed_val = self.seed_value.get()
        if((not seed_val.isdigit()) and (seed_val != "")):
            Error_GUI(f"Seed value is not allowed: '{seed_val}'")
            return False
        return True
    
    def _check_final_note_door_value(self):
        '''Verifies the note door limits are digits'''
        final_note_door_val = self.final_note_door_value.get()
        if(not final_note_door_val.isdigit()):
            Error_GUI(f"Final Note Door Value Must Be An Positive Integer: '{str(final_note_door_val)}'")
            return False
        final_note_door_val = int(final_note_door_val)
        if(final_note_door_val < 0):
            Error_GUI("Final Note Door Value Must Be Greater Than Zero.")
            return False
        if((self.struct_var.get() == 4) and (final_note_door_val > 2000)):
            Error_GUI("Final Note Door Value Must Be Less Than 2000 Under These Settings.")
            return False
        elif(final_note_door_val > 900):
            Error_GUI("Final Note Door Value Must Be Less Than 900 Under These Settings.")
            return False
        return True
    
    def _check_final_puzzle_value(self):
        '''Verifies the puzzle door limits are digits'''
        final_puzzle_val = self.final_puzzle_value.get()
        if(not final_puzzle_val.isdigit()):
            Error_GUI(f"Final Puzzle Value Must Be An Integer: '{str(final_puzzle_val)}'")
            return False
        final_puzzle_val= int(final_puzzle_val)
        if(final_puzzle_val < 0):
            Error_GUI("Final Puzzle Value Must Be Greater Than Zero.")
            return False
        elif(final_puzzle_val > 100):
            Error_GUI("Final Puzzle Value Must Be Less Than 100 Under These Settings.")
            return False
        return True
    
    def _submit(self):
        '''If all input paramaters meet the requirements, we move onto actually randomizing the game'''
        if(self._check_rom_directory() and self._check_seed_value() and self._check_final_note_door_value() and self._check_final_puzzle_value()):
            self._save_current_configuration(button_press=False)
            progression_app = Progression_GUI(self)
            progression_app._main()
        else:
            print("It Failed")
    
    def _main(self):
        '''Places all of the widgest on the GUI and runs the loop for the window'''
        self.ttp_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Tool_Tips.png")
        ##################
        ### LEFT FRAME ###
        ##################
        self.left_frame = tk.LabelFrame(self.app_window)
        self.left_frame["borderwidth"] = 0
        self.left_frame["highlightthickness"] = 0
        self.left_frame.pack(side='left', expand=tk.TRUE, fill=tk.BOTH)
        ### ROM ###
        self.rom_frame = tk.LabelFrame(self.left_frame, text="ROM File")
        self.rom_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.select_rom_button_ttp_canvas = tk.Label(self.rom_frame, image=self.ttp_image)
        self.select_rom_button_ttp_canvas.pack(padx=5, pady=5, side='left')
        self.select_rom_button_ttp = self.CreateToolTip(self.select_rom_button_ttp_canvas, self, tool_tips_dict["ROM"]["SELECT_ROM_FILE"])
        self.select_rom_button = tk.Button(self.rom_frame, text='Select ROM File', command=self._select_rom_file)
        self.select_rom_button.pack(padx=5, pady=5, side='left')
        self.rom_file_entry = tk.StringVar(self.rom_frame)
        self.rom_file_display = tk.Entry(self.rom_frame, textvariable=self.rom_file_entry, state='readonly', width=40)
        self.rom_file_display.pack(padx=5, pady=5, expand=tk.TRUE, fill=tk.X, side='left')
        self.rom_file_display.grid_columnconfigure(1, weight=1)
        self.rom_file_display.grid_rowconfigure(0, weight=1)
        ### Seed ##
        self.seed_frame = tk.LabelFrame(self.left_frame, text="Seed")
        self.seed_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.random_seed_button_ttp_canvas = tk.Label(self.seed_frame, image=self.ttp_image)
        self.random_seed_button_ttp_canvas.pack(padx=5, pady=5, side='left')
        self.random_seed_button_ttp = self.CreateToolTip(self.random_seed_button_ttp_canvas, self, tool_tips_dict["SEED"]["RANDOM_SEED_BUTTON"])
        self._seed_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Seed.png")
        self.random_seed_button = tk.Button(self.seed_frame, text='Select ROM File', command=self._random_seed, image=self._seed_image)
        self.random_seed_button.pack(padx=5, pady=5, side='left')
        self.seed_value = tk.StringVar(self.seed_frame)
        self.seed_entry = tk.Entry(self.seed_frame, textvariable=self.seed_value, width=20)
        self.seed_entry.pack(padx=5, pady=5, expand=tk.TRUE, fill=tk.X, side='left')
        ### General Settings ###
        # Flagged Objects
        self.flagged_object_frame = tk.LabelFrame(self.left_frame, text="Jiggies/Empty Honeycombs/Mumbo Tokens")
        self.flagged_object_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.flagged_object_ttp_canvas = tk.Label(self.flagged_object_frame, image=self.ttp_image)
        self.flagged_object_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.flagged_object_ttp = self.CreateToolTip(self.flagged_object_ttp_canvas, self, tool_tips_dict["FLAGGED_OBJECTS"]["FRAME"])
        self.flagged_object_var = tk.StringVar(self.flagged_object_frame)
        self.flagged_object_options = ["None", "Shuffle (World)", "Shuffle (Game)"]
        self.flagged_object_dropdown = ttk.Combobox(self.flagged_object_frame, textvariable=self.flagged_object_var)
        self.flagged_object_dropdown['values'] = self.flagged_object_options
        self.flagged_object_dropdown['state'] = 'readonly'
        self.flagged_object_dropdown.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.final_puzzle_ttp_canvas = tk.Label(self.flagged_object_frame, image=self.ttp_image)
        self.final_puzzle_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.final_puzzle_checkbox_ttp = self.CreateToolTip(self.final_puzzle_ttp_canvas, self, tool_tips_dict["GRUNTILDAS_LAIR"]["FINAL_PUZZLE"])
        self.final_text = tk.Label(self.flagged_object_frame, text="Door of Grunty Jiggies:")
        self.final_text.grid(row=0, column=3, padx=self.padx, pady=self.pady)
        self.final_text = tk.Label(self.flagged_object_frame, text="Random Value?")
        self.final_text.grid(row=0, column=4, padx=self.padx, pady=self.pady)
        self.final_puzzle_var = tk.IntVar()
        self.final_puzzle_checkbox = tk.Checkbutton(self.flagged_object_frame, text="Door Of Grunty Only", variable=self.final_puzzle_var)
        self.final_puzzle_checkbox.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.final_puzzle_value = tk.StringVar(self.flagged_object_frame)
        self.final_puzzle_entry = tk.Entry(self.flagged_object_frame, textvariable=self.final_puzzle_value, width=6)
        self.final_puzzle_entry.grid(row=1, column=3, padx=self.padx, pady=self.pady)
        self.flagged_object_abnormalities_var = tk.IntVar()
        self.flagged_object_abnormalities_checkbutton = tk.Checkbutton(self.flagged_object_frame, text="Include Abnormalities", variable=self.flagged_object_abnormalities_var)
        self.flagged_object_abnormalities_checkbutton.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.flagged_object_softlock_var = tk.IntVar()
        self.flagged_object_softlock_checkbutton = tk.Checkbutton(self.flagged_object_frame, text="Include Potential Softlocks", variable=self.flagged_object_softlock_var)
        self.flagged_object_softlock_checkbutton.grid(row=2, column=3, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self._jiggy_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Jiggy.png")
        self.random_puzzle_value_button = tk.Button(self.flagged_object_frame, text='Random Puzzle Value', command=self._random_puzzle_value, image=self._jiggy_image)
        self.random_puzzle_value_button.grid(row=1, column=4, padx=self.padx, pady=self.pady)
        # Non Flagged Objects
        self.non_flagged_object_frame = tk.LabelFrame(self.left_frame, text="Jinjos/1-Ups/Misc Objects")
        self.non_flagged_object_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.non_flagged_object_ttp_canvas = tk.Label(self.non_flagged_object_frame, image=self.ttp_image)
        self.non_flagged_object_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.non_flagged_object_ttp = self.CreateToolTip(self.non_flagged_object_ttp_canvas, self, tool_tips_dict["NON_FLAGGED_OBJECTS"]["FRAME"])
        self.non_flagged_object_var = tk.StringVar(self.non_flagged_object_frame)
        self.non_flagged_object_options = ["None", "Shuffle (World)"]
        self.non_flagged_object_dropdown = ttk.Combobox(self.non_flagged_object_frame, textvariable=self.non_flagged_object_var)
        self.non_flagged_object_dropdown['values'] = self.non_flagged_object_options
        self.non_flagged_object_dropdown['state'] = 'readonly'
        self.non_flagged_object_dropdown.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.non_flagged_object_abnormalities_var = tk.IntVar()
        self.non_flagged_object_abnormalities_checkbutton = tk.Checkbutton(self.non_flagged_object_frame, text="Include Abnormalities (May Include Eggs and Feathers)", variable=self.non_flagged_object_abnormalities_var)
        self.non_flagged_object_abnormalities_checkbutton.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Structs
        self.struct_frame = tk.LabelFrame(self.left_frame, text="Notes/Blue Eggs/Red Feathers/Gold Feathers")
        self.struct_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.struct_ttp_canvas = tk.Label(self.struct_frame, image=self.ttp_image)
        self.struct_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.struct_ttp = self.CreateToolTip(self.struct_ttp_canvas, self, tool_tips_dict["STRUCTS"]["FRAME"])
        self.struct_var = tk.StringVar(self.struct_frame)
        self.struct_options = ["None", "Shuffle (World)", "Shuffle (Game)", "Randomize", "All Notes"]
        self.struct_dropdown = ttk.Combobox(self.struct_frame, textvariable=self.struct_var)
        self.struct_dropdown['values'] = self.struct_options
        self.struct_dropdown['state'] = 'readonly'
        self.struct_dropdown.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.final_note_door_ttp_canvas = tk.Label(self.struct_frame, image=self.ttp_image)
        self.final_note_door_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.final_note_door_checkbox_ttp = self.CreateToolTip(self.final_note_door_ttp_canvas, self, tool_tips_dict["GRUNTILDAS_LAIR"]["FINAL_NOTE_DOOR"])
        self.final_note_door_var = tk.StringVar(self.struct_frame)
        self.note_door_options = ["Scaling Note Doors", "Final Note Door Only"]
        self.final_note_door_dropdown = ttk.Combobox(self.struct_frame, textvariable=self.final_note_door_var)
        self.final_note_door_dropdown['values'] = self.note_door_options
        self.final_note_door_dropdown['state'] = 'readonly'
        self.final_note_door_dropdown.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.final_note_door_value = tk.StringVar(self.struct_frame)
        self.final_text = tk.Label(self.struct_frame, text="810 Note Door Value:")
        self.final_text.grid(row=0, column=2, columnspan=2, padx=self.padx, pady=self.pady)
        self.final_note_door_entry = tk.Entry(self.struct_frame, textvariable=self.final_note_door_value, width=6)
        self.final_note_door_entry.grid(row=1, column=2, padx=self.padx, pady=self.pady, sticky='e')
        self.final_text = tk.Label(self.struct_frame, text="Notes")
        self.final_text.grid(row=1, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.final_text = tk.Label(self.struct_frame, text="Random Value?")
        self.final_text.grid(row=0, column=4, padx=self.padx, pady=self.pady)
        self._note_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Note.png")
        self.random_note_value_button = tk.Button(self.struct_frame, text='Random Note Value', command=self._random_note_value, image=self._note_image)
        self.random_note_value_button.grid(row=1, column=4, padx=self.padx, pady=self.pady)
        # World Entrances
        self.world_entrance_frame = tk.LabelFrame(self.left_frame, text="World Entrances (Includes Randomized Moves)")
        self.world_entrance_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.world_entrance_ttp_canvas = tk.Label(self.world_entrance_frame, image=self.ttp_image)
        self.world_entrance_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.world_entrance_ttp = self.CreateToolTip(self.world_entrance_ttp_canvas, self, tool_tips_dict["WORLD_ENTRANCES"]["FRAME"])
        self.world_entrance_var = tk.StringVar(self.world_entrance_frame)
        self.world_entrance_options = ["None", "Basic Shuffle", "Bottles Shuffle"]
        self.world_entrance_dropdown = ttk.Combobox(self.world_entrance_frame, textvariable=self.world_entrance_var)
        self.world_entrance_dropdown['values'] = self.world_entrance_options
        self.world_entrance_dropdown['state'] = 'readonly'
        self.world_entrance_dropdown.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Within World Warps
        self.within_world_warp_frame = tk.LabelFrame(self.left_frame, text="Within The World Warps*")
        self.within_world_warp_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.within_world_warp_ttp_canvas = tk.Label(self.within_world_warp_frame, image=self.ttp_image)
        self.within_world_warp_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.within_world_warp_ttp = self.CreateToolTip(self.within_world_warp_ttp_canvas, self, tool_tips_dict["WITHIN_WORLD_WARPS"]["FRAME"])
        self.within_world_warps_var = tk.StringVar(self.within_world_warp_frame)
        self.within_world_warps_options = ["None", "Shuffle By World", "Shuffle By Game"]
        self.within_world_warps_dropdown = ttk.Combobox(self.within_world_warp_frame, textvariable=self.within_world_warps_var)
        self.within_world_warps_dropdown['values'] = self.within_world_warps_options
        self.within_world_warps_dropdown['state'] = 'readonly'
        self.within_world_warps_dropdown.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Enemies
        self.enemies_frame = tk.LabelFrame(self.left_frame, text="Ground/Wall/Flying Enemies")
        self.enemies_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.enemies_ttp_canvas = tk.Label(self.enemies_frame, image=self.ttp_image)
        self.enemies_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.enemies_ttp = self.CreateToolTip(self.enemies_ttp_canvas, self, tool_tips_dict["ENEMIES"]["FRAME"])
        self.enemies_var = tk.StringVar(self.enemies_frame)
        self.enemies_options = ["None", "Shuffle", "Randomize", "All Toughies"]
        self.enemies_dropdown = ttk.Combobox(self.enemies_frame, textvariable=self.enemies_var)
        self.enemies_dropdown['values'] = self.enemies_options
        self.enemies_dropdown['state'] = 'readonly'
        self.enemies_dropdown.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.enemies_beta_var = tk.IntVar()
        self.enemies_beta_checkbutton = tk.Checkbutton(self.enemies_frame, text="Beta Enemy (If Randomize)", variable=self.enemies_beta_var)
        self.enemies_beta_checkbutton.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        ### Aesthetic Settings ###
        # BK Model
        self.bk_model_frame = tk.LabelFrame(self.left_frame, text="Banjo-Kazooie Model Color")
        self.bk_model_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.bk_model_ttp_canvas = tk.Label(self.bk_model_frame, image=self.ttp_image)
        self.bk_model_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.bk_model_frame_ttp = self.CreateToolTip(self.bk_model_ttp_canvas, self, tool_tips_dict["BK_COLOR"]["FRAME"])
        self.bk_model_json = read_json(f"{self.cwd}Randomization_Processes/Misc_Manipulation/Model_Data/BK_Model_Presets.json")
        self.bk_model_var = tk.StringVar(self.bk_model_frame)
        self.bk_model_options = []
        for item in sorted(self.bk_model_json):
            self.bk_model_options.append(item)
        self.bk_model_var.set(self.bk_model_options[0])
        self.bk_model_dropdown = ttk.Combobox(self.bk_model_frame, textvariable=self.bk_model_var)
        self.bk_model_dropdown['values'] = self.bk_model_options
        self.bk_model_dropdown['state'] = 'readonly'
        self.bk_model_dropdown.grid(row=0, column=1, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.random_bk_model_preset_button = tk.Button(self.bk_model_frame, text='Random Preset', command=self._random_bk_model_preset)
        self.random_bk_model_preset_button.grid(row=0, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.random_bk_model_colors_button = tk.Button(self.bk_model_frame, text='Random Colors', command=self._random_bk_model_colors)
        self.random_bk_model_colors_button.grid(row=0, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.banjo_fur_text = tk.Label(self.bk_model_frame, text="Banjo's Fur")
        self.banjo_fur_text.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.banjo_fur_var = tk.StringVar(self.bk_model_frame)
        self.banjo_fur_entry = tk.Entry(self.bk_model_frame, textvariable=self.banjo_fur_var, width=9)
        self.banjo_fur_entry.grid(row=1, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.tooth_necklace_text = tk.Label(self.bk_model_frame, text="Tooth Necklace")
        self.tooth_necklace_text.grid(row=1, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.tooth_necklace_var = tk.StringVar(self.bk_model_frame)
        self.tooth_necklace_entry = tk.Entry(self.bk_model_frame, textvariable=self.tooth_necklace_var, width=9)
        self.tooth_necklace_entry.grid(row=1, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.banjo_skin_text = tk.Label(self.bk_model_frame, text="Banjo's Skin")
        self.banjo_skin_text.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.banjo_skin_var = tk.StringVar(self.bk_model_frame)
        self.banjo_skin_entry = tk.Entry(self.bk_model_frame, textvariable=self.banjo_skin_var, width=9)
        self.banjo_skin_entry.grid(row=2, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.banjo_feet_text = tk.Label(self.bk_model_frame, text="Banjo's Toes")
        self.banjo_feet_text.grid(row=2, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.banjo_feet_var = tk.StringVar(self.bk_model_frame)
        self.banjo_feet_entry = tk.Entry(self.bk_model_frame, textvariable=self.banjo_feet_var, width=5)
        self.banjo_feet_entry.grid(row=2, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_primary_text = tk.Label(self.bk_model_frame, text="Kazooie Primary")
        self.kazooie_primary_text.grid(row=3, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_primary_var = tk.StringVar(self.bk_model_frame)
        self.kazooie_primary_entry = tk.Entry(self.bk_model_frame, textvariable=self.kazooie_primary_var, width=9)
        self.kazooie_primary_entry.grid(row=3, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_wing_primary_text = tk.Label(self.bk_model_frame, text="Wing Primary")
        self.kazooie_wing_primary_text.grid(row=3, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_wing_primary_var = tk.StringVar(self.bk_model_frame)
        self.kazooie_wing_primary_entry = tk.Entry(self.bk_model_frame, textvariable=self.kazooie_wing_primary_var, width=5)
        self.kazooie_wing_primary_entry.grid(row=3, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_secondary_text = tk.Label(self.bk_model_frame, text="Kazooie Secondary")
        self.kazooie_secondary_text.grid(row=4, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_secondary_var = tk.StringVar(self.bk_model_frame)
        self.kazooie_secondary_entry = tk.Entry(self.bk_model_frame, textvariable=self.kazooie_secondary_var, width=9)
        self.kazooie_secondary_entry.grid(row=4, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_wing_secondary_text = tk.Label(self.bk_model_frame, text="Wing Secondary")
        self.kazooie_wing_secondary_text.grid(row=4, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_wing_secondary_var = tk.StringVar(self.bk_model_frame)
        self.kazooie_wing_secondary_entry = tk.Entry(self.bk_model_frame, textvariable=self.kazooie_wing_secondary_var, width=5)
        self.kazooie_wing_secondary_entry.grid(row=4, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.backpack_text = tk.Label(self.bk_model_frame, text="Backpack")
        self.backpack_text.grid(row=5, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.backpack_var = tk.StringVar(self.bk_model_frame)
        self.backpack_entry = tk.Entry(self.bk_model_frame, textvariable=self.backpack_var, width=9)
        self.backpack_entry.grid(row=5, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.wading_boots_text = tk.Label(self.bk_model_frame, text="Wading Boots")
        self.wading_boots_text.grid(row=5, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.wading_boots_var = tk.StringVar(self.bk_model_frame)
        self.wading_boots_entry = tk.Entry(self.bk_model_frame, textvariable=self.wading_boots_var, width=9)
        self.wading_boots_entry.grid(row=5, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.shorts_vertex_text = tk.Label(self.bk_model_frame, text="Shorts Main")
        self.shorts_vertex_text.grid(row=6, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.shorts_vertex_var = tk.StringVar(self.bk_model_frame)
        self.shorts_vertex_entry = tk.Entry(self.bk_model_frame, textvariable=self.shorts_vertex_var, width=9)
        self.shorts_vertex_entry.grid(row=6, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.shorts_texture_text = tk.Label(self.bk_model_frame, text="Shorts Front")
        self.shorts_texture_text.grid(row=6, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.shorts_texture_var = tk.StringVar(self.bk_model_frame)
        self.shorts_texture_entry = tk.Entry(self.bk_model_frame, textvariable=self.shorts_texture_var, width=9)
        self.shorts_texture_entry.grid(row=6, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.bk_model_var.trace('w', self._update_bk_model)
        # Other Models
        self.other_model_frame = tk.LabelFrame(self.left_frame, text="Models & Animations")
        self.other_model_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.other_model_ttp_canvas = tk.Label(self.other_model_frame, image=self.ttp_image)
        self.other_model_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.other_model_frame_ttp = self.CreateToolTip(self.other_model_ttp_canvas, self, tool_tips_dict["MODELS_AND_ANIMATIONS"]["MODELS"])
        self.other_model_var = tk.IntVar(self.other_model_frame)
        self.other_model_checkbox = tk.Checkbutton(self.other_model_frame, text="Model Manipulation", variable=self.other_model_var)
        self.other_model_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.animation_ttp_canvas = tk.Label(self.other_model_frame, image=self.ttp_image)
        self.animation_ttp_canvas.grid(row=0, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.animation_frame_ttp = self.CreateToolTip(self.animation_ttp_canvas, self, tool_tips_dict["MODELS_AND_ANIMATIONS"]["ANIMATIONS"])
        self.animation_var = tk.IntVar(self.other_model_frame)
        self.animation_checkbox = tk.Checkbutton(self.other_model_frame, text="Animation Manipulation", variable=self.animation_var)
        self.animation_checkbox.grid(row=0, column=3, padx=self.padx, pady=self.pady, sticky='w')
        # Sounds/Music
        self.sound_music_frame = tk.LabelFrame(self.left_frame, text="Short Sounds/Fanfare & Jingles/Looped Music")
        self.sound_music_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.short_sounds_ttp_canvas = tk.Label(self.sound_music_frame, image=self.ttp_image)
        self.short_sounds_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.short_sounds_checkbutton_ttp = self.CreateToolTip(self.short_sounds_ttp_canvas, self, tool_tips_dict["SOUNDS_MUSIC"]["SHUFFLE_SOUNDS"])
        self.short_sounds_var = tk.IntVar()
        self.short_sounds_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Shuffle Sounds", variable=self.short_sounds_var)
        self.short_sounds_checkbutton.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.jingle_checkbutton_ttp_canvas = tk.Label(self.sound_music_frame, image=self.ttp_image)
        self.jingle_checkbutton_ttp_canvas.grid(row=0, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.jingle_checkbutton_ttp = self.CreateToolTip(self.jingle_checkbutton_ttp_canvas, self, tool_tips_dict["SOUNDS_MUSIC"]["SHUFFLE_JINGLES"])
        self.jingles_var = tk.IntVar()
        self.jingle_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Shuffle Jingles", variable=self.jingles_var)
        self.jingle_checkbutton.grid(row=0, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.music_checkbutton_ttp_canvas = tk.Label(self.sound_music_frame, image=self.ttp_image)
        self.music_checkbutton_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.music_checkbutton_ttp = self.CreateToolTip(self.music_checkbutton_ttp_canvas, self, tool_tips_dict["SOUNDS_MUSIC"]["SHUFFLE_MUSIC"])
        self.music_var = tk.IntVar()
        self.music_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Shuffle Music", variable=self.music_var)
        self.music_checkbutton.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.beta_sounds_checkbutton_ttp_canvas = tk.Label(self.sound_music_frame, image=self.ttp_image)
        self.beta_sounds_checkbutton_ttp_canvas.grid(row=1, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.beta_sounds_checkbutton_ttp = self.CreateToolTip(self.beta_sounds_checkbutton_ttp_canvas, self, tool_tips_dict["SOUNDS_MUSIC"]["INCLUDE_BETA_SOUNDS"])
        self.beta_sounds_var = tk.IntVar()
        self.beta_sounds_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Include Beta Sounds", variable=self.beta_sounds_var)
        self.beta_sounds_checkbutton.grid(row=1, column=3, padx=self.padx, pady=self.pady, sticky='w')
        # Sprites/Textures
        self.texture_frame = tk.LabelFrame(self.left_frame, text="Sprites/Textures")
        self.texture_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.skybox_ttp_canvas = tk.Label(self.texture_frame, image=self.ttp_image)
        self.skybox_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.skybox_checkbutton_ttp = self.CreateToolTip(self.skybox_ttp_canvas, self, tool_tips_dict["SPRITES_TEXTURES"]["SHUFFLE_SKYBOXES"])
        self.skybox_var = tk.IntVar()
        self.skybox_checkbutton = tk.Checkbutton(self.texture_frame, text="Shuffle Skyboxes", variable=self.skybox_var)
        self.skybox_checkbutton.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.talking_sprite_ttp_canvas = tk.Label(self.texture_frame, image=self.ttp_image)
        self.talking_sprite_ttp_canvas.grid(row=0, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.talking_sprite_checkbutton_ttp = self.CreateToolTip(self.talking_sprite_ttp_canvas, self, tool_tips_dict["SPRITES_TEXTURES"]["SHUFFLE_TALKING_SPRITES"])
        self.talking_sprite_var = tk.IntVar()
        self.talking_sprite_checkbutton = tk.Checkbutton(self.texture_frame, text="Shuffle Talking Sprites", variable=self.talking_sprite_var)
        self.talking_sprite_checkbutton.grid(row=0, column=3, padx=self.padx, pady=self.pady, sticky='w')
        ###################
        ### RIGHT FRAME ###
        ###################
        self.right_frame = tk.LabelFrame(self.app_window)
        self.right_frame.pack(side='left', expand=tk.TRUE, fill=tk.BOTH)
        ### Config and Submit ###
        self.config_and_submit = tk.LabelFrame(self.right_frame)
        self.config_and_submit["borderwidth"] = 0
        self.config_and_submit["highlightthickness"] = 0
        self.config_and_submit.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Load
        self._load_config_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Load_Config.png")
        self.load_config_button = tk.Button(self.config_and_submit, text='Load Config', command=self._load_configuration, image=self._load_config_image)
        self.load_config_button.pack(padx=self.padx, pady=self.pady, expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Save
        self._save_config_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Save_Config.png")
        self.save_config_button = tk.Button(self.config_and_submit, text='Save Config', command=self._save_current_configuration, image=self._save_config_image)
        self.save_config_button.pack(padx=self.padx, pady=self.pady, expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Read Me
        self._read_me_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Read_Me.png")
        self.read_me = tk.Button(self.config_and_submit, text='Open ReadMe', command=self._open_readme_file, image=self._read_me_image)
        self.read_me.pack(padx=self.padx, pady=self.pady, expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Submit
        self._submit_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Submit.png")
        self.submit = tk.Button(self.config_and_submit, text='Submit', command=self._submit, image=self._submit_image)
        self.submit.pack(padx=self.padx, pady=self.pady, expand=tk.TRUE, fill=tk.BOTH, side='left')
        ### World Specific ###
        # Spiral Mountain
        # Gruntilda's Lair
        self.gruntildas_lair_frame = tk.LabelFrame(self.right_frame, text="Gruntilda's Lair")
        self.gruntildas_lair_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.gruntildas_lair_frame["borderwidth"] = 0
        self.gruntildas_lair_frame["highlightthickness"] = 0
        self.skip_furnace_fun_ttp_canvas = tk.Label(self.gruntildas_lair_frame, image=self.ttp_image)
        self.skip_furnace_fun_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.skip_furnace_fun_checkbox_ttp = self.CreateToolTip(self.skip_furnace_fun_ttp_canvas, self, tool_tips_dict["GRUNTILDAS_LAIR"]["SKIP_FURNACE_FUN_AND_BRENTILDA"])
        self.skip_furnace_fun_var = tk.IntVar()
        self.skip_furnace_fun_checkbox = tk.Checkbutton(self.gruntildas_lair_frame, text="Skip Furnace Fun/Brentilda Rando Hints", variable=self.skip_furnace_fun_var)
        self.skip_furnace_fun_checkbox.grid(row=0, column=1, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.remove_magic_barriers_ttp_canvas = tk.Label(self.gruntildas_lair_frame, image=self.ttp_image)
        self.remove_magic_barriers_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.remove_magic_barriers_checkbox_ttp = self.CreateToolTip(self.remove_magic_barriers_ttp_canvas, self, tool_tips_dict["GRUNTILDAS_LAIR"]["NO_DETRANSFORMATIONS"])
        self.remove_magic_barriers_var = tk.IntVar()
        self.remove_magic_barriers_checkbox = tk.Checkbutton(self.gruntildas_lair_frame, text="No Detransformations", variable=self.remove_magic_barriers_var)
        self.remove_magic_barriers_checkbox.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.gruntilda_difficulty_ttp_canvas = tk.Label(self.gruntildas_lair_frame, image=self.ttp_image)
        self.gruntilda_difficulty_ttp_canvas.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.gruntilda_difficulty_checkbox_ttp = self.CreateToolTip(self.gruntilda_difficulty_ttp_canvas, self, tool_tips_dict["GRUNTILDAS_LAIR"]["HARDER_FINAL_BATTLE"])
        self.gruntilda_difficulty_text = tk.Label(self.gruntildas_lair_frame, text="Final Battle Difficulty?\n0 For Default; 3 For Hard")
        self.gruntilda_difficulty_text.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.gruntilda_difficulty_var = tk.IntVar()
        self.gruntilda_difficulty_scale = tk.Scale(self.gruntildas_lair_frame, from_=0, to=3, orient=tkinter.HORIZONTAL, variable=self.gruntilda_difficulty_var)
        self.gruntilda_difficulty_scale.grid(row=2, column=2, columnspan=2, padx=self.padx, pady=self.pady, sticky='n')
        # Mumbo's Mountain
        self.mumbos_mountain_frame = tk.LabelFrame(self.right_frame, text="Mumbo's Mountain")
        self.mumbos_mountain_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.mumbos_mountain_frame["borderwidth"] = 0
        self.mumbos_mountain_frame["highlightthickness"] = 0
        self.flowers_ttp_canvas = tk.Label(self.mumbos_mountain_frame, image=self.ttp_image)
        self.flowers_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.flowers_checkbox_ttp = self.CreateToolTip(self.flowers_ttp_canvas, self, tool_tips_dict["MUMBOS_MOUNTAIN"]["INCLUDE_FLOWERS"])
        self.flowers_var = tk.IntVar()
        self.flowers_checkbox = tk.Checkbutton(self.mumbos_mountain_frame, text="Include Flowers (Shuffling/Randomizing)", variable=self.flowers_var)
        self.flowers_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Treasure Trove Cove
        self.treasure_trove_cove_frame = tk.LabelFrame(self.right_frame, text="Treasure Trove Cove")
        self.treasure_trove_cove_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.treasure_trove_cove_frame["borderwidth"] = 0
        self.treasure_trove_cove_frame["highlightthickness"] = 0
        self.scattered_structs_ttp_canvas = tk.Label(self.treasure_trove_cove_frame, image=self.ttp_image)
        self.scattered_structs_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.scattered_structs_checkbox_ttp = self.CreateToolTip(self.scattered_structs_ttp_canvas, self, tool_tips_dict["TREASURE_TROVE_COVE"]["SCATTERED_STRUCTS"])
        self.scattered_structs_var = tk.IntVar()
        self.scattered_structs_checkbox = tk.Checkbutton(self.treasure_trove_cove_frame, text="Scattered Notes/Eggs/Feathers", variable=self.scattered_structs_var)
        self.scattered_structs_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Clanker's Cavern
        self.clankers_cavern_frame = tk.LabelFrame(self.right_frame, text="Clanker's Cavern")
        self.clankers_cavern_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.clankers_cavern_frame["borderwidth"] = 0
        self.clankers_cavern_frame["highlightthickness"] = 0
        self.hard_rings_ttp_canvas = tk.Label(self.clankers_cavern_frame, image=self.ttp_image)
        self.hard_rings_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.hard_rings_checkbox_ttp = self.CreateToolTip(self.hard_rings_ttp_canvas, self, tool_tips_dict["CLANKERS_CAVERN"]["SHUFFLE_CLANKER_RING_ORDER"])
        self.hard_rings_var = tk.IntVar()
        self.hard_rings_checkbox = tk.Checkbutton(self.clankers_cavern_frame, text="Shuffle Clanker Ring Order", variable=self.hard_rings_var)
        self.hard_rings_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Bubblegloop Swamp
        self.bubblegloop_swamp_frame = tk.LabelFrame(self.right_frame, text="Bubblegloop Swamp")
        self.bubblegloop_swamp_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.bubblegloop_swamp_frame["borderwidth"] = 0
        self.bubblegloop_swamp_frame["highlightthickness"] = 0
        self.croctus_ttp_canvas = tk.Label(self.bubblegloop_swamp_frame, image=self.ttp_image)
        self.croctus_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.croctus_checkbox_ttp = self.CreateToolTip(self.croctus_ttp_canvas, self, tool_tips_dict["BUBBLEGLOOP_SWAMP"]["SHUFFLE_CROCTUS_ORDER"])
        self.croctus_var = tk.IntVar()
        self.croctus_checkbox = tk.Checkbutton(self.bubblegloop_swamp_frame, text="Shuffle Croctus Order", variable=self.croctus_var)
        self.croctus_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.mr_vile_ttp_canvas = tk.Label(self.bubblegloop_swamp_frame, image=self.ttp_image)
        self.mr_vile_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.mr_vile_checkbox_ttp = self.CreateToolTip(self.mr_vile_ttp_canvas, self, tool_tips_dict["BUBBLEGLOOP_SWAMP"]["MR_VILE_BIGGER_BADDER_CROCODILE"])
        self.mr_vile_var = tk.IntVar()
        self.mr_vile_checkbox = tk.Checkbutton(self.bubblegloop_swamp_frame, text="Mr. Vile: Bigger, Badder Crocodile", variable=self.mr_vile_var)
        self.mr_vile_checkbox.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.tiptup_choir_ttp_canvas = tk.Label(self.bubblegloop_swamp_frame, image=self.ttp_image)
        self.tiptup_choir_ttp_canvas.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.tiptup_choir_checkbox_ttp = self.CreateToolTip(self.tiptup_choir_ttp_canvas, self, tool_tips_dict["BUBBLEGLOOP_SWAMP"]["TIPTUP_CHOIR_NO_ASSIGNED_SEATS"])
        self.tiptup_choir_var = tk.IntVar()
        self.tiptup_choir_checkbox = tk.Checkbutton(self.bubblegloop_swamp_frame, text="Tiptup Choir: No Assigned Seats", variable=self.tiptup_choir_var)
        self.tiptup_choir_checkbox.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Freezeezy Peak
        self.freezeezy_peak_frame = tk.LabelFrame(self.right_frame, text="Freezeezy Peak")
        self.freezeezy_peak_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.freezeezy_peak_frame["borderwidth"] = 0
        self.freezeezy_peak_frame["highlightthickness"] = 0
        self.hard_races_ttp_canvas = tk.Label(self.freezeezy_peak_frame, image=self.ttp_image)
        self.hard_races_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.hard_races_checkbox_ttp = self.CreateToolTip(self.hard_races_ttp_canvas, self, tool_tips_dict["FREEZEEZY_PEAK"]["BOGGY_RACES_MOVED_FLAGS"])
        self.hard_races_var = tk.IntVar()
        self.hard_races_checkbox = tk.Checkbutton(self.freezeezy_peak_frame, text="Boggy Races: Moved Flags", variable=self.hard_races_var)
        self.hard_races_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Gobi's Valley
        self.gobis_valley_frame = tk.LabelFrame(self.right_frame, text="Gobi's Valley")
        self.gobis_valley_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.gobis_valley_frame["borderwidth"] = 0
        self.gobis_valley_frame["highlightthickness"] = 0
        self.ancient_ones_ttp_canvas = tk.Label(self.gobis_valley_frame, image=self.ttp_image)
        self.ancient_ones_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.ancient_ones_checkbox_ttp = self.CreateToolTip(self.ancient_ones_ttp_canvas, self, tool_tips_dict["GOBIS_VALLEY"]["SHUFFLED_ANCIENT_ONES_ORDER"])
        self.ancient_ones_var = tk.IntVar()
        self.ancient_ones_checkbox = tk.Checkbutton(self.gobis_valley_frame, text="Shuffle Ancient Ones Order", variable=self.ancient_ones_var)
        self.ancient_ones_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.maze_jinxy_heads_ttp_canvas = tk.Label(self.gobis_valley_frame, image=self.ttp_image)
        self.maze_jinxy_heads_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.maze_jinxy_heads_checkbox_ttp = self.CreateToolTip(self.maze_jinxy_heads_ttp_canvas, self, tool_tips_dict["GOBIS_VALLEY"]["SHUFFLE_MAZE_JINXY_HEADS_ORDER"])
        self.maze_jinxy_heads_var = tk.IntVar()
        self.maze_jinxy_heads_checkbox = tk.Checkbutton(self.gobis_valley_frame, text="Shuffle Maze Jinxy Heads Order", variable=self.maze_jinxy_heads_var)
        self.maze_jinxy_heads_checkbox.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.matching_puzzle_ttp_canvas = tk.Label(self.gobis_valley_frame, image=self.ttp_image)
        self.matching_puzzle_ttp_canvas.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.matching_puzzle_checkbox_ttp = self.CreateToolTip(self.matching_puzzle_ttp_canvas, self, "Randomized Matching Puzzle Not Implemented Yet")
        self.matching_puzzle_var = tk.IntVar()
        self.matching_puzzle_checkbox = tk.Checkbutton(self.gobis_valley_frame, text="Randomize Matching Puzzle", variable=self.matching_puzzle_var)
        self.matching_puzzle_checkbox.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Mad Monster Mansion
        self.mad_monster_mansion_frame = tk.LabelFrame(self.right_frame, text="Mad Monster Mansion")
        self.mad_monster_mansion_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.mad_monster_mansion_frame["borderwidth"] = 0
        self.mad_monster_mansion_frame["highlightthickness"] = 0
        self.lit_pots_ttp_canvas = tk.Label(self.mad_monster_mansion_frame, image=self.ttp_image)
        self.lit_pots_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.lit_pots_checkbox_ttp = self.CreateToolTip(self.lit_pots_ttp_canvas, self, tool_tips_dict["MAD_MONSTER_MANSION"]["POTS_ARE_LIT"])
        self.lit_pots_var = tk.IntVar()
        self.lit_pots_checkbox = tk.Checkbutton(self.mad_monster_mansion_frame, text="Pots Are Lit", variable=self.lit_pots_var)
        self.lit_pots_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Rusty Bucket Bay
        self.rusty_bucket_bay_frame = tk.LabelFrame(self.right_frame, text="Rusty Bucket Bay")
        self.rusty_bucket_bay_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.rusty_bucket_bay_frame["borderwidth"] = 0
        self.rusty_bucket_bay_frame["highlightthickness"] = 0
        self.buttons_ttp_canvas = tk.Label(self.rusty_bucket_bay_frame, image=self.ttp_image)
        self.buttons_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.buttons_checkbox_ttp = self.CreateToolTip(self.buttons_ttp_canvas, self, tool_tips_dict["RUSTY_BUCKET_BAY"]["RANDOMIZED_BUTTON_COMBO"])
        self.buttons_var = tk.IntVar()
        self.buttons_checkbox = tk.Checkbutton(self.rusty_bucket_bay_frame, text="Randomized Button Combo", variable=self.buttons_var)
        self.buttons_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Click Clock Wood
        self.click_clock_wood_frame = tk.LabelFrame(self.right_frame, text="Click Clock Wood")
        self.click_clock_wood_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.click_clock_wood_frame["borderwidth"] = 0
        self.click_clock_wood_frame["highlightthickness"] = 0
        self.ccw_ttp_canvas = tk.Label(self.click_clock_wood_frame, image=self.ttp_image)
        self.ccw_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.ccw_checkbox_ttp = self.CreateToolTip(self.ccw_ttp_canvas, self, tool_tips_dict["CLICK_CLOCK_WOOD"]["SHUFFLE_BY"])
        self.ccw_text = tk.Label(self.click_clock_wood_frame, text="Shuffle By:")
        self.ccw_text.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.ccw_var = tk.StringVar(self.click_clock_wood_frame)
        self.ccw_options = ["Season", "Within World"]
        self.ccw_dropdown = ttk.Combobox(self.click_clock_wood_frame, textvariable=self.ccw_var)
        self.ccw_dropdown['values'] = self.ccw_options
        self.ccw_dropdown['state'] = 'readonly'
        self.ccw_dropdown.grid(row=0, column=2, padx=self.padx, pady=self.pady, sticky='w')
        ### Misc Settings ###
        self.misc_frame = tk.LabelFrame(self.right_frame, text="Misc Options")
        self.misc_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Cheat Sheet
        self.cheat_sheet_ttp_canvas = tk.Label(self.misc_frame, image=self.ttp_image)
        self.cheat_sheet_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.cheat_sheet_checkbutton_ttp = self.CreateToolTip(self.cheat_sheet_ttp_canvas, self, tool_tips_dict["MISC_OPTIONS"]["CREATE_CHEAT_SHEET"])
        self.cheat_sheet_var = tk.IntVar()
        self.cheat_sheet_checkbutton = tk.Checkbutton(self.misc_frame, text="Create Cheat Sheet(s)", variable=self.cheat_sheet_var)
        self.cheat_sheet_checkbutton.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Remove Files
        self.remove_files_ttp_canvas = tk.Label(self.misc_frame, image=self.ttp_image)
        self.remove_files_ttp_canvas.grid(row=0, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.remove_files_checkbutton_ttp = self.CreateToolTip(self.remove_files_ttp_canvas, self, tool_tips_dict["MISC_OPTIONS"]["REMOVE_EXTRA_FILES"])
        self.remove_files_var = tk.IntVar()
        self.remove_files_checkbutton = tk.Checkbutton(self.misc_frame, text="Remove Extra Files", variable=self.remove_files_var)
        self.remove_files_checkbutton.grid(row=0, column=3, padx=self.padx, pady=self.pady, sticky='w')
        # Tool Tips
        self.tool_tips_ttp_canvas = tk.Label(self.misc_frame, image=self.ttp_image)
        self.tool_tips_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.tool_tips_checkbutton_ttp = self.CreateToolTip(self.tool_tips_ttp_canvas, self, tool_tips_dict["MISC_OPTIONS"]["TOOL_TIPS"])
        self.tool_tips_var = tk.IntVar()
        self.tool_tips_checkbutton = tk.Checkbutton(self.misc_frame, text="Show Tool Tips", variable=self.tool_tips_var)
        self.tool_tips_checkbutton.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        ########################
        ### DEFAULT SETTINGS ###
        ########################
        try:
            self._load_configuration(button_press=False)
        except Exception:
            self._set_recommended_defaults()
        ##########################
        ### GUI WINDOW OPTIONS ###
        ##########################
        ### Close Window ##
        self.app_window.protocol("WM_DELETE_WINDOW", self.app_window.destroy)
        ### Main Loop ###
        self.app_window.mainloop()

if __name__ == '__main__':
    user_app = User_GUI()
    user_app._main()
