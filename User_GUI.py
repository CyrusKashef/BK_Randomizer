'''
Created on Aug 21, 2021

@author: Cyrus

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
  #######        ############                ###   ###          ######################
 #       #       #          #   SUBMIT    ###         ###   NO  #                    #
#  START  # ---> # User GUI # ---------> #     ERROR?    # ---> # Progression_GUI.py #
 #       #   |   #          #             ###         ###       #                    #
  #######    |   ############                ###   ###          ######################
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
    "SETTING_CODE": {
        "GENERATING_SETTING_CODE": "Generates a settings code to verify matching settings with another user.\n" +
                                   "This code does not apply for the file directory, seed value, BK's model,\n" +
                                   "colors, music settings, skyboxes, sprites, and miscellaneous settings.",
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
            "RANDOMIZE:\n" +
            "    For every item in the world, randomly assign a new Object ID.\n" +
            "    Recommended using FINAL NOTE DOOR feature. You can set whether\n" +
            "    extra notes will spawn to make it easier.\n" +
            "ALL NOTES:\n" +
            "    All eggs and feathers become notes. Brentildas are replaced\n" +
            "    with egg and feather refills. The refill at that Brentilda\n" +
            "    location is random.\n"+
            "Allow Save & Quit/Reset\n" +
            "    Sets the limits of all world's notes to 127 to allow exiting\n" +
            "    the save file. Cannot be used for 'All Notes' feature.",
        "CARRY_LIMIT": "Changes how many eggs/feathers can be carried,\n" +
                       "before and after finding Cheato.",
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
            "    exploration. Logic may not work if worlds are opened out of order."+
            "LEVEL EXIT:\n"+
            "    When leaving the level, do you want to spawn at the entrance you\n"+
            "    came in, or the entrance that normally belongs to that world?",
        },
    "WITHIN_WORLD_WARPS": {
        "FRAME": 
            "NONE:\n" +
            "    Skips the setting.\n" +
            "SHUFFLE BY WORLD:\n" +
            "    Shuffles the warps that are within the world." +
            "SHUFFLE BY GAME:\n" +
            "    Shuffles the warps throughout the worlds.\n" +
            "    Feature is prone to crashes and softlocks.\n" +
            "    Use at own risk!",
        },
    "STARTING_AREA": {
        "NEW_GAME":
            "Spawns you at the location upon a new game.",
        },
    "ENEMIES": {
        "FRAME":
            "NONE:\n"+
            "    Skips the setting.\n" +
            "SHUFFLE:\n" +
            "    Shuffles the enemies within the world by category \n" +
            "    (ground, wall, air), whether checked or not.\n"
            "RANDOMIZE:\n"+
            "    For every enemy in the game (with some exceptions),\n" +
            "    randomly assign a new enemy that has a checkbox next to it.\n" +
            "SOFTLOCK:\n"+
            "    Any enemy with a * means it can softlock the game in some way.\n" +
            "    May cause an incompletable seed. Use at own risk!",
        },
    "BK_COLOR": {
        "FRAME": "Change BK's colors to presets",
        },
    "CUSTOMIZABLE": {
        "MODELS":
            "Every checkbox with an (A) means it applies aethetic changes\n" +
            "like model or animation replacements. Every checkbox with (P)\n" +
            "changes the death property of an object (like an enemy).",
        },
    "SOUNDS_MUSIC": {
        "FULL_DESCRIPTION":
            "SHUFFLE_SOUNDS: Shuffles short sounds, like ones for eggs, notes, and feathers.\n" +
            "SHUFFLE_JINGLES: Shuffles jingles that last a few seconds.\n" +
            "SHUFFLE_MUSIC: Shuffles music for levels and minigames.\n" +
            "INCLUDE_BETA_SOUNDS: Shuffles the other categories with unused versions.\n" +
            "INCLUDE_JARRING_SOUNDS: Includes harsher sounding sounds with the other categories."
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
                        "automatically opened. No floating jiggies will remove all\n" +
                        "Jiggies that aren't spawned by an event.",
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
                             "both in the water and in the air.",
        "SUPER_SLIPPERY_SAND": "At some point, you'll trigger the anti-tampering\n" +
                               "and you won't be able to change direction unless\n" +
                               "you jump. Have fun!"
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
        "MOTZAND_KEYS": "Motzand's music pattern is randomized.",
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
from random import randint, choice
import logging
from logging.handlers import RotatingFileHandler
from mmap import mmap

####################
### FILE IMPORTS ###
####################

from Progression_GUI import Progression_GUI_Class
from Randomization_Processes.Common_Functions import read_json, leading_zeros
from Randomization_Processes.Dicts_And_Lists.Game_Engine import start_level_ids
from Randomization_Processes.Dicts_And_Lists.Enemies import master_enemy_dict



#######################
### ERROR GUI CLASS ###
#######################

def Error_GUI(error_msg):
    '''Brings up a GUI that displays an error message'''
    def update_bottles_gif(ind):
        '''Updates The Gif Frame'''
        frame = frames[ind]
        ind += 1
        if ind == frame_count:
            ind = 0
        bottles_talking_label.configure(image=frame)
        bottles_talking_label.after(60, update_bottles_gif, ind)
    error_window = tk.Tk()
    error_msg = error_msg
    error_window.winfo_toplevel().title("Banjo-Kazooie Randomizer Error")
    error_window.config(background="#F3E5AB")
    # Bottles Talking
    frame_count = 10
    frames = [tk.PhotoImage(master=error_window, file=(f"{os.getcwd()}/Pictures/Bottles_Speaking.gif"), format = 'gif -index %i' %(i)) for i in range(frame_count)]
    bottles_talking_label = tk.Label(error_window, background="#F3E5AB")
    bottles_talking_label.pack(padx=5, pady=2)
    error_label = tk.Label(error_window, text=error_msg, background="#F3E5AB", font=("LITHOGRAPH-BOLD", 12))
    error_label.config(anchor='center')
    error_label.pack(padx=5, pady=2)
    ok_btn = tk.Button(error_window, text='Doh!', background="#F3E5AB", command=error_window.destroy, font=("LITHOGRAPH-BOLD", 12))
    ok_btn.config(anchor='center')
    ok_btn.pack(padx=5, pady=2)
    error_window.protocol("WM_DELETE_WINDOW", error_window.destroy)
    error_window.after(0, update_bottles_gif, 0)
    error_window.mainloop()

######################
### USER GUI CLASS ###
######################

class User_GUI_Class():
    '''Creates a GUI where users give the directory of the ROM file, select options for the randomization, and optionally provide a seed value'''
    def __init__(self, BK_RANDO_VERSION):
        '''Creates the Tkinter GUI'''
        self.BK_RANDO_VERSION = BK_RANDO_VERSION
        self.cwd = os.getcwd() + "/"
        self.app_window = tk.Tk()
        self.app_window.winfo_toplevel().title(f"Banjo-Kazooie Randomizer v{self.BK_RANDO_VERSION}")
        self.padx = 3
        self.pady = 1
        self.white = "#FFFFFF"
        self.blue = "#0040AA"
        self.red = "#990000"
        self.generic_background_color = "#BFBF00"
        self.black = "#000000"
        self.font_type = "LITHOGRAPH-BOLD"
        self.large_font_size = 22
        self.medium_font_size = 16
        self.small_font_size = 10
        ### LOGGER ###
        self.logger = logging.getLogger("Rotating Log")
        self.logger.setLevel(logging.INFO)
        FORMAT = '[%(levelname)s] %(asctime)-15s - %(funcName)s: %(message)s'
        handler = RotatingFileHandler(f"{self.cwd}\Randomizer_Log_File.log", maxBytes=(512*1024), backupCount=1)
        self.logger.addHandler(handler)
        logging.basicConfig(format=FORMAT)
    
    ######################
    ### TOOL TIP CLASS ###
    ######################
    
    class CreateToolTip(object):
        '''Create a tooltip for a given widget'''
        def __init__(self, widget, master, text='widget info'):
            self.widget = widget
            self.master = master
            self.text = text
            self.widget.bind("<Enter>", self.enter)
            self.widget.bind("<Leave>", self.close)
    
        def enter(self, event=None):
            '''When hovering over the tool tip icon, start displaying the tool tip'''
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
            '''When no longer hovering over the tool tip icon, stop displaying the tool tip'''
            try:
                if self.tw:
                    self.tw.destroy()
            except Exception:
                pass
    
    #############################
    ### FILE BUTTON FUNCTIONS ###
    #############################
    
    def _select_rom_file(self):
        '''Opens a browser to select the ROM file ending in .z64'''
        self.logger.info("Selecting ROM file")
        filename = tkinter.filedialog.askopenfilename(initialdir=self.cwd, title="Select The BK ROM File", filetype =(("Rom Files","*.z64"),("all files","*.*")) )
        if(not filename):
            return
        self.rom_file_entry.set(filename)
        self._verify_rom_file(filename)
    
    def _verify_rom_file(self, filename):
        '''PyDoc'''
        rom_version_dict = {
            "NTSC-U v1.0": [0xA4, 0xBF, 0x93, 0x06, 0xBF, 0x0C, 0xDF, 0xD1],
            "NTSC-U v1.1": [0xCD, 0x75, 0x59, 0xAC, 0xB2, 0x6C, 0xF5, 0xAE],
            "PAL v1.0":    [0x3F, 0x73, 0xB1, 0xCC, 0x48, 0x44, 0xF9, 0x92],
            "NTSC-J v1.1": [0x68, 0x51, 0x20, 0xD5, 0x5F, 0xCA, 0x0D, 0xCD]
            }
        with open(filename, "r+b") as rom_file:
            mm_rom = mmap(rom_file.fileno(), 0)
            rom_checksum = []
            for index in range(0x10, 0x18):
                rom_checksum.append(mm_rom[index])
            version = "Ellie Bobellie"
            for rom_version in rom_version_dict:
                if(rom_version_dict[rom_version] == rom_checksum):
                    version = rom_version
                    break
            if(version == "NTSC-U v1.0"):
                return True
            elif(version in ["NTSC-U v1.1", "PAL v1.0", "NTSC-J v1.1"]):
                Error_GUI(f"The selected ROM is '{version}'.\nThis version is not supported by the Randomizer.\nPlease use a NTSC-U v1.0 BK ROM.")
                return False
            else:
                Error_GUI(f"You're using either a modded game\n or a non-BK ROM ending in z64.\nPlease use a NTSC-U v1.0 BK ROM.")
                return False
    
    def _open_file(self, file_to_open):
        '''Generic open file button. If they use this for the README, bless their hearts'''
        self.logger.info(f"Openning File: {file_to_open}")
        os.startfile(file_to_open)
    
    ###############################
    ### RANDOM BUTTON FUNCTIONS ###
    ###############################
    
    def _random_seed(self):
        '''Randomly selects a seed'''
        self.logger.info("Select Random Seed")
        self.seed_value.set(str(randint(10000000, 19940303)))
    
    def _random_note_value(self):
        '''Randomly selects a note value'''
        self.logger.info("Select Random Note Value")
        self.final_note_door_value.set("?")
    
    def _random_puzzle_value(self):
        '''Randomly selects a puzzle value'''
        self.logger.info("Select Random Puzzle Value")
        self.final_puzzle_var.set(1)
        self.final_puzzle_value.set("?")
    
    def _random_bk_model_preset(self):
        '''Randomly selects a BK Preset from the JSON file'''
        self.logger.info("Select Random BK Model Preset")
        key_list = []
        for key in self.bk_model_json:
            key_list.append(key)
        random_bk_model = choice(key_list)
        self.bk_model_var.set(random_bk_model)
    
    def _random_hex(self, digit_len):
        '''Randomly generates hex values for the colors in BK'''
        max_num = "F" * digit_len
        random_hex_val = leading_zeros(randint(0, int(max_num, 16)), digit_len).upper()
        if(digit_len == 4):
            choices = [str(hex(num))[2:].upper() for num in range(0x1, 0xF, 0x2)]
            new_end_val = choice(choices)
            random_hex_val = random_hex_val[:-1] + new_end_val
        elif(digit_len == 6):
            random_hex_val = random_hex_val + "FF"
        return random_hex_val
    
    def _random_bk_model_colors(self):
        '''Randomly generates all of the BK model's hex colors'''
        self.logger.info("Select Random Colors For BK")
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
        '''When selecting a BK preset, it will update the color fields with the proper hex values'''
        self.logger.info("Update BK Model")
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
            preset_image_path = f"{self.cwd}Pictures/BK_Models/{bk_model_preset}.png"
            if(os.path.isfile(preset_image_path)):
                self.bk_model_image = tk.PhotoImage(file=preset_image_path)
            else:
                self.bk_model_image = tk.PhotoImage(file=f"{self.cwd}Pictures/BK_Models/Question_Mark.png")
            self.bk_model_image_label.config(image=self.bk_model_image)
        else:
            self.banjo_fur_var.set("?")
            self.tooth_necklace_var.set("?")
            self.banjo_skin_var.set("?")
            self.banjo_feet_var.set("?")
            self.kazooie_primary_var.set("?")
            self.kazooie_secondary_var.set("?")
            self.kazooie_wing_primary_var.set("?")
            self.kazooie_wing_secondary_var.set("?")
            self.backpack_var.set("?")
            self.wading_boots_var.set("?")
            self.shorts_vertex_var.set("?")
            self.shorts_texture_var.set("?")
            self.bk_model_image = tk.PhotoImage(file=f"{self.cwd}Pictures/BK_Models/Question_Mark.png")
            self.bk_model_image_label.config(image=self.bk_model_image)
    
    def _select_non_softlock_enemies(self):
        '''Checks the boxes for all non-softlock enemies and unchecks all softlock enemies'''
        self.logger.info("Select Non-Softlock Enemies")
        for enemy_name in self.enemy_checkbox_dict:
            if("*" in enemy_name):
                self.enemy_checkbox_dict[enemy_name].set(0)
            else:
                self.enemy_checkbox_dict[enemy_name].set(1)
    
    def _remove_all_enemies(self):
        '''Unchecks all enemy checkboxes'''
        self.logger.info("Deselect All Enemies")
        for enemy_name in self.enemy_checkbox_dict:
            self.enemy_checkbox_dict[enemy_name].set(0)
    
    def _all_custom_aesthetics(self):
        '''PyDoc'''
        self.logger.info("Select All Custom Aesthetic")
        for custom_name in self.customizable_checkbox_dict:
            if(custom_name.startswith("(A)")):
                self.customizable_checkbox_dict[custom_name].set(1)
    
    def _no_customization(self):
        '''PyDoc'''
        self.logger.info("Removing Customizations")
        for custom_name in self.customizable_checkbox_dict:
            self.customizable_checkbox_dict[custom_name].set(0)
    
    def _random_customization(self):
        '''PyDoc'''
        self.logger.info("Random Customization")
        if(self.hiding_customization):
            self.logger.info("Hiding Customization")
            for custom_name in self.customizable_checkbox_dict:
                self.customizable_checkbox_dict[custom_name].set(2)
            self.random_customization_button.configure(text='Random By Seed\nAnd Hide Options')
            for checkbutton_count, checkbutton in enumerate(self.customization_checkbuttons):
                checkbutton.grid(row=(checkbutton_count // 4) + 1, column=(checkbutton_count % 4), padx=self.padx, pady=self.pady, sticky='w')
            self.hiding_customization = False
        else:
            for custom_name in self.customizable_checkbox_dict:
                self.customizable_checkbox_dict[custom_name].set(randint(0, 1))
            self.logger.info("Re-Adding Customization")
            self.random_customization_button.configure(text='Show Customize\nCheckboxes')
            for checkbutton in self.customization_checkbuttons:
                checkbutton.grid_remove()
            self.hiding_customization = True
    
    def _default_starting_area(self):
        '''Selects a random starting area'''
        self.logger.info("Select Default Starting Area")
        self.new_area_var.set("SM - Main")
        self.skip_intro_cutscene_var.set(0)
    
    def _new_area_option(self, *args):
        '''If the starting area is not the default area, skip the intro cutscene'''
        self.logger.info("Selecting 'Skip Intro Cutscene'")
        if(self.new_area_var.get() != "SM - Main"):
            self.skip_intro_cutscene_var.set(1)
        if(self.new_area_var.get() == "Random Starting Area (Auto Have All Moves)"):
            self.all_starting_moves_var.set(1)
            self.all_starting_moves_checkbutton.configure(state='disabled')
        else:
            self.all_starting_moves_checkbutton.configure(state='normal')
    
    def _set_random_carry_capacities(self, *args):
        '''Select random capacities for blue eggs, red feathers, and gold feathers'''
        self.logger.info("Random Carry Capacities")
        self.before_blue_egg_carry_value.set("?")
        self.after_blue_egg_carry_value.set("?")
        self.before_red_feather_carry_value.set("?")
        self.after_red_feather_carry_value.set("?")
        self.before_gold_feather_carry_value.set("?")
        self.after_gold_feather_carry_value.set("?")
    
    def _display_map_file_description(self, *args):
        '''Pulls the description from a Models, Animations, Properties json file'''
        self.logger.info("Display Models, Animations, & Properties File Description")
        filename = self.customizable_var.get()
        file_path = f"{self.cwd}Randomization_Processes/Misc_Manipulation/Models_Animations_Properties/{filename}.json"
        if(filename == "None"):
            map_file_desc = "No Model/Animation/Properties file selected.\nSelect a preset to check its description!"
        elif(filename == "Random Preset"):
            map_file_desc = "Selects a random preset from the list!"
        elif(os.path.isfile(file_path)):
            try:
                property_dict = read_json(file_path)
            except Exception:
                Error_GUI(f"Error: Could not open JSON file.\nPlease check for proper formatting!")
                self.customizable_var.set("None")
                map_file_desc = "No Model/Animation/Properties file selected.\nSelect a preset to check its description!"
            if(("Description" in property_dict) and (property_dict["Description"])):
                map_file_desc = ""
                desc_len = len(property_dict["Description"])
                for line_num in range(desc_len):
                    map_file_desc += property_dict["Description"][str(line_num)]
                    if(line_num < (desc_len - 1)):
                        map_file_desc += "\n"
            else:
                map_file_desc = "This preset doesn't have a description?"
        else:
            map_file_desc = "Select a preset to check its description!"
        self.customizable_file_description.config(text=map_file_desc)
    
    def _lock_final_puzzle_value(self, *args):
        self.logger.info("Lock Final Puzzle Value")
        if(self.final_puzzle_var.get() == 0):
            self.final_puzzle_value.set("25")
            self.final_puzzle_entry.configure(state='disabled')
            self.remove_floating_jiggies_var.set(0)
            self.remove_floating_jiggies_checkbox.grid_remove()
        else:
            self.final_puzzle_entry.configure(state='normal')
            self.remove_floating_jiggies_checkbox.grid(row=3, column=3, padx=self.padx, pady=self.pady, sticky='w')
    
    def _lock_struct_options(self, *args):
        self.logger.info("Lock Struct Options")
        if(self.struct_var.get() == "None"):
            self.struct_note_count_var.set("Produce Extra Notes")
            self.struct_note_count_dropdown.grid_remove()
            self.note_overflow_var.set("Allow Save & Quit/Reset")
            self.note_overflow_dropdown.grid_remove()
        elif(self.struct_var.get() == "Shuffle (World)"):
            self.struct_note_count_var.set("Produce Extra Notes")
            self.struct_note_count_dropdown.grid_remove()
            self.note_overflow_var.set("Allow Save & Quit/Reset")
            self.note_overflow_dropdown.grid_remove()
        elif(self.struct_var.get() == "Shuffle (Game)"):
            self.struct_note_count_var.set("Produce Extra Notes")
            self.struct_note_count_dropdown.grid_remove()
            self.note_overflow_dropdown.grid(row=0, column=2, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        elif(self.struct_var.get() == "Randomize"):
            self.struct_note_count_dropdown.grid(row=1, column=2, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
            self.note_overflow_dropdown.grid(row=0, column=2, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        elif(self.struct_var.get() == "All Notes"):
            self.struct_note_count_var.set("Produce Extra Notes")
            self.struct_note_count_dropdown.grid_remove()
            self.note_overflow_var.set("Allow Save & Quit/Reset")
            self.note_overflow_dropdown.grid_remove()
    
    ################################
    ### RANDOMIZER SETTINGS CODE ###
    ################################
    
    def _randomizer_settings_int_to_char_translator(self):
        '''Translates the randomizer settings code from numeric to char'''
#         print(f"Randomizer Settings Generated Code: {self.randomizer_settings_code}")
        randomizer_settings_code = self.generated_randomizer_settings_code
        ascii_code = ""
        while(randomizer_settings_code > 0):
            curr_val = (randomizer_settings_code % 26) + 65
            ascii_code = chr(curr_val) + ascii_code
            randomizer_settings_code = randomizer_settings_code // 26
        self.randomizer_setting_code_value.set(ascii_code)
    
    def _add_randomizer_settings_to_code(self, add_val, counter_add=1):
        '''Adds the numerical value of a setting to the randomizer settings code'''
        self.generated_randomizer_settings_code += (int(add_val) << self.randomizer_settings_count)
        self.randomizer_settings_count += counter_add
    
    def _generate_randomizer_settings_code(self):
        '''Generates the randomizer settings code by turning all settings into numerical values'''
        self.logger.info("Generating Randomizer Settings Code")
        self.generated_randomizer_settings_code = 0
        self.randomizer_settings_count = 0
        ### General Settings ###
        # Flagged Objects
        self._add_randomizer_settings_to_code(["None", "Shuffle (World)", "Shuffle (Game)"].index(self.flagged_object_var.get()), 2)
        self._add_randomizer_settings_to_code(self.flagged_object_abnormalities_var.get())
        self._add_randomizer_settings_to_code(self.flagged_object_softlock_var.get())
        self._add_randomizer_settings_to_code(self.final_puzzle_var.get())
        if(self.final_puzzle_value.get() == "?"):
            self._add_randomizer_settings_to_code(100, 8)
        else:
            self._add_randomizer_settings_to_code(self.final_puzzle_value.get(), 8)
        self._add_randomizer_settings_to_code(["Base Game Costs", "World Order Scaled Costs", "Free Transformations"].index(self.free_transformations_var.get()), 2)
        self._add_randomizer_settings_to_code(self.one_health_banjo_var.get())
        self._add_randomizer_settings_to_code(self.remove_floating_jiggies_var.get())
        # Non-Flagged Objects
        self._add_randomizer_settings_to_code(["None", "Shuffle (World)"].index(self.non_flagged_object_var.get()))
        self._add_randomizer_settings_to_code(self.non_flagged_object_abnormalities_var.get())
        self._add_randomizer_settings_to_code(self.starting_lives_value.get(), 8)
        # Structs
        self._add_randomizer_settings_to_code(["None", "Shuffle (World)", "Shuffle (Game)", "Randomize", "All Notes"].index(self.struct_var.get()), 3)
        self._add_randomizer_settings_to_code(["Allow Save & Quit/Reset", "Possible No Save & Quit/Reset"].index(self.note_overflow_var.get()))
        self._add_randomizer_settings_to_code(["Produce Extra Notes", "Produce Exactly Enough Notes"].index(self.struct_note_count_var.get()))
        self._add_randomizer_settings_to_code(["Scaling Note Doors", "Final Note Door Only"].index(self.final_note_door_var.get()))
        if(self.final_note_door_value.get() == "?"):
            self._add_randomizer_settings_to_code(2001, 11)
        else:
            self._add_randomizer_settings_to_code(self.final_note_door_value.get(), 11)
        if(self.before_blue_egg_carry_value.get() == "?"):
            self._add_randomizer_settings_to_code(256, 9)
        else:
            self._add_randomizer_settings_to_code(self.before_blue_egg_carry_value.get(), 9)
        if(self.before_blue_egg_carry_value.get() == "?"):
            self._add_randomizer_settings_to_code(256, 9)
        else:
            self._add_randomizer_settings_to_code(self.after_blue_egg_carry_value.get(), 9)
        if(self.before_blue_egg_carry_value.get() == "?"):
            self._add_randomizer_settings_to_code(256, 9)
        else:
            self._add_randomizer_settings_to_code(self.before_red_feather_carry_value.get(), 9)
        if(self.before_blue_egg_carry_value.get() == "?"):
            self._add_randomizer_settings_to_code(256, 9)
        else:
            self._add_randomizer_settings_to_code(self.after_red_feather_carry_value.get(), 9)
        if(self.before_blue_egg_carry_value.get() == "?"):
            self._add_randomizer_settings_to_code(256, 9)
        else:
            self._add_randomizer_settings_to_code(self.before_gold_feather_carry_value.get(), 9)
        if(self.before_blue_egg_carry_value.get() == "?"):
            self._add_randomizer_settings_to_code(256, 9)
        else:
            self._add_randomizer_settings_to_code(self.after_gold_feather_carry_value.get(), 9)
        # World Entrances
        self._add_randomizer_settings_to_code(["None", "Basic Shuffle", "Bottles Shuffle"].index(self.world_entrance_var.get()), 2)
        self._add_randomizer_settings_to_code(["Exit From World You Were Just In", "Exit From Entrance You Entered From"].index(self.world_exit_var.get()))
        self._add_randomizer_settings_to_code(self.all_starting_moves_var.get())
        # Within World Warps
        self._add_randomizer_settings_to_code(["None", "Shuffle By World", "Shuffle By Game"].index(self.within_world_warps_var.get()), 2)
        # Starting World
        starting_world_options = [option for option in start_level_ids]
        starting_world_options.insert(0, "Random Starting Area (Auto Have All Moves)")
        self._add_randomizer_settings_to_code(starting_world_options.index(self.new_area_var.get()), 8)
        self._add_randomizer_settings_to_code(self.skip_intro_cutscene_var.get())
        # Enemies
        self._add_randomizer_settings_to_code(["None", "Shuffle", "Randomize"].index(self.enemies_var.get()), 2)
        for enemy_name in sorted(self.enemy_checkbox_dict):
            self._add_randomizer_settings_to_code(self.enemy_checkbox_dict[enemy_name].get())
        ### Aesthetic Settings ###
        # Models, Animations, Properties
        for custom_name in sorted(self.customizable_checkbox_dict):
            self._add_randomizer_settings_to_code(self.customizable_checkbox_dict[custom_name].get())
        ### World Specific ###
        # Gruntilda's Lair
        self._add_randomizer_settings_to_code(self.skip_furnace_fun_var.get())
        self._add_randomizer_settings_to_code(self.remove_magic_barriers_var.get())
        self._add_randomizer_settings_to_code(self.gruntilda_difficulty_var.get(), 2)
        self._add_randomizer_settings_to_code(self.monster_house_var.get())
        self._add_randomizer_settings_to_code(self.what_floor_var.get())
        self._add_randomizer_settings_to_code(self.grunty_size_var.get())
        # Mumbo's Mountain
        self._add_randomizer_settings_to_code(self.flowers_var.get())
        # Treasure Trove Cove
        self._add_randomizer_settings_to_code(self.scattered_structs_var.get())
        self._add_randomizer_settings_to_code(self.super_slippery_ttc_var.get())
        # Clanker's Cavern
        self._add_randomizer_settings_to_code(self.hard_rings_var.get())
        # Bubblegloop Swamp
        self._add_randomizer_settings_to_code(self.croctus_var.get())
        self._add_randomizer_settings_to_code(self.mr_vile_var.get())
        self._add_randomizer_settings_to_code(self.tiptup_choir_var.get())
        # Freezeezy Peak
        self._add_randomizer_settings_to_code(self.hard_races_var.get())
        # Gobi's Valley
        self._add_randomizer_settings_to_code(self.ancient_ones_var.get())
        self._add_randomizer_settings_to_code(self.maze_jinxy_heads_var.get())
        self._add_randomizer_settings_to_code(self.matching_puzzle_var.get())
        # Mad Monster Mansion
        self._add_randomizer_settings_to_code(self.lit_pots_var.get())
        self._add_randomizer_settings_to_code(self.motzand_keys_var.get())
        # Rusty Bucket Bay
        self._add_randomizer_settings_to_code(self.buttons_var.get())
        # Click Clock Wood
        self._add_randomizer_settings_to_code(["Season", "Within World"].index(self.ccw_var.get()))
        self._randomizer_settings_int_to_char_translator()
#         print(f"Code: {self.generated_randomizer_settings_code}")
    
    def _randomizer_settings_char_to_int_translator(self):
        '''Translates the randomizer settings code from char to numeric'''
        ascii_code = self.randomizer_setting_code_value.get()
        randomizer_settings_code = 0
        for char_count, char_value in enumerate(reversed(ascii_code)):
            randomizer_settings_code += (ord(char_value) - 65) * (26 ** char_count)
        return randomizer_settings_code
#         print(f"Randomizer Settings Applied Code:   {self.randomizer_settings_code}")
    
    def _get_randomizer_setting(self, bit_count=1, options_list=None):
        '''Generates the randomizer settings code'''
        compare_to_value = (2 ** bit_count) - 1
        set_this_option = self.applied_randomizer_settings_code & compare_to_value
        self.applied_randomizer_settings_code = self.applied_randomizer_settings_code >> bit_count
        if(options_list):
            return options_list[set_this_option]
        else:
            return set_this_option
    
    def _apply_randomizer_settings_code(self):
        '''Applies settings based on the randomizer settings code provided'''
        self.logger.info("Apply Randomizer Settings Code")
        try:
            self.applied_randomizer_settings_code = self._randomizer_settings_char_to_int_translator()
            self._randomizer_settings_char_to_int_translator()
            ### General Settings ###
            # Flagged Objects
            self.flagged_object_var.set(self._get_randomizer_setting(bit_count=2, options_list=["None", "Shuffle (World)", "Shuffle (Game)"]))
            self.flagged_object_abnormalities_var.set(self._get_randomizer_setting())
            self.flagged_object_softlock_var.set(self._get_randomizer_setting())
            self.final_puzzle_var.set(self._get_randomizer_setting())
            final_puzzle_value = self._get_randomizer_setting(bit_count=8)
            if(final_puzzle_value == 100):
                self.final_puzzle_value.set("?")
            else:
                self.final_puzzle_value.set(str(final_puzzle_value))
            self.free_transformations_var.set(self._get_randomizer_setting(bit_count=2, options_list=["Base Game Costs", "World Order Scaled Costs", "Free Transformations"]))
            self.one_health_banjo_var.set(self._get_randomizer_setting())
            self.remove_floating_jiggies_var.set(self._get_randomizer_setting())
            # Non-Flagged Objects
            self.non_flagged_object_var.set(self._get_randomizer_setting(options_list=["None", "Shuffle (World)"]))
            self.non_flagged_object_abnormalities_var.set(self._get_randomizer_setting())
            self.starting_lives_value.set(self._get_randomizer_setting(bit_count=8))
            # Structs
            self.struct_var.set(self._get_randomizer_setting(bit_count=3, options_list=["None", "Shuffle (World)", "Shuffle (Game)", "Randomize", "All Notes"]))
            self.note_overflow_var.set(self._get_randomizer_setting(options_list=["Allow Save & Quit/Reset", "Possible No Save & Quit/Reset"]))
            self.struct_note_count_var.set(self._get_randomizer_setting(options_list=["Produce Extra Notes", "Produce Exactly Enough Notes"]))
            self.final_note_door_var.set(self._get_randomizer_setting(options_list=["Scaling Note Doors", "Final Note Door Only"]))
            final_note_door_value = self._get_randomizer_setting(bit_count=11)
            if(final_note_door_value == 2001):
                self.final_note_door_value.set("?")
            else:
                self.final_note_door_value.set(str(final_note_door_value))
            # Carrying Capacities
            before_blue_egg_carry_value = self._get_randomizer_setting(bit_count=9)
            if(before_blue_egg_carry_value == 256):
                self.before_blue_egg_carry_value.set("?")
            else:
                self.before_blue_egg_carry_value.set(str(before_blue_egg_carry_value))
            after_blue_egg_carry_value = self._get_randomizer_setting(bit_count=9)
            if(after_blue_egg_carry_value == 256):
                self.after_blue_egg_carry_value.set("?")
            else:
                self.after_blue_egg_carry_value.set(str(after_blue_egg_carry_value))
            before_red_feather_carry_value = self._get_randomizer_setting(bit_count=9)
            if(before_red_feather_carry_value == 256):
                self.before_red_feather_carry_value.set("?")
            else:
                self.before_red_feather_carry_value.set(str(before_red_feather_carry_value))
            after_red_feather_carry_value = self._get_randomizer_setting(bit_count=9)
            if(after_red_feather_carry_value == 256):
                self.after_red_feather_carry_value.set("?")
            else:
                self.after_red_feather_carry_value.set(str(after_red_feather_carry_value))
            before_gold_feather_carry_value = self._get_randomizer_setting(bit_count=9)
            if(before_gold_feather_carry_value == 256):
                self.before_gold_feather_carry_value.set("?")
            else:
                self.before_gold_feather_carry_value.set(str(before_gold_feather_carry_value))
            after_gold_feather_carry_value = self._get_randomizer_setting(bit_count=9)
            if(after_gold_feather_carry_value == 256):
                self.after_gold_feather_carry_value.set("?")
            else:
                self.after_gold_feather_carry_value.set(str(after_gold_feather_carry_value))
            # World Entrances
            self.world_entrance_var.set(self._get_randomizer_setting(bit_count=2, options_list=["None", "Basic Shuffle", "Bottles Shuffle"]))
            self.world_exit_var.set(self._get_randomizer_setting(options_list=["Exit From World You Were Just In", "Exit From Entrance You Entered From"]))
            self.all_starting_moves_var.set(self._get_randomizer_setting())
            # Within World Warps
            self.within_world_warps_var.set(self._get_randomizer_setting(bit_count=2, options_list=["None", "Shuffle By World", "Shuffle By Game"]))
            # Starting World
            starting_world_options = [option for option in start_level_ids]
            starting_world_options.insert(0, "Random Starting Area (Auto Have All Moves)")
            self.new_area_var.set(self._get_randomizer_setting(bit_count=8, options_list=starting_world_options))
            self.skip_intro_cutscene_var.set(self._get_randomizer_setting())
            # Enemies
            self.enemies_var.set(self._get_randomizer_setting(bit_count=2, options_list=["None", "Shuffle", "Randomize"]))
            for enemy_name in sorted(self.enemy_checkbox_dict):
                self.enemy_checkbox_dict[enemy_name].set(self._get_randomizer_setting())
            ### Aesthetic Settings ###
            for custom_name in sorted(self.customizable_checkbox_dict):
                self.customizable_checkbox_dict[custom_name].set(self._get_randomizer_setting())
            ### World Specific ###
            # Gruntilda's Lair
            self.skip_furnace_fun_var.set(self._get_randomizer_setting())
            self.remove_magic_barriers_var.set(self._get_randomizer_setting())
            self.gruntilda_difficulty_var.set(self._get_randomizer_setting(bit_count=2))
            self.monster_house_var.set(self._get_randomizer_setting())
            self.what_floor_var.set(self._get_randomizer_setting())
            self.grunty_size_var.set(self._get_randomizer_setting())
            # Mumbo's Mountain
            self.flowers_var.set(self._get_randomizer_setting())
            # Treasure Trove Cove
            self.scattered_structs_var.set(self._get_randomizer_setting())
            self.super_slippery_ttc_var.set(self._get_randomizer_setting())
            # Clanker's Cavern
            self.hard_rings_var.set(self._get_randomizer_setting())
            # Bubblegloop Swamp
            self.croctus_var.set(self._get_randomizer_setting())
            self.mr_vile_var.set(self._get_randomizer_setting())
            self.tiptup_choir_var.set(self._get_randomizer_setting())
            # Freezeezy Peak
            self.hard_races_var.set(self._get_randomizer_setting())
            # Gobi's Valley
            self.ancient_ones_var.set(self._get_randomizer_setting())
            self.maze_jinxy_heads_var.set(self._get_randomizer_setting())
            self.matching_puzzle_var.set(self._get_randomizer_setting())
            # Mad Monster Mansion
            self.lit_pots_var.set(self._get_randomizer_setting())
            self.motzand_keys_var.set(self._get_randomizer_setting())
            # Rusty Bucket Bay
            self.buttons_var.set(self._get_randomizer_setting())
            # Click Clock Wood
            self.ccw_var.set(self._get_randomizer_setting(options_list=["Season", "Within World"]))
        except IndexError:
            Error_GUI(f"Error: Something went wrong with applying the settings.\nPlease check your settings code.")
    
    ######################
    ### SETTING VALUES ###
    ######################
    
    def _set_recommended_defaults(self):
        '''Sets the recommended defaults for first time users or when an error occurs with a loaded json file'''
        self.logger.info("Set Recommended Defaults")
        ### ROM and Seed ###
        # ROM
        self.rom_file_entry.set("")
        # Seed
        self.seed_value.set("")
        ### General Settings ###
        # Flagged Objects
        self.flagged_object_var.set("Shuffle (World)")
        self.flagged_object_abnormalities_var.set(0)
        self.flagged_object_softlock_var.set(0)
        self.final_puzzle_var.set(0)
        self.final_puzzle_value.set(25)
        self.free_transformations_var.set("Base Game Costs")
        self.one_health_banjo_var.set(0)
        self.remove_floating_jiggies_var.set(0)
        # Non-Flagged Objects
        self.non_flagged_object_var.set("Shuffle (World)")
        self.non_flagged_object_abnormalities_var.set(0)
        self.starting_lives_value.set(3)
        # Structs
        self.struct_var.set("Shuffle (World)")
        self.note_overflow_var.set("Allow Save & Quit/Reset")
        self.struct_note_count_var.set("Produce Extra Notes")
        self.final_note_door_var.set("Scaling Note Doors")
        self.final_note_door_value.set(810)
        self.before_blue_egg_carry_value.set(100)
        self.after_blue_egg_carry_value.set(200)
        self.before_red_feather_carry_value.set(50)
        self.after_red_feather_carry_value.set(100)
        self.before_gold_feather_carry_value.set(10)
        self.after_gold_feather_carry_value.set(20)
        # World Entrances
        self.world_entrance_var.set("Basic Shuffle")
        self.world_exit_var.set("Exit From World You Were Just In")
        self.all_starting_moves_var.set(0)
        # Within World Warps
        self.within_world_warps_var.set("Shuffle By World")
        # Starting Area
        self.new_area_var.set("SM - Main")
        self.skip_intro_cutscene_var.set(0)
#         self.load_area_var.set("GL - MM Puzzle/Entrance Room")
        # Enemies
        self.enemies_var.set("Randomize")
        for enemy_name in self.enemy_checkbox_dict:
            if("*" in enemy_name):
                self.enemy_checkbox_dict[enemy_name].set(0)
            else:
                self.enemy_checkbox_dict[enemy_name].set(1)
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
        # Models, Animations, Properties
        for custom_name in self.customizable_checkbox_dict:
            self.customizable_checkbox_dict[custom_name].set(0)
        # Sounds/Music
        self.short_sounds_var.set(0)
        self.jingles_var.set(0)
        self.music_var.set(0)
        self.beta_sounds_var.set(0)
        self.jarring_sounds_var.set(0)
        # Sprites/Textures
        self.skybox_var.set(0)
        self.talking_sprite_var.set(0)
        ### Misc Settings ###
        self.remove_files_var.set(1)
        self.tool_tips_var.set(1)
        ### World Specific ###
        # Gruntilda's Lair
        self.skip_furnace_fun_var.set(0)
        self.remove_magic_barriers_var.set(0)
        self.gruntilda_difficulty_var.set(0)
        self.monster_house_var.set(1)
        self.what_floor_var.set(1)
        self.grunty_size_var.set(1)
        # Mumbo's Mountain
        self.flowers_var.set(0)
        # Treasure Trove Cove
        self.scattered_structs_var.set(0)
        self.super_slippery_ttc_var.set(0)
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
        self.motzand_keys_var.set(0)
        # Rusty Bucket Bay
        self.buttons_var.set(0)
        # Click Clock Wood
        self.ccw_var.set("Season")
    
    def _load_configuration(self, button_press=True, random_file=False):
        '''Opens a chosen JSON file and sets the parameters to match those'''
        self.logger.info("Load Configuration")
        setting_not_found = []
        if(random_file):
            try:
                list_of_files = os.listdir(f"{self.cwd}Configurations/")
                if("Last_Used_Configuration.json" in list_of_files):
                    list_of_files.remove("Last_Used_Configuration.json")
                list_of_configs = [file for file in list_of_files if(file.endswith(".json"))]
                filename = f"{self.cwd}Configurations/{choice(list_of_configs)}"
                with open(filename, "r") as json_file:
                    json_data = json.load(json_file)
            except FileNotFoundError:
                Error_GUI("Error: File Not Found?!\nLeaving Settings As They Are.")
                return
            except Exception:
                Error_GUI("Error Occurred During Random Configuration.\nLeaving Settings As They Are.")
                return
        elif(button_press):
            try:
                config_default_dir = f"{self.cwd}Configurations/"
                filename = tkinter.filedialog.askopenfilename(initialdir=config_default_dir, title="Select A JSON Config File", filetypes =(("Json Files","*.json"),("all files","*.*")))
                with open(filename, "r") as json_file:
                    json_data = json.load(json_file)
            except FileNotFoundError:
                Error_GUI("JSON File Was Not Found Or Operation Was Canceled.\nLeaving The Settings As They Are.")
                return
            except Exception:
                Error_GUI("Error Occurred During Random Configuration.\nLeaving The Settings As They Are.")
                return
        else:
            try:
                filename = f"{self.cwd}Configurations/Last_Used_Configuration.json"
                with open(filename, "r") as json_file:
                    json_data = json.load(json_file)
            except FileNotFoundError:
                self._set_recommended_defaults()
                Error_GUI("Last Used Configuration File Not Found.\nImplementing The Default Settings!")
                return
            except Exception:
                Error_GUI("Error Occurred During Random Configuration.\nLeaving Settings As They Are.")
                return
        ### ROM and Seed ###
        # ROM
        if(json_data["ROM_File"] != ""):
            self.rom_file_entry.set(json_data["ROM_File"])
        # Seed
        try:
            self.seed_value.set(json_data["Seed"])
        except KeyError:
            setting_not_found.append("Seed")
            self.seed_value.set("")
        ### General Settings ###
        # Flagged Objects
        try:
            self.flagged_object_var.set(json_data["Flagged_Objects_Option"])
        except KeyError:
            setting_not_found.append("Flagged_Objects_Option")
            self.flagged_object_var.set("Shuffle (World)")
        try:
            self.flagged_object_abnormalities_var.set(json_data["Flagged_Objects_Abnormalities"])
        except KeyError:
            setting_not_found.append("Flagged_Objects_Abnormalities")
            self.flagged_object_abnormalities_var.set(0)
        try:
            self.flagged_object_softlock_var.set(json_data["Flagged_Objects_Softlock"])
        except KeyError:
            setting_not_found.append("Flagged_Objects_Softlock")
            self.flagged_object_softlock_var.set(0)
        try:
            self.final_puzzle_var.set(json_data["Final_Puzzle"])
        except KeyError:
            setting_not_found.append("Final_Puzzle")
            self.final_puzzle_var.set(0)
        try:
            self.final_puzzle_value.set(json_data["Final_Puzzle_Value"])
        except KeyError:
            setting_not_found.append("Final_Puzzle_Value")
            self.final_puzzle_value.set(25)
        try:
            self.free_transformations_var.set(json_data["Free_Transformations"])
        except KeyError:
            setting_not_found.append("Free_Transformations")
            self.free_transformations_var.set("Base Game Costs")
        try:
            self.one_health_banjo_var.set(json_data["One_Health_Only"])
        except KeyError:
            setting_not_found.append("One_Health_Only")
            self.one_health_banjo_var.set(0)
        try:
            self.remove_floating_jiggies_var.set(json_data["Remove_Floating_Jiggies"])
        except Exception:
            setting_not_found.append("Remove_Floating_Jiggies")
            self.remove_floating_jiggies_var.set(0)
        # Non-Flagged Objects
        try:
            self.non_flagged_object_var.set(json_data["Non_Flagged_Objects_Option"])
        except KeyError:
            setting_not_found.append("Non_Flagged_Objects_Option")
            self.non_flagged_object_var.set("Shuffle (World)")
        try:
            self.non_flagged_object_abnormalities_var.set(json_data["Non_Flagged_Objects_Abnormalities"])
        except KeyError:
            setting_not_found.append("Non_Flagged_Objects_Abnormalities")
            self.non_flagged_object_abnormalities_var.set(0)
        try:
            self.starting_lives_value.set(json_data["Starting_Lives"])
        except KeyError:
            setting_not_found.append("Starting_Lives")
            self.starting_lives_value.set(3)
        # Structs
        try:
            self.struct_var.set(json_data["Struct_Option"])
        except KeyError:
            setting_not_found.append("Struct_Option")
            self.struct_var.set("Shuffle (World)")
        try:
            self.note_overflow_var.set(json_data["Note_Overflow"])
        except KeyError:
            setting_not_found.append("Note_Overflow")
            self.note_overflow_var.set("Allow Save & Quit/Reset")
        try:
            self.struct_note_count_var.set(json_data["Struct_Note_Count"])
        except KeyError:
            setting_not_found.append("Struct_Note_Count")
            self.struct_note_count_var.set("Produce Extra Notes")
        try:
            self.final_note_door_var.set(json_data["Final_Note_Door"])
        except KeyError:
            setting_not_found.append("Final_Note_Door")
            self.final_note_door_var.set("Scaling Note Doors")
        try:
            self.final_note_door_value.set(json_data["Final_Note_Door_Value"])
        except KeyError:
            setting_not_found.append("Final_Note_Door_Value")
            self.final_note_door_value.set(810)
        try:
            self.before_blue_egg_carry_value.set(json_data["Before_Cheato_Blue_Eggs"])
        except KeyError:
            setting_not_found.append("Before_Cheato_Blue_Eggs")
            self.before_blue_egg_carry_value.set(100)
        try:
            self.after_blue_egg_carry_value.set(json_data["After_Cheato_Blue_Eggs"])
        except KeyError:
            setting_not_found.append("After_Cheato_Blue_Eggs")
            self.after_blue_egg_carry_value.set(200)
        try:
            self.before_red_feather_carry_value.set(json_data["Before_Cheato_Red_Feathers"])
        except KeyError:
            setting_not_found.append("Before_Cheato_Red_Feathers")
            self.before_red_feather_carry_value.set(50)
        try:
            self.after_red_feather_carry_value.set(json_data["After_Cheato_Red_Feathers"])
        except KeyError:
            setting_not_found.append("After_Cheato_Red_Feathers")
            self.after_red_feather_carry_value.set(100)
        try:
            self.before_gold_feather_carry_value.set(json_data["Before_Cheato_Gold_Feathers"])
        except KeyError:
            setting_not_found.append("Before_Cheato_Gold_Feathers")
            self.before_gold_feather_carry_value.set(10)
        try:
            self.after_gold_feather_carry_value.set(json_data["After_Cheato_Gold_Feathers"])
        except KeyError:
            setting_not_found.append("After_Cheato_Gold_Feathers")
            self.after_gold_feather_carry_value.set(20)
        # World Entrances
        try:
            self.world_entrance_var.set(json_data["World_Entrance_Option"])
        except KeyError:
            setting_not_found.append("World_Entrance_Option")
            self.world_entrance_var.set("Basic Shuffle")
        try:
            self.world_exit_var.set(json_data["World_Exit"])
        except KeyError:
            setting_not_found.append("World_Exit")
            self.world_exit_var.set("Exit From World You Were Just In")
        try:
            self.all_starting_moves_var.set(json_data["All_Moves"])
        except KeyError:
            setting_not_found.append("All_Moves")
            self.all_starting_moves_var.set(0)
        # Within World Warps
        try:
            self.within_world_warps_var.set(json_data["Within_World_Warps_Option"])
        except KeyError:
            setting_not_found.append("Within_World_Warps_Option")
            self.within_world_warps_var.set("Shuffle By World")
        # Starting World
        try:
            self.new_area_var.set(json_data["Starting_Area"])
        except KeyError:
            setting_not_found.append("Starting_Area")
            self.new_area_var.set("SM - Main")
        try:
            self.skip_intro_cutscene_var.set(json_data["Skip_Intro_Cutscene"])
        except KeyError:
            setting_not_found.append("Skip_Intro_Cutscene")
            self.skip_intro_cutscene_var.set(0)
        # Enemies
        try:
            self.enemies_var.set(json_data["Enemies_Option"])
        except KeyError:
            setting_not_found.append("Enemies_Option")
            self.enemies_var.set("Randomize")
        for enemy_name in self.enemy_checkbox_dict:
            try:
                self.enemy_checkbox_dict[enemy_name].set(json_data[f"Include {enemy_name}"])
            except KeyError:
                setting_not_found.append(f"Include {enemy_name}")
                for enemy_name in self.enemy_checkbox_dict:
                    if("*" in enemy_name):
                        self.enemy_checkbox_dict[enemy_name].set(0)
                    else:
                        self.enemy_checkbox_dict[enemy_name].set(1)
        ### Aesthetic Settings ###
        # BK Model
        try:
            self.bk_model_var.set(json_data["BK_Model_Option"])
        except KeyError:
            setting_not_found.append("BK_Model_Option")
            self.bk_model_var.set("Default")
        try:
            self.banjo_fur_var.set(json_data["Banjo_Fur"])
        except KeyError:
            setting_not_found.append("Banjo_Fur")
            self.banjo_fur_var.set(self.bk_model_json[self.bk_model_var.get()]["Banjo_Fur"])
        try:
            self.tooth_necklace_var.set(json_data["Tooth_Necklace"])
        except KeyError:
            setting_not_found.append("Tooth_Necklace")
            self.tooth_necklace_var.set(self.bk_model_json[self.bk_model_var.get()]["Tooth_Necklace"])
        try:
            self.banjo_skin_var.set(json_data["Banjo_Skin"])
        except KeyError:
            setting_not_found.append("Banjo_Skin")
            self.banjo_skin_var.set(self.bk_model_json[self.bk_model_var.get()]["Banjo_Skin"])
        try:
            self.banjo_feet_var.set(json_data["Banjo_Feet"])
        except KeyError:
            setting_not_found.append("Banjo_Feet")
            self.banjo_feet_var.set(self.bk_model_json[self.bk_model_var.get()]["Banjo_Feet"])
        try:
            self.kazooie_primary_var.set(json_data["Kazooie_Primary"])
        except KeyError:
            setting_not_found.append("Kazooie_Primary")
            self.kazooie_primary_var.set(self.bk_model_json[self.bk_model_var.get()]["Kazooie_Primary"])
        try:
            self.kazooie_secondary_var.set(json_data["Kazooie_Secondary"])
        except KeyError:
            setting_not_found.append("Kazooie_Secondary")
            self.kazooie_secondary_var.set(self.bk_model_json[self.bk_model_var.get()]["Kazooie_Secondary"])
        try:
            self.kazooie_wing_primary_var.set(json_data["Kazooie_Wing_Primary"])
        except KeyError:
            setting_not_found.append("Kazooie_Wing_Primary")
            self.kazooie_wing_primary_var.set(self.bk_model_json[self.bk_model_var.get()]["Kazooie_Wing_Primary"])
        try:
            self.kazooie_wing_secondary_var.set(json_data["Kazooie_Wing_Secondary"])
        except KeyError:
            setting_not_found.append("Kazooie_Wing_Secondary")
            self.kazooie_wing_secondary_var.set(self.bk_model_json[self.bk_model_var.get()]["Kazooie_Wing_Secondary"])
        try:
            self.backpack_var.set(json_data["Backpack"])
        except KeyError:
            setting_not_found.append("Backpack")
            self.backpack_var.set(self.bk_model_json[self.bk_model_var.get()]["Backpack"])
        try:
            self.wading_boots_var.set(json_data["Wading_Boots"])
        except KeyError:
            setting_not_found.append("Wading_Boots")
            self.wading_boots_var.set(self.bk_model_json[self.bk_model_var.get()]["Wading_Boots"])
        try:
            self.shorts_vertex_var.set(json_data["Shorts_Vertex"])
        except KeyError:
            setting_not_found.append("Shorts_Vertex")
            self.shorts_vertex_var.set(self.bk_model_json[self.bk_model_var.get()]["Shorts_Vertex"])
        try:
            self.shorts_texture_var.set(json_data["Shorts_Texture"])
        except KeyError:
            setting_not_found.append("Shorts_Texture")
            self.shorts_texture_var.set(self.bk_model_json[self.bk_model_var.get()]["Shorts_Texture"])
        # Enemy Models
        for custom_name in self.customizable_checkbox_dict:
            try:
                self.customizable_checkbox_dict[custom_name].set(json_data[f"Include {custom_name}"])
            except KeyError:
                setting_not_found.append(f"Include {custom_name}")
                self.customizable_checkbox_dict[custom_name].set(0)
        # Sounds/Music
        try:
            self.short_sounds_var.set(json_data["Short_Sound_Option"])
        except KeyError:
            setting_not_found.append("Short_Sound_Option")
            self.short_sounds_var.set(0)
        try:
            self.jingles_var.set(json_data["Jingle_Option"])
        except KeyError:
            setting_not_found.append("Jingle_Option")
            self.jingles_var.set(0)
        try:
            self.music_var.set(json_data["Music_Option"])
        except KeyError:
            setting_not_found.append("Music_Option")
            self.music_var.set(0)
        try:
            self.beta_sounds_var.set(json_data["Beta_Sounds"])
        except KeyError:
            setting_not_found.append("Beta_Sounds")
            self.beta_sounds_var.set(0)
        try:
            self.jarring_sounds_var.set(json_data["Jarring_Sounds"])
        except KeyError:
            setting_not_found.append("Jarring_Sounds")
            self.jarring_sounds_var.set(0)
        # Sprites/Textures
        try:
            self.skybox_var.set(json_data["Skybox_Option"])
        except KeyError:
            setting_not_found.append("Skybox_Option")
            self.skybox_var.set(0)
        try:
            self.talking_sprite_var.set(json_data["Talking_Sprite_Option"])
        except KeyError:
            setting_not_found.append("Talking_Sprite_Option")
            self.talking_sprite_var.set(0)
        ### Misc Settings ###
        try:
            self.remove_files_var.set(json_data["Remove_Files"])
        except KeyError:
            setting_not_found.append("Remove_Files")
            self.remove_files_var.set(1)
        try:
            self.tool_tips_var.set(json_data["Tool_Tips"])
        except KeyError:
            setting_not_found.append("Tool_Tips")
            self.tool_tips_var.set(1)
        ### World Specific ###
        # Gruntilda's Lair
        try:
            self.skip_furnace_fun_var.set(json_data["Furnace_Fun_Skip"])
        except KeyError:
            setting_not_found.append("Furnace_Fun_Skip")
            self.skip_furnace_fun_var.set(0)
        try:
            self.remove_magic_barriers_var.set(json_data["Remove_Magic_Barriers"])
        except KeyError:
            setting_not_found.append("Remove_Magic_Barriers")
            self.remove_magic_barriers_var.set(0)
        try:
            self.gruntilda_difficulty_var.set(json_data["Final_Battle_Difficulty"])
        except KeyError:
            setting_not_found.append("Final_Battle_Difficulty")
            self.gruntilda_difficulty_var.set(0)
        try:
            self.monster_house_var.set(json_data["Monster_House"])
        except KeyError:
            setting_not_found.append("Monster_House")
            self.monster_house_var.set(1)
        try:
            self.what_floor_var.set(json_data["What_Floor"])
        except KeyError:
            setting_not_found.append("What_Floor")
            self.what_floor_var.set(1)
        try:
            self.grunty_size_var.set(json_data["Mini_Me"])
        except KeyError:
            setting_not_found.append("Mini_Me")
            self.grunty_size_var.set(1)
        # Mumbo's Mountain
        try:
            self.flowers_var.set(json_data["MM_Flowers"])
        except KeyError:
            setting_not_found.append("MM_Flowers")
            self.flowers_var.set(0)
        # Treasure Trove Cove
        try:
            self.scattered_structs_var.set(json_data["Scattered_Notes_Eggs_Feathers"])
        except KeyError:
            setting_not_found.append("Scattered_Notes_Eggs_Feathers")
            self.scattered_structs_var.set(0)
        try:
            self.super_slippery_ttc_var.set(json_data["Super_Slippery_Sand"])
        except KeyError:
            setting_not_found.append("Super_Slippery_Sand")
            self.super_slippery_ttc_var.set(0)
        # Clanker's Cavern
        try:
            self.hard_rings_var.set(json_data["CC_Hard_Rings"])
        except KeyError:
            setting_not_found.append("CC_Hard_Rings")
            self.hard_rings_var.set(0)
        # Bubblegloop Swamp
        try:
            self.croctus_var.set(json_data["BGS_Croctus"])
        except KeyError:
            setting_not_found.append("BGS_Croctus")
            self.croctus_var.set(0)
        try:
            self.mr_vile_var.set(json_data["BGS_Mr_Vile"])
        except KeyError:
            setting_not_found.append("BGS_Mr_Vile")
            self.mr_vile_var.set(0)
        try:
            self.tiptup_choir_var.set(json_data["BGS_Tiptup_Choir"])
        except KeyError:
            setting_not_found.append("BGS_Tiptup_Choir")
            self.tiptup_choir_var.set(0)
        # Freezeezy Peak
        try:
            self.hard_races_var.set(json_data["FP_Hard_Races"])
        except KeyError:
            setting_not_found.append("FP_Hard_Races")
            self.hard_races_var.set(0)
        # Gobi's Valley
        try:
            self.ancient_ones_var.set(json_data["GV_Ancient_Ones"])
        except KeyError:
            setting_not_found.append("GV_Ancient_Ones")
            self.ancient_ones_var.set(0)
        try:
            self.maze_jinxy_heads_var.set(json_data["GV_Maze_Jinxy_Heads"])
        except KeyError:
            setting_not_found.append("GV_Maze_Jinxy_Heads")
            self.maze_jinxy_heads_var.set(0)
        try:
            self.matching_puzzle_var.set(json_data["GV_Matching_Puzzle"])
        except KeyError:
            setting_not_found.append("GV_Matching_Puzzle")
            self.matching_puzzle_var.set(0)
        # Mad Monster Mansion
        try:
            self.lit_pots_var.set(json_data["MMM_Lit_Pots"])
        except KeyError:
            setting_not_found.append("MMM_Lit_Pots")
            self.lit_pots_var.set(0)
        try:
            self.motzand_keys_var.set(json_data["Motzand_Keys"])
        except KeyError:
            setting_not_found.append("Motzand_Keys")
            self.motzand_keys_var.set(0)
        # Rusty Bucket Bay
        try:
            self.buttons_var.set(json_data["RBB_Buttons"])
        except KeyError:
            setting_not_found.append("RBB_Buttons")
            self.buttons_var.set(0)
        # Click Clock Wood
        try:
            self.ccw_var.set(json_data["CCW_Option"])
        except KeyError:
            setting_not_found.append("CCW_Option")
            self.ccw_var.set("Season")
        if(setting_not_found):
            if(len(setting_not_found) < 6):
                error_msg = "Error: The Following Settings Weren't Set!\n"
                for error in setting_not_found:
                    error_msg += error + "\n"
                error_msg += "Please manually set those settings."
                Error_GUI(error_msg)
            else:
                Error_GUI(f"Error: {len(setting_not_found)} Settings Weren't Set!\nPlease manually set your settings.")
            return
    
    def _set_random_settings(self):
        '''Opens a chosen JSON file and sets the parameters to match those'''
        self.logger.info("Set Random Settings")
        ### ROM and Seed ###
        # ROM
#         self.rom_file_entry.set()
        # Seed
        self.seed_value.set(randint(10000000, 19940303))
        ### General Settings ###
        # Flagged Objects
        self.flagged_object_var.set(choice(["None", "Shuffle (World)", "Shuffle (Game)"]))
        self.flagged_object_abnormalities_var.set(randint(0, 1))
        self.flagged_object_softlock_var.set(randint(0, 1))
        self.final_puzzle_var.set(randint(0, 1))
        if(self.final_puzzle_var.get() == 1):
            self.final_puzzle_value.set(randint(0, 99))
        else:
            self.final_puzzle_value.set(25)
        self.free_transformations_var.set(choice(["Base Game Costs", "World Order Scaled Costs", "Free Transformations"]))
        self.one_health_banjo_var.set(randint(0, 1))
        self.remove_floating_jiggies_var.set(0),
        # Non-Flagged Objects
        self.non_flagged_object_var.set(choice(["None", "Shuffle (World)"]))
        self.non_flagged_object_abnormalities_var.set(randint(0, 1))
        self.starting_lives_value.set(randint(0, 69))
        # Structs
        self.struct_var.set(choice(["None", "Shuffle (World)", "Shuffle (Game)", "Randomize", "All Notes"]))
        self.note_overflow_var.set("Allow Save & Quit/Reset")
        self.struct_note_count_var.set(choice(["Produce Extra Notes", "Produce Exactly Enough Notes"]))
        self.final_note_door_var.set(choice(["Scaling Note Doors", "Final Note Door Only"]))
        if(self.struct_var.get() == "All Notes"):
            self.final_note_door_value.set(randint(0, 2000))
        else:
            self.final_note_door_value.set(randint(0, 900))
        self.before_blue_egg_carry_value.set(randint(0, 255))
        self.after_blue_egg_carry_value.set(randint(int(self.before_blue_egg_carry_value.get()), 255))
        self.before_red_feather_carry_value.set(randint(0, 255))
        self.after_red_feather_carry_value.set(randint(int(self.before_red_feather_carry_value.get()), 255))
        self.before_gold_feather_carry_value.set(randint(0, 255))
        self.after_gold_feather_carry_value.set(randint(int(self.before_gold_feather_carry_value.get()), 255))
        # World Entrances
        self.world_entrance_var.set(choice(["None", "Basic Shuffle", "Bottles Shuffle"]))
        self.world_exit_var.set(choice(["Exit From World You Were Just In", "Exit From Entrance You Entered From"]))
        self.all_starting_moves_var.set(randint(0, 1))
        # Within World Warps
        self.within_world_warps_var.set(choice(["None", "Shuffle By World", "Shuffle By Game"]))
        # Starting World
        self.new_area_var.set(choice([option for option in start_level_ids]))
        if(self.new_area_var.get() == "SM - Main"):
            self.skip_intro_cutscene_var.set(randint(0, 1))
        else:
            self.skip_intro_cutscene_var.set(1)
        # Enemies
        self.enemies_var.set(choice(["None", "Shuffle", "Randomize"]))
        for enemy_name in self.enemy_checkbox_dict:
            self.enemy_checkbox_dict[enemy_name].set(randint(0, 1))
        ### Aesthetic Settings ###
        # BK Model
        self._random_bk_model_colors()
        # Enemy Models
        for custom_name in self.customizable_checkbox_dict:
            self.customizable_checkbox_dict[custom_name].set(randint(0, 1))
        # Sounds/Music
        self.short_sounds_var.set(randint(0, 1))
        self.jingles_var.set(randint(0, 1))
        self.music_var.set(randint(0, 1))
        self.beta_sounds_var.set(randint(0, 1))
        self.jarring_sounds_var.set(randint(0, 1))
        # Sprites/Textures
        self.skybox_var.set(randint(0, 1))
        self.talking_sprite_var.set(randint(0, 1))
        ### World Specific ###
        # Gruntilda's Lair
        self.skip_furnace_fun_var.set(randint(0, 1))
        self.remove_magic_barriers_var.set(randint(0, 1))
        self.gruntilda_difficulty_var.set(randint(0, 3))
        self.monster_house_var.set(randint(0, 1))
        self.what_floor_var.set(randint(0, 1))
        self.grunty_size_var.set(randint(0, 1))
        if(not (self.monster_house_var.get() or self.what_floor_var.get() or self.grunty_size_var.get()) and self.gruntilda_difficulty_var.get()):
            grunty_option = randint(0, 2)
            if(grunty_option == 0):
                self.monster_house_var.set(1)
            elif(grunty_option == 1):
                self.what_floor_var.set(1)
            else:
                self.grunty_size_var.set(1)
        # Mumbo's Mountain
        self.flowers_var.set(randint(0, 1))
        # Treasure Trove Cove
        self.scattered_structs_var.set(randint(0, 1))
        # Clanker's Cavern
        self.hard_rings_var.set(randint(0, 1))
        # Bubblegloop Swamp
        self.croctus_var.set(randint(0, 1))
        self.mr_vile_var.set(randint(0, 1))
        self.tiptup_choir_var.set(randint(0, 1))
        # Freezeezy Peak
        self.hard_races_var.set(randint(0, 1))
        # Gobi's Valley
        self.ancient_ones_var.set(randint(0, 1))
        self.maze_jinxy_heads_var.set(randint(0, 1))
        self.matching_puzzle_var.set(randint(0, 1))
        # Mad Monster Mansion
        self.lit_pots_var.set(randint(0, 1))
        self.motzand_keys_var.set(randint(0, 1))
        # Rusty Bucket Bay
        self.buttons_var.set(randint(0, 1))
        # Click Clock Wood
        self.ccw_var.set(choice(["Season", "Within World"]))
    
    def _save_current_configuration(self, button_press=True):
        '''Writes the current configuration to a JSON file'''
        self.logger.info("Save Current Configuration")
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
            "Final_Puzzle": self.final_puzzle_var.get(),
            "Final_Puzzle_Value": self.final_puzzle_value.get(),
            "Free_Transformations": self.free_transformations_var.get(),
            "One_Health_Only": self.one_health_banjo_var.get(),
            "Remove_Floating_Jiggies": self.remove_floating_jiggies_var.get(),
            # Non-Flagged Objects
            "Non_Flagged_Objects_Option": self.non_flagged_object_var.get(),
            "Non_Flagged_Objects_Abnormalities": self.non_flagged_object_abnormalities_var.get(),
            "Starting_Lives": self.starting_lives_value.get(),
            # Structs
            "Struct_Option": self.struct_var.get(),
            "Note_Overflow": self.note_overflow_var.get(),
            "Struct_Note_Count": self.struct_note_count_var.get(),
            "Final_Note_Door": self.final_note_door_var.get(),
            "Final_Note_Door_Value": self.final_note_door_value.get(),
            "Before_Cheato_Blue_Eggs": self.before_blue_egg_carry_value.get(),
            "After_Cheato_Blue_Eggs": self.after_blue_egg_carry_value.get(),
            "Before_Cheato_Red_Feathers": self.before_red_feather_carry_value.get(),
            "After_Cheato_Red_Feathers": self.after_red_feather_carry_value.get(),
            "Before_Cheato_Gold_Feathers": self.before_gold_feather_carry_value.get(),
            "After_Cheato_Gold_Feathers": self.after_gold_feather_carry_value.get(),
            # World Entrances
            "World_Entrance_Option": self.world_entrance_var.get(),
            "World_Exit": self.world_exit_var.get(),
            "All_Moves": self.all_starting_moves_var.get(),
            # Within World Warps
            "Within_World_Warps_Option": self.within_world_warps_var.get(),
            # Starting World
            "Starting_Area": self.new_area_var.get(),
            "Skip_Intro_Cutscene": self.skip_intro_cutscene_var.get(),
            # Enemies
            "Enemies_Option": self.enemies_var.get(),
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
            # Sounds/Music
            "Short_Sound_Option": self.short_sounds_var.get(),
            "Jingle_Option": self.jingles_var.get(),
            "Music_Option": self.music_var.get(),
            "Beta_Sounds": self.beta_sounds_var.get(),
            "Jarring_Sounds": self.jarring_sounds_var.get(),
            # Sprites/Textures
            "Skybox_Option": self.skybox_var.get(),
            "Talking_Sprite_Option": self.talking_sprite_var.get(),
            ### Misc Settings ###
            "Remove_Files": self.remove_files_var.get(),
            "Tool_Tips": self.tool_tips_var.get(),
            ### World Specific ###
            # Gruntilda's Lair
            "Furnace_Fun_Skip": self.skip_furnace_fun_var.get(),
            "Remove_Magic_Barriers": self.remove_magic_barriers_var.get(),
            "Final_Battle_Difficulty": self.gruntilda_difficulty_var.get(),
            "Monster_House": self.monster_house_var.get(),
            "What_Floor": self.what_floor_var.get(),
            "Mini_Me": self.grunty_size_var.get(),
            # Mumbo's Mountain
            "MM_Flowers": self.flowers_var.get(),
            # Treasure Trove Cove
            "Scattered_Notes_Eggs_Feathers": self.scattered_structs_var.get(),
            "Super_Slippery_Sand": self.super_slippery_ttc_var.get(),
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
            "Motzand_Keys": self.motzand_keys_var.get(),
            # Rusty Bucket Bay
            "RBB_Buttons": self.buttons_var.get(),
            # Click Clock Wood
            "CCW_Option": self.ccw_var.get(),
            }
        # Enemies
        for enemy_name in master_enemy_dict:
            current_config[f"Include {enemy_name}"] = self.enemy_checkbox_dict[enemy_name].get()
        # Enemies
        for custom_name in self.customizable_checkbox_dict:
            current_config[f"Include {custom_name}"] = self.customizable_checkbox_dict[custom_name].get()
        if(button_press):
            try:
                json_file = tkinter.filedialog.asksaveasfile(filetypes=(("Json Files","*.json"),("all files","*.*")), defaultextension=json)
                json.dump(current_config, json_file, indent=4)
            except Exception:
                pass # log something here?
        else:
            config_file = f"{self.cwd}Configurations/Last_Used_Configuration.json"
            with open(config_file, "w+") as json_file: 
                json.dump(current_config, json_file, indent=4)
    
    #########################################
    ### VERIFY SETTINGS BEFORE SUBMITTING ###
    #########################################
    
    # GENERAL
    
    def _check_rom_directory(self):
        '''Checks if ROM file ends in .z64 and is located in the folder with GZIP.EXE'''
        self.logger.info("Check ROM Directory")
        rom_path = self.rom_file_entry.get()
        if("\\" in rom_path):
            rom_file = rom_path.split("\\")[-1]
        elif("/" in rom_path):
            rom_file = rom_path.split("/")[-1]
        else:
            Error_GUI("Unknown Directory?")
        if((rom_path == "") or (not os.path.isfile(rom_path))):
            Error_GUI("Please provide the directory to the ROM.")
            return False
        rom_ext = rom_file.split(".")[-1]
        if(rom_ext not in ["z64"]):
            Error_GUI(f"Rom Extention is not allowed: {rom_ext}")
            return False
        return self._verify_rom_file(rom_path)
    
    def _check_seed_value(self):
        '''Verifies the seed value is either blank or only consists of digits'''
        self.logger.info("Check Seed Value")
        seed_val = self.seed_value.get()
        if((not seed_val.isdigit()) and (seed_val != "")):
            Error_GUI(f"Seed value is not allowed: '{seed_val}'")
            return False
        return True
    
    # COLLECTABLES
    
    def _check_final_puzzle_value(self):
        '''Verifies the puzzle door limits are digits'''
        self.logger.info("Check Final Puzzle Value")
        final_puzzle_val = self.final_puzzle_value.get()
        if(final_puzzle_val == "?"):
            return True
        if(not final_puzzle_val.isdigit()):
            Error_GUI(f"Final Puzzle Value Must Be An Integer: '{str(final_puzzle_val)}'")
            return False
        final_puzzle_val= int(final_puzzle_val)
        if(final_puzzle_val < 0):
            Error_GUI("Final Puzzle Value Must Be Greater Than Or Equal To Zero.")
            return False
        elif(final_puzzle_val > 100):
            Error_GUI("Final Puzzle Value Must Be Less Than 100 Under These Settings.")
            return False
        elif((self.remove_floating_jiggies_var.get() == 1) and (final_puzzle_val > 50)):
            Error_GUI("Final Puzzle Value Must Be Less Than 51 When Removing Floating Jiggies.")
            return False
        return True
    
    def _check_final_note_door_value(self):
        '''Verifies the note door limits are digits'''
        self.logger.info("Check Final Note Door Value")
        final_note_door_val = self.final_note_door_value.get()
        if(final_note_door_val == "?"):
            return True
        if(not final_note_door_val.isdigit()):
            Error_GUI(f"Final Note Door Value Must Be An Positive Integer: '{str(final_note_door_val)}'")
            return False
        final_note_door_val = int(final_note_door_val)
        if(final_note_door_val < 0):
            Error_GUI("Final Note Door Value Must Be Greater Than Zero.")
            return False
        if((self.struct_var.get() == "All Notes") and (final_note_door_val > 2000)):
            Error_GUI("Final Note Door Value Must Be Less Than 2000 Under These Settings.")
            return False
        elif((self.struct_var.get() != "All Notes") and (final_note_door_val > 900)):
            Error_GUI("Final Note Door Value Must Be Less Than 900 Under These Settings.")
            return False
        return True
    
    def _check_cheato_values(self):
        '''Verifies the carrying capacities before and after Cheato are digits between 0 and 255'''
        self.logger.info("Check Carrying Capacities")
        for value in [self.before_blue_egg_carry_value.get(), self.after_blue_egg_carry_value.get(),
                      self.before_red_feather_carry_value.get(), self.after_red_feather_carry_value.get(),
                      self.before_gold_feather_carry_value.get(), self.after_gold_feather_carry_value.get()]:
            if(value == "?"):
                pass
            elif((not value.isdigit()) or (int(value) < 0) or (int(value) > 255)):
                Error_GUI("Egg and Feather carrying capacities should be between 0 and 255.")
                return False
        return True
    
    def _check_starting_life_count(self):
        '''Verifies the starting life count is between 0 and 255'''
        self.logger.info("Check Life Count")
        starting_lives = self.starting_lives_entry.get()
        if((not starting_lives.isdigit()) or (int(self.starting_lives_entry.get()) < 0) or (int(self.starting_lives_entry.get()) > 255)):
            Error_GUI("Starting life count should be between 0 and 255.")
            return False
        return True
    
    # SUBMIT
    
    def _submit(self):
        '''If all input paramaters meet the requirements, we move onto actually randomizing the game'''
        self.logger.info("Submitting Configuration")
        if(self._check_rom_directory() and self._check_seed_value() and
           self._check_final_note_door_value() and self._check_final_puzzle_value() and self._check_cheato_values() and self._check_starting_life_count()):
            self.logger.debug("##### All Settings Seem To Check Out! #####")
            self._save_current_configuration(button_press=False)
            progression_app = Progression_GUI_Class(self)
            progression_app._main()
            del progression_app
        else:
            self.logger.debug("At Least One Setting Seem To Be Invalid. Please check all settings.")
    
    ######################
    ### FRONT END CODE ###
    ######################
    
    def _main(self):
        '''Places all of the widgest on the GUI and runs the loop for the window'''
        self.logger.info("Creating GUI Main")
        self.ttp_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Tool_Tips.png")
        self._tab_control = ttk.Notebook(self.app_window)
        style = ttk.Style()
        style.theme_create(
            "Tabs_Font",
            parent="alt",
            settings={
                "TNotebook": {
                    "configure": {
                        "tabmargins": [2, 5, 2, 0],
                        "background": self.generic_background_color,
                        },
                    },
                "TNotebook.Tab": {
                    "configure": {
                        "padding": [5, 5],
                        "foreground": self.white,
                        "background": self.red,
                        "anchor": tk.CENTER,
                        "font": ("Arial bold", 10),
                        },
                    "map": {
                        "foreground": [("selected", self.white)],
                        "background": [("selected", self.blue)],
                        "expand": [("selected", [1, 1, 1, 0])],
                        }
                    },
                "Horizontal.TProgressbar": {
                    "configure": {
                        "troughcolor": "#990000",
                        "background": "#0040AA",
                        "anchor": tk.CENTER,
                        "padding": [10, 10],
                        "width": 20,
                        },
                    },
                }
        )
        style.theme_use("Tabs_Font")
        ########################
        ### GENERAL SETTINGS ###
        ########################
        self._general_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._general_tab, text="General")
        ### ROM ###
        curr_background_color = "#F3E5AB"
        self.rom_frame = tk.LabelFrame(self._general_tab, text="ROM File", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.rom_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.select_rom_button_ttp_canvas = tk.Label(self.rom_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.select_rom_button_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        self.select_rom_button_ttp = self.CreateToolTip(self.select_rom_button_ttp_canvas, self, tool_tips_dict["ROM"]["SELECT_ROM_FILE"])
        self.folder_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Open_File.png")
        self.select_rom_button = tk.Button(self.rom_frame, text='Select ROM File', image=self.folder_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size), command=self._select_rom_file)
        self.select_rom_button.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.rom_file_entry = tk.StringVar(self.rom_frame)
        self.rom_file_display = tk.Entry(self.rom_frame, textvariable=self.rom_file_entry, state='readonly', width=35, font=(self.font_type, self.medium_font_size))
        self.rom_file_display.grid(row=0, column=2, columnspan=2, padx=10, pady=self.pady)
        rom_file_disclaimer_text = "ROMs must be v1.0 NTSC of Banjo-Kazooie, ending in .z64"
        self.rom_file_disclaimer_label = tk.Label(self.rom_frame, text=rom_file_disclaimer_text, foreground=self.black, background=curr_background_color, font=(self.font_type, 12), anchor="w", justify="left")
        self.rom_file_disclaimer_label.grid(row=1, column=1, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        ### Seed ###
        self.seed_frame = tk.LabelFrame(self._general_tab, text="Seed", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.seed_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.random_seed_button_ttp_canvas = tk.Label(self.seed_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.random_seed_button_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        self.random_seed_button_ttp = self.CreateToolTip(self.random_seed_button_ttp_canvas, self, tool_tips_dict["SEED"]["RANDOM_SEED_BUTTON"])
        self._seed_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Seed.png")
        self.random_seed_button = tk.Button(self.seed_frame, text='Select ROM File', command=self._random_seed, image=self._seed_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.random_seed_button.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.seed_value = tk.StringVar(self.seed_frame)
        self.seed_entry = tk.Entry(self.seed_frame, textvariable=self.seed_value, width=20, font=(self.font_type, self.medium_font_size))
        self.seed_entry.grid(row=0, column=2, columnspan=2, padx=10, pady=self.pady)
        ### Randomizer Setting Code ###
        self.randomizer_setting_code_frame = tk.LabelFrame(self._general_tab, text="Randomizer Setting Code", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.randomizer_setting_code_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.randomizer_setting_code_ttp_canvas = tk.Label(self.randomizer_setting_code_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.randomizer_setting_code_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        self.randomizer_setting_code_ttp = self.CreateToolTip(self.randomizer_setting_code_ttp_canvas, self, tool_tips_dict["SETTING_CODE"]["GENERATING_SETTING_CODE"])
        self.generate_randomizer_setting_code_button = tk.Button(self.randomizer_setting_code_frame, text='Generate Settings Code', command=self._generate_randomizer_settings_code, foreground=self.white, background=self.red, font=(self.font_type, self.medium_font_size))
        self.generate_randomizer_setting_code_button.grid(row=0, column=1, padx=10, pady=self.pady)
        self.apply_randomizer_setting_code_button = tk.Button(self.randomizer_setting_code_frame, text='Apply Settings Code', command=self._apply_randomizer_settings_code, foreground=self.white, background=self.red, font=(self.font_type, self.medium_font_size))
        self.apply_randomizer_setting_code_button.grid(row=0, column=2, padx=10, pady=self.pady)
        self.randomizer_setting_code_value = tk.StringVar(self.randomizer_setting_code_frame)
        self.randomizer_setting_code_entry = tk.Entry(self.randomizer_setting_code_frame, textvariable=self.randomizer_setting_code_value, width=45, font=(self.font_type, self.medium_font_size))
        self.randomizer_setting_code_entry.grid(row=1, column=0, columnspan=5, padx=10, pady=self.pady, sticky='w')
        ### Random Settings ###
        self.random_settings_frame = tk.LabelFrame(self._general_tab, text="Random Settings", foreground=self.red, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.random_settings_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.random_config_button = tk.Button(self.random_settings_frame, text='Randomly Select Configurations', foreground=self.white, background=self.red, font=(self.font_type, self.small_font_size), command=(lambda: self._load_configuration(random_file=True)))
        self.random_config_button.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        self.random_settings_button = tk.Button(self.random_settings_frame, text='Randomly Select EVERY Setting', foreground=self.white, background=self.red, font=(self.font_type, self.small_font_size), command=self._set_random_settings)
        self.random_settings_button.grid(row=0, column=1, padx=self.padx, pady=self.pady)
        ########################
        ### COLLECTABLES TAB ###
        ########################
        self._collectables_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._collectables_tab, text="Collectables")
        # Flagged Objects
        self.flagged_object_frame = tk.LabelFrame(self._collectables_tab, text="Jiggies, Empty Honeycombs, & Mumbo Tokens", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.flagged_object_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.flagged_object_ttp_canvas = tk.Label(self.flagged_object_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.flagged_object_ttp_canvas.grid(row=0, column=0, rowspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.flagged_object_ttp = self.CreateToolTip(self.flagged_object_ttp_canvas, self, tool_tips_dict["FLAGGED_OBJECTS"]["FRAME"])
        self.flagged_object_var = tk.StringVar(self.flagged_object_frame)
        self.flagged_object_options = ["None", "Shuffle (World)", "Shuffle (Game)"]
        self.flagged_object_dropdown = ttk.Combobox(self.flagged_object_frame, textvariable=self.flagged_object_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.flagged_object_dropdown['values'] = self.flagged_object_options
        self.flagged_object_dropdown['state'] = 'readonly'
        self.flagged_object_dropdown.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.flagged_object_abnormalities_var = tk.IntVar()
        self.flagged_object_abnormalities_checkbutton = tk.Checkbutton(self.flagged_object_frame, text="Include Abnormalities", variable=self.flagged_object_abnormalities_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.flagged_object_abnormalities_checkbutton.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.flagged_object_softlock_var = tk.IntVar()
        self.flagged_object_softlock_checkbutton = tk.Checkbutton(self.flagged_object_frame, text="Include Potential Softlocks", variable=self.flagged_object_softlock_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.flagged_object_softlock_checkbutton.grid(row=1, column=2, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self._jiggy_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Jiggy.png")
        self.random_puzzle_value_button = tk.Button(self.flagged_object_frame, text='Random Puzzle Value', command=self._random_puzzle_value, image=self._jiggy_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.random_puzzle_value_button.grid(row=2, column=2, rowspan=2, padx=self.padx, pady=self.pady)
        self.final_puzzle_ttp_canvas = tk.Label(self.flagged_object_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_puzzle_ttp_canvas.grid(row=2, column=0, rowspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.final_puzzle_checkbox_ttp = self.CreateToolTip(self.final_puzzle_ttp_canvas, self, tool_tips_dict["GRUNTILDAS_LAIR"]["FINAL_PUZZLE"])
        self.final_puzzle_var = tk.IntVar()
        self.final_puzzle_checkbox = tk.Checkbutton(self.flagged_object_frame, text="Door Of Grunty Only", variable=self.final_puzzle_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_puzzle_checkbox.grid(row=2, column=1, rowspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.final_text = tk.Label(self.flagged_object_frame, text="Door of Grunty Jiggies:", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_text.grid(row=2, column=3, padx=self.padx, pady=self.pady)
        self.final_puzzle_value = tk.StringVar(self.flagged_object_frame)
        self.final_puzzle_entry = tk.Entry(self.flagged_object_frame, textvariable=self.final_puzzle_value, width=6)
        self.final_puzzle_entry.grid(row=2, column=4, padx=self.padx, pady=self.pady)
        self.remove_floating_jiggies_var = tk.IntVar()
        self.remove_floating_jiggies_checkbox = tk.Checkbutton(self.flagged_object_frame, text="No Floating Jiggies", variable=self.remove_floating_jiggies_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.remove_floating_jiggies_checkbox.grid(row=3, column=3, padx=self.padx, pady=self.pady)
        self.one_health_banjo_var = tk.IntVar()
        self.one_health_banjo_checkbox = tk.Checkbutton(self.flagged_object_frame, text="One Health Only", variable=self.one_health_banjo_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.one_health_banjo_checkbox.grid(row=4, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.free_transformations_text = tk.Label(self.flagged_object_frame, text="Token Option:", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.free_transformations_text.grid(row=4, column=2, padx=self.padx, pady=self.pady, sticky='e')
        self.free_transformations_var = tk.StringVar(self.flagged_object_frame)
        self.free_transformations_options = ["Base Game Costs", "World Order Scaled Costs", "Free Transformations"]
        self.free_transformations_dropdown = ttk.Combobox(self.flagged_object_frame, textvariable=self.free_transformations_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size), width=23)
        self.free_transformations_dropdown['values'] = self.free_transformations_options
        self.free_transformations_dropdown['state'] = 'readonly'
        self.free_transformations_dropdown.grid(row=4, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.final_puzzle_var.trace('w', self._lock_final_puzzle_value)
        # Structs
        self.struct_frame = tk.LabelFrame(self._collectables_tab, text="Notes, Blue Eggs, Red Feathers, & Gold Feathers", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.struct_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.struct_ttp_canvas = tk.Label(self.struct_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.struct_ttp_canvas.grid(row=0, column=0, rowspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.struct_ttp = self.CreateToolTip(self.struct_ttp_canvas, self, tool_tips_dict["STRUCTS"]["FRAME"])
        self.struct_var = tk.StringVar(self.struct_frame)
        self.struct_options = ["None", "Shuffle (World)", "Shuffle (Game)", "Randomize", "All Notes"]
        self.struct_dropdown = ttk.Combobox(self.struct_frame, textvariable=self.struct_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.struct_dropdown['values'] = self.struct_options
        self.struct_dropdown['state'] = 'readonly'
        self.struct_dropdown.grid(row=0, column=1, rowspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.note_overflow_var = tk.StringVar(self.struct_frame)
        self.note_overflow_options = ["Allow Save & Quit/Reset", "Possible No Save & Quit/Reset"]
        self.note_overflow_dropdown = ttk.Combobox(self.struct_frame, textvariable=self.note_overflow_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size), width=26)
        self.note_overflow_dropdown['values'] = self.note_overflow_options
        self.note_overflow_dropdown['state'] = 'readonly'
        self.note_overflow_dropdown.grid(row=0, column=2, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.struct_note_count_var = tk.StringVar(self.struct_frame)
        self.struct_note_count_options = ["Produce Extra Notes", "Produce Exactly Enough Notes"]
        self.struct_note_count_dropdown = ttk.Combobox(self.struct_frame, textvariable=self.struct_note_count_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size), width=26)
        self.struct_note_count_dropdown['values'] = self.struct_note_count_options
        self.struct_note_count_dropdown['state'] = 'readonly'
        self.struct_note_count_dropdown.grid(row=1, column=2, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.final_note_door_ttp_canvas = tk.Label(self.struct_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_note_door_ttp_canvas.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.final_note_door_checkbox_ttp = self.CreateToolTip(self.final_note_door_ttp_canvas, self, tool_tips_dict["GRUNTILDAS_LAIR"]["FINAL_NOTE_DOOR"])
        self.final_note_door_var = tk.StringVar(self.struct_frame)
        self.note_door_options = ["Scaling Note Doors", "Final Note Door Only"]
        self.final_note_door_dropdown = ttk.Combobox(self.struct_frame, textvariable=self.final_note_door_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_note_door_dropdown['values'] = self.note_door_options
        self.final_note_door_dropdown['state'] = 'readonly'
        self.final_note_door_dropdown.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.final_note_door_value = tk.StringVar(self.struct_frame)
        self._note_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Note.png")
        self.random_note_value_button = tk.Button(self.struct_frame, text='Random Note Value', command=self._random_note_value, image=self._note_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.random_note_value_button.grid(row=2, column=2, padx=self.padx, pady=self.pady)
        self.final_text = tk.Label(self.struct_frame, text="810 Note Door Value:", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_text.grid(row=2, column=3, padx=self.padx, pady=self.pady)
        self.final_note_door_entry = tk.Entry(self.struct_frame, textvariable=self.final_note_door_value, width=6)
        self.final_note_door_entry.grid(row=2, column=4, padx=self.padx, pady=self.pady, sticky='e')
        self.final_text = tk.Label(self.struct_frame, text="Notes", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_text.grid(row=2, column=5, padx=self.padx, pady=self.pady, sticky='w')
        self.carry_limit_frame = tk.LabelFrame(self.struct_frame, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.carry_limit_frame.grid(row=3, column=0, columnspan=6, padx=self.padx, pady=self.pady, sticky='w')
        self.carry_limit_frame["borderwidth"] = 0
        self.carry_limit_frame["highlightthickness"] = 0
        self.carry_limit_ttp_canvas = tk.Label(self.carry_limit_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.carry_limit_ttp_canvas.grid(row=0, column=0, rowspan=3, padx=self.padx, pady=self.pady, sticky='w')
        self.carry_limit_ttp = self.CreateToolTip(self.carry_limit_ttp_canvas, self, tool_tips_dict["STRUCTS"]["CARRY_LIMIT"])
        self.final_text = tk.Label(self.carry_limit_frame, text="Before Cheato", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_text.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.final_text = tk.Label(self.carry_limit_frame, text="After Cheato", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_text.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.final_text = tk.Label(self.carry_limit_frame, text="Blue Eggs", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_text.grid(row=0, column=2, padx=self.padx, pady=self.pady)
        self.final_text = tk.Label(self.carry_limit_frame, text="Red Feathers", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_text.grid(row=0, column=3, padx=self.padx, pady=self.pady)
        self.final_text = tk.Label(self.carry_limit_frame, text="Gold Feathers", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_text.grid(row=0, column=4, padx=self.padx, pady=self.pady)
        self.before_blue_egg_carry_value = tk.StringVar(self.struct_frame)
        self.blue_egg_carry_entry = tk.Entry(self.carry_limit_frame, textvariable=self.before_blue_egg_carry_value, width=6)
        self.blue_egg_carry_entry.grid(row=1, column=2, padx=self.padx, pady=self.pady)
        self.after_blue_egg_carry_value = tk.StringVar(self.struct_frame)
        self.blue_egg_carry_entry = tk.Entry(self.carry_limit_frame, textvariable=self.after_blue_egg_carry_value, width=6)
        self.blue_egg_carry_entry.grid(row=2, column=2, padx=self.padx, pady=self.pady)
        self.before_red_feather_carry_value = tk.StringVar(self.struct_frame)
        self.red_feather_carry_entry = tk.Entry(self.carry_limit_frame, textvariable=self.before_red_feather_carry_value, width=6)
        self.red_feather_carry_entry.grid(row=1, column=3, padx=self.padx, pady=self.pady)
        self.after_red_feather_carry_value = tk.StringVar(self.struct_frame)
        self.red_feather_carry_entry = tk.Entry(self.carry_limit_frame, textvariable=self.after_red_feather_carry_value, width=6)
        self.red_feather_carry_entry.grid(row=2, column=3, padx=self.padx, pady=self.pady)
        self.before_gold_feather_carry_value = tk.StringVar(self.struct_frame)
        self.gold_feather_carry_entry = tk.Entry(self.carry_limit_frame, textvariable=self.before_gold_feather_carry_value, width=6)
        self.gold_feather_carry_entry.grid(row=1, column=4, padx=self.padx, pady=self.pady)
        self.after_gold_feather_carry_value = tk.StringVar(self.struct_frame)
        self.gold_feather_carry_entry = tk.Entry(self.carry_limit_frame, textvariable=self.after_gold_feather_carry_value, width=6)
        self.gold_feather_carry_entry.grid(row=2, column=4, padx=self.padx, pady=self.pady)
        self.random_carry_capacity_button = tk.Button(self.carry_limit_frame, text='Random Carry\nCapacities', foreground=self.white, background=self.red, font=(self.font_type, self.small_font_size), command=self._set_random_carry_capacities)
        self.random_carry_capacity_button.grid(row=1, rowspan=2, column=5, padx=self.padx, pady=self.pady)
        self.struct_var.trace('w', self._lock_struct_options)
        # Non Flagged Objects
        self.non_flagged_object_frame = tk.LabelFrame(self._collectables_tab, text="Jinjos, 1-Ups, & Misc Objects", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.non_flagged_object_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.non_flagged_object_ttp_canvas = tk.Label(self.non_flagged_object_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.non_flagged_object_ttp_canvas.grid(row=0, column=0, rowspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.non_flagged_object_ttp = self.CreateToolTip(self.non_flagged_object_ttp_canvas, self, tool_tips_dict["NON_FLAGGED_OBJECTS"]["FRAME"])
        self.non_flagged_object_var = tk.StringVar(self.non_flagged_object_frame)
        self.non_flagged_object_options = ["None", "Shuffle (World)"]
        self.non_flagged_object_dropdown = ttk.Combobox(self.non_flagged_object_frame, textvariable=self.non_flagged_object_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.non_flagged_object_dropdown['values'] = self.non_flagged_object_options
        self.non_flagged_object_dropdown['state'] = 'readonly'
        self.non_flagged_object_dropdown.grid(row=0, column=1, columnspan=3, padx=self.padx, pady=self.pady, sticky='w')
        self.non_flagged_object_abnormalities_var = tk.IntVar()
        self.non_flagged_object_abnormalities_checkbutton = tk.Checkbutton(self.non_flagged_object_frame, text="Include Abnormalities (May Include Eggs and Feathers)", variable=self.non_flagged_object_abnormalities_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.non_flagged_object_abnormalities_checkbutton.grid(row=1, column=1, columnspan=3, padx=self.padx, pady=self.pady, sticky='sw')
        self.starting_lives_text = tk.Label(self.non_flagged_object_frame, text="Starting Life Count:", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.starting_lives_text.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.starting_lives_value = tk.StringVar(self.struct_frame)
        self.starting_lives_entry = tk.Entry(self.non_flagged_object_frame, textvariable=self.starting_lives_value, width=6)
        self.starting_lives_entry.grid(row=2, column=2, padx=self.padx, pady=self.pady, sticky='w')
        #################
        ### WARPS TAB ###
        #################
        self._warps_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._warps_tab, text="Warps")
        # World Entrances
        self.world_entrance_frame = tk.LabelFrame(self._warps_tab, text="World Entrances (Includes Randomized Moves)", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.world_entrance_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.world_entrance_ttp_canvas = tk.Label(self.world_entrance_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.world_entrance_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.world_entrance_ttp = self.CreateToolTip(self.world_entrance_ttp_canvas, self, tool_tips_dict["WORLD_ENTRANCES"]["FRAME"])
        self.world_entrance_var = tk.StringVar(self.world_entrance_frame)
        self.world_entrance_options = ["None", "Basic Shuffle", "Bottles Shuffle"]
        self.world_entrance_dropdown = ttk.Combobox(self.world_entrance_frame, textvariable=self.world_entrance_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.world_entrance_dropdown['values'] = self.world_entrance_options
        self.world_entrance_dropdown['state'] = 'readonly'
        self.world_entrance_dropdown.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.world_exit_var = tk.StringVar(self.world_entrance_frame)
        self.world_exit_options = ["Exit From World You Were Just In", "Exit From Entrance You Entered From"]
        self.world_exit_dropdown = ttk.Combobox(self.world_entrance_frame, textvariable=self.world_exit_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size), width=33)
        self.world_exit_dropdown['values'] = self.world_exit_options
        self.world_exit_dropdown['state'] = 'readonly'
        self.world_exit_dropdown.grid(row=0, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.all_starting_moves_var = tk.IntVar()
        self.all_starting_moves_checkbutton = tk.Checkbutton(self.world_entrance_frame, text="Start Game With All Moves", variable=self.all_starting_moves_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.all_starting_moves_checkbutton.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='sw')
        # Within World Warps
        self.within_world_warp_frame = tk.LabelFrame(self._warps_tab, text="Within The World Warps", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.within_world_warp_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.within_world_warp_ttp_canvas = tk.Label(self.within_world_warp_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.within_world_warp_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.within_world_warp_ttp = self.CreateToolTip(self.within_world_warp_ttp_canvas, self, tool_tips_dict["WITHIN_WORLD_WARPS"]["FRAME"])
        self.within_world_warps_var = tk.StringVar(self.within_world_warp_frame)
        self.within_world_warps_options = ["None", "Shuffle By World", "Shuffle By Game"]
        self.within_world_warps_dropdown = ttk.Combobox(self.within_world_warp_frame, textvariable=self.within_world_warps_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.within_world_warps_dropdown['values'] = self.within_world_warps_options
        self.within_world_warps_dropdown['state'] = 'readonly'
        self.within_world_warps_dropdown.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        warp_disclaimer_text = (
            "WARNING:\n" +
            "  The 'Shuffle By Game' option has some warps that crash\n"+
            "  and notes do not save between warps. Logic not suited for\n"+
            "  world entrance shuffle. Would not recommend. Use at own risk."
            )
        self.warp_disclaimer_label = tk.Label(self.within_world_warp_frame, text=warp_disclaimer_text, foreground=self.black, background=curr_background_color, font=(self.font_type, 12), anchor="w", justify="left")
        self.warp_disclaimer_label.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Starting Area
        self.starting_area_frame = tk.LabelFrame(self._warps_tab, text="Starting Area:", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.starting_area_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.starting_area_ttp_canvas = tk.Label(self.starting_area_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.starting_area_ttp_canvas.grid(row=0, column=0, rowspan=2, padx=self.padx, pady=self.pady, sticky='w')
        starting_area_disclaimer_text = (
            "WARNING:\n" +
            "  The 'Starting Area' option is not programmed into any logic\n"+
            "  and may softlock the player early on if not all moves are\n"+
            "  active. Mostly for developer usage. Use at own risk."
            )
        self.starting_area_label = tk.Label(self.starting_area_frame, text=starting_area_disclaimer_text, foreground=self.black, background=curr_background_color, font=(self.font_type, 12), anchor="w", justify="left")
        self.starting_area_label.grid(row=0, column=1, columnspan=4, padx=self.padx, pady=self.pady, sticky='w')
        self.new_area_ttp = self.CreateToolTip(self.starting_area_ttp_canvas, self, tool_tips_dict["STARTING_AREA"]["NEW_GAME"])
        self.new_area_text = tk.Label(self.starting_area_frame, text="Starting Area", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.new_area_text.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.new_area_var = tk.StringVar(self.world_entrance_frame)
        self.starting_area_options = [option for option in start_level_ids]
        self.starting_area_options.insert(0, "Random Starting Area (Auto Have All Moves)")
        self.new_area_dropdown = ttk.Combobox(self.starting_area_frame, textvariable=self.new_area_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size), width=39)
        self.new_area_dropdown['values'] = self.starting_area_options
        self.new_area_dropdown['state'] = 'readonly'
        self.new_area_dropdown.grid(row=1, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.skip_intro_cutscene_var = tk.IntVar()
        self.skip_intro_cutscene_checkbutton = tk.Checkbutton(self.starting_area_frame, text="Skip Intro Cutscene", variable=self.skip_intro_cutscene_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.skip_intro_cutscene_checkbutton.grid(row=2, column=1, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.default_starting_area_button = tk.Button(self.starting_area_frame, text='Default\nStarting Area', command=self._default_starting_area, foreground=self.white, background=self.red, font=(self.font_type, self.small_font_size))
        self.default_starting_area_button.grid(row=1, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.new_area_var.trace('w', self._new_area_option)
        ###################
        ### ENEMIES TAB ###
        ###################
        self._enemies_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._enemies_tab, text="Enemies")
        # Enemies
        self.enemies_frame = tk.LabelFrame(self._enemies_tab, text="Ground, Wall, & Flying Enemies", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.enemies_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.enemies_frame["borderwidth"] = 0
        self.enemies_frame["highlightthickness"] = 0
        self.enemies_ttp_canvas = tk.Label(self.enemies_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.enemies_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.enemies_ttp = self.CreateToolTip(self.enemies_ttp_canvas, self, tool_tips_dict["ENEMIES"]["FRAME"])
        self.enemies_var = tk.StringVar(self.enemies_frame)
        self.enemies_options = ["None", "Shuffle", "Randomize"]
        self.enemies_dropdown = ttk.Combobox(self.enemies_frame, textvariable=self.enemies_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.enemies_dropdown['values'] = self.enemies_options
        self.enemies_dropdown['state'] = 'readonly'
        self.enemies_dropdown.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.non_softlock_enemies_button = tk.Button(self.enemies_frame, text='Select All\nNon-Softlock Enemies', foreground=self.white, background=self.red, font=(self.font_type, self.small_font_size), command=(lambda: self._select_non_softlock_enemies()))
        self.non_softlock_enemies_button.grid(row=0, column=2, padx=self.padx, pady=self.pady, sticky='e')
        self.clear_enemies_button = tk.Button(self.enemies_frame, text='Remove All\nEnemies', foreground=self.white, background=self.red, font=(self.font_type, self.small_font_size), command=(lambda: self._remove_all_enemies()))
        self.clear_enemies_button.grid(row=0, column=3, padx=self.padx, pady=self.pady, sticky='e')
        self.enemy_checklist_frame = tk.LabelFrame(self.enemies_frame, text="Enemies To Include In Randomization:", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.enemy_checklist_frame.grid(row=1, column=0, columnspan=6, padx=self.padx, pady=self.pady, sticky='w')
        self.enemy_checklist_frame["borderwidth"] = 0
        self.enemy_checklist_frame["highlightthickness"] = 0
        self.softlock_enemies_text = tk.Label(self.enemy_checklist_frame, text="WARNING: Enemies with * may softlock/crash the game. Check the box at your own risk.", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.softlock_enemies_text.grid(row=0, column=0, columnspan=6, padx=self.padx, pady=self.pady, sticky='w')
        self.enemy_checkbox_dict = {}
        for enemy_count, enemy_name in enumerate(sorted(master_enemy_dict)):
            self.enemy_checkbox_dict[enemy_name] = tk.IntVar()
            enemy_checkbutton = tk.Checkbutton(self.enemy_checklist_frame, text=enemy_name, variable=self.enemy_checkbox_dict[enemy_name], foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size), width=13, anchor="w")
            enemy_checkbutton.grid(row=(enemy_count // 4) + 1, column=(enemy_count % 4), padx=self.padx, pady=self.pady, sticky='w')
        #####################
        ### AESTHETIC TAB ###
        #####################
        self._aesthetic_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._aesthetic_tab, text="Aesthetics")
        # BK Model
        self.bk_model_frame = tk.LabelFrame(self._aesthetic_tab, text="Banjo-Kazooie Model Color", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.bk_model_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.bk_model_ttp_canvas = tk.Label(self.bk_model_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.bk_model_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.bk_model_frame_ttp = self.CreateToolTip(self.bk_model_ttp_canvas, self, tool_tips_dict["BK_COLOR"]["FRAME"])
        self.bk_model_json = read_json(f"{self.cwd}Randomization_Processes/Misc_Manipulation/Model_Data/BK_Model_Presets.json")
        self.bk_model_var = tk.StringVar(self.bk_model_frame)
        self.bk_model_options = ["Seed Determined Preset", "Seed Determined Colors"]
        for item in sorted(self.bk_model_json):
            self.bk_model_options.append(item)
        self.bk_model_var.set(self.bk_model_options[0])
        self.bk_model_dropdown = ttk.Combobox(self.bk_model_frame, textvariable=self.bk_model_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size), width=30)
        self.bk_model_dropdown['values'] = self.bk_model_options
        self.bk_model_dropdown['state'] = 'readonly'
        self.bk_model_dropdown.grid(row=0, column=1, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.random_bk_model_preset_button = tk.Button(self.bk_model_frame, text='Random Preset', command=self._random_bk_model_preset, foreground=self.white, background=self.red, font=(self.font_type, self.small_font_size))
        self.random_bk_model_preset_button.grid(row=0, column=3, padx=self.padx, pady=self.pady, sticky='w')
        if(self.bk_model_var.get() in ["Seed Determined Preset", "Seed Determined Colors"]):
            self.bk_model_image = tk.PhotoImage(file=f"{self.cwd}Pictures/BK_Models/Default.png")
        else:
            self.bk_model_image = tk.PhotoImage(file=f"{self.cwd}Pictures/BK_Models/{self.bk_model_var.get()}.png")
        self.bk_model_image_label = tk.Label(self.bk_model_frame, text='Preview', foreground=curr_background_color, background=curr_background_color, font=(self.font_type, self.small_font_size), image=self.bk_model_image)
        self.bk_model_image_label.grid(row=0, column=4, padx=self.padx, pady=self.pady, sticky='w')
        
        self.banjo_fur_text = tk.Label(self.bk_model_frame, text="Banjo's Fur", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.banjo_fur_text.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.banjo_fur_var = tk.StringVar(self.bk_model_frame)
        self.banjo_fur_entry = tk.Entry(self.bk_model_frame, textvariable=self.banjo_fur_var, width=9)
        self.banjo_fur_entry.grid(row=1, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.tooth_necklace_text = tk.Label(self.bk_model_frame, text="Tooth Necklace", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.tooth_necklace_text.grid(row=1, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.tooth_necklace_var = tk.StringVar(self.bk_model_frame)
        self.tooth_necklace_entry = tk.Entry(self.bk_model_frame, textvariable=self.tooth_necklace_var, width=9)
        self.tooth_necklace_entry.grid(row=1, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.banjo_skin_text = tk.Label(self.bk_model_frame, text="Banjo's Skin", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.banjo_skin_text.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.banjo_skin_var = tk.StringVar(self.bk_model_frame)
        self.banjo_skin_entry = tk.Entry(self.bk_model_frame, textvariable=self.banjo_skin_var, width=9)
        self.banjo_skin_entry.grid(row=2, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.banjo_feet_text = tk.Label(self.bk_model_frame, text="Banjo's Toes", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.banjo_feet_text.grid(row=2, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.banjo_feet_var = tk.StringVar(self.bk_model_frame)
        self.banjo_feet_entry = tk.Entry(self.bk_model_frame, textvariable=self.banjo_feet_var, width=5)
        self.banjo_feet_entry.grid(row=2, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_primary_text = tk.Label(self.bk_model_frame, text="Kazooie Primary", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.kazooie_primary_text.grid(row=3, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_primary_var = tk.StringVar(self.bk_model_frame)
        self.kazooie_primary_entry = tk.Entry(self.bk_model_frame, textvariable=self.kazooie_primary_var, width=9)
        self.kazooie_primary_entry.grid(row=3, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_wing_primary_text = tk.Label(self.bk_model_frame, text="Wing Primary", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.kazooie_wing_primary_text.grid(row=3, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_wing_primary_var = tk.StringVar(self.bk_model_frame)
        self.kazooie_wing_primary_entry = tk.Entry(self.bk_model_frame, textvariable=self.kazooie_wing_primary_var, width=5)
        self.kazooie_wing_primary_entry.grid(row=3, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_secondary_text = tk.Label(self.bk_model_frame, text="Kazooie Secondary", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.kazooie_secondary_text.grid(row=4, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_secondary_var = tk.StringVar(self.bk_model_frame)
        self.kazooie_secondary_entry = tk.Entry(self.bk_model_frame, textvariable=self.kazooie_secondary_var, width=9)
        self.kazooie_secondary_entry.grid(row=4, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_wing_secondary_text = tk.Label(self.bk_model_frame, text="Wing Secondary", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.kazooie_wing_secondary_text.grid(row=4, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.kazooie_wing_secondary_var = tk.StringVar(self.bk_model_frame)
        self.kazooie_wing_secondary_entry = tk.Entry(self.bk_model_frame, textvariable=self.kazooie_wing_secondary_var, width=5)
        self.kazooie_wing_secondary_entry.grid(row=4, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.backpack_text = tk.Label(self.bk_model_frame, text="Backpack", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.backpack_text.grid(row=5, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.backpack_var = tk.StringVar(self.bk_model_frame)
        self.backpack_entry = tk.Entry(self.bk_model_frame, textvariable=self.backpack_var, width=9)
        self.backpack_entry.grid(row=5, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.wading_boots_text = tk.Label(self.bk_model_frame, text="Wading Boots", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.wading_boots_text.grid(row=5, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.wading_boots_var = tk.StringVar(self.bk_model_frame)
        self.wading_boots_entry = tk.Entry(self.bk_model_frame, textvariable=self.wading_boots_var, width=9)
        self.wading_boots_entry.grid(row=5, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.shorts_vertex_text = tk.Label(self.bk_model_frame, text="Shorts Main", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.shorts_vertex_text.grid(row=6, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.shorts_vertex_var = tk.StringVar(self.bk_model_frame)
        self.shorts_vertex_entry = tk.Entry(self.bk_model_frame, textvariable=self.shorts_vertex_var, width=9)
        self.shorts_vertex_entry.grid(row=6, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.shorts_texture_text = tk.Label(self.bk_model_frame, text="Shorts Front", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.shorts_texture_text.grid(row=6, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.shorts_texture_var = tk.StringVar(self.bk_model_frame)
        self.shorts_texture_entry = tk.Entry(self.bk_model_frame, textvariable=self.shorts_texture_var, width=9)
        self.shorts_texture_entry.grid(row=6, column=4, padx=self.padx, pady=self.pady, sticky='w')
        self.bk_model_var.trace('w', self._update_bk_model)
        # Sounds/Music
        self.sound_music_frame = tk.LabelFrame(self._aesthetic_tab, text="Short Sounds, Fanfare/Jingles, & Looped Music", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.sound_music_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.short_sounds_ttp_canvas = tk.Label(self.sound_music_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.short_sounds_ttp_canvas.grid(row=0, column=0, rowspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.short_sounds_checkbutton_ttp = self.CreateToolTip(self.short_sounds_ttp_canvas, self, tool_tips_dict["SOUNDS_MUSIC"]["FULL_DESCRIPTION"])
        self.short_sounds_var = tk.IntVar()
        self.short_sounds_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Shuffle Sounds", variable=self.short_sounds_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.short_sounds_checkbutton.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Jingles
        self.jingles_var = tk.IntVar()
        self.jingle_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Shuffle Jingles", variable=self.jingles_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.jingle_checkbutton.grid(row=0, column=3, padx=self.padx, pady=self.pady, sticky='w')
        # Music
        self.music_var = tk.IntVar()
        self.music_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Shuffle Music", variable=self.music_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.music_checkbutton.grid(row=0, column=5, padx=self.padx, pady=self.pady, sticky='w')
        # Beta Sounds
        self.beta_sounds_var = tk.IntVar()
        self.beta_sounds_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Include Beta Sounds", variable=self.beta_sounds_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.beta_sounds_checkbutton.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Jarring Sounds
        self.jarring_sounds_var = tk.IntVar()
        self.jarring_sounds_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Include Jarring Sounds", variable=self.jarring_sounds_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.jarring_sounds_checkbutton.grid(row=1, column=3, padx=self.padx, pady=self.pady, sticky='w')
        # Sprites/Textures
        self.texture_frame = tk.LabelFrame(self._aesthetic_tab, text="Sprites & Textures", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.texture_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.skybox_ttp_canvas = tk.Label(self.texture_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.skybox_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.skybox_checkbutton_ttp = self.CreateToolTip(self.skybox_ttp_canvas, self, tool_tips_dict["SPRITES_TEXTURES"]["SHUFFLE_SKYBOXES"])
        self.skybox_var = tk.IntVar()
        self.skybox_checkbutton = tk.Checkbutton(self.texture_frame, text="Shuffle Skyboxes", variable=self.skybox_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.skybox_checkbutton.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.talking_sprite_ttp_canvas = tk.Label(self.texture_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.talking_sprite_ttp_canvas.grid(row=0, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.talking_sprite_checkbutton_ttp = self.CreateToolTip(self.talking_sprite_ttp_canvas, self, tool_tips_dict["SPRITES_TEXTURES"]["SHUFFLE_TALKING_SPRITES"])
        self.talking_sprite_var = tk.IntVar()
        self.talking_sprite_checkbutton = tk.Checkbutton(self.texture_frame, text="Shuffle Talking Sprites", variable=self.talking_sprite_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.talking_sprite_checkbutton.grid(row=0, column=3, padx=self.padx, pady=self.pady, sticky='w')
        ###########################
        ### CUSTOM SETTINGS TAB ###
        ###########################
        self._custom_settings_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._custom_settings_tab, text="MAP Config")
        self.customizable_frame = tk.LabelFrame(self._custom_settings_tab, text="Models, Animations, & Properties", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.customizable_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.customizable_frame["borderwidth"] = 0
        self.customizable_frame["highlightthickness"] = 0
        customizable_disclaimer_text = (
            "    WARNING:\n" +
            "        The Models/Animations/Properties configurations have been tested\n"+
            "        mainly on Emulator, but barely Everdrive. If playing on Everdrive,\n" +
            "        enable at own risk."
            )
        self.customizable_disclaimer_label = tk.Label(self.customizable_frame, text=customizable_disclaimer_text, foreground=self.black, background=curr_background_color, font=(self.font_type, 12), anchor="w", justify="left")
        self.customizable_disclaimer_label.grid(row=0, column=0, columnspan=4, padx=self.padx, pady=self.pady, sticky='w')
        self.customizable_ttp_canvas = tk.Label(self.customizable_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.customizable_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.customizable_frame_ttp = self.CreateToolTip(self.customizable_ttp_canvas, self, tool_tips_dict["CUSTOMIZABLE"]["MODELS"])
        self.all_aesthetics_button = tk.Button(self.customizable_frame, text='Select All\nCustom Aesthetic', foreground=self.white, background=self.red, font=(self.font_type, self.small_font_size), command=(lambda: self._all_custom_aesthetics()))
        self.all_aesthetics_button.grid(row=1, column=1, padx=self.padx, pady=self.pady)
        self.no_customization_button = tk.Button(self.customizable_frame, text='Uncheck All\nCustom Options', foreground=self.white, background=self.red, font=(self.font_type, self.small_font_size), command=(lambda: self._no_customization()))
        self.no_customization_button.grid(row=1, column=2, padx=self.padx, pady=self.pady)
        self.random_customization_button = tk.Button(self.customizable_frame, text='Random Customs\nAnd Hide Options', foreground=self.white, background=self.red, font=(self.font_type, self.small_font_size), command=(lambda: self._random_customization()), width=15)
        self.random_customization_button.grid(row=1, column=3, padx=self.padx, pady=self.pady)
        self.customizable_checklist_frame = tk.LabelFrame(self.customizable_frame, text="(A) = Aesthetical Only; (P) = Contains Property Changes", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.customizable_checklist_frame.grid(row=2, column=0, columnspan=6, padx=self.padx, pady=self.pady, sticky='w')
        self.customizable_checklist_frame["borderwidth"] = 0
        self.customizable_checklist_frame["highlightthickness"] = 0
        self.customizable_checkbox_dict = {}
        self.hiding_customization = False
        self.customization_checkbuttons = []
        for json_count, json_name in enumerate(sorted(os.listdir(f"{self.cwd}/Randomization_Processes/Misc_Manipulation/Models_Animations_Properties/JSON_Files/"))):
            display_name = json_name.split(".json")[0]
            self.customizable_checkbox_dict[display_name] = tk.IntVar()
            custom_checkbutton = tk.Checkbutton(self.customizable_checklist_frame, text=display_name, variable=self.customizable_checkbox_dict[display_name], foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size), width=13, anchor="w")
            custom_checkbutton.grid(row=(json_count // 4) + 2, column=(json_count % 4), padx=self.padx, pady=self.pady, sticky='w')
            self.customization_checkbuttons.append(custom_checkbutton)
        ##########################
        ### WORLD SPECIFIC TAB ###
        ##########################
        self._world_specific_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._world_specific_tab, text="Worlds")
        self._world_specific_tab_control = ttk.Notebook(self._world_specific_tab, width=self.app_window.winfo_width())
        # Spiral Mountain
        # Gruntilda's Lair
        curr_background_color = "#660066"
        self._gruntildas_lair_tab = ttk.Frame(self._world_specific_tab_control, width=10)
        self._world_specific_tab_control.add(self._gruntildas_lair_tab, text="GL")
        self.gruntildas_lair_frame = tk.LabelFrame(self._gruntildas_lair_tab, text="Gruntilda's Lair", foreground=self.white, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.gruntildas_lair_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.gruntildas_lair_frame["borderwidth"] = 0
        self.gruntildas_lair_frame["highlightthickness"] = 0
        self.skip_furnace_fun_ttp_canvas = tk.Label(self.gruntildas_lair_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color)
        self.skip_furnace_fun_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.skip_furnace_fun_checkbox_ttp = self.CreateToolTip(self.skip_furnace_fun_ttp_canvas, self, tool_tips_dict["GRUNTILDAS_LAIR"]["SKIP_FURNACE_FUN_AND_BRENTILDA"])
        self.skip_furnace_fun_var = tk.IntVar()
        self.skip_furnace_fun_checkbox = tk.Checkbutton(self.gruntildas_lair_frame, text="Skip Furnace Fun/Brentilda Rando Hints", variable=self.skip_furnace_fun_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.skip_furnace_fun_checkbox.grid(row=0, column=1, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.remove_magic_barriers_ttp_canvas = tk.Label(self.gruntildas_lair_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.remove_magic_barriers_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.remove_magic_barriers_checkbox_ttp = self.CreateToolTip(self.remove_magic_barriers_ttp_canvas, self, tool_tips_dict["GRUNTILDAS_LAIR"]["NO_DETRANSFORMATIONS"])
        self.remove_magic_barriers_var = tk.IntVar()
        self.remove_magic_barriers_checkbox = tk.Checkbutton(self.gruntildas_lair_frame, text="No Detransformations", variable=self.remove_magic_barriers_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.remove_magic_barriers_checkbox.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.gruntilda_difficulty_ttp_canvas = tk.Label(self.gruntildas_lair_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.gruntilda_difficulty_ttp_canvas.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.gruntilda_difficulty_checkbox_ttp = self.CreateToolTip(self.gruntilda_difficulty_ttp_canvas, self, tool_tips_dict["GRUNTILDAS_LAIR"]["HARDER_FINAL_BATTLE"])
        self.gruntilda_difficulty_text = tk.Label(self.gruntildas_lair_frame, text="Final Battle Difficulty?\n0 For Default; 3 For Hard", foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.gruntilda_difficulty_text.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.gruntilda_difficulty_var = tk.IntVar()
        self.gruntilda_difficulty_scale = tk.Scale(self.gruntildas_lair_frame, from_=0, to=3, orient=tkinter.HORIZONTAL, variable=self.gruntilda_difficulty_var, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.gruntilda_difficulty_scale.grid(row=2, column=2, columnspan=2, padx=self.padx, pady=self.pady, sticky='n')
        self.monster_house_var = tk.IntVar()
        self.monster_house_checkbox = tk.Checkbutton(self.gruntildas_lair_frame, text="Monster House", variable=self.monster_house_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.monster_house_checkbox.grid(row=3, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.what_floor_var = tk.IntVar()
        self.what_floor_checkbox = tk.Checkbutton(self.gruntildas_lair_frame, text="What Floor?", variable=self.what_floor_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.what_floor_checkbox.grid(row=3, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.grunty_size_var = tk.IntVar()
        self.grunty_size_checkbox = tk.Checkbutton(self.gruntildas_lair_frame, text="Mini Me", variable=self.grunty_size_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.grunty_size_checkbox.grid(row=4, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Mumbo's Mountain
        curr_background_color = "#009999"
        self._mumbos_mountain_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._mumbos_mountain_tab, text="MM")
        self.mumbos_mountain_frame = tk.LabelFrame(self._mumbos_mountain_tab, text="Mumbo's Mountain", foreground=self.white, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.mumbos_mountain_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.mumbos_mountain_frame["borderwidth"] = 0
        self.mumbos_mountain_frame["highlightthickness"] = 0
        self.flowers_ttp_canvas = tk.Label(self.mumbos_mountain_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.flowers_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.flowers_checkbox_ttp = self.CreateToolTip(self.flowers_ttp_canvas, self, tool_tips_dict["MUMBOS_MOUNTAIN"]["INCLUDE_FLOWERS"])
        self.flowers_var = tk.IntVar()
        self.flowers_checkbox = tk.Checkbutton(self.mumbos_mountain_frame, text="Include Flowers (Shuffling/Randomizing)", variable=self.flowers_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.flowers_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Treasure Trove Cove
        curr_background_color = "#DDDD00"
        self._treasure_trove_cove_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._treasure_trove_cove_tab, text="TTC")
        self.treasure_trove_cove_frame = tk.LabelFrame(self._treasure_trove_cove_tab, text="Treasure Trove Cove", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.treasure_trove_cove_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.treasure_trove_cove_frame["borderwidth"] = 0
        self.treasure_trove_cove_frame["highlightthickness"] = 0
        self.scattered_structs_ttp_canvas = tk.Label(self.treasure_trove_cove_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.scattered_structs_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.scattered_structs_checkbox_ttp = self.CreateToolTip(self.scattered_structs_ttp_canvas, self, tool_tips_dict["TREASURE_TROVE_COVE"]["SCATTERED_STRUCTS"])
        self.scattered_structs_var = tk.IntVar()
        self.scattered_structs_checkbox = tk.Checkbutton(self.treasure_trove_cove_frame, text="Scattered Notes/Eggs/Feathers", variable=self.scattered_structs_var, selectcolor=curr_background_color, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.scattered_structs_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.super_slippery_ttc_ttp_canvas = tk.Label(self.treasure_trove_cove_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.super_slippery_ttc_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.super_slippery_ttc_checkbox_ttp = self.CreateToolTip(self.super_slippery_ttc_ttp_canvas, self, tool_tips_dict["TREASURE_TROVE_COVE"]["SUPER_SLIPPERY_SAND"])
        self.super_slippery_ttc_var = tk.IntVar()
        self.super_slippery_ttc_checkbox = tk.Checkbutton(self.treasure_trove_cove_frame, text="Super Slippery Sand", variable=self.super_slippery_ttc_var, selectcolor=curr_background_color, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.super_slippery_ttc_checkbox.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Clanker's Cavern
        curr_background_color = "#808080"
        self._clankers_cavern_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._clankers_cavern_tab, text="CC")
        self.clankers_cavern_frame = tk.LabelFrame(self._clankers_cavern_tab, text="Clanker's Cavern", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.clankers_cavern_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.clankers_cavern_frame["borderwidth"] = 0
        self.clankers_cavern_frame["highlightthickness"] = 0
        self.hard_rings_ttp_canvas = tk.Label(self.clankers_cavern_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.hard_rings_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.hard_rings_checkbox_ttp = self.CreateToolTip(self.hard_rings_ttp_canvas, self, tool_tips_dict["CLANKERS_CAVERN"]["SHUFFLE_CLANKER_RING_ORDER"])
        self.hard_rings_var = tk.IntVar()
        self.hard_rings_checkbox = tk.Checkbutton(self.clankers_cavern_frame, text="Shuffle Clanker Ring Order", variable=self.hard_rings_var, selectcolor=curr_background_color, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.hard_rings_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Bubblegloop Swamp
        curr_background_color = "#006600"
        self._bubblegloop_swamp_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._bubblegloop_swamp_tab, text="BGS")
        self.bubblegloop_swamp_frame = tk.LabelFrame(self._bubblegloop_swamp_tab, text="Bubblegloop Swamp", foreground=self.white, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.bubblegloop_swamp_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.bubblegloop_swamp_frame["borderwidth"] = 0
        self.bubblegloop_swamp_frame["highlightthickness"] = 0
        self.croctus_ttp_canvas = tk.Label(self.bubblegloop_swamp_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.croctus_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.croctus_checkbox_ttp = self.CreateToolTip(self.croctus_ttp_canvas, self, tool_tips_dict["BUBBLEGLOOP_SWAMP"]["SHUFFLE_CROCTUS_ORDER"])
        self.croctus_var = tk.IntVar()
        self.croctus_checkbox = tk.Checkbutton(self.bubblegloop_swamp_frame, text="Shuffle Croctus Order", variable=self.croctus_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.croctus_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.mr_vile_ttp_canvas = tk.Label(self.bubblegloop_swamp_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.mr_vile_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.mr_vile_checkbox_ttp = self.CreateToolTip(self.mr_vile_ttp_canvas, self, tool_tips_dict["BUBBLEGLOOP_SWAMP"]["MR_VILE_BIGGER_BADDER_CROCODILE"])
        self.mr_vile_var = tk.IntVar()
        self.mr_vile_checkbox = tk.Checkbutton(self.bubblegloop_swamp_frame, text="Mr. Vile: Bigger, Badder Crocodile", variable=self.mr_vile_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.mr_vile_checkbox.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.tiptup_choir_ttp_canvas = tk.Label(self.bubblegloop_swamp_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.tiptup_choir_ttp_canvas.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.tiptup_choir_checkbox_ttp = self.CreateToolTip(self.tiptup_choir_ttp_canvas, self, tool_tips_dict["BUBBLEGLOOP_SWAMP"]["TIPTUP_CHOIR_NO_ASSIGNED_SEATS"])
        self.tiptup_choir_var = tk.IntVar()
        self.tiptup_choir_checkbox = tk.Checkbutton(self.bubblegloop_swamp_frame, text="Tiptup Choir: No Assigned Seats", variable=self.tiptup_choir_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.tiptup_choir_checkbox.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Freezeezy Peak
        curr_background_color = "#66CCCC"
        self._freezeezy_peak_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._freezeezy_peak_tab, text="FP")
        self.freezeezy_peak_frame = tk.LabelFrame(self._freezeezy_peak_tab, text="Freezeezy Peak", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.freezeezy_peak_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.freezeezy_peak_frame["borderwidth"] = 0
        self.freezeezy_peak_frame["highlightthickness"] = 0
        self.hard_races_ttp_canvas = tk.Label(self.freezeezy_peak_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.hard_races_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.hard_races_checkbox_ttp = self.CreateToolTip(self.hard_races_ttp_canvas, self, tool_tips_dict["FREEZEEZY_PEAK"]["BOGGY_RACES_MOVED_FLAGS"])
        self.hard_races_var = tk.IntVar()
        self.hard_races_checkbox = tk.Checkbutton(self.freezeezy_peak_frame, text="Boggy Races: Moved Flags", variable=self.hard_races_var, selectcolor=curr_background_color, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.hard_races_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Gobi's Valley
        curr_background_color = "#AA6600"
        self._gobis_valley_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._gobis_valley_tab, text="GV")
        self.gobis_valley_frame = tk.LabelFrame(self._gobis_valley_tab, text="Gobi's Valley", foreground=self.white, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.gobis_valley_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.gobis_valley_frame["borderwidth"] = 0
        self.gobis_valley_frame["highlightthickness"] = 0
        self.ancient_ones_ttp_canvas = tk.Label(self.gobis_valley_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.ancient_ones_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.ancient_ones_checkbox_ttp = self.CreateToolTip(self.ancient_ones_ttp_canvas, self, tool_tips_dict["GOBIS_VALLEY"]["SHUFFLED_ANCIENT_ONES_ORDER"])
        self.ancient_ones_var = tk.IntVar()
        self.ancient_ones_checkbox = tk.Checkbutton(self.gobis_valley_frame, text="Shuffle Ancient Ones Order", variable=self.ancient_ones_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.ancient_ones_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.maze_jinxy_heads_ttp_canvas = tk.Label(self.gobis_valley_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.maze_jinxy_heads_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.maze_jinxy_heads_checkbox_ttp = self.CreateToolTip(self.maze_jinxy_heads_ttp_canvas, self, tool_tips_dict["GOBIS_VALLEY"]["SHUFFLE_MAZE_JINXY_HEADS_ORDER"])
        self.maze_jinxy_heads_var = tk.IntVar()
        self.maze_jinxy_heads_checkbox = tk.Checkbutton(self.gobis_valley_frame, text="Shuffle Maze Jinxy Heads Order", variable=self.maze_jinxy_heads_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.maze_jinxy_heads_checkbox.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.matching_puzzle_ttp_canvas = tk.Label(self.gobis_valley_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.matching_puzzle_ttp_canvas.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.matching_puzzle_checkbox_ttp = self.CreateToolTip(self.matching_puzzle_ttp_canvas, self, "Randomized Matching Puzzle Not Implemented Yet")
        self.matching_puzzle_var = tk.IntVar()
        self.matching_puzzle_checkbox = tk.Checkbutton(self.gobis_valley_frame, text="Randomize Matching Puzzle", variable=self.matching_puzzle_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.matching_puzzle_checkbox.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Mad Monster Mansion
        curr_background_color = "#000033"
        self._mad_monster_mansion_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._mad_monster_mansion_tab, text="MMM")
        self.mad_monster_mansion_frame = tk.LabelFrame(self._mad_monster_mansion_tab, text="Mad Monster Mansion", foreground=self.white, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.mad_monster_mansion_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.mad_monster_mansion_frame["borderwidth"] = 0
        self.mad_monster_mansion_frame["highlightthickness"] = 0
        self.lit_pots_ttp_canvas = tk.Label(self.mad_monster_mansion_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.lit_pots_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.lit_pots_checkbox_ttp = self.CreateToolTip(self.lit_pots_ttp_canvas, self, tool_tips_dict["MAD_MONSTER_MANSION"]["POTS_ARE_LIT"])
        self.lit_pots_var = tk.IntVar()
        self.lit_pots_checkbox = tk.Checkbutton(self.mad_monster_mansion_frame, text="Pots Are Lit", variable=self.lit_pots_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.lit_pots_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.lit_pots_ttp_canvas = tk.Label(self.mad_monster_mansion_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.lit_pots_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.motzand_keys_checkbox_ttp = self.CreateToolTip(self.lit_pots_ttp_canvas, self, tool_tips_dict["MAD_MONSTER_MANSION"]["MOTZAND_KEYS"])
        self.motzand_keys_var = tk.IntVar()
        self.motzand_keys_checkbox = tk.Checkbutton(self.mad_monster_mansion_frame, text="Randomize Motzand's Song", variable=self.motzand_keys_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.motzand_keys_checkbox.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Rusty Bucket Bay
        curr_background_color = "#660000"
        self._rusty_bucket_bay_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._rusty_bucket_bay_tab, text="RBB")
        self.rusty_bucket_bay_frame = tk.LabelFrame(self._rusty_bucket_bay_tab, text="Rusty Bucket Bay", foreground=self.white, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.rusty_bucket_bay_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.rusty_bucket_bay_frame["borderwidth"] = 0
        self.rusty_bucket_bay_frame["highlightthickness"] = 0
        self.buttons_ttp_canvas = tk.Label(self.rusty_bucket_bay_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.buttons_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.buttons_checkbox_ttp = self.CreateToolTip(self.buttons_ttp_canvas, self, tool_tips_dict["RUSTY_BUCKET_BAY"]["RANDOMIZED_BUTTON_COMBO"])
        self.buttons_var = tk.IntVar()
        self.buttons_checkbox = tk.Checkbutton(self.rusty_bucket_bay_frame, text="Randomized Button Combo", variable=self.buttons_var, selectcolor=curr_background_color, foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.buttons_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Click Clock Wood
        curr_background_color = "#AA5500"
        self._click_clock_wood_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._click_clock_wood_tab, text="CCW")
        self.click_clock_wood_frame = tk.LabelFrame(self._click_clock_wood_tab, text="Click Clock Wood", foreground=self.white, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.click_clock_wood_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.click_clock_wood_frame["borderwidth"] = 0
        self.click_clock_wood_frame["highlightthickness"] = 0
        self.ccw_ttp_canvas = tk.Label(self.click_clock_wood_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.ccw_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.ccw_checkbox_ttp = self.CreateToolTip(self.ccw_ttp_canvas, self, tool_tips_dict["CLICK_CLOCK_WOOD"]["SHUFFLE_BY"])
        self.ccw_text = tk.Label(self.click_clock_wood_frame, text="Shuffle By:", foreground=self.white, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.ccw_text.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.ccw_var = tk.StringVar(self.click_clock_wood_frame)
        self.ccw_options = ["Season", "Within World"]
        self.ccw_dropdown = ttk.Combobox(self.click_clock_wood_frame, textvariable=self.ccw_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.ccw_dropdown['values'] = self.ccw_options
        self.ccw_dropdown['state'] = 'readonly'
        self.ccw_dropdown.grid(row=0, column=2, padx=self.padx, pady=self.pady, sticky='w')
        #########################################
        ### END OF WORLD SPECIFIC TAB CONTROL ###
        #########################################
        self._world_specific_tab_control.pack(expand=1, fill="both")
        #########################
        ### MISCELLANEOUS TAB ###
        #########################
        self._misc_tab = ttk.Frame(self._tab_control)
        self._tab_control.add(self._misc_tab, text="Misc.")
        curr_background_color = "#F3E5AB"
        self.misc_frame = tk.LabelFrame(self._misc_tab, text="Miscellaneous", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.misc_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.misc_frame["borderwidth"] = 0
        self.misc_frame["highlightthickness"] = 0
        # Remove Files
        self.remove_files_ttp_canvas = tk.Label(self.misc_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.remove_files_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.remove_files_checkbutton_ttp = self.CreateToolTip(self.remove_files_ttp_canvas, self, tool_tips_dict["MISC_OPTIONS"]["REMOVE_EXTRA_FILES"])
        self.remove_files_var = tk.IntVar()
        self.remove_files_checkbutton = tk.Checkbutton(self.misc_frame, text="Remove Extra Files", variable=self.remove_files_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.remove_files_checkbutton.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Tool Tips
        self.tool_tips_ttp_canvas = tk.Label(self.misc_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.tool_tips_ttp_canvas.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.tool_tips_checkbutton_ttp = self.CreateToolTip(self.tool_tips_ttp_canvas, self, tool_tips_dict["MISC_OPTIONS"]["TOOL_TIPS"])
        self.tool_tips_var = tk.IntVar()
        self.tool_tips_checkbutton = tk.Checkbutton(self.misc_frame, text="Show Tool Tips", variable=self.tool_tips_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.tool_tips_checkbutton.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        ##########################
        ### END OF TAB CONTROL ###
        ##########################
        self._tab_control.pack(expand=1, fill="both")
        #########################
        ### CONFIG AND SUBMIT ###
        #########################
        self.config_and_submit = tk.LabelFrame(self.app_window)
        self.config_and_submit["borderwidth"] = 0
        self.config_and_submit["highlightthickness"] = 0
        self.config_and_submit.pack(expand=tk.TRUE, fill=tk.BOTH)
        # Load
        self._load_config_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Load_Config.png")
        self.load_config_button = tk.Button(self.config_and_submit, text='Load Config', command=self._load_configuration, image=self._load_config_image, background=self.generic_background_color)
        self.load_config_button.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Save
        self._save_config_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Save_Config.png")
        self.save_config_button = tk.Button(self.config_and_submit, text='Save Config', command=self._save_current_configuration, image=self._save_config_image, background=self.generic_background_color)
        self.save_config_button.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Read Me
        self._read_me_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Read_Me.png")
        self.read_me = tk.Button(self.config_and_submit, text='Open ReadMe', command=(lambda: self._open_file(f"{self.cwd}ReadMe.txt")), image=self._read_me_image, background=self.generic_background_color)
        self.read_me.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')
        # Submit
        self._submit_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Submit.png")
        self.submit = tk.Button(self.config_and_submit, text='Submit', command=self._submit, image=self._submit_image, background=self.generic_background_color)
        self.submit.pack(expand=tk.TRUE, fill=tk.BOTH, side='left')
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

############
### MAIN ###
############

if __name__ == '__main__':
    user_app = User_GUI_Class()
    user_app._main()
