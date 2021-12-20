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
            "    Recommended using FINAL NOTE DOOR feature.\n" +
            "ALL NOTES:\n" +
            "    All eggs and feathers become notes. Brentildas are replaced\n" +
            "    with egg and feather refills. The refill at that Brentilda\n" +
            "    location is random.",
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
            "    exploration. Logic may not work if worlds are opened out of order.",
        },
    "WITHIN_WORLD_WARPS": {
        "FRAME": 
            "NONE:\n" +
            "    Skips the setting.\n" +
            "SHUFFLE:\n" +
            "    Shuffles the warps that are within the world."
        },
    "STARTING_AREA": {
        "NEW_GAME":
            "Spawns you at the location upon a new game.",
        "LOAD_GAME":
            "Spawns you at the location upon a new game."
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
    "CUSTOMIZABLE": {
        "MODELS": "Swaps, shuffles, and randomizes some models.",
        "ANIMATIONS": "Swaps, shuffles, and randomizes some animations.",
        "PROPERTIES": "Swaps, shuffles, and randomizes some properties.",
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
from random import randint, choice

####################
### FILE IMPORTS ###
####################

from Progression_GUI import Progression_GUI_Class
from Randomization_Processes.Common_Functions import read_json, space_in_directory, leading_zeros
from Randomization_Processes.Dicts_And_Lists.Game_Engine import start_level_ids
from Randomization_Processes.Dicts_And_Lists.Enemies import master_enemy_dict

#################
### VARIABLES ###
#################

BK_RANDO_VERSION = "2.0"

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
    # Mumbo Jumbo Talking
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
    error_window.after(0, update_bottles_gif, 0)
    error_window.mainloop()

######################
### USER GUI CLASS ###
######################

class User_GUI_Class():
    '''Creates a GUI where users give the directory of the ROM file, select options for the randomization, and optionally provide a seed value'''
    def __init__(self):
        '''Creates the Tkinter GUI'''
        self.cwd = os.getcwd() + "/"
        self.app_window = tk.Tk()
        self.app_window.winfo_toplevel().title(f"Banjo-Kazooie Randomizer v{BK_RANDO_VERSION}")
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
        filename = tkinter.filedialog.askopenfilename(initialdir=self.cwd, title="Select The BK ROM File", filetype =(("Rom Files","*.z64"),("all files","*.*")) )
        if(" " in filename):
            filename = space_in_directory(filename)
        self.rom_file_entry.set(filename)
    
    def _open_file(self, file_to_open):
        '''Generic open file button. If they use this for the README, bless their hearts'''
        os.startfile(file_to_open)
    
    ###############################
    ### RANDOM BUTTON FUNCTIONS ###
    ###############################
    
    def _random_seed(self):
        '''Randomly selects a seed'''
        self.seed_value.set(str(randint(10000000, 19940303)))
    
    def _random_note_value(self):
        '''Randomly selects a note value'''
        self.final_note_door_var.set("Final Note Door Only")
        if(self.struct_var.get() == "All Notes"):
            self.final_note_door_value.set(str(randint(0, 2000)))
        else:
            self.final_note_door_value.set(str(randint(0, 900)))
    
    def _random_puzzle_value(self):
        '''Randomly selects a puzzle value'''
        self.final_puzzle_var.set(1)
        self.final_puzzle_value.set(str(randint(0, 99)))
    
    def _random_bk_model_preset(self):
        key_list = []
        for key in self.bk_model_json:
            key_list.append(key)
        random_bk_model = choice(key_list)
        self.bk_model_var.set(random_bk_model)
    
    def _random_hex(self, digit_len):
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
    
    ######################
    ### SETTING VALUES ###
    ######################
    
    def _set_recommended_defaults(self):
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
        self.free_transformations_var.set(0),
        # Non-Flagged Objects
        self.non_flagged_object_var.set("Shuffle (World)")
        self.non_flagged_object_abnormalities_var.set(0)
        # Structs
        self.struct_var.set("Shuffle (World)")
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
        self.all_starting_moves_var.set(0)
        # Within World Warps
        self.within_world_warps_var.set("Shuffle By World")
        # Starting Area
        self.new_area_var.set("SM - Main")
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
        # Enemy Models
        self.other_model_var.set(0)
        self.animation_var.set(0)
        self.properties_var.set(0)
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
        self.tool_tips_var.set(1)
        ### World Specific ###
        # Gruntilda's Lair
        self.final_puzzle_var.set(0)
        self.final_puzzle_value.set(0)
        self.skip_furnace_fun_var.set(0)
        self.remove_magic_barriers_var.set(0)
        self.gruntilda_difficulty_var.set(0)
        self.monster_house_var.set(1)
        self.what_floor_var.set(1)
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
    
    def _load_configuration(self, button_press=True, random_file=False):
        '''Opens a chosen JSON file and sets the parameters to match those'''
        if(random_file):
            list_of_files = os.listdir(f"{self.cwd}Configurations/")
            if("Last_Used_Configuration.json" in list_of_files):
                list_of_files.remove("Last_Used_Configuration.json")
            list_of_configs = [file for file in list_of_files if(file.endswith(".json"))]
            filename = f"{self.cwd}Configurations/{choice(list_of_configs)}"
        elif(button_press):
            config_default_dir = f"{self.cwd}Configurations/"
            filename = tkinter.filedialog.askopenfilename(initialdir=config_default_dir, title="Select A JSON Config File", filetypes =(("Json Files","*.json"),("all files","*.*")))
        else:
            filename = self.cwd + "Configurations/Last_Used_Configuration.json"
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
        self.final_puzzle_var.set(json_data["Final_Puzzle"])
        self.final_puzzle_value.set(json_data["Final_Puzzle_Value"])
        self.free_transformations_var.set(json_data["Free Transformations"]),
        # Non-Flagged Objects
        self.non_flagged_object_var.set(json_data["Non_Flagged_Objects_Option"])
        self.non_flagged_object_abnormalities_var.set(json_data["Non_Flagged_Objects_Abnormalities"])
        # Structs
        self.struct_var.set(json_data["Struct_Option"])
        self.final_note_door_var.set(json_data["Final_Note_Door"])
        self.final_note_door_value.set(json_data["Final_Note_Door_Value"])
        self.before_blue_egg_carry_value.set(json_data["Before_Cheato_Blue_Eggs"]),
        self.after_blue_egg_carry_value.set(json_data["After_Cheato_Blue_Eggs"]),
        self.before_red_feather_carry_value.set(json_data["Before_Cheato_Red_Feathers"]),
        self.after_red_feather_carry_value.set(json_data["After_Cheato_Red_Feathers"]),
        self.before_gold_feather_carry_value.set(json_data["Before_Cheato_Gold_Feathers"]),
        self.after_gold_feather_carry_value.set(json_data["After_Cheato_Gold_Feathers"]),
        # World Entrances
        self.world_entrance_var.set(json_data["World_Entrance_Option"])
        self.all_starting_moves_var.set(json_data["All_Moves"])
        # Within World Warps
        self.within_world_warps_var.set(json_data["Within_World_Warps_Option"])
        # Starting World
        self.new_area_var.set(json_data["Starting_Area"])
        self.skip_intro_cutscene_var.set(json_data["Skip_Intro_Cutscene"])
        # Enemies
        self.enemies_var.set(json_data["Enemies_Option"])
        for enemy_name in self.enemy_checkbox_dict:
            self.enemy_checkbox_dict[enemy_name].set(json_data[f"Include {enemy_name}"])
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
        self.properties_var.set(json_data["Properties_Option"])
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
        self.skip_furnace_fun_var.set(json_data["Furnace_Fun_Skip"])
        self.remove_magic_barriers_var.set(json_data["Remove_Magic_Barriers"])
        self.gruntilda_difficulty_var.set(json_data["Final_Battle_Difficulty"])
        self.monster_house_var.set(json_data["Monster_House"])
        self.what_floor_var.set(json_data["What_Floor"])
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
    
    def _set_random_settings(self):
        '''Opens a chosen JSON file and sets the parameters to match those'''
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
        self.final_puzzle_value.set(randint(0, 99))
        self.free_transformations_var.set(randint(0, 1)),
        # Non-Flagged Objects
        self.non_flagged_object_var.set(choice(["None", "Shuffle (World)"]))
        self.non_flagged_object_abnormalities_var.set(randint(0, 1))
        # Structs
        self.struct_var.set(choice(["None", "Shuffle (World)", "Shuffle (Game)", "Randomize", "All Notes"]))
        self.final_note_door_var.set(choice(["Scaling Note Doors", "Final Note Door Only"]))
        if(self.struct_var.get() == "All Notes"):
            self.final_note_door_value.set(randint(0, 2000))
        else:
            self.final_note_door_value.set(randint(0, 900))
        self.before_blue_egg_carry_value.set(randint(0, 255))
        self.after_blue_egg_carry_value.set(randint(self.before_blue_egg_carry_value.get(), 255))
        self.before_red_feather_carry_value.set(randint(0, 255))
        self.after_red_feather_carry_value.set(randint(self.before_red_feather_carry_value.get(), 255))
        self.before_gold_feather_carry_value.set(randint(0, 255))
        self.after_gold_feather_carry_value.set(randint(self.before_gold_feather_carry_value.get(), 255))
        # World Entrances
        self.world_entrance_var.set(choice(["None", "Basic Shuffle", "Bottles Shuffle"]))
        self.all_starting_moves_var.set(randint(0, 1))
        # Within World Warps
        self.within_world_warps_var.set(choice(["None", "Shuffle By World", "Shuffle By Game"]))
        # Starting World
        self.new_area_var.set(choice([option for option in start_level_ids]))
        # Enemies
        self.enemies_var.set(choice(["None", "Shuffle", "Randomize"]))
        for enemy_name in self.enemy_checkbox_dict:
            self.enemy_checkbox_dict[enemy_name].set(randint(0, 1))
        ### Aesthetic Settings ###
        # BK Model
        self._random_bk_model_colors()
        # Enemy Models
        self.other_model_var.set(randint(0, 1))
        self.animation_var.set(randint(0, 1))
        self.properties_var.set(randint(0, 1))
        # Sounds/Music
        self.short_sounds_var.set(randint(0, 1))
        self.jingles_var.set(randint(0, 1))
        self.music_var.set(randint(0, 1))
        self.beta_sounds_var.set(randint(0, 1))
        # Sprites/Textures
        self.skybox_var.set(randint(0, 1))
        self.talking_sprite_var.set(randint(0, 1))
        ### Misc Settings ###
#         self.cheat_sheet_var.set(randint(0, 1))
#         self.remove_files_var.set(randint(0, 1))
#         self.tool_tips_var.set(randint(0, 1))
        ### World Specific ###
        # Gruntilda's Lair
        self.skip_furnace_fun_var.set(randint(0, 1))
        self.remove_magic_barriers_var.set(randint(0, 1))
        self.gruntilda_difficulty_var.set(randint(0, 3))
        self.monster_house_var.set(randint(0, 1))
        self.what_floor_var.set(randint(0, 1))
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
        # Rusty Bucket Bay
        self.buttons_var.set(randint(0, 1))
        # Click Clock Wood
        self.ccw_var.set(choice(["Season", "Within World"]))
    
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
            "Final_Puzzle": self.final_puzzle_var.get(),
            "Final_Puzzle_Value": self.final_puzzle_value.get(),
            "Free Transformations": self.free_transformations_var.get(),
            # Non-Flagged Objects
            "Non_Flagged_Objects_Option": self.non_flagged_object_var.get(),
            "Non_Flagged_Objects_Abnormalities": self.non_flagged_object_abnormalities_var.get(),
            # Structs
            "Struct_Option": self.struct_var.get(),
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
            "Other_Model_Option": self.other_model_var.get(),
            "Animation_Option": self.animation_var.get(),
            "Properties_Option": self.properties_var.get(),
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
            "Furnace_Fun_Skip": self.skip_furnace_fun_var.get(),
            "Remove_Magic_Barriers": self.remove_magic_barriers_var.get(),
            "Final_Battle_Difficulty": self.gruntilda_difficulty_var.get(),
            "Monster_House": self.monster_house_var.get(),
            "What_Floor": self.what_floor_var.get(),
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
        # Enemies
        for enemy_name in master_enemy_dict:
            current_config[f"Include {enemy_name}"] = self.enemy_checkbox_dict[enemy_name].get()
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
    
    #########################################
    ### VERIFY SETTINGS BEFORE SUBMITTING ###
    #########################################
    
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
            progression_app = Progression_GUI_Class(self)
            progression_app._main()
        else:
            print("It Failed")
    
    ######################
    ### FRONT END CODE ###
    ######################
    
    def _main(self):
        '''Places all of the widgest on the GUI and runs the loop for the window'''
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
        self.select_rom_button.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.rom_file_entry = tk.StringVar(self.rom_frame)
        self.rom_file_display = tk.Entry(self.rom_frame, textvariable=self.rom_file_entry, state='readonly', width=40, font=(self.font_type, self.medium_font_size))
        self.rom_file_display.grid(row=1, column=1, columnspan=2, padx=10, pady=self.pady)
        ### Seed ###
        self.seed_frame = tk.LabelFrame(self._general_tab, text="Seed", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.seed_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.random_seed_button_ttp_canvas = tk.Label(self.seed_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.random_seed_button_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        self.random_seed_button_ttp = self.CreateToolTip(self.random_seed_button_ttp_canvas, self, tool_tips_dict["SEED"]["RANDOM_SEED_BUTTON"])
        self._seed_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Seed.png")
        self.random_seed_button = tk.Button(self.seed_frame, text='Select ROM File', command=self._random_seed, image=self._seed_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.random_seed_button.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.seed_value = tk.StringVar(self.seed_frame)
        self.seed_entry = tk.Entry(self.seed_frame, textvariable=self.seed_value, width=20, font=(self.font_type, self.medium_font_size))
        self.seed_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=self.pady)
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
        self.flagged_object_softlock_checkbutton.grid(row=1, column=3, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self._jiggy_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Jiggy.png")
        self.random_puzzle_value_button = tk.Button(self.flagged_object_frame, text='Random Puzzle Value', command=self._random_puzzle_value, image=self._jiggy_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.random_puzzle_value_button.grid(row=2, column=3, padx=self.padx, pady=self.pady)
        self.final_puzzle_ttp_canvas = tk.Label(self.flagged_object_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_puzzle_ttp_canvas.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.final_puzzle_checkbox_ttp = self.CreateToolTip(self.final_puzzle_ttp_canvas, self, tool_tips_dict["GRUNTILDAS_LAIR"]["FINAL_PUZZLE"])
        self.final_puzzle_var = tk.IntVar()
        self.final_puzzle_checkbox = tk.Checkbutton(self.flagged_object_frame, text="Door Of Grunty Only", variable=self.final_puzzle_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_puzzle_checkbox.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.final_text = tk.Label(self.flagged_object_frame, text="Door of Grunty Jiggies:", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_text.grid(row=2, column=4, padx=self.padx, pady=self.pady)
        self.final_puzzle_value = tk.StringVar(self.flagged_object_frame)
        self.final_puzzle_entry = tk.Entry(self.flagged_object_frame, textvariable=self.final_puzzle_value, width=6)
        self.final_puzzle_entry.grid(row=2, column=5, padx=self.padx, pady=self.pady)
        self.free_transformations_var = tk.IntVar()
        self.free_transformations_checkbox = tk.Checkbutton(self.flagged_object_frame, text="Free Transformations", variable=self.free_transformations_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.free_transformations_checkbox.grid(row=3, column=1, padx=self.padx, pady=self.pady, sticky='w')
        # Structs
        self.struct_frame = tk.LabelFrame(self._collectables_tab, text="Notes, Blue Eggs, Red Feathers, & Gold Feathers", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.struct_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.struct_ttp_canvas = tk.Label(self.struct_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.struct_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.struct_ttp = self.CreateToolTip(self.struct_ttp_canvas, self, tool_tips_dict["STRUCTS"]["FRAME"])
        self.struct_var = tk.StringVar(self.struct_frame)
        self.struct_options = ["None", "Shuffle (World)", "Shuffle (Game)", "Randomize", "All Notes"]
        self.struct_dropdown = ttk.Combobox(self.struct_frame, textvariable=self.struct_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.struct_dropdown['values'] = self.struct_options
        self.struct_dropdown['state'] = 'readonly'
        self.struct_dropdown.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.final_note_door_ttp_canvas = tk.Label(self.struct_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_note_door_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.final_note_door_checkbox_ttp = self.CreateToolTip(self.final_note_door_ttp_canvas, self, tool_tips_dict["GRUNTILDAS_LAIR"]["FINAL_NOTE_DOOR"])
        self.final_note_door_var = tk.StringVar(self.struct_frame)
        self.note_door_options = ["Scaling Note Doors", "Final Note Door Only"]
        self.final_note_door_dropdown = ttk.Combobox(self.struct_frame, textvariable=self.final_note_door_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_note_door_dropdown['values'] = self.note_door_options
        self.final_note_door_dropdown['state'] = 'readonly'
        self.final_note_door_dropdown.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.final_note_door_value = tk.StringVar(self.struct_frame)
        self._note_image = tk.PhotoImage(file=f"{self.cwd}Pictures/Note.png")
        self.random_note_value_button = tk.Button(self.struct_frame, text='Random Note Value', command=self._random_note_value, image=self._note_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.random_note_value_button.grid(row=1, column=2, padx=self.padx, pady=self.pady)
        self.final_text = tk.Label(self.struct_frame, text="810 Note Door Value:", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_text.grid(row=1, column=3, padx=self.padx, pady=self.pady)
        self.final_note_door_entry = tk.Entry(self.struct_frame, textvariable=self.final_note_door_value, width=6)
        self.final_note_door_entry.grid(row=1, column=4, padx=self.padx, pady=self.pady, sticky='e')
        self.final_text = tk.Label(self.struct_frame, text="Notes", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.final_text.grid(row=1, column=5, padx=self.padx, pady=self.pady, sticky='w')
        self.carry_limit_frame = tk.LabelFrame(self.struct_frame, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.carry_limit_frame.grid(row=2, column=0, columnspan=6, padx=self.padx, pady=self.pady, sticky='w')
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
        self.non_flagged_object_dropdown.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.non_flagged_object_abnormalities_var = tk.IntVar()
        self.non_flagged_object_abnormalities_checkbutton = tk.Checkbutton(self.non_flagged_object_frame, text="Include Abnormalities (May Include Eggs and Feathers)", variable=self.non_flagged_object_abnormalities_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.non_flagged_object_abnormalities_checkbutton.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='sw')
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
        self.all_starting_moves_var = tk.IntVar()
        self.all_starting_moves_checkbutton = tk.Checkbutton(self.world_entrance_frame, text="Start Game With All Moves", variable=self.all_starting_moves_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.all_starting_moves_checkbutton.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='sw')
        # Within World Warps
        self.within_world_warp_frame = tk.LabelFrame(self._warps_tab, text="Within The World Warps*", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
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
        # Starting Area
        self.starting_area_frame = tk.LabelFrame(self._warps_tab, text="Starting Area", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.starting_area_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.starting_area_ttp_canvas = tk.Label(self.starting_area_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.starting_area_ttp_canvas.grid(row=0, column=0, rowspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.new_area_ttp = self.CreateToolTip(self.starting_area_ttp_canvas, self, tool_tips_dict["STARTING_AREA"]["NEW_GAME"])
        self.new_area_text = tk.Label(self.starting_area_frame, text="New Game Start Area", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.new_area_text.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.new_area_var = tk.StringVar(self.world_entrance_frame)
        self.starting_area_options = [option for option in start_level_ids]
        self.new_area_dropdown = ttk.Combobox(self.starting_area_frame, textvariable=self.new_area_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size), width=30)
        self.new_area_dropdown['values'] = self.starting_area_options
        self.new_area_dropdown['state'] = 'readonly'
        self.new_area_dropdown.grid(row=0, column=2, padx=self.padx, pady=self.pady, sticky='w')
#         self.load_area_text = tk.Label(self.starting_area_frame, text="Load Game Area", foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
#         self.load_area_text.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
#         self.load_area_var = tk.StringVar(self.world_entrance_frame)
#         self.load_area_var.set("GL - MM Puzzle/Entrance Room")
#         self.load_area_label = tk.Label(self.starting_area_frame, textvariable=self.load_area_var, foreground=self.black, background="#AAAAAA", font=(self.font_type, self.small_font_size), width=30, anchor="w")
#         self.load_area_label.grid(row=1, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.skip_intro_cutscene_var = tk.IntVar()
        self.skip_intro_cutscene_checkbutton = tk.Checkbutton(self.starting_area_frame, text="Skip Intro Cutscene", variable=self.skip_intro_cutscene_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.skip_intro_cutscene_checkbutton.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
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
        self.bk_model_options = []
        for item in sorted(self.bk_model_json):
            self.bk_model_options.append(item)
        self.bk_model_var.set(self.bk_model_options[0])
        self.bk_model_dropdown = ttk.Combobox(self.bk_model_frame, textvariable=self.bk_model_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.bk_model_dropdown['values'] = self.bk_model_options
        self.bk_model_dropdown['state'] = 'readonly'
        self.bk_model_dropdown.grid(row=0, column=1, columnspan=2, padx=self.padx, pady=self.pady, sticky='w')
        self.random_bk_model_preset_button = tk.Button(self.bk_model_frame, text='Random Preset', command=self._random_bk_model_preset, foreground=self.white, background=self.red, font=(self.font_type, self.small_font_size))
        self.random_bk_model_preset_button.grid(row=0, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.random_bk_model_colors_button = tk.Button(self.bk_model_frame, text='Random Colors', command=self._random_bk_model_colors, foreground=self.white, background=self.red, font=(self.font_type, self.small_font_size))
        self.random_bk_model_colors_button.grid(row=0, column=4, padx=self.padx, pady=self.pady, sticky='w')
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
        self.short_sounds_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.short_sounds_checkbutton_ttp = self.CreateToolTip(self.short_sounds_ttp_canvas, self, tool_tips_dict["SOUNDS_MUSIC"]["SHUFFLE_SOUNDS"])
        self.short_sounds_var = tk.IntVar()
        self.short_sounds_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Shuffle Sounds", variable=self.short_sounds_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.short_sounds_checkbutton.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.jingle_checkbutton_ttp_canvas = tk.Label(self.sound_music_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.jingle_checkbutton_ttp_canvas.grid(row=0, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.jingle_checkbutton_ttp = self.CreateToolTip(self.jingle_checkbutton_ttp_canvas, self, tool_tips_dict["SOUNDS_MUSIC"]["SHUFFLE_JINGLES"])
        self.jingles_var = tk.IntVar()
        self.jingle_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Shuffle Jingles", variable=self.jingles_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.jingle_checkbutton.grid(row=0, column=3, padx=self.padx, pady=self.pady, sticky='w')
        self.music_checkbutton_ttp_canvas = tk.Label(self.sound_music_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.music_checkbutton_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.music_checkbutton_ttp = self.CreateToolTip(self.music_checkbutton_ttp_canvas, self, tool_tips_dict["SOUNDS_MUSIC"]["SHUFFLE_MUSIC"])
        self.music_var = tk.IntVar()
        self.music_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Shuffle Music", variable=self.music_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.music_checkbutton.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.beta_sounds_checkbutton_ttp_canvas = tk.Label(self.sound_music_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.beta_sounds_checkbutton_ttp_canvas.grid(row=1, column=2, padx=self.padx, pady=self.pady, sticky='w')
        self.beta_sounds_checkbutton_ttp = self.CreateToolTip(self.beta_sounds_checkbutton_ttp_canvas, self, tool_tips_dict["SOUNDS_MUSIC"]["INCLUDE_BETA_SOUNDS"])
        self.beta_sounds_var = tk.IntVar()
        self.beta_sounds_checkbutton = tk.Checkbutton(self.sound_music_frame, text="Include Beta Sounds", variable=self.beta_sounds_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.beta_sounds_checkbutton.grid(row=1, column=3, padx=self.padx, pady=self.pady, sticky='w')
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
        self._tab_control.add(self._custom_settings_tab, text="Customizable")
        # Models
        self.other_model_frame = tk.LabelFrame(self._custom_settings_tab, text="Models, Animations, & Properties", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.other_model_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.other_model_frame["borderwidth"] = 0
        self.other_model_frame["highlightthickness"] = 0
        self.other_model_ttp_canvas = tk.Label(self.other_model_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.other_model_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.other_model_frame_ttp = self.CreateToolTip(self.other_model_ttp_canvas, self, tool_tips_dict["CUSTOMIZABLE"]["MODELS"])
        self.other_model_var = tk.IntVar(self.other_model_frame)
        self.other_model_checkbox = tk.Checkbutton(self.other_model_frame, text="Model Manipulation", variable=self.other_model_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.other_model_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.open_models_json_image = tk.PhotoImage(file=f"{self.cwd}Pictures/BK_Model.png")
        self.open_models_json_button = tk.Button(self.other_model_frame, text='Edit Models Json', command=(lambda: self._open_file(f"{self.cwd}Randomization_Processes/Misc_Manipulation/Model_Data/Swappable_Models.json")), image=self.open_models_json_image, background=self.generic_background_color)
        self.open_models_json_button.grid(row=0, column=2, padx=self.padx, pady=self.pady, sticky='w')
        # Animations
        self.animation_ttp_canvas = tk.Label(self.other_model_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.animation_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.animation_frame_ttp = self.CreateToolTip(self.animation_ttp_canvas, self, tool_tips_dict["CUSTOMIZABLE"]["ANIMATIONS"])
        self.animation_var = tk.IntVar(self.other_model_frame)
        self.animation_checkbox = tk.Checkbutton(self.other_model_frame, text="Animation Manipulation", variable=self.animation_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.animation_checkbox.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.open_animation_json_image = tk.PhotoImage(file=f"{self.cwd}Pictures/BK_Animation.png")
        self.open_animation_json_button = tk.Button(self.other_model_frame, text='Edit animation Json', command=(lambda: self._open_file(f"{self.cwd}Randomization_Processes/Misc_Manipulation/Animation_Data/Swappable_Animations.json")), image=self.open_animation_json_image, background=self.generic_background_color)
        self.open_animation_json_button.grid(row=1, column=2, padx=self.padx, pady=self.pady, sticky='w')
        # Properties
        self.properties_ttp_canvas = tk.Label(self.other_model_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.small_font_size))
        self.properties_ttp_canvas.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.properties_frame_ttp = self.CreateToolTip(self.properties_ttp_canvas, self, tool_tips_dict["CUSTOMIZABLE"]["PROPERTIES"])
        self.properties_var = tk.IntVar(self.other_model_frame)
        self.properties_checkbox = tk.Checkbutton(self.other_model_frame, text="Properties Manipulation", variable=self.properties_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.properties_checkbox.grid(row=2, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.open_properties_json_image = tk.PhotoImage(file=f"{self.cwd}Pictures/BK_Properties.png")
        self.open_properties_json_button = tk.Button(self.other_model_frame, text='Edit properties Json', command=(lambda: self._open_file(f"{self.cwd}Randomization_Processes/Misc_Manipulation/Properties_Data/Swappable_Properties.json")), image=self.open_properties_json_image, background=self.generic_background_color)
        self.open_properties_json_button.grid(row=2, column=2, padx=self.padx, pady=self.pady, sticky='w')
        # Customize Description Frame
        self.customize_description_frame = tk.LabelFrame(self.other_model_frame, text="How To Customize:", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.customize_description_frame.grid(row=3, column=0, columnspan=6, padx=self.padx, pady=self.pady, sticky='w')
        self.customize_description_frame["borderwidth"] = 0
        self.customize_description_frame["highlightthickness"] = 0
        description_text = (
            "* Next to each option, there's a button that will open a JSON file.\n" +
            "* The JSON is broken into sections. The names of the sections don't matter,\n" +
            "  but they must be distinct from the other sections.\n" +
            "* Each section may have different subsection types:\n" +
            "  - Original/Replacements: Each original will be randomly replaced with a\n" +
            "    replacement. For models and animations, replacements must be the same\n" +
            "    size or smaller than the original and each replacement will only be used\n" +
            "    once. For properties, any number of original/replacement files are allowed\n" +
            "    and each property can be used more than once.\n" +
            "  - Swap: Swap1 will swap into Swap2, Swap2=>Swap3... Last Swap#=>Swap1.\n" +
            "  - Shuffle: All items in the subcategory will be shuffled within each other.\n" +
            "* For more address values, check out Hack64.net under ROM Map."
            )
        self.customize_description_text = tk.Label(self.customize_description_frame, text=description_text, foreground=self.black, background=curr_background_color, font=(self.font_type, 12), anchor="w", justify="left")
        self.customize_description_text.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
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
        # Mumbo's Mountain
        curr_background_color = "#009999"
        self._mumbos_mountain_tab = ttk.Frame(self._world_specific_tab_control)
        self._world_specific_tab_control.add(self._mumbos_mountain_tab, text="MM")
        self.mumbos_mountain_frame = tk.LabelFrame(self._mumbos_mountain_tab, text="Mumbo's Mountain", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.mumbos_mountain_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.mumbos_mountain_frame["borderwidth"] = 0
        self.mumbos_mountain_frame["highlightthickness"] = 0
        self.flowers_ttp_canvas = tk.Label(self.mumbos_mountain_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.flowers_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.flowers_checkbox_ttp = self.CreateToolTip(self.flowers_ttp_canvas, self, tool_tips_dict["MUMBOS_MOUNTAIN"]["INCLUDE_FLOWERS"])
        self.flowers_var = tk.IntVar()
        self.flowers_checkbox = tk.Checkbutton(self.mumbos_mountain_frame, text="Include Flowers (Shuffling/Randomizing)", variable=self.flowers_var, selectcolor=curr_background_color, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
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
        self.bubblegloop_swamp_frame = tk.LabelFrame(self._bubblegloop_swamp_tab, text="Bubblegloop Swamp", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.bubblegloop_swamp_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.bubblegloop_swamp_frame["borderwidth"] = 0
        self.bubblegloop_swamp_frame["highlightthickness"] = 0
        self.croctus_ttp_canvas = tk.Label(self.bubblegloop_swamp_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.croctus_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.croctus_checkbox_ttp = self.CreateToolTip(self.croctus_ttp_canvas, self, tool_tips_dict["BUBBLEGLOOP_SWAMP"]["SHUFFLE_CROCTUS_ORDER"])
        self.croctus_var = tk.IntVar()
        self.croctus_checkbox = tk.Checkbutton(self.bubblegloop_swamp_frame, text="Shuffle Croctus Order", variable=self.croctus_var, selectcolor=curr_background_color, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.croctus_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.mr_vile_ttp_canvas = tk.Label(self.bubblegloop_swamp_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.mr_vile_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.mr_vile_checkbox_ttp = self.CreateToolTip(self.mr_vile_ttp_canvas, self, tool_tips_dict["BUBBLEGLOOP_SWAMP"]["MR_VILE_BIGGER_BADDER_CROCODILE"])
        self.mr_vile_var = tk.IntVar()
        self.mr_vile_checkbox = tk.Checkbutton(self.bubblegloop_swamp_frame, text="Mr. Vile: Bigger, Badder Crocodile", variable=self.mr_vile_var, selectcolor=curr_background_color, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.mr_vile_checkbox.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.tiptup_choir_ttp_canvas = tk.Label(self.bubblegloop_swamp_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.tiptup_choir_ttp_canvas.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.tiptup_choir_checkbox_ttp = self.CreateToolTip(self.tiptup_choir_ttp_canvas, self, tool_tips_dict["BUBBLEGLOOP_SWAMP"]["TIPTUP_CHOIR_NO_ASSIGNED_SEATS"])
        self.tiptup_choir_var = tk.IntVar()
        self.tiptup_choir_checkbox = tk.Checkbutton(self.bubblegloop_swamp_frame, text="Tiptup Choir: No Assigned Seats", variable=self.tiptup_choir_var, selectcolor=curr_background_color, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
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
        self.gobis_valley_frame = tk.LabelFrame(self._gobis_valley_tab, text="Gobi's Valley", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.gobis_valley_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.gobis_valley_frame["borderwidth"] = 0
        self.gobis_valley_frame["highlightthickness"] = 0
        self.ancient_ones_ttp_canvas = tk.Label(self.gobis_valley_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.ancient_ones_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.ancient_ones_checkbox_ttp = self.CreateToolTip(self.ancient_ones_ttp_canvas, self, tool_tips_dict["GOBIS_VALLEY"]["SHUFFLED_ANCIENT_ONES_ORDER"])
        self.ancient_ones_var = tk.IntVar()
        self.ancient_ones_checkbox = tk.Checkbutton(self.gobis_valley_frame, text="Shuffle Ancient Ones Order", variable=self.ancient_ones_var, selectcolor=curr_background_color, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.ancient_ones_checkbox.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.maze_jinxy_heads_ttp_canvas = tk.Label(self.gobis_valley_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.maze_jinxy_heads_ttp_canvas.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.maze_jinxy_heads_checkbox_ttp = self.CreateToolTip(self.maze_jinxy_heads_ttp_canvas, self, tool_tips_dict["GOBIS_VALLEY"]["SHUFFLE_MAZE_JINXY_HEADS_ORDER"])
        self.maze_jinxy_heads_var = tk.IntVar()
        self.maze_jinxy_heads_checkbox = tk.Checkbutton(self.gobis_valley_frame, text="Shuffle Maze Jinxy Heads Order", variable=self.maze_jinxy_heads_var, selectcolor=curr_background_color, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.maze_jinxy_heads_checkbox.grid(row=1, column=1, padx=self.padx, pady=self.pady, sticky='w')
        self.matching_puzzle_ttp_canvas = tk.Label(self.gobis_valley_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.matching_puzzle_ttp_canvas.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.matching_puzzle_checkbox_ttp = self.CreateToolTip(self.matching_puzzle_ttp_canvas, self, "Randomized Matching Puzzle Not Implemented Yet")
        self.matching_puzzle_var = tk.IntVar()
        self.matching_puzzle_checkbox = tk.Checkbutton(self.gobis_valley_frame, text="Randomize Matching Puzzle", variable=self.matching_puzzle_var, selectcolor=curr_background_color, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
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
        self.click_clock_wood_frame = tk.LabelFrame(self._click_clock_wood_tab, text="Click Clock Wood", foreground=self.black, background=curr_background_color, font=(self.font_type, self.large_font_size))
        self.click_clock_wood_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.click_clock_wood_frame["borderwidth"] = 0
        self.click_clock_wood_frame["highlightthickness"] = 0
        self.ccw_ttp_canvas = tk.Label(self.click_clock_wood_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.ccw_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.ccw_checkbox_ttp = self.CreateToolTip(self.ccw_ttp_canvas, self, tool_tips_dict["CLICK_CLOCK_WOOD"]["SHUFFLE_BY"])
        self.ccw_text = tk.Label(self.click_clock_wood_frame, text="Shuffle By:", foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
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
        # Cheat Sheet
        self.cheat_sheet_ttp_canvas = tk.Label(self.misc_frame, image=self.ttp_image, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.cheat_sheet_ttp_canvas.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky='w')
        self.cheat_sheet_checkbutton_ttp = self.CreateToolTip(self.cheat_sheet_ttp_canvas, self, tool_tips_dict["MISC_OPTIONS"]["CREATE_CHEAT_SHEET"])
        self.cheat_sheet_var = tk.IntVar()
        self.cheat_sheet_checkbutton = tk.Checkbutton(self.misc_frame, text="Create Cheat Sheet(s)", variable=self.cheat_sheet_var, foreground=self.black, background=curr_background_color, font=(self.font_type, self.medium_font_size))
        self.cheat_sheet_checkbutton.grid(row=0, column=1, padx=self.padx, pady=self.pady, sticky='w')
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