'''
Created on Sep 5, 2021

@author: Cyrus
'''

########################
### PYTHON FUNCTIONS ###
########################

import random

####################
### FILE IMPORTS ###
####################

from .Generic_World import World
from .Generic_Setup_File import SetupFile
from ..Dicts_And_Lists import Structs, Non_Flagged_Objects, Enemies, Flagged_Objects

class world_manipulation_main():
    def __init__(self):
        self.world_list = []
        self.flagged_object_info_list = []
        self.non_flag_object_info_list = []
        self.struct_info_list = []
        self.brentilda_info_list = []
        self.bottles_info_list = []
        self.ground_enemy_info_list = []
        self.flying_enemy_info_list = []
        self.wall_enemy_info_list = []
        self.misc_enemy_info_list = []
        self.warp_entry_index_dict = {}
        self.warp_entry_info_dict = {}
        self.croctus_info_list = []
        self.clanker_rings_info_list = []
        self.ancient_ones_info_list = []
        self.jinxy_head_info_list = []
    
    def _shuffle_list(self, original_list, seed_val=0, address=0):
        random.seed(a=(seed_val + address))
        random.shuffle(original_list)
    
    def _create_worlds(self):
        # MUMBOS MOUNTAIN
        self.mumbos_mountain = World("Mumbo's Mountain")
        self.mumbos_mountain._add_setup_file(SetupFile("9788", "Main Area"))
        self.mumbos_mountain._add_setup_file(SetupFile("97D8", "Ticker's Tower"))
        self.mumbos_mountain._add_setup_file(SetupFile("97E8", "Mumbo's Skull"))
        self.world_list.append(self.mumbos_mountain)
        # TREASURE TROVE COVE
#         self.treasure_trove_cove = World("Treasure Trove Cove")
        # CLANKER'S CAVERN
#         self.clankers_cavern = World("Clanker's Cavern")
        # BUBBLEGLOOP SWAMP
#         self.bubblegloop_swamp = World("Bubblegloop Swamp")
        # FREEZEEZY PEAK
#         self.freezeezy_peak = World("Freezeezy Peak")
        # GOBI'S VALLEY
#         self.gobis_valley = World("Gobi's Valley")
        # MAD MONSTER MANSION
#         self.mad_monster_mansion = World("Mad Monster Mansion")
        # RUSTY BUCKET BAY
#         self.rusty_bucket_bay = World("Rusty Bucket Bay")
        # CLICK CLOCK WOOD
#         self.click_clock_wood_spring = World("Click Clock Wood Spring")
#         self.click_clock_wood_summer = World("Click Clock Wood Summer")
#         self.click_clock_wood_fall = World("Click Clock Wood Fall")
#         self.click_clock_wood_winter = World("Click Clock Wood Winter")
#         self.click_clock_wood = World("Click Clock Wood")
        # GRUNTILDA'S LAIR
