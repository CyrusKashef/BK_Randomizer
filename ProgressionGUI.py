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

from Randomization_Processes.Setup_Functions import setup_tmp_folder, set_seed, make_copy_of_rom
from Randomization_Processes.Decompress_Functions import decompressor
from Randomization_Processes.Compress_Functions import reinsert_setup_files
from Randomization_Processes.World_Manipulation import World_Manipulation_Main

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
        def __init__(self, window, bar_length=100, bar_mode='determinate'):
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
        decompressor(self.master.cwd, self.randomized_rom_path)
    
    def _randomize_world(self):
        '''Pydoc'''
        print("Start of Randomize World")
        world_manip = World_Manipulation_Main.world_manipulation_main()
        world_manip._create_worlds()
        world_manip._structs_main()
        world_manip._non_flag_objects_main()
        world_manip._enemies_main()
        world_manip._flagged_objects_main()
        print("End of Randomize World")
    
    def _misc_options(self):
        '''Pydoc'''
        print("Start of Misc Options")
        time.sleep(randint(1,3))
        print("End of Misc Options")
    
    def _compress_main(self):
        '''Pydoc'''
        reinsert_setup_files(self.seed_val, self.master.cwd)
    
    def _crc_tool(self):
        '''Pydoc'''
        print("Start of CRC Tool")
        time.sleep(randint(1,3))
        print("End of CRC Tool")

    def _randomization_process(self):
        self.pb_label.set_text("Setting up...")
        self._setup()
        self.pb_label.set_text("Decompressing...")
        self._decompress_main()
        self.progress_bar.update_bar(20)
        self.pb_label.set_text("Randomizing Worlds...")
        self._randomize_world()
        self.progress_bar.update_bar(40)
        self.pb_label.set_text("Miscellaneous Options...")
        self._misc_options()
        self.progress_bar.update_bar(60)
        self.pb_label.set_text("Compressing...")
        self._compress_main()
        self.progress_bar.update_bar(80)
        self.pb_label.set_text("Using CRC Tool...")
        self._crc_tool()
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