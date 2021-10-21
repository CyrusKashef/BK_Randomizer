'''
Created on Aug 21, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

import tkinter as tk
import tkinter.filedialog
import os
import json

####################
### FILE IMPORTS ###
####################

from ProgressionGUI import Progression_GUI
from Randomization_Processes.Common_Functions import read_json

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
        self.app_window = tk.Tk()
        self.app_window.winfo_toplevel().title(f"Banjo-Kazooie Randomizer v{BK_RANDO_VERSION}")
        self.cwd = os.getcwd() + "\\"
    
    def _select_rom_file(self):
        '''Opens a browser to select the ROM file ending in .z64'''
        filename = tkinter.filedialog.askopenfilename(initialdir=self.cwd, title="Select The BK ROM File", filetype =(("Rom Files","*.z64"),("all files","*.*")) )
        self.rom_file_entry.set(filename)
    
    def _set_recommended_defaults(self):
        '''Sets the recommended defaults for first time users or when an error occurs with a loaded json file'''
        ### ROM and Seed ###
        # ROM
        self.rom_file_entry.set(self.cwd)
        # Seed
        self.seed_value.set("")
        ### General Settings ###
        # Flagged Objects
        self.flagged_object_var.set("Shuffle")
        self.flagged_object_abnormalities_var.set(0)
        self.flagged_object_softlock_var.set(0)
        # Non-Flagged Objects
        self.non_flagged_object_var.set("Shuffle")
        self.non_flagged_object_abnormalities_var.set(0)
        # Structs
        self.struct_var.set("Shuffle")
        # World Entrances
        self.world_entrance_var.set("Shuffle")
        # Within World Warps
        self.within_world_warps_var.set("Shuffle")
        # Enemies
        self.enemies_var.set("Randomize")
        self.enemies_abnormalities_var.set(0)
        self.enemies_softlock_var.set(0)
        ### Aesthetic Settings ###
        # BK Model
        self.bk_model1_var.set("Default")
        # Enemy Models
        self.enemy_model_var.set("None")
        # Sounds/Music
        self.short_sounds_var.set("None")
        self.jingles_var.set("None")
        self.music_var.set("None")
        self.beta_sounds_var.set(0)
        # Sprites/Textures
        self.skybox_var.set("None")
        self.talking_sprite_var.set("None")
        ### Misc Settings ###
        self.cheat_sheet_var.set(1)
        self.remove_files_var.set(1)
        ### World Specific ###
        # Gruntilda's Lair
        self.final_note_door_var.set(0)
        self.final_note_door_value.set(0)
        self.final_puzzle_var.set(0)
        self.final_puzzle_value.set(0)
        self.skip_furnace_fun_var.set(0)
        # Mumbo's Mountain
        self.flowers_var.set(0)
        # Treasure Trove Cove
        self.flying_notes_var.set(0)
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
        self.extra_enemies_var.set(0)
        self.fake_items_var.set(0)
        # Rusty Bucket Bay
        self.buttons_var.set(0)
        # Click Clock Wood
        self.ccw_var.set("By Season*")
        self.season_order_var.set(0)
    
    def _load_configuration(self, button_press=True):
        '''Opens a chosen JSON file and sets the parameters to match those'''
        if(button_press):
            config_default_dir = f"{self.cwd}Configurations\\"
            filename = tkinter.filedialog.askopenfilename(initialdir=config_default_dir, title="Select A JSON Config File", filetype =(("Json Files","*.json"),("all files","*.*")))
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
        self.enemies_abnormalities_var.set(json_data["Enemies_Abnormalities"])
        self.enemies_softlock_var.set(json_data["Enemies_Softlock"])
        ### Aesthetic Settings ###
        # BK Model
        self.bk_model1_var.set(json_data["BK_Model_Option"])
        # Enemy Models
        self.enemy_model_var.set(json_data["Enemy_Model_Option"])
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
        ### World Specific ###
        # Gruntilda's Lair
        self.final_note_door_var.set(json_data["Final_Note_Door"])
        self.final_note_door_value.set(json_data["Final_Note_Door_Value"])
        self.final_puzzle_var.set(json_data["Final_Puzzle"])
        self.final_puzzle_value.set(json_data["Final_Puzzle_Value"])
        self.skip_furnace_fun_var.set(json_data["Furnace_Fun_Skip"])
        # Mumbo's Mountain
        self.flowers_var.set(json_data["MM_Flowers"])
        # Treasure Trove Cove
        self.flying_notes_var.set(json_data["TTC_Flying_Notes"])
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
        self.extra_enemies_var.set(json_data["MMM_Extra_Enemies"])
        self.fake_items_var.set(json_data["MMM_Fake_Items"])
        # Rusty Bucket Bay
        self.buttons_var.set(json_data["RBB_Buttons"])
        # Click Clock Wood
        self.ccw_var.set(json_data["CCW_Option"])
        self.season_order_var.set(json_data["CCW_Season_Order"])
    
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
            "Enemies_Abnormalities": self.enemies_abnormalities_var.get(),
            "Enemies_Softlock": self.enemies_softlock_var.get(),
            ### Aesthetic Settings ###
            # BK Model
            "BK_Model_Option": self.bk_model1_var.get(),
            # Enemy Models
            "Enemy_Model_Option" : self.enemy_model_var.get(),
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
            ### World Specific ###
            # Gruntilda's Lair
            "Final_Note_Door": self.final_note_door_var.get(),
            "Final_Note_Door_Value": self.final_note_door_value.get(),
            "Final_Puzzle": self.final_puzzle_var.get(),
            "Final_Puzzle_Value": self.final_puzzle_value.get(),
            "Furnace_Fun_Skip": self.skip_furnace_fun_var.get(),
            # Mumbo's Mountain
            "MM_Flowers": self.flowers_var.get(),
            # Treasure Trove Cove
            "TTC_Flying_Notes": self.flying_notes_var.get(),
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
            "MMM_Extra_Enemies": self.extra_enemies_var.get(),
            "MMM_Fake_Items": self.fake_items_var.get(),
            # Rusty Bucket Bay
            "RBB_Buttons": self.buttons_var.get(),
            # Click Clock Wood
            "CCW_Option": self.ccw_var.get(),
            "CCW_Season_Order": self.season_order_var.get(),
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
#         if((self.final_puzzle_value.get() == 4) and (final_puzzle_val > 100)):
#             Error_GUI("Final Puzzle Value Must Be Less Than 100 Under These Settings.")
#             self.error_gui._show_window()
#             return False
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
    
    ################################################################################################################
    #                                                                  |                                           #
    #                                                                  |    Gruntilda's Lair            Value      #
    #    ROM_DIR: ______________________________________  [Select_ROM] |    [] Final Note Door Only    ________    #
    #                                                                  |    [] Final Puzzle Only       ________    #
    #    SEED:    ______________________________________               |                                           #
    #                                                                  |    Mumbo's Mountain                       #
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |    [] Flowers                             #
    #                                                                  |                                           #
    #    [Load_Config]   [Save_Config]   [Read_Me]        [Submit]     |    Treasure Trove Cove                    #
    #                                                                  |    [] Flying Notes                        #
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |                                           #
    #                                                                  |    Clanker's Cavern                       #
    #    Jiggies/Empty Honeycombs/Mumbo Tokens                         |    [] Hard Rings                          #
    #    O None   O Shuffle   O Randomize   O Oh Whoops All Jiggies    |                                           #
    #    [] Include Abnormalities   [] Include Potential Soft-Locks    |    Bubblegloop Swamp                      #
    #                                                                  |    [] Croctus                             #
    #    Jinjos/1-Ups/Misc Objects                                     |                                           #
    #    O None   O Shuffle                                            |    Freezeezy Peak                         #
    #    [] Include Abnormalities (May Include Eggs)                   |    [] Hard Races                          #
    #                                                                  |                                           #
    #    Notes/Blue Eggs/Red Feathers/Gold Feathers                    |    Gobi's Valley                          #
    #    O None   O Shuffle   O Randomize   O Oh Whoops All Notes      |    [] Ancient Ones                        #
    #    [] Include World Specialties                                  |    [] Maze Jinxy Heads                    #
    #                                                                  |                                           #
    #    World Entrances (Includes Randomized Moves)                   |    Mad Monster Mansion                    #
    #    O None   O Shuffle                                            |    [] Extra Enemies                       #
    #                                                                  |                                           #
    #    Within The World Warps                                        |    Rusty Bucket Bay                       #
    #    O None   O Ins And Outs Separate    O All Logical Warps       |    [] Buttons                             #
    #                                                                  |                                           #
    #    Ground Enemies, Wall Enemies, and Flying Enemies              |    Click Clock Wood                       #
    #    O None   O Shuffle   O Randomize   O Oh Whoops All Toughies   |    O By Season    O Within World          #
    #    [] Include Vents   [] Include Potential Soft-Locks            |    [] Season Order                        #
    #                                                                  |                                           #
    ################################################################################################################
    
    def _main(self):
        '''Places all of the widgest on the GUI and runs the loop for the window'''
        ##################
        ### LEFT FRAME ###
        ##################
        self.left_frame = tk.LabelFrame(self.app_window)
        self.left_frame.pack(side='left')
        ### ROM and Seed ###
        y_position = 10
        self.rom_and_seed = tk.LabelFrame(self.left_frame, text="Rom And Seed")
        self.rom_and_seed.pack(ipadx=205, ipady=50)
        self.rom_text = tk.Label(self.rom_and_seed, text="Rom: ")
        self.rom_text.place(x=10, y=y_position)
        y_position += 3
        self.rom_file_entry = tk.StringVar(self.rom_and_seed)
        self.rom_file_display = tk.Entry(self.rom_and_seed, textvariable=self.rom_file_entry, state='readonly', width=55)
        self.rom_file_display.place(x=50, y=y_position)
        y_position += 27
        self.select_rom_button = tk.Button(self.rom_and_seed, text='Select ROM File', command=self._select_rom_file)
        self.select_rom_button.place(x=10, y=y_position)
        y_position += 3
        self.seed_text = tk.Label(self.rom_and_seed, text="Seed:")
        self.seed_text.place(x=110, y=y_position)
        y_position += 3
        self.seed_value = tk.StringVar(self.rom_and_seed)
        self.seed_entry = tk.Entry(self.rom_and_seed, textvariable=self.seed_value, width=38)
        self.seed_entry.place(x=150, y=y_position)
        ### Config and Submit ###
        y_position = 10
        self.config_and_submit = tk.LabelFrame(self.left_frame, text="Config And Submit")
        self.config_and_submit.pack(ipadx=205, ipady=35)
        self.load_config_button = tk.Button(self.config_and_submit, text='Load Config', command=self._load_configuration)
        self.load_config_button.place(x=10, y=y_position)
        self.save_config_button = tk.Button(self.config_and_submit, text='Save Config', command=self._save_current_configuration)
        self.save_config_button.place(x=100, y=y_position)
        self.read_me = tk.Button(self.config_and_submit, text='Open ReadMe', command=self._open_readme_file)
        self.read_me.place(x=190, y=y_position)
        self.submit = tk.Button(self.config_and_submit, text='Submit', command=self._submit)
        self.submit.place(x=330, y=y_position)
        ### General Settings ###
        self.general_settings = tk.LabelFrame(self.left_frame, text="General Settings")
        self.general_settings.pack(ipadx=205, ipady=155)
        # Flagged Objects
        y_position = 10
        self.flagged_object_text = tk.Label(self.general_settings, text="Jiggies/Empty Honeycombs/Mumbo Tokens")
        self.flagged_object_text.place(x=10, y=y_position)
        self.flagged_object_var = tk.StringVar(self.general_settings)
        self.flagged_object_options = ["None", "Shuffle"]
        self.flagged_object_var.set(self.flagged_object_options[0])
        self.flagged_object_dropdown = tk.OptionMenu(self.general_settings, self.flagged_object_var, *self.flagged_object_options)
        self.flagged_object_dropdown.place(x=265, y=y_position-5)
        y_position += 25
        self.flagged_object_abnormalities_var = tk.IntVar()
        self.flagged_object_abnormalities_checkbutton = tk.Checkbutton(self.general_settings, text="Include Abnormalities", variable=self.flagged_object_abnormalities_var)
        self.flagged_object_abnormalities_checkbutton.place(x=10, y=y_position)
        self.flagged_object_softlock_var = tk.IntVar()
        self.flagged_object_softlock_checkbutton = tk.Checkbutton(self.general_settings, text="Include Potential Softlocks", variable=self.flagged_object_softlock_var)
        self.flagged_object_softlock_checkbutton.place(x=170, y=y_position)
        y_position += 35
        # Non Flagged Objects
        self.non_flagged_object_text = tk.Label(self.general_settings, text="Jinjos/1-Ups/Misc Objects")
        self.non_flagged_object_text.place(x=10, y=y_position)
        self.non_flagged_object_var = tk.StringVar(self.general_settings)
        self.non_flagged_object_options = ["None", "Shuffle"]
        self.non_flagged_object_var.set(self.non_flagged_object_options[0])
        self.non_flagged_object_dropdown = tk.OptionMenu(self.general_settings, self.non_flagged_object_var, *self.non_flagged_object_options)
        self.non_flagged_object_dropdown.place(x=265, y=y_position-5)
        y_position += 25
        self.non_flagged_object_abnormalities_var = tk.IntVar()
        self.non_flagged_object_abnormalities_checkbutton = tk.Checkbutton(self.general_settings, text="Include Abnormalities (May Include Eggs)", variable=self.non_flagged_object_abnormalities_var)
        self.non_flagged_object_abnormalities_checkbutton.place(x=10, y=y_position)
        y_position += 35
        # Structs
        self.struct_text = tk.Label(self.general_settings, text="Notes/Blue Eggs/Red Feathers/Gold Feathers")
        self.struct_text.place(x=10, y=y_position)
        self.struct_var = tk.StringVar(self.general_settings)
        self.struct_options = ["None", "Shuffle", "Randomize", "All Notes"]
        self.struct_var.set(self.struct_options[0])
        self.struct_dropdown = tk.OptionMenu(self.general_settings, self.struct_var, *self.struct_options)
        self.struct_dropdown.place(x=265, y=y_position-5)
        y_position += 35
        # World Entrances
        self.world_entrance_text = tk.Label(self.general_settings, text="World Entrances (Includes Randomized Moves)")
        self.world_entrance_text.place(x=10, y=y_position)
        self.world_entrance_var = tk.StringVar(self.general_settings)
        self.world_entrance_options = ["None", "Shuffle"]
        self.world_entrance_var.set(self.world_entrance_options[0])
        self.world_entrance_dropdown = tk.OptionMenu(self.general_settings, self.world_entrance_var, *self.world_entrance_options)
        self.world_entrance_dropdown.place(x=265, y=y_position-5)
        y_position += 35
        # Within World Warps
        self.within_world_warp_text = tk.Label(self.general_settings, text="Within The World Warps")
        self.within_world_warp_text.place(x=10, y=y_position)
        self.within_world_warps_var = tk.StringVar(self.general_settings)
        self.within_world_warps_options = ["None", "Shuffle"]
        self.within_world_warps_var.set(self.within_world_warps_options[0])
        self.within_world_warps_dropdown = tk.OptionMenu(self.general_settings, self.within_world_warps_var, *self.within_world_warps_options)
        self.within_world_warps_dropdown.place(x=265, y=y_position-5)
        y_position += 35
        # Enemies
        self.enemy_text = tk.Label(self.general_settings, text="Ground/Wall/Flying Enemies")
        self.enemy_text.place(x=10, y=y_position)
        self.enemies_var = tk.StringVar(self.general_settings)
        self.enemies_options = ["None", "Shuffle", "Randomize", "All Toughies*"]
        self.enemies_var.set(self.enemies_options[0])
        self.enemies_dropdown = tk.OptionMenu(self.general_settings, self.enemies_var, *self.enemies_options)
        self.enemies_dropdown.place(x=265, y=y_position-5)
        y_position += 25
        self.enemies_abnormalities_var = tk.IntVar()
        self.enemies_abnormalities_checkbutton = tk.Checkbutton(self.general_settings, text="Include Abnormalities", variable=self.enemies_abnormalities_var)
        self.enemies_abnormalities_checkbutton.place(x=10, y=y_position)
        self.enemies_softlock_var = tk.IntVar()
        self.enemies_softlock_checkbutton = tk.Checkbutton(self.general_settings, text="Include Potential Softlocks", variable=self.enemies_softlock_var)
        self.enemies_softlock_checkbutton.place(x=170, y=y_position)
        y_position += 35
        ### Aesthetic Settings ###
        y_position = 5
        self.aethetic_settings = tk.LabelFrame(self.left_frame, text="Aesthetic Settings")
        self.aethetic_settings.pack(ipadx=205, ipady=105)
        # BK Model
        self.bk_model_text = tk.Label(self.aethetic_settings, text="Banjo-Kazooie Model Color")
        self.bk_model_text.place(x=10, y=y_position)
        self.bk_model1_json = read_json(f"{self.cwd}Randomization_Processes/Model_Data/BK_Model1_Presets.json")
        self.bk_model1_var = tk.StringVar(self.aethetic_settings)
        self.bk_model_options = []
        for item in self.bk_model1_json:
            self.bk_model_options.append(item)
        self.bk_model1_var.set(self.bk_model_options[0])
        self.bk_model1_dropdown = tk.OptionMenu(self.aethetic_settings, self.bk_model1_var, *self.bk_model_options)
        self.bk_model1_dropdown.place(x=265, y=y_position-5)
        y_position += 30
        # Enemy Models
        self.enemy_model_text = tk.Label(self.aethetic_settings, text="Enemy Model Colors*")
        self.enemy_model_text.place(x=10, y=y_position)
        self.enemy_model_var = tk.StringVar(self.aethetic_settings)
        self.enemy_model_options = ["None"]
        self.enemy_model_var.set(self.enemy_model_options[0])
        self.enemy_model_dropdown = tk.OptionMenu(self.aethetic_settings, self.enemy_model_var, *self.enemy_model_options)
        self.enemy_model_dropdown.place(x=265, y=y_position-5)
        y_position += 30
        # Sounds/Music
        self.sounds_music_text = tk.Label(self.aethetic_settings, text="Short Sounds/Fanfare & Jingles/Looped Music")
        self.sounds_music_text.place(x=10, y=y_position)
        y_position += 20
        self.short_sounds_var = tk.IntVar()
        self.short_sounds_checkbutton = tk.Checkbutton(self.aethetic_settings, text="Shuffle Sounds", variable=self.short_sounds_var)
        self.short_sounds_checkbutton.place(x=10, y=y_position)
        self.jingles_var = tk.IntVar()
        self.jingle_checkbutton = tk.Checkbutton(self.aethetic_settings, text="Shuffle Jingles", variable=self.jingles_var)
        self.jingle_checkbutton.place(x=120, y=y_position)
        self.music_var = tk.IntVar()
        self.music_checkbutton = tk.Checkbutton(self.aethetic_settings, text="Shuffle Music", variable=self.music_var)
        self.music_checkbutton.place(x=230, y=y_position)
        y_position += 20
        self.beta_sounds_var = tk.IntVar()
        self.beta_sounds_checkbutton = tk.Checkbutton(self.aethetic_settings, text="Include Beta Sounds", variable=self.beta_sounds_var)
        self.beta_sounds_checkbutton.place(x=10, y=y_position)
        y_position += 30
        # Sprites/Textures
        self.skybox_text = tk.Label(self.aethetic_settings, text="Sprites/Textures")
        self.skybox_text.place(x=10, y=y_position)
        y_position += 20
        self.skybox_var = tk.IntVar()
        self.skybox_checkbutton = tk.Checkbutton(self.aethetic_settings, text="Shuffle Skyboxes*", variable=self.skybox_var)
        self.skybox_checkbutton.place(x=10, y=y_position)
        self.talking_sprite_var = tk.IntVar()
        self.talking_sprite_checkbutton = tk.Checkbutton(self.aethetic_settings, text="Shuffle Talking Sprites*", variable=self.talking_sprite_var)
        self.talking_sprite_checkbutton.place(x=130, y=y_position)
        ### Misc Settings ###
        y_position = 5
        self.misc_settings = tk.LabelFrame(self.left_frame, text="Misc Settings")
        self.misc_settings.pack(ipadx=205, ipady=30)
        # Cheat Sheet
        self.cheat_sheet_var = tk.IntVar()
        self.cheat_sheet_checkbutton = tk.Checkbutton(self.misc_settings, text="Create Cheat Sheet*", variable=self.cheat_sheet_var)
        self.cheat_sheet_checkbutton.place(x=10, y=y_position)
        # Remove Files
        self.remove_files_var = tk.IntVar()
        self.remove_files_checkbutton = tk.Checkbutton(self.misc_settings, text="Remove Extra Files*", variable=self.remove_files_var)
        self.remove_files_checkbutton.place(x=170, y=y_position)
        ###################
        ### RIGHT FRAME ###
        ###################
        ### World Specific ###
        self.right_frame = tk.LabelFrame(self.app_window)
        self.right_frame.pack(side='left')
        self.world_settings = tk.LabelFrame(self.right_frame, text="World Settings")
        self.world_settings.pack(ipadx=105, ipady=377)
        # Gruntilda's Lair
        y_position = 5
        self.gruntildas_lair_text = tk.Label(self.world_settings, text="Gruntilda's Lair")
        self.gruntildas_lair_text.place(x=10, y=y_position)
        self.value_text = tk.Label(self.world_settings, text="Final Value")
        self.value_text.place(x=135, y=y_position)
        y_position += 20
        self.final_note_door_var = tk.IntVar()
        self.final_note_door_checkbox = tk.Checkbutton(self.world_settings, text="Final Note Door", variable=self.final_note_door_var)
        self.final_note_door_checkbox.place(x=10, y=y_position)
        y_position += 3
        self.final_note_door_value = tk.StringVar(self.world_settings)
        self.final_note_door_entry = tk.Entry(self.world_settings, textvariable=self.final_note_door_value, width=10)
        self.final_note_door_entry.place(x=135, y=y_position)
        y_position += 20
        self.final_puzzle_var = tk.IntVar()
        self.final_puzzle_checkbox = tk.Checkbutton(self.world_settings, text="Final Puzzle", variable=self.final_puzzle_var)
        self.final_puzzle_checkbox.place(x=10, y=y_position)
        y_position += 3
        self.final_puzzle_value = tk.StringVar(self.world_settings)
        self.final_puzzle_entry = tk.Entry(self.world_settings, textvariable=self.final_puzzle_value, width=10)
        self.final_puzzle_entry.place(x=135, y=y_position)
        y_position += 20
        self.skip_furnace_fun_var = tk.IntVar()
        self.skip_furnace_fun_checkbox = tk.Checkbutton(self.world_settings, text="Skip Furnace Fun", variable=self.skip_furnace_fun_var)
        self.skip_furnace_fun_checkbox.place(x=10, y=y_position)
        y_position += 30
        # Mumbo's Mountain
        self.mumbos_mountain_text = tk.Label(self.world_settings, text="Mumbo's Mountain")
        self.mumbos_mountain_text.place(x=10, y=y_position)
        y_position += 20
        self.flowers_var = tk.IntVar()
        self.flowers_checkbox = tk.Checkbutton(self.world_settings, text="Flowers", variable=self.flowers_var)
        self.flowers_checkbox.place(x=10, y=y_position)
        y_position += 30
        # Treasure Trove Cove
        self.treasure_trove_cove_text = tk.Label(self.world_settings, text="Treasure Trove Cove")
        self.treasure_trove_cove_text.place(x=10, y=y_position)
        y_position += 20
        self.flying_notes_var = tk.IntVar()
        self.flying_notes_checkbox = tk.Checkbutton(self.world_settings, text="Flying Notes*", variable=self.flying_notes_var)
        self.flying_notes_checkbox.place(x=10, y=y_position)
        y_position += 30
        # Clanker's Cavern
        self.clankers_cavern_text = tk.Label(self.world_settings, text="Clanker's Cavern")
        self.clankers_cavern_text.place(x=10, y=y_position)
        y_position += 20
        self.hard_rings_var = tk.IntVar()
        self.hard_rings_checkbox = tk.Checkbutton(self.world_settings, text="Hard Rings", variable=self.hard_rings_var)
        self.hard_rings_checkbox.place(x=10, y=y_position)
        y_position += 30
        # Bubblegloop Swamp
        self.bubblegloop_swamp_text = tk.Label(self.world_settings, text="Bubblegloop Swamp")
        self.bubblegloop_swamp_text.place(x=10, y=y_position)
        y_position += 20
        self.croctus_var = tk.IntVar()
        self.croctus_checkbox = tk.Checkbutton(self.world_settings, text="Croctus", variable=self.croctus_var)
        self.croctus_checkbox.place(x=10, y=y_position)
        y_position += 20
        self.mr_vile_var = tk.IntVar()
        self.mr_vile_checkbox = tk.Checkbutton(self.world_settings, text="Mr. Vile*", variable=self.mr_vile_var)
        self.mr_vile_checkbox.place(x=10, y=y_position)
        y_position += 20
        self.tiptup_choir_var = tk.IntVar()
        self.tiptup_choir_checkbox = tk.Checkbutton(self.world_settings, text="Tiptup Choir*", variable=self.tiptup_choir_var)
        self.tiptup_choir_checkbox.place(x=10, y=y_position)
        y_position += 30
        # Freezeezy Peak
        self.freezeezy_peak_text = tk.Label(self.world_settings, text="Freezeezy Peak")
        self.freezeezy_peak_text.place(x=10, y=y_position)
        y_position += 20
        self.hard_races_var = tk.IntVar()
        self.hard_races_checkbox = tk.Checkbutton(self.world_settings, text="Hard Races", variable=self.hard_races_var)
        self.hard_races_checkbox.place(x=10, y=y_position)
        y_position += 30
        # Gobi's Valley
        self.gobis_valley_text = tk.Label(self.world_settings, text="Gobi's Valley")
        self.gobis_valley_text.place(x=10, y=y_position)
        y_position += 20
        self.ancient_ones_var = tk.IntVar()
        self.ancient_ones_checkbox = tk.Checkbutton(self.world_settings, text="Ancient Ones", variable=self.ancient_ones_var)
        self.ancient_ones_checkbox.place(x=10, y=y_position)
        y_position += 20
        self.maze_jinxy_heads_var = tk.IntVar()
        self.maze_jinxy_heads_checkbox = tk.Checkbutton(self.world_settings, text="Maze Jinxy Heads", variable=self.maze_jinxy_heads_var)
        self.maze_jinxy_heads_checkbox.place(x=10, y=y_position)
        y_position += 20
        self.matching_puzzle_var = tk.IntVar()
        self.matching_puzzle_checkbox = tk.Checkbutton(self.world_settings, text="Matching Puzzle*", variable=self.matching_puzzle_var)
        self.matching_puzzle_checkbox.place(x=10, y=y_position)
        y_position += 30
        # Mad Monster Mansion
        self.mad_monster_mansion_text = tk.Label(self.world_settings, text="Mad Monster Mansion")
        self.mad_monster_mansion_text.place(x=10, y=y_position)
        y_position += 20
        self.extra_enemies_var = tk.IntVar()
        self.extra_enemies_checkbox = tk.Checkbutton(self.world_settings, text="Tricky Enemies*", variable=self.extra_enemies_var)
        self.extra_enemies_checkbox.place(x=10, y=y_position)
        y_position += 20
        self.fake_items_var = tk.IntVar()
        self.fake_items_checkbox = tk.Checkbutton(self.world_settings, text="Tricky Items*", variable=self.fake_items_var)
        self.fake_items_checkbox.place(x=10, y=y_position)
        y_position += 30
        # Rusty Bucket Bay
        self.rusty_bucket_bay_text = tk.Label(self.world_settings, text="Rusty Bucket Bay")
        self.rusty_bucket_bay_text.place(x=10, y=y_position)
        y_position += 20
        self.buttons_var = tk.IntVar()
        self.buttons_checkbox = tk.Checkbutton(self.world_settings, text="Buttons", variable=self.buttons_var)
        self.buttons_checkbox.place(x=10, y=y_position)
        y_position += 30
        # Click Clock Wood
        self.click_clock_wood_text = tk.Label(self.world_settings, text="Click Clock Wood")
        self.click_clock_wood_text.place(x=10, y=y_position)
        y_position += 25
        self.ccw_var = tk.StringVar(self.world_settings)
        self.ccw_options = ["By Season*", "Within World*"]
        self.ccw_var.set(self.ccw_options[0])
        self.ccw_dropdown = tk.OptionMenu(self.world_settings, self.ccw_var, *self.ccw_options)
        self.ccw_dropdown.place(x=10, y=y_position-5)
        y_position += 25
        self.season_order_var = tk.IntVar()
        self.season_order_checkbox = tk.Checkbutton(self.world_settings, text="Season Order*", variable=self.season_order_var)
        self.season_order_checkbox.place(x=10, y=y_position)
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