'''
Created on Aug 23, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

import tkinter as tk
from tkinter import ttk
from tkinter import HORIZONTAL
import threading

import time
from random import randint

####################
### FILE IMPORTS ###
####################

from Randomization_Processes.Common_Functions import read_json
from Randomization_Processes.Setup_Functions import setup_tmp_folder, set_seed, make_copy_of_rom
from Randomization_Processes.Decompress_Functions import Decompressor
from Randomization_Processes.Compress_Functions import Compressor
from Randomization_Processes.World_Manipulation import World_Manipulation_Main
from Randomization_Processes.Misc_Manipulation import Misc_Manipulation_Main
from Randomization_Processes.CRC_Tool import run_crc_tool
from Randomization_Processes.Clean_Up import CleanUp

#################
### GUI CLASS ###
#################

class Progression_GUI():
    def __init__(self, master):
        '''Pydoc'''
        self.master = master
        self.rom_path = self.master.rom_file_entry.get()
        if(master.app_window):
            self.progress_bar_window = tk.Toplevel(master.app_window)
        else:
            self.progress_bar_window = tk.Tk()
        self.progress_bar_window.geometry("300x50")
    
    class App_Variable_Label():
        '''Pydoc'''
        def __init__(self, window, label_text):
            '''Pydoc'''
            self.text = tk.StringVar()
            self.text.set(label_text)
            self.label = tk.Label(window, textvariable=self.text)

        def set_text(self, new_text):
            '''Pydoc'''
            self.text.set(new_text)

        def pack_label(self):
            '''Pydoc'''
            self.label.pack()
    
    class App_ProgressBar():
        '''Pydoc'''
        def __init__(self, window, bar_length=290, bar_mode='determinate'):
            '''Pydoc'''
            self.progressbar = ttk.Progressbar(window, orient = HORIZONTAL, length=bar_length, mode=bar_mode)
            self.progressbar.config(maximum=100)

        def update_bar(self, percentage):
            '''Pydoc'''
            self.progressbar['value'] = percentage

        def pack_bar(self):
            '''Pydoc'''
            self.progressbar.pack()
    
    def _setup(self):
        '''Pydoc'''
        setup_tmp_folder(self.master.cwd)
        self.seed_val = set_seed(self.master.seed_value.get())
        self.randomized_rom_path = make_copy_of_rom(self.seed_val, self.master.cwd, self.rom_path)
    
    def _decompress_main(self):
        '''Pydoc'''
        decompressor = Decompressor(self.master.cwd, self.randomized_rom_path)
        decompressor._decompress_main()
    
    def _randomize_world(self):
        '''Pydoc'''
        print("Start of Randomize World")
        world_manip = World_Manipulation_Main.world_manipulation_main(self.master, self.seed_val)
        world_manip._create_worlds()
        world_manip._structs_main()
        world_manip._non_flag_objects_main()
        world_manip._enemies_main()
        world_manip._flagged_objects_main()
        world_manip._note_doors_main()
        if(self.master.skip_furnace_fun_var.get() == 1):
            world_manip._skip_furnace_fun()
        if(self.master.hard_rings_var.get() == 1):
            world_manip._shuffle_clanker_rings()
        if(self.master.croctus_var.get() == 1):
            world_manip._shuffle_croctus()
        if(self.master.hard_races_var.get() == 1):
            world_manip._shuffle_boggy_race_flags()
        if(self.master.ancient_ones_var.get() == 1):
            world_manip._shuffle_ancient_ones()
        if(self.master.maze_jinxy_heads_var.get() == 1):
            world_manip._shuffle_jinxy_heads()
        print("End of Randomize World")
    
    def _misc_options(self):
        '''Pydoc'''
        print("Start of Misc Options")
        misc_manip = Misc_Manipulation_Main.misc_manipulation(self.master.cwd, self.seed_val)
        if((self.master.final_note_door_var.get() == 1) or (self.master.final_puzzle_var.get() == 1)):
            misc_manip._gruntildas_lair_requirements(self.master.final_note_door_var.get(), self.master.final_note_door_value.get(),
                                                     self.master.final_puzzle_var.get(), self.master.final_puzzle_value.get())
        if(self.master.buttons_var.get() == 1):
            misc_manip._rbb_buttons_main()
        if(self.master.bk_model1_var.get() != "Default"):
            bk_model1_json = self.master.bk_model1_json
            preset_name = self.master.bk_model1_var.get()
            misc_manip._bk_model(seed_val=self.seed_val,
                                 banjo_fur_color=bk_model1_json[preset_name]["Banjo_Fur"],
                                 banjo_skin_color=bk_model1_json[preset_name]["Banjo_Skin"],
                                 banjo_toes_color=bk_model1_json[preset_name]["Banjo_Toes"],
                                 kazooie_feather_color=bk_model1_json[preset_name]["Kazooie_Feather"],
                                 kazooie_spot_color=bk_model1_json[preset_name]["Kazooie_Spot"],
                                 backpack_color=bk_model1_json[preset_name]["Backpack"],
                                 banjo_shorts_color=bk_model1_json[preset_name]["Shorts"]
                                 )
        if((self.master.short_sounds_var.get() == 1) or (self.master.jingles_var.get() == 1) or (self.master.music_var.get() == 1)):
            misc_manip._shuffle_music(self.seed_val, self.master.cwd, self.rom_path, self.master.short_sounds_var.get(), self.master.jingles_var.get(), self.master.music_var.get(), self.master.beta_sounds_var.get())
        print("End of Misc Options")
    
    def _compress_main(self):
        '''Pydoc'''
        compressor = Compressor(self.seed_val, self.master.cwd)
        compressor.reinsert_setup_files()
        compressor.misc_compress()
    
    def _crc_tool(self):
        '''Pydoc'''
        print("Start of CRC Tool")
        run_crc_tool(self.seed_val, self.rom_path)
        print("End of CRC Tool")

    def _clean_up(self):
        '''Pydoc'''
        print("Start of Clean Up")
        if(self.master.remove_files_var.get() == 1):
            clean_up = CleanUp(self.master.cwd)
            clean_up._remove_bin_files()
        print("End of Clean Up")

    def _randomization_process(self):
        self.pb_label.set_text("Setting up...")
        self._setup()
        self.progress_bar.update_bar(5)
        self.pb_label.set_text("Decompressing...")
        self._decompress_main()
        self.progress_bar.update_bar(20)
        self.pb_label.set_text("Randomizing Worlds...")
        self._randomize_world()
        self.progress_bar.update_bar(60)
        self.pb_label.set_text("Miscellaneous Options...")
        self._misc_options()
        self.progress_bar.update_bar(70)
        self.pb_label.set_text("Compressing...")
        self._compress_main()
        self.progress_bar.update_bar(85)
        self.pb_label.set_text("Using CRC Tool...")
        self._crc_tool()
        self.progress_bar.update_bar(95)
        self.pb_label.set_text("Cleaning Up Extra Files...")
        self._clean_up()
        self.progress_bar.update_bar(100)
        self.pb_label.set_text("Done! You Can Close The Window!")

    def _main(self):
        ########################
        ### PROGRESS BAR GUI ###
        ########################
        # Label
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
        ### Main Loop ###
        self.progress_bar_window.mainloop()