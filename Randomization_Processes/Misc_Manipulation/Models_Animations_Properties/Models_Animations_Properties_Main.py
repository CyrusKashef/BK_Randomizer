'''
Created on Mar 8, 2022

@author: Cyrus
'''

from Randomization_Processes.Misc_Manipulation.Models_Animations_Properties.Swap_Models_Main import Swap_Models_Manipulation_Class
from Randomization_Processes.Misc_Manipulation.Models_Animations_Properties.Properties_Main import Properties_Manipulation_Class
from Randomization_Processes.Misc_Manipulation.Models_Animations_Properties.Animation_Main import Swap_Animations_Manipulation
from ...Common_Functions import read_json

class Models_Animations_Properties_Class():
    def __init__(self, seed_val, file_dir, randomized_rom_path, selected_json, cheat_sheet=0):
        self.seed_val = seed_val
        self.file_dir = file_dir
        self.randomized_rom_path = randomized_rom_path
        self.cheat_sheet = cheat_sheet
        self._master_dict = read_json(f"{self.file_dir}Randomization_Processes/Misc_Manipulation/Models_Animations_Properties/{selected_json}.json")
    
    def _models_main(self):
        models_dict = self._master_dict["Models"]
        swap_model_manip = Swap_Models_Manipulation_Class(self.seed_val, self.file_dir, self.randomized_rom_path, models_dict)
        swap_model_manip._model_manip_main()
    
    def _animations_main(self):
        animations_dict = self._master_dict["Animations"]
        swap_animation_manip = Swap_Animations_Manipulation(self.seed_val, self.file_dir, self.randomized_rom_path, animations_dict)
        swap_animation_manip._animation_manip_main()
    
    def _properties_main(self):
        properties_dict = self._master_dict["Properties"]
        properties_manip_obj = Properties_Manipulation_Class(self.seed_val, self.file_dir, properties_dict)
        properties_manip_obj._swap_properties_main()
        if(self.cheat_sheet == 1):
            properties_manip_obj._generate_cheat_sheet()