#         self.gruntildas_lair = World("Gruntilda's Lair")
    
    ###############
    ### STRUCTS ###
    ###############
    def _gather_structs(self, world_object):
        for setup_file in world_object._setup_list:
            for item_search_string in Structs.collectable_struct_id_list:
                setup_file._locate_item_index(item_search_string, "Struct")
            if(world_object._world_name == "Mumbo's Mountain"):
                for item_search_string in Structs.abnormal_collectable_struct_id_list:
                    setup_file._locate_item_index(item_search_string, "Struct")
    
    def _shuffle_structs_within_world(self, world_object):
        for setup_file in world_object._setup_list:
            for struct_info_list in setup_file.struct_info_list:
                self.struct_info_list.append(struct_info_list)
        self._shuffle_list(self.struct_info_list)
    
    def _move_structs_within_world(self, world_object):
        list_index_start = 0
        for setup_file in world_object._setup_list:
            for list_index in range(len(setup_file.struct_index_list)):
                setup_file._set_struct(setup_file.struct_index_list[list_index], self.struct_info_list[list_index_start + list_index])
            list_index_start += len(setup_file.struct_index_list)

    def _structs_main(self):
        for world_object in self.world_list:
            self._gather_structs(world_object)
            self._shuffle_structs_within_world(world_object)
            self._move_structs_within_world(world_object)
    
    ###########################
    ### NON FLAGGED OBJECTS ###
    ###########################
    
    def _gather_non_flag_objects(self, world_object):
        for setup_file in world_object._setup_list:
            for item_search_string in Non_Flagged_Objects.obj_no_flag_id_list:
                setup_file._locate_item_index(item_search_string, "No_Flagged_Object")
            for item_search_string in Non_Flagged_Objects.abnormal_obj_no_flag_id_list:
                setup_file._locate_item_index(item_search_string, "No_Flagged_Object")
    
    def _shuffle_non_flag_objects_within_world(self, world_object):
        for setup_file in world_object._setup_list:
            for non_flag_object_info_list in setup_file.non_flag_object_info_list:
                self.non_flag_object_info_list.append(non_flag_object_info_list)
        self._shuffle_list(self.non_flag_object_info_list)
    
    def _move_non_flag_objects_within_world(self, world_object):
        list_index_start = 0
        for setup_file in world_object._setup_list:
            for list_index in range(len(setup_file.non_flag_object_index_list)):
                setup_file._set_object(setup_file.non_flag_object_index_list[list_index], self.non_flag_object_info_list[list_index_start + list_index])
            list_index_start += len(setup_file.non_flag_object_index_list)

    def _non_flag_objects_main(self):
        for world_object in self.world_list:
            self._gather_non_flag_objects(world_object)
            self._shuffle_non_flag_objects_within_world(world_object)
            self._move_non_flag_objects_within_world(world_object)

    ###############
    ### ENEMIES ###
    ###############
    
    def _gather_enemies(self, world_object):
        for setup_file in world_object._setup_list:
            for item_search_string in Enemies.enemy_id_dict["Global"]["Ground"]:
                setup_file._locate_item_index(item_search_string, "Ground_Enemy")
            if("Ground" in Enemies.enemy_id_dict[world_object._world_name]):
                for item_search_string in Enemies.enemy_id_dict[world_object._world_name]["Ground"]:
                    setup_file._locate_item_index(item_search_string, "Ground_Enemy")
            for item_search_string in Enemies.enemy_id_dict["Global"]["Wall"]:
                setup_file._locate_item_index(item_search_string, "Wall_Enemy")
            if("Wall" in Enemies.enemy_id_dict[world_object._world_name]):
                for item_search_string in Enemies.enemy_id_dict[world_object._world_name]["Wall"]:
                    setup_file._locate_item_index(item_search_string, "Wall_Enemy")
            for item_search_string in Enemies.enemy_id_dict["Global"]["Flying"]:
                setup_file._locate_item_index(item_search_string, "Flying_Enemy")
            if("Flying" in Enemies.enemy_id_dict[world_object._world_name]):
                for item_search_string in Enemies.enemy_id_dict[world_object._world_name]["Flying"]:
                    setup_file._locate_item_index(item_search_string, "Flying_Enemy")
    
    def _shuffle_enemies_within_world(self, world_object):
        for setup_file in world_object._setup_list:
            for ground_enemy_info_list in setup_file.ground_enemy_info_list:
                self.ground_enemy_info_list.append(ground_enemy_info_list)
            for wall_enemy_info_list in setup_file.wall_enemy_info_list:
                self.wall_enemy_info_list.append(wall_enemy_info_list)
            for flying_enemy_info_list in setup_file.flying_enemy_info_list:
                self.flying_enemy_info_list.append(flying_enemy_info_list)
        self._shuffle_list(self.ground_enemy_info_list)
        self._shuffle_list(self.wall_enemy_info_list)
        self._shuffle_list(self.flying_enemy_info_list)
    
    def _randomize_enemies(self, world_object):
        ground_enemy_list = Enemies.enemy_id_dict["Global"]["Ground"]
        if("Ground" in Enemies.enemy_id_dict[world_object._world_name]):
            ground_enemy_list += Enemies.enemy_id_dict[world_object._world_name]["Ground"]
        wall_enemy_list = Enemies.enemy_id_dict["Global"]["Wall"]
        if("Wall" in Enemies.enemy_id_dict[world_object._world_name]):
            wall_enemy_list += Enemies.enemy_id_dict[world_object._world_name]["Wall"]
        flying_enemy_list = Enemies.enemy_id_dict["Global"]["Flying"]
        if("Flying" in Enemies.enemy_id_dict[world_object._world_name]):
            flying_enemy_list += Enemies.enemy_id_dict[world_object._world_name]["Flying"]
        for setup_file in world_object._setup_list:
            for item_count in range(len(setup_file.ground_enemy_info_list)):
                new_enemy = random.choice(ground_enemy_list)
                new_enemy_info = {
                    "Script1": int(new_enemy[:2], 16),
                    "Script2": int(new_enemy[2:4], 16),
                    "Obj_ID1": int(new_enemy[4:6], 16),
                    "Obj_ID2": int(new_enemy[6:], 16),
                    }
                self.ground_enemy_info_list.append(new_enemy_info)
            for item_count in range(len(setup_file.wall_enemy_info_list)):
                new_enemy = random.choice(wall_enemy_list)
                new_enemy_info = {
                    "Script1": int(new_enemy[:2], 16),
                    "Script2": int(new_enemy[2:4], 16),
                    "Obj_ID1": int(new_enemy[4:6], 16),
                    "Obj_ID2": int(new_enemy[6:], 16),
                    }
                self.wall_enemy_info_list.append(new_enemy_info)
            for item_count in range(len(setup_file.flying_enemy_info_list)):
                new_enemy = random.choice(flying_enemy_list)
                new_enemy_info = {
                    "Script1": int(new_enemy[:2], 16),
                    "Script2": int(new_enemy[2:4], 16),
                    "Obj_ID1": int(new_enemy[4:6], 16),
                    "Obj_ID2": int(new_enemy[6:], 16),
                    }
                self.flying_enemy_info_list.append(new_enemy_info)
        
    def _move_enemies_within_world(self, world_object):
        list_index_start = 0
        for setup_file in world_object._setup_list:
            for list_index in range(len(setup_file.ground_enemy_index_list)):
                setup_file._set_object(setup_file.ground_enemy_index_list[list_index], self.ground_enemy_info_list[list_index_start + list_index])
            list_index_start += len(setup_file.ground_enemy_index_list)
        list_index_start = 0
        for setup_file in world_object._setup_list:
            for list_index in range(len(setup_file.wall_enemy_index_list)):
                setup_file._set_object(setup_file.wall_enemy_index_list[list_index], self.wall_enemy_info_list[list_index_start + list_index])
            list_index_start += len(setup_file.wall_enemy_index_list)
        list_index_start = 0
        for setup_file in world_object._setup_list:
            for list_index in range(len(setup_file.flying_enemy_index_list)):
                setup_file._set_object(setup_file.flying_enemy_index_list[list_index], self.flying_enemy_info_list[list_index_start + list_index])
            list_index_start += len(setup_file.flying_enemy_index_list)

    def _enemies_main(self):
        for world_object in self.world_list:
            self._gather_enemies(world_object)
            #self._shuffle_enemies_within_world(world_object)
            self._randomize_enemies(world_object)
            self._move_enemies_within_world(world_object)
    
    #######################
    ### FLAGGED OBJECTS ###
    #######################
    
    def _gather_flagged_objects(self, world_object):
        for setup_file in world_object._setup_list:
            for item_id in Flagged_Objects.flagged_object_dict[world_object._world_name]:
                object_search_string = Flagged_Objects.flagged_object_dict[world_object._world_name][item_id]["Object"]
                flag_search_string = Flagged_Objects.flagged_object_dict[world_object._world_name][item_id]["Flag"]
                setup_file._locate_flagged_object_index(object_search_string, flag_search_string)
    
    def _shuffle_flagged_objects_within_world(self, world_object):
        for setup_file in world_object._setup_list:
            for flagged_object_info_list in setup_file.flagged_object_info_list:
                self.flagged_object_info_list.append(flagged_object_info_list)
        self._shuffle_list(self.flagged_object_info_list)
    
    def _move_flagged_objects_within_world(self, world_object):
        list_index_start = 0
        for setup_file in world_object._setup_list:
            for list_index in range(len(setup_file.flagged_object_index_list)):
                obj_index = setup_file.flagged_object_index_list[list_index][0]
                flag_index = setup_file.flagged_object_index_list[list_index][1]
                obj_info = self.flagged_object_info_list[list_index+list_index_start][0]
                flag_info = self.flagged_object_info_list[list_index+list_index_start][1]
                setup_file._set_flagged_object(obj_index, obj_info, flag_index, flag_info)
            list_index_start += len(setup_file.flagged_object_index_list)
    
    def _flagged_objects_main(self):
        for world_object in self.world_list:
            self._gather_flagged_objects(world_object)
            self._shuffle_flagged_objects_within_world(world_object)
            self._move_flagged_objects_within_world(world_object)
    
    ########################
    ### SEQUENCE OBJECTS ###
    ########################
        
    def _gather_clanker_rings(self):
        pass

    def _gather_croctus(self):
        pass
    
    def _gather_boggy_race_flags(self):
        pass
    
    def _gather_ancient_ones(self):
        pass
    
    def _gather_jinxy_heads(self):
        pass
    
    def _get_ccw_buttons(self):
        pass