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
        self.rom_file_entry.set(self.cwd)
        self.seed_value.set("")
        self.flagged_object_radio_button_var.set(2)
        self.flagged_object_abnormalities_var.set(0)
        self.flagged_object_softlock_var.set(0)
        self.non_flagged_object_radio_button_var.set(2)
        self.non_flagged_object_abnormalities_var.set(0)
        self.struct_radio_button_var.set(2)
        self.struct_abnormalities_var.set(0)
        self.world_entrance_radio_button_var.set(2)
        self.within_world_warps_radio_button_var.set(2)
        self.enemies_radio_button_var.set(2)
        self.enemies_abnormalities_var.set(0)
        self.enemies_softlock_var.set(0)
        self.final_note_door_var.set(0)
        self.final_note_door_value.set(0)
        self.final_puzzle_var.set(0)
        self.final_puzzle_value.set(0)
        self.flowers_var.set(0)
        self.flying_notes_var.set(0)
        self.hard_rings_var.set(0)
        self.croctus_var.set(0)
        self.hard_races_var.set(0)
        self.ancient_ones_var.set(0)
        self.maze_jinxy_heads_var.set(0)
        self.extra_enemies_var.set(0)
        self.buttons_var.set(0)
        self.ccw_radio_button_var.set(1)
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
        self.rom_file_entry.set(json_data["ROM_File"])
        #self.seed_value.set(json_data["Seed"])
        self.flagged_object_radio_button_var.set(json_data["Flagged_Objects_Radio_Button"])
        self.flagged_object_abnormalities_var.set(json_data["Flagged_Objects_Abnormalities"])
        self.flagged_object_softlock_var.set(json_data["Flagged_Objects_Softlock"])
        self.non_flagged_object_radio_button_var.set(json_data["Non_Flagged_Objects_Radio_Button"])
        self.non_flagged_object_abnormalities_var.set(json_data["Non_Flagged_Objects_Abnormalities"])
        self.struct_radio_button_var.set(json_data["Struct_Radio_Button"])
        self.struct_abnormalities_var.set(json_data["Struct_Abnormalities"])
        self.world_entrance_radio_button_var.set(json_data["World_Entrance_Radio_Button"])
        self.within_world_warps_radio_button_var.set(json_data["Within_World_Warps_Radio_Button"])
        self.enemies_radio_button_var.set(json_data["Enemies_Radio_Button"])
        self.enemies_abnormalities_var.set(json_data["Enemies_Abnormalities"])
        self.enemies_softlock_var.set(json_data["Enemies_Softlock"])
        self.final_note_door_var.set(json_data["Final_Note_Door"])
        self.final_note_door_value.set(json_data["Final_Note_Door_Value"])
        self.final_puzzle_var.set(json_data["Final_Puzzle"])
        self.final_puzzle_value.set(json_data["Final_Puzzle_Value"])
        self.flowers_var.set(json_data["MM_Flowers"])
        self.flying_notes_var.set(json_data["TTC_Flying_Notes"])
        self.hard_rings_var.set(json_data["CC_Hard_Rings"])
        self.croctus_var.set(json_data["BGS_Croctus"])
        self.hard_races_var.set(json_data["FP_Hard_Races"])
        self.ancient_ones_var.set(json_data["GV_Ancient_Ones"])
        self.maze_jinxy_heads_var.set(json_data["GV_Maze_Jinxy_Heads"])
        self.extra_enemies_var.set(json_data["MMM_Extra_Enemies"])
        self.buttons_var.set(json_data["RBB_Buttons"])
        self.ccw_radio_button_var.set(json_data["CCW_Radio_Button"])
        self.season_order_var.set(json_data["CCW_Season_Order"])
    
    def _save_current_configuration(self, button_press=True):
        '''Writes the current configuration to a JSON file'''
        current_config = {
            "ROM_File": self.rom_file_entry.get(),
            "Seed": self.seed_value.get(),
            "Flagged_Objects_Radio_Button": self.flagged_object_radio_button_var.get(),
            "Flagged_Objects_Abnormalities": self.flagged_object_abnormalities_var.get(),
            "Flagged_Objects_Softlock": self.flagged_object_softlock_var.get(),
            "Non_Flagged_Objects_Radio_Button": self.non_flagged_object_radio_button_var.get(),
            "Non_Flagged_Objects_Abnormalities": self.non_flagged_object_abnormalities_var.get(),
            "Struct_Radio_Button": self.struct_radio_button_var.get(),
            "Struct_Abnormalities": self.struct_abnormalities_var.get(),
            "World_Entrance_Radio_Button": self.world_entrance_radio_button_var.get(),
            "Within_World_Warps_Radio_Button": self.within_world_warps_radio_button_var.get(),
            "Enemies_Radio_Button": self.enemies_radio_button_var.get(),
            "Enemies_Abnormalities": self.enemies_abnormalities_var.get(),
            "Enemies_Softlock": self.enemies_softlock_var.get(),
            "Final_Note_Door": self.final_note_door_var.get(),
            "Final_Note_Door_Value": self.final_note_door_value.get(),
            "Final_Puzzle": self.final_puzzle_var.get(),
            "Final_Puzzle_Value": self.final_puzzle_value.get(),
            "MM_Flowers": self.flowers_var.get(),
            "TTC_Flying_Notes": self.flying_notes_var.get(),
            "CC_Hard_Rings": self.hard_rings_var.get(),
            "BGS_Croctus": self.croctus_var.get(),
            "FP_Hard_Races": self.hard_races_var.get(),
            "GV_Ancient_Ones": self.ancient_ones_var.get(),
            "GV_Maze_Jinxy_Heads": self.maze_jinxy_heads_var.get(),
            "MMM_Extra_Enemies": self.extra_enemies_var.get(),
            "RBB_Buttons": self.buttons_var.get(),
            "CCW_Radio_Button": self.ccw_radio_button_var.get(),
            "CCW_Season_Order": self.season_order_var.get(),
            }
        if(button_press):
            json_file = tkinter.filedialog.asksaveasfile(filetypes=(("Json Files","*.json"),("all files","*.*")), defaultextension=json)
            json.dump(current_config, json_file)
        else:
            config_file = self.cwd + "Configurations\\Last_Used_Configuration.json"
            with open(config_file, "w+") as json_file: 
                json.dump(current_config, json_file)
    
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
        if((self.struct_radio_button_var.get() == 4) and (final_note_door_val > 2000)):
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
        self.rom_and_seed = tk.LabelFrame(self.left_frame, text="Rom And Seed")
        self.rom_and_seed.pack(ipadx=205, ipady=50)
        self.rom_text = tk.Label(self.rom_and_seed, text="Rom: ")
        self.rom_text.place(x=10, y=10)
        self.rom_file_entry = tk.StringVar(self.rom_and_seed)
        self.rom_file_display = tk.Entry(self.rom_and_seed, textvariable=self.rom_file_entry, state='readonly', width=55)
        self.rom_file_display.place(x=50, y=13)
        self.select_rom_button = tk.Button(self.rom_and_seed, text='Select ROM File', command=self._select_rom_file)
        self.select_rom_button.place(x=10, y=40)
        self.seed_text = tk.Label(self.rom_and_seed, text="Seed:")
        self.seed_text.place(x=110, y=43)
        self.seed_value = tk.StringVar(self.rom_and_seed)
        self.seed_entry = tk.Entry(self.rom_and_seed, textvariable=self.seed_value, width=38)
        self.seed_entry.place(x=150, y=46)
        ### Config and Submit ###
        self.config_and_submit = tk.LabelFrame(self.left_frame, text="Config And Submit")
        self.config_and_submit.pack(ipadx=205, ipady=35)
        self.load_config_button = tk.Button(self.config_and_submit, text='Load Config', command=self._load_configuration)
        self.load_config_button.place(x=10, y=10)
        self.save_config_button = tk.Button(self.config_and_submit, text='Save Config', command=self._save_current_configuration)
        self.save_config_button.place(x=100, y=10)
        self.read_me = tk.Button(self.config_and_submit, text='Open ReadMe', command=self._open_readme_file)
        self.read_me.place(x=190, y=10)
        self.submit = tk.Button(self.config_and_submit, text='Submit', command=self._submit)
        self.submit.place(x=330, y=10)
        ### Overall Settings ###
        self.general_settings = tk.LabelFrame(self.left_frame, text="General Settings")
        self.general_settings.pack(ipadx=205, ipady=230)
        # Flagged Objects
        self.flagged_object_text = tk.Label(self.general_settings, text="Jiggies/Empty Honeycombs/Mumbo Tokens")
        self.flagged_object_text.place(x=10, y=10)
        self.flagged_object_radio_button_var = tk.IntVar()
        self.flagged_object_radio_button_none = tk.Radiobutton(self.general_settings, text="None", variable=self.flagged_object_radio_button_var, value=1)
        self.flagged_object_radio_button_none.place(x=10, y=30)
        self.flagged_object_radio_button_shuffle = tk.Radiobutton(self.general_settings, text="Shuffle", variable=self.flagged_object_radio_button_var, value=2)
        self.flagged_object_radio_button_shuffle.place(x=80, y=30)
        self.flagged_object_radio_button_randomize = tk.Radiobutton(self.general_settings, text="Randomize", variable=self.flagged_object_radio_button_var, value=3)
        self.flagged_object_radio_button_randomize.place(x=150, y=30)
        self.flagged_object_radio_button_oh_whoops = tk.Radiobutton(self.general_settings, text="Oh Whoops All Jiggies", variable=self.flagged_object_radio_button_var, value=4)
        self.flagged_object_radio_button_oh_whoops.place(x=240, y=30)
        self.flagged_object_abnormalities_var = tk.IntVar()
        self.flagged_object_abnormalities_checkbutton = tk.Checkbutton(self.general_settings, text="Include Abnormalities", variable=self.flagged_object_abnormalities_var)
        self.flagged_object_abnormalities_checkbutton.place(x=10, y=55)
        self.flagged_object_softlock_var = tk.IntVar()
        self.flagged_object_softlock_checkbutton = tk.Checkbutton(self.general_settings, text="Include Potential Softlocks", variable=self.flagged_object_softlock_var)
        self.flagged_object_softlock_checkbutton.place(x=170, y=55)
        # Non Flagged Objects
        self.non_flagged_object_text = tk.Label(self.general_settings, text="Jinjos/1-Ups/Misc Objects")
        self.non_flagged_object_text.place(x=10, y=90)
        self.non_flagged_object_radio_button_var = tk.IntVar()
        self.non_flagged_object_radio_button_none = tk.Radiobutton(self.general_settings, text="None", variable=self.non_flagged_object_radio_button_var, value=1)
        self.non_flagged_object_radio_button_none.place(x=10, y=110)
        self.non_flagged_object_radio_button_shuffle = tk.Radiobutton(self.general_settings, text="Shuffle", variable=self.non_flagged_object_radio_button_var, value=2)
        self.non_flagged_object_radio_button_shuffle.place(x=80, y=110)
        self.non_flagged_object_abnormalities_var = tk.IntVar()
        self.non_flagged_object_abnormalities_checkbutton = tk.Checkbutton(self.general_settings, text="Include Abnormalities (May Include Eggs)", variable=self.non_flagged_object_abnormalities_var)
        self.non_flagged_object_abnormalities_checkbutton.place(x=10, y=135)
        # Structs
        self.struct_text = tk.Label(self.general_settings, text="Notes/Blue Eggs/Red Feathers/Gold Feathers")
        self.struct_text.place(x=10, y=170)
        self.struct_radio_button_var = tk.IntVar()
        self.struct_radio_button_none = tk.Radiobutton(self.general_settings, text="None", variable=self.struct_radio_button_var, value=1)
        self.struct_radio_button_none.place(x=10, y=190)
        self.struct_radio_button_shuffle = tk.Radiobutton(self.general_settings, text="Shuffle", variable=self.struct_radio_button_var, value=2)
        self.struct_radio_button_shuffle.place(x=80, y=190)
        self.struct_radio_button_randomize = tk.Radiobutton(self.general_settings, text="Randomize", variable=self.struct_radio_button_var, value=3)
        self.struct_radio_button_randomize.place(x=150, y=190)
        self.struct_radio_button_oh_whoops = tk.Radiobutton(self.general_settings, text="Oh Whoops All Notes", variable=self.struct_radio_button_var, value=4)
        self.struct_radio_button_oh_whoops.place(x=240, y=190)
        self.struct_abnormalities_var = tk.IntVar()
        self.struct_abnormalities_checkbutton = tk.Checkbutton(self.general_settings, text="Include Abnormalities", variable=self.struct_abnormalities_var)
        self.struct_abnormalities_checkbutton.place(x=10, y=215)
        # World Entrances
        self.struct_text = tk.Label(self.general_settings, text="World Entrances (Includes Randomized Moves)")
        self.struct_text.place(x=10, y=250)
        self.world_entrance_radio_button_var = tk.IntVar()
        self.world_entrance_radio_button_none = tk.Radiobutton(self.general_settings, text="None", variable=self.world_entrance_radio_button_var, value=1)
        self.world_entrance_radio_button_none.place(x=10, y=270)
        self.world_entrance_radio_button_shuffle = tk.Radiobutton(self.general_settings, text="Shuffle", variable=self.world_entrance_radio_button_var, value=2)
        self.world_entrance_radio_button_shuffle.place(x=80, y=270)
        # Within World Warps
        self.struct_text = tk.Label(self.general_settings, text="Within The World Warps")
        self.struct_text.place(x=10, y=305)
        self.within_world_warps_radio_button_var = tk.IntVar()
        self.within_world_warps_radio_button_none = tk.Radiobutton(self.general_settings, text="None", variable=self.within_world_warps_radio_button_var, value=1)
        self.within_world_warps_radio_button_none.place(x=10, y=325)
        self.within_world_warps_radio_button_shuffle = tk.Radiobutton(self.general_settings, text="Shuffle", variable=self.within_world_warps_radio_button_var, value=2)
        self.within_world_warps_radio_button_shuffle.place(x=80, y=325)
        # Enemies
        self.struct_text = tk.Label(self.general_settings, text="Ground Enemies, Wall Enemies, and Flying Enemies")
        self.struct_text.place(x=10, y=360)
        self.enemies_radio_button_var = tk.IntVar()
        self.enemies_radio_button_none = tk.Radiobutton(self.general_settings, text="None", variable=self.enemies_radio_button_var, value=1)
        self.enemies_radio_button_none.place(x=10, y=380)
        self.enemies_radio_button_shuffle = tk.Radiobutton(self.general_settings, text="Shuffle", variable=self.enemies_radio_button_var, value=2)
        self.enemies_radio_button_shuffle.place(x=80, y=380)
        self.enemies_radio_button_randomize = tk.Radiobutton(self.general_settings, text="Randomize", variable=self.enemies_radio_button_var, value=3)
        self.enemies_radio_button_randomize.place(x=150, y=380)
        self.enemies_radio_button_oh_whoops = tk.Radiobutton(self.general_settings, text="Oh Whoops All Toughies", variable=self.enemies_radio_button_var, value=4)
        self.enemies_radio_button_oh_whoops.place(x=240, y=380)
        self.enemies_abnormalities_var = tk.IntVar()
        self.enemies_abnormalities_checkbutton = tk.Checkbutton(self.general_settings, text="Include Abnormalities", variable=self.enemies_abnormalities_var)
        self.enemies_abnormalities_checkbutton.place(x=10, y=405)
        self.enemies_softlock_var = tk.IntVar()
        self.enemies_softlock_checkbutton = tk.Checkbutton(self.general_settings, text="Include Potential Softlocks", variable=self.enemies_softlock_var)
        self.enemies_softlock_checkbutton.place(x=170, y=405)
        ###################
        ### RIGHT FRAME ###
        ###################
        ### World Specific ###
        self.right_frame = tk.LabelFrame(self.app_window)
        self.right_frame.pack(side='left')
        self.world_settings = tk.LabelFrame(self.right_frame, text="World Settings")
        self.world_settings.pack(ipadx=105, ipady=315)
        # Gruntilda's Lair
        self.gruntildas_lair_text = tk.Label(self.world_settings, text="Gruntilda's Lair")
        self.gruntildas_lair_text.place(x=10, y=10)
        self.value_text = tk.Label(self.world_settings, text="Final Value")
        self.value_text.place(x=135, y=10)
        self.final_note_door_var = tk.IntVar()
        self.final_note_door_checkbox = tk.Checkbutton(self.world_settings, text="Final Note Door", variable=self.final_note_door_var)
        self.final_note_door_checkbox.place(x=10, y=30)
        self.final_note_door_value = tk.StringVar(self.world_settings)
        self.final_note_door_entry = tk.Entry(self.world_settings, textvariable=self.final_note_door_value, width=10)
        self.final_note_door_entry.place(x=135, y=33)
        self.final_puzzle_var = tk.IntVar()
        self.final_puzzle_checkbox = tk.Checkbutton(self.world_settings, text="Final Puzzle", variable=self.final_puzzle_var)
        self.final_puzzle_checkbox.place(x=10, y=60)
        self.final_puzzle_value = tk.StringVar(self.world_settings)
        self.final_puzzle_entry = tk.Entry(self.world_settings, textvariable=self.final_puzzle_value, width=10)
        self.final_puzzle_entry.place(x=135, y=63)
        # Mumbo's Mountain
        self.mumbos_mountain_text = tk.Label(self.world_settings, text="Mumbo's Mountain")
        self.mumbos_mountain_text.place(x=10, y=90)
        self.flowers_var = tk.IntVar()
        self.flowers_checkbox = tk.Checkbutton(self.world_settings, text="Flowers", variable=self.flowers_var)
        self.flowers_checkbox.place(x=10, y=110)
        # Treasure Trove Cove
        self.treasure_trove_cove_text = tk.Label(self.world_settings, text="Treasure Trove Cove")
        self.treasure_trove_cove_text.place(x=10, y=140)
        self.flying_notes_var = tk.IntVar()
        self.flying_notes_checkbox = tk.Checkbutton(self.world_settings, text="Flying Notes", variable=self.flying_notes_var)
        self.flying_notes_checkbox.place(x=10, y=160)
        # Clanker's Cavern
        self.clankers_cavern_text = tk.Label(self.world_settings, text="Clanker's Cavern")
        self.clankers_cavern_text.place(x=10, y=190)
        self.hard_rings_var = tk.IntVar()
        self.hard_rings_checkbox = tk.Checkbutton(self.world_settings, text="Hard Rings", variable=self.hard_rings_var)
        self.hard_rings_checkbox.place(x=10, y=210)
        # Bubblegloop Swamp
        self.bubblegloop_swamp_text = tk.Label(self.world_settings, text="Bubblegloop Swamp")
        self.bubblegloop_swamp_text.place(x=10, y=240)
        self.croctus_var = tk.IntVar()
        self.croctus_checkbox = tk.Checkbutton(self.world_settings, text="Croctus", variable=self.croctus_var)
        self.croctus_checkbox.place(x=10, y=260)
        # Freezeezy Peak
        self.freezeezy_peak_text = tk.Label(self.world_settings, text="Freezeezy Peak")
        self.freezeezy_peak_text.place(x=10, y=290)
        self.hard_races_var = tk.IntVar()
        self.hard_races_checkbox = tk.Checkbutton(self.world_settings, text="Hard Races", variable=self.hard_races_var)
        self.hard_races_checkbox.place(x=10, y=310)
        # Gobi's Valley
        self.gobis_valley_text = tk.Label(self.world_settings, text="Gobi's Valley")
        self.gobis_valley_text.place(x=10, y=340)
        self.ancient_ones_var = tk.IntVar()
        self.ancient_ones_checkbox = tk.Checkbutton(self.world_settings, text="Ancient Ones", variable=self.ancient_ones_var)
        self.ancient_ones_checkbox.place(x=10, y=360)
        self.maze_jinxy_heads_var = tk.IntVar()
        self.maze_jinxy_heads_checkbox = tk.Checkbutton(self.world_settings, text="Maze Jinxy Heads", variable=self.maze_jinxy_heads_var)
        self.maze_jinxy_heads_checkbox.place(x=10, y=380)
        # Mad Monster Mansion
        self.mad_monster_mansion_text = tk.Label(self.world_settings, text="Mad Monster Mansion")
        self.mad_monster_mansion_text.place(x=10, y=410)
        self.extra_enemies_var = tk.IntVar()
        self.extra_enemies_checkbox = tk.Checkbutton(self.world_settings, text="Extra Enemies", variable=self.extra_enemies_var)
        self.extra_enemies_checkbox.place(x=10, y=430)
        # Rusty Bucket Bay
        self.rusty_bucket_bay_text = tk.Label(self.world_settings, text="Rusty Bucket Bay")
        self.rusty_bucket_bay_text.place(x=10, y=460)
        self.buttons_var = tk.IntVar()
        self.buttons_checkbox = tk.Checkbutton(self.world_settings, text="Buttons", variable=self.buttons_var)
        self.buttons_checkbox.place(x=10, y=480)
        # Click Clock Wood
        self.click_clock_wood_text = tk.Label(self.world_settings, text="Click Clock Wood")
        self.click_clock_wood_text.place(x=10, y=510)
        self.ccw_radio_button_var = tk.IntVar()
        self.ccw_radio_button_by_season = tk.Radiobutton(self.world_settings, text="By Season", variable=self.ccw_radio_button_var, value=1)
        self.ccw_radio_button_by_season.place(x=10, y=530)
        self.ccw_radio_button_within_world = tk.Radiobutton(self.world_settings, text="Within World", variable=self.ccw_radio_button_var, value=2)
        self.ccw_radio_button_within_world.place(x=100, y=530)
        self.season_order_var = tk.IntVar()
        self.season_order_checkbox = tk.Checkbutton(self.world_settings, text="Season Order", variable=self.season_order_var)
        self.season_order_checkbox.place(x=10, y=550)
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