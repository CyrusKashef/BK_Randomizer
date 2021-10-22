'''
Created on Sep 5, 2021

@author: Cyrus

World Manipulation Features
* Structs (Notes/Eggs/Feathers)
* Flagged Objects (Jiggies/Empty Honeycombs/Mumbo Tokens)
* Non-Flagged Objects (Jinjos/1-Ups/Misc Items)
* Enemies (Ground/Flying/Wall)
* World Order Warps
* Within World Warps
* Removing Note Doors
* Skip Furnace Fun
* CC Specifics (CC Rings)
* FP Specifics (Hard Race)
* GV Specifics (Ancient Ones/Jinxy Heads)
* CCW Specifics (Season Order)

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
from ..Dicts_And_Lists import Structs, Non_Flagged_Objects, Enemies, Flagged_Objects, Sequences
from .World_Order_Logic import World_Order_Basic
from .World_Order_Logic_Bottles import World_Order_Bottles
from ..Common_Functions import leading_zeros, possible_negative, fit_for_hex

################################
### WORLD MANIPULATION CLASS ###
################################

class world_manipulation_main():
    '''The world manipulation class makes changes within the world maps'''
    def __init__(self, grandmaster, seed):
        '''Initializes the world manipulation class'''
        self.grandmaster = grandmaster
        self.seed = seed
        self.world_list = []
        self.flagged_object_info_list = []
        self.non_flag_object_info_list = []
        self.struct_info_list = []
        self.ground_enemy_info_list = []
        self.flying_enemy_info_list = []
        self.wall_enemy_info_list = []
        self.warp_entry_index_dict = {}
        self.warp_entry_info_dict = {}
        self.croctus_info_list = []
        self.clanker_rings_info_list = []
        self.ancient_ones_info_list = []
        self.jinxy_head_info_list = []
    
    def _shuffle_list(self, original_list, address=0):
        '''Shuffles list based on the current address, if applicable'''
        random.seed(a=(self.seed + address))
        random.shuffle(original_list)
    
    def _choose_from_list(self, original_list, address=0, increment=0):
        '''Selects an option from a list based on the current address and the number of increments, if applicable'''
        random.seed(a=(self.seed + address + increment))
        random_choice = random.choice(original_list)
        return random_choice
    
    def _create_worlds(self):
        '''Creates every world using the generic world and generic setup file classes, including individual seasons for click clock wood, if applicable'''
        # MUMBOS MOUNTAIN
        self.mumbos_mountain = World("Mumbo's Mountain")
        self.mumbos_mountain._add_setup_file(SetupFile("9788", "Main Area"))
        self.mumbos_mountain._add_setup_file(SetupFile("97D8", "Ticker's Tower"))
        self.mumbos_mountain._add_setup_file(SetupFile("97E8", "Mumbo's Skull"))
        self.world_list.append(self.mumbos_mountain)
        # TREASURE TROVE COVE
        self.treasure_trove_cove = World("Treasure Trove Cove")
        self.treasure_trove_cove._add_setup_file(SetupFile("97B0", "Main Area"))
        self.treasure_trove_cove._add_setup_file(SetupFile("97A0", "Blubber's Ship"))
        self.treasure_trove_cove._add_setup_file(SetupFile("97A8", "Nipper's Shell"))
        self.treasure_trove_cove._add_setup_file(SetupFile("97C8", "Sandcastle"))
        self.world_list.append(self.treasure_trove_cove)
        # CLANKER'S CAVERN
        self.clankers_cavern = World("Clanker's Cavern")
        self.clankers_cavern._add_setup_file(SetupFile("97D0", "Main Area"))
        self.clankers_cavern._add_setup_file(SetupFile("9888", "Inside Clanker Mouth And Belly"))
        self.clankers_cavern._add_setup_file(SetupFile("9880", "Inside Clanker Blowhole Entrance"))
        self.clankers_cavern._add_setup_file(SetupFile("9890", "Inside Clanker Gold Feather Room"))
        self.world_list.append(self.clankers_cavern)
        # BUBBLEGLOOP SWAMP
        self.bubblegloop_swamp = World("Bubblegloop Swamp")
        self.bubblegloop_swamp._add_setup_file(SetupFile("97E0", "Main Area"))
        self.bubblegloop_swamp._add_setup_file(SetupFile("97F8", "Mr Vile"))
        self.bubblegloop_swamp._add_setup_file(SetupFile("9800", "Tiptup Choir"))
        self.bubblegloop_swamp._add_setup_file(SetupFile("99B0", "Mumbo's Skull"))
        self.world_list.append(self.bubblegloop_swamp)
        # FREEZEEZY PEAK
        self.freezeezy_peak = World("Freezeezy Peak")
        self.freezeezy_peak._add_setup_file(SetupFile("98B0", "Main Area"))
        self.freezeezy_peak._add_setup_file(SetupFile("9980", "Boggy's Igloo"))
        self.freezeezy_peak._add_setup_file(SetupFile("99B8", "Mumbo's Skull"))
        self.freezeezy_peak._add_setup_file(SetupFile("9A10", "Inside The Tree"))
        self.freezeezy_peak._add_setup_file(SetupFile("9B70", "Wozza's Cave"))
        self.world_list.append(self.freezeezy_peak)
        # GOBI'S VALLEY
        self.gobis_valley = World("Gobi's Valley")
        self.gobis_valley._add_setup_file(SetupFile("9808", "Main Area"))
        self.gobis_valley._add_setup_file(SetupFile("9810", "Puzzle Room"))
        self.gobis_valley._add_setup_file(SetupFile("9818", "King Sandybutt's Tomb"))
        self.gobis_valley._add_setup_file(SetupFile("9820", "Water Room"))
        self.gobis_valley._add_setup_file(SetupFile("9828", "Rupee"))
        self.gobis_valley._add_setup_file(SetupFile("9848", "Jinxy"))
        self.world_list.append(self.gobis_valley)
        # MAD MONSTER MANSION
        self.mad_monster_mansion = World("Mad Monster Mansion")
        self.mad_monster_mansion._add_setup_file(SetupFile("9850", "Main Area"))
        self.mad_monster_mansion._add_setup_file(SetupFile("9BE0", "Septic Tank (Inside Loggo)"))
        self.mad_monster_mansion._add_setup_file(SetupFile("9858", "Church"))
        self.mad_monster_mansion._add_setup_file(SetupFile("9860", "Cellar"))
        self.mad_monster_mansion._add_setup_file(SetupFile("9898", "Tumblar's Shed"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98A0", "Well"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98A8", "Dining Room"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98B8", "Egg Room"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98C0", "Note Room"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98C8", "Red Feather Room"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98D0", "Secret Church Room"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98D8", "Bathroom"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98E0", "Bedroom"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98E8", "Gold Feather Room"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98F0", "Drain Pipe"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98F8", "Mumbo's Skull"))
        self.world_list.append(self.mad_monster_mansion)
        # RUSTY BUCKET BAY
        self.rusty_bucket_bay = World("Rusty Bucket Bay")
        self.rusty_bucket_bay._add_setup_file(SetupFile("9900", "Main Area"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9BD0", "Anchor Room"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9918", "Engine Room"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9920", "Big Fish Warehouse"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9928", "Boat Room"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9930", "First Blue Container (Chompas)"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9938", "Third Blue Container (Mini Kabooms)"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9940", "Sea-Grublin's Cabin"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9948", "Kaboom's Room"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9950", "Mini Kaboom's Room (Pipe)"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9958", "Kitchen"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9960", "Navigation Room"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9968", "Second Blue Container (Sea Grublins)"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9970", "Captain's Room"))
        self.world_list.append(self.rusty_bucket_bay)
        # CLICK CLOCK WOOD - Seasons
        if(self.grandmaster.ccw_var.get() == "By Season"):
            self.click_clock_wood_lobby = World("Click Clock Wood - Lobby")
            self.click_clock_wood_lobby._add_setup_file(SetupFile("9978", "Lobby"))
            self.world_list.append(self.click_clock_wood_lobby)
            self.click_clock_wood_spring = World("Click Clock Wood - Spring")
            self.click_clock_wood_spring._add_setup_file(SetupFile("9990", "Spring Main Area"))
            self.click_clock_wood_spring._add_setup_file(SetupFile("99C8", "Spring Mumbo's Skull"))
            self.click_clock_wood_spring._add_setup_file(SetupFile("9A50", "Spring Beehive"))
            self.click_clock_wood_spring._add_setup_file(SetupFile("9A68", "Spring Nabnut's House"))
            self.click_clock_wood_spring._add_setup_file(SetupFile("9AA0", "Spring Whipcrack Room"))
            self.world_list.append(self.click_clock_wood_spring)
            self.click_clock_wood_summer = World("Click Clock Wood - Summer")
            self.click_clock_wood_summer._add_setup_file(SetupFile("9998", "Summer Main Area"))
            self.click_clock_wood_summer._add_setup_file(SetupFile("99D0", "Summer Mumbo's Skull"))
            self.click_clock_wood_summer._add_setup_file(SetupFile("9A48", "Summer Beehive"))
            self.click_clock_wood_summer._add_setup_file(SetupFile("9A70", "Summer Nabnut's House"))
            self.click_clock_wood_summer._add_setup_file(SetupFile("9AA8", "Summer Whipcrack Room"))
            self.world_list.append(self.click_clock_wood_summer)
            self.click_clock_wood_fall = World("Click Clock Wood - Fall")
            self.click_clock_wood_fall._add_setup_file(SetupFile("99A0", "Fall Main Area"))
            self.click_clock_wood_fall._add_setup_file(SetupFile("99D8", "Fall Mumbo's Skull"))
            self.click_clock_wood_fall._add_setup_file(SetupFile("9A58", "Fall Beehive"))
            self.click_clock_wood_fall._add_setup_file(SetupFile("9A78", "Fall Nabnut's House"))
            self.click_clock_wood_fall._add_setup_file(SetupFile("9A90", "Fall Nabnut's Attic"))
            self.click_clock_wood_fall._add_setup_file(SetupFile("9AB0", "Fall Whipcrack Room"))
            self.world_list.append(self.click_clock_wood_fall)
            self.click_clock_wood_winter = World("Click Clock Wood - Winter")
            self.click_clock_wood_winter._add_setup_file(SetupFile("99A8", "Winter Main Area"))
            self.click_clock_wood_winter._add_setup_file(SetupFile("99E0", "Winter Mumbo's Skull"))
            self.click_clock_wood_winter._add_setup_file(SetupFile("9A80", "Winter Nabnut's House"))
            self.click_clock_wood_winter._add_setup_file(SetupFile("9A88", "Winter Nabnut's Attic 1 (Nuts)"))
            self.click_clock_wood_winter._add_setup_file(SetupFile("9A98", "Winter Nabnut's Attic 2 (Water)"))
            self.click_clock_wood_winter._add_setup_file(SetupFile("9AB8", "Winter Whipcrack Room"))
            self.world_list.append(self.click_clock_wood_winter)
        # CLICK CLOCK WOOD - All
        elif(self.grandmaster.ccw_var.get() == "Within World"):
            self.click_clock_wood = World("Click Clock Wood")
            self.click_clock_wood._add_setup_file(SetupFile("9978", "Lobby"))
            self.click_clock_wood._add_setup_file(SetupFile("9990", "Spring Main Area"))
            self.click_clock_wood._add_setup_file(SetupFile("99C8", "Spring Mumbo's Skull"))
            self.click_clock_wood._add_setup_file(SetupFile("9A50", "Spring Beehive"))
            self.click_clock_wood._add_setup_file(SetupFile("9A68", "Spring Nabnut's House"))
            self.click_clock_wood._add_setup_file(SetupFile("9AA0", "Spring Whipcrack Room"))
            self.click_clock_wood._add_setup_file(SetupFile("9998", "Summer Main Area"))
            self.click_clock_wood._add_setup_file(SetupFile("99D0", "Summer Mumbo's Skull"))
            self.click_clock_wood._add_setup_file(SetupFile("9A48", "Summer Beehive"))
            self.click_clock_wood._add_setup_file(SetupFile("9A70", "Summer Nabnut's House"))
            self.click_clock_wood._add_setup_file(SetupFile("9AA8", "Summer Whipcrack Room"))
            self.click_clock_wood._add_setup_file(SetupFile("99A0", "Fall Main Area"))
            self.click_clock_wood._add_setup_file(SetupFile("99D8", "Fall Mumbo's Skull"))
            self.click_clock_wood._add_setup_file(SetupFile("9A58", "Fall Beehive"))
            self.click_clock_wood._add_setup_file(SetupFile("9A78", "Fall Nabnut's House"))
            self.click_clock_wood._add_setup_file(SetupFile("9A90", "Fall Nabnut's Attic"))
            self.click_clock_wood._add_setup_file(SetupFile("9AB0", "Fall Whipcrack Room"))
            self.click_clock_wood._add_setup_file(SetupFile("99A8", "Winter Main Area"))
            self.click_clock_wood._add_setup_file(SetupFile("99E0", "Winter Mumbo's Skull"))
            self.click_clock_wood._add_setup_file(SetupFile("9A80", "Winter Nabnut's House"))
            self.click_clock_wood._add_setup_file(SetupFile("9A88", "Winter Nabnut's Attic 1 (Nuts)"))
            self.click_clock_wood._add_setup_file(SetupFile("9A98", "Winter Nabnut's Attic 2 (Water)"))
            self.click_clock_wood._add_setup_file(SetupFile("9AB8", "Winter Whipcrack Room"))
            self.world_list.append(self.click_clock_wood)
        # GRUNTILDA'S LAIR
        self.gruntildas_lair = World("Gruntilda's Lair")
        self.gruntildas_lair._add_setup_file(SetupFile("9AC0", "Floor 1 MM Puzzle And Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AC8", "Floor 2 TTC and CC Puzzles"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AD0", "Floor 3 CCW Puzzle"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B00", "Floor 4 Giant Gruntilda Statue"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AE8", "Floor 5 Giant Urn and GV Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AF0", "Floor 6 Grunty's Head and FP Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B40", "Floor 7 CCW Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9C10", "Floor 8 Gruntilda Puzzle And Dingpot"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AD8", "Floor 3 Pipe Room"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AE0", "TTC Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AF8", "CC Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B08", "BGS Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B18", "GV Puzzle"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B20", "MMM Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B28", "Floor 6 Water Switch Area"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B30", "RBB Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B38", "MMM and RBB Puzzles"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B48", "Coffin Room"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B78", "Path To Quiz Show"))
        self.gruntildas_lair._add_setup_file(SetupFile("9BE8", "Furnace Fun"))
        self.gruntildas_lair._add_setup_file(SetupFile("9BF8", "Gruntilda Boss Fight"))
        self.world_list.append(self.gruntildas_lair)
    
    ###############
    ### STRUCTS ###
    ###############
    def _gather_structs(self, world_object):
        '''Collects the structs per setup for the world'''
        for setup_file in world_object._setup_list:
            for item_search_string in Structs.collectable_struct_id_list:
                setup_file._locate_item_index(item_search_string, "Struct")
            if((world_object._world_name == "Mumbo's Mountain") and (self.grandmaster.flowers_var.get())):
                for item_search_string in Structs.abnormal_collectable_struct_id_list:
                    setup_file._locate_item_index(item_search_string, "Struct")
    
    def _shuffle_structs_within_world(self, world_object):
        '''Shuffles the structs found within the world'''
        for setup_file in world_object._setup_list:
            for struct_info_list in setup_file.struct_info_list:
                self.struct_info_list.append(struct_info_list)
        self._shuffle_list(self.struct_info_list)
    
    def _randomize_structs(self, world_object):
        '''Randomizes the value of each struct found'''
        struct_list = [
            { # Note
            "Obj_ID1": 0x16,
            "Obj_ID2": 0x40,
            "Unknown1": 0x0,
            "Unknown2": 0xB4,
            "Size": 0x0,
            },
            { # Egg
            "Obj_ID1": 0x16,
            "Obj_ID2": 0x50,
            "Unknown1": 0x0,
            "Unknown2": 0xA0,
            "Size": 0x0,
            },
            { # Red Feather
            "Obj_ID1": 0x0,
            "Obj_ID2": 0xE0,
            "Unknown1": 0x0,
            "Unknown2": 0xDC,
            "Size": 0x0,
            },
            { # Gold Feather
            "Obj_ID1": 0x15,
            "Obj_ID2": 0xF0,
            "Unknown1": 0x0,
            "Unknown2": 0xDC,
            "Size": 0x0,
            },
            ]
        for setup_file in world_object._setup_list:
            for item_count in range(len(setup_file.struct_info_list)):
                new_struct_info = self._choose_from_list(struct_list, setup_file.setup_address, increment=item_count)
                self.struct_info_list.append(new_struct_info)
    
    def _oh_whoops_all_notes(self, world_object):
        '''Turns all found structs into notes'''
        note_info = {
            "Obj_ID1": 0x16,
            "Obj_ID2": 0x40,
            "Unknown1": 0x0,
            "Unknown2": 0xB4,
            "Size": 0x0,
            }
        for setup_file in world_object._setup_list:
            for struct_info_count in setup_file.struct_info_list:
                self.struct_info_list.append(note_info)
    
    def _move_structs_within_world(self, world_object):
        '''Places the randomized struct list back into the world'''
        list_index_start = 0
        for setup_file in world_object._setup_list:
            for list_index in range(len(setup_file.struct_index_list)):
                setup_file._set_struct(setup_file.struct_index_list[list_index], self.struct_info_list[list_index_start + list_index])
            list_index_start += len(setup_file.struct_index_list)

    def _structs_main(self):
        '''Runs the struct options that are not NONE'''
        if(self.grandmaster.struct_var.get() == "Shuffle"):
            for world_object in self.world_list:
                self._gather_structs(world_object)
                self._shuffle_structs_within_world(world_object)
                self._move_structs_within_world(world_object)
                self.struct_info_list = []
        if(self.grandmaster.struct_var.get() == "Randomize"):
            for world_object in self.world_list:
                self._gather_structs(world_object)
                self._randomize_structs(world_object)
                self._move_structs_within_world(world_object)
                self.struct_info_list = []
        if(self.grandmaster.struct_var.get() == "All Notes"):
            for world_object in self.world_list:
                self._gather_structs(world_object)
                self._oh_whoops_all_notes(world_object)
                self._move_structs_within_world(world_object)
                self.struct_info_list = []
            self._brentilda_main()
    
    ###########################
    ### NON FLAGGED OBJECTS ###
    ###########################
    
    def _gather_non_flag_objects(self, world_object):
        '''Collects the non-flagged objects per setup for the world'''
        for setup_file in world_object._setup_list:
            for item_search_string in Non_Flagged_Objects.obj_no_flag_id_list:
                setup_file._locate_item_index(item_search_string, "No_Flagged_Object")
            if(self.grandmaster.non_flagged_object_abnormalities_var.get()):
                for item_search_string in Non_Flagged_Objects.abnormal_obj_no_flag_id_list:
                    setup_file._locate_item_index(item_search_string, "No_Flagged_Object")
    
    def _shuffle_non_flag_objects_within_world(self, world_object):
        '''Shuffles the non-flagged objects found within the world'''
        for setup_file in world_object._setup_list:
            for non_flag_object_info_list in setup_file.non_flag_object_info_list:
                self.non_flag_object_info_list.append(non_flag_object_info_list)
        self._shuffle_list(self.non_flag_object_info_list, setup_file.setup_address)
    
    def _move_non_flag_objects_within_world(self, world_object):
        '''Places the randomized non-flagged objects list back into the world'''
        list_index_start = 0
        for setup_file in world_object._setup_list:
            for list_index in range(len(setup_file.non_flag_object_index_list)):
                setup_file._set_object(setup_file.non_flag_object_index_list[list_index], self.non_flag_object_info_list[list_index_start + list_index])
            list_index_start += len(setup_file.non_flag_object_index_list)

    def _non_flag_objects_main(self):
        '''Runs the non-flagged objects options that are not NONE'''
        if(self.grandmaster.non_flagged_object_var.get() == "Shuffle"):
            for world_object in self.world_list:
                self._gather_non_flag_objects(world_object)
                self._shuffle_non_flag_objects_within_world(world_object)
                self._move_non_flag_objects_within_world(world_object)
                self.non_flag_object_info_list = []

    ###############
    ### ENEMIES ###
    ###############
    
    def _gather_enemies(self, world_object):
        '''Collects the enemies per setup for the world'''
        for setup_file in world_object._setup_list:
            for item_search_string in Enemies.enemy_id_dict["Global"]["Ground"]:
                setup_file._locate_item_index(item_search_string, "Ground_Enemy")
            for item_search_string in Enemies.additional_enemy_id_dict["Ground"]:
                setup_file._locate_item_index(item_search_string, "Ground_Enemy")
            if("Ground" in Enemies.enemy_id_dict[world_object._world_name]):
                for item_search_string in Enemies.enemy_id_dict[world_object._world_name]["Ground"]:
                    setup_file._locate_item_index(item_search_string, "Ground_Enemy")
            for item_search_string in Enemies.enemy_id_dict["Global"]["Wall"]:
                setup_file._locate_item_index(item_search_string, "Wall_Enemy")
            for item_search_string in Enemies.additional_enemy_id_dict["Wall"]:
                setup_file._locate_item_index(item_search_string, "Wall_Enemy")
            if("Wall" in Enemies.enemy_id_dict[world_object._world_name]):
                for item_search_string in Enemies.enemy_id_dict[world_object._world_name]["Wall"]:
                    setup_file._locate_item_index(item_search_string, "Wall_Enemy")
            for item_search_string in Enemies.enemy_id_dict["Global"]["Flying"]:
                setup_file._locate_item_index(item_search_string, "Flying_Enemy")
            for item_search_string in Enemies.additional_enemy_id_dict["Flying"]:
                setup_file._locate_item_index(item_search_string, "Flying_Enemy")
            if("Flying" in Enemies.enemy_id_dict[world_object._world_name]):
                for item_search_string in Enemies.enemy_id_dict[world_object._world_name]["Flying"]:
                    setup_file._locate_item_index(item_search_string, "Flying_Enemy")
            if(self.grandmaster.enemies_abnormalities_var.get()):
                for item_search_string in Enemies.abnormal_enemy_id_list["Global"]["Ground"]:
                    setup_file._locate_item_index(item_search_string, "Ground_Enemy")
                for item_search_string in Enemies.additional_abnormal_enemy_id_dict["Ground"]:
                    setup_file._locate_item_index(item_search_string, "Ground_Enemy")
                if("Ground" in Enemies.abnormal_enemy_id_list[world_object._world_name]):
                    for item_search_string in Enemies.enemy_id_dict[world_object._world_name]["Ground"]:
                        setup_file._locate_item_index(item_search_string, "Ground_Enemy")
                for item_search_string in Enemies.abnormal_enemy_id_list["Global"]["Wall"]:
                    setup_file._locate_item_index(item_search_string, "Wall_Enemy")
                for item_search_string in Enemies.additional_abnormal_enemy_id_dict["Wall"]:
                    setup_file._locate_item_index(item_search_string, "Wall_Enemy")
                if("Wall" in Enemies.abnormal_enemy_id_list[world_object._world_name]):
                    for item_search_string in Enemies.abnormal_enemy_id_list[world_object._world_name]["Wall"]:
                        setup_file._locate_item_index(item_search_string, "Wall_Enemy")
                for item_search_string in Enemies.abnormal_enemy_id_list["Global"]["Flying"]:
                    setup_file._locate_item_index(item_search_string, "Flying_Enemy")
                for item_search_string in Enemies.additional_abnormal_enemy_id_dict["Flying"]:
                    setup_file._locate_item_index(item_search_string, "Flying_Enemy")
                if("Flying" in Enemies.abnormal_enemy_id_list[world_object._world_name]):
                    for item_search_string in Enemies.abnormal_enemy_id_list[world_object._world_name]["Flying"]:
                        setup_file._locate_item_index(item_search_string, "Flying_Enemy")
    
    def _shuffle_enemies_within_world(self, world_object):
        '''Shuffles the enemies found within the world'''
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
        '''Randomizes the value of each enemies found'''
        ground_enemy_list = []
        for enemy_id in Enemies.enemy_id_dict["Global"]["Ground"]:
            ground_enemy_list.append(enemy_id)
        if("Ground" in Enemies.enemy_id_dict[world_object._world_name]):
            for enemy_id in Enemies.enemy_id_dict[world_object._world_name]["Ground"]:
                ground_enemy_list.append(enemy_id)
        wall_enemy_list = []
        for enemy_id in Enemies.enemy_id_dict["Global"]["Wall"]:
            wall_enemy_list.append(enemy_id)
        
        if("Wall" in Enemies.enemy_id_dict[world_object._world_name]):
            for enemy_id in Enemies.enemy_id_dict[world_object._world_name]["Wall"]:
                wall_enemy_list.append(enemy_id)
        flying_enemy_list = []
        for enemy_id in Enemies.enemy_id_dict["Global"]["Flying"]:
            flying_enemy_list.append(enemy_id)
        if("Flying" in Enemies.enemy_id_dict[world_object._world_name]):
            for enemy_id in Enemies.enemy_id_dict[world_object._world_name]["Flying"]:
                flying_enemy_list.append(enemy_id)
        for setup_file in world_object._setup_list:
            for item_count in range(len(setup_file.ground_enemy_info_list)):
                new_enemy = self._choose_from_list(ground_enemy_list, setup_file.setup_address, increment=item_count)
                new_enemy_info = {
                    "Script1": int(new_enemy[:2], 16),
                    "Script2": int(new_enemy[2:4], 16),
                    "Obj_ID1": int(new_enemy[4:6], 16),
                    "Obj_ID2": int(new_enemy[6:], 16),
                    }
                self.ground_enemy_info_list.append(new_enemy_info)
            for item_count in range(len(setup_file.wall_enemy_info_list)):
                new_enemy = self._choose_from_list(wall_enemy_list, setup_file.setup_address, increment=item_count)
                new_enemy_info = {
                    "Script1": int(new_enemy[:2], 16),
                    "Script2": int(new_enemy[2:4], 16),
                    "Obj_ID1": int(new_enemy[4:6], 16),
                    "Obj_ID2": int(new_enemy[6:], 16),
                    }
                self.wall_enemy_info_list.append(new_enemy_info)
            for item_count in range(len(setup_file.flying_enemy_info_list)):
                new_enemy = self._choose_from_list(flying_enemy_list, setup_file.setup_address, increment=item_count)
                new_enemy_info = {
                    "Script1": int(new_enemy[:2], 16),
                    "Script2": int(new_enemy[2:4], 16),
                    "Obj_ID1": int(new_enemy[4:6], 16),
                    "Obj_ID2": int(new_enemy[6:], 16),
                    }
                self.flying_enemy_info_list.append(new_enemy_info)
        
    def _move_enemies_within_world(self, world_object):
        '''Places the randomized enemies list back into the world'''
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
        '''Runs the enemies options that are not NONE'''
        if(self.grandmaster.enemies_var.get() == "Shuffle"):
            for world_object in self.world_list:
                self._gather_enemies(world_object)
                self._shuffle_enemies_within_world(world_object)
                self._move_enemies_within_world(world_object)
                self.ground_enemy_info_list = []
                self.flying_enemy_info_list = []
                self.wall_enemy_info_list = []
        elif(self.grandmaster.enemies_var.get() == "Randomize"):
            for world_object in self.world_list:
                self._gather_enemies(world_object)
                self._randomize_enemies(world_object)
                self._move_enemies_within_world(world_object)
                self.ground_enemy_info_list = []
                self.flying_enemy_info_list = []
                self.wall_enemy_info_list = []
    
    #######################
    ### FLAGGED OBJECTS ###
    #######################
    
    def _gather_flagged_objects(self, world_object):
        '''Collects the flagged objects per setup for the world'''
        for setup_file in world_object._setup_list:
            for item_id in Flagged_Objects.flagged_object_dict[world_object._world_name]:
                object_search_string = Flagged_Objects.flagged_object_dict[world_object._world_name][item_id]["Object"]
                flag_search_string = Flagged_Objects.flagged_object_dict[world_object._world_name][item_id]["Flag"]
                setup_file._locate_flagged_object_index(object_search_string, flag_search_string)
    
    def _shuffle_flagged_objects_within_world(self, world_object):
        '''Shuffles the flagged objects found within the world'''
        for setup_file in world_object._setup_list:
            for flagged_object_info_list in setup_file.flagged_object_info_list:
                self.flagged_object_info_list.append(flagged_object_info_list)
        self._shuffle_list(self.flagged_object_info_list)
    
    def _move_flagged_objects_within_world(self, world_object):
        '''Places the randomized flagged objects list back into the world'''
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
        '''Runs the flagged objects options that are not NONE'''
        if(self.grandmaster.flagged_object_var.get() == "Shuffle"):
            for world_object in self.world_list:
                self._gather_flagged_objects(world_object)
                self._shuffle_flagged_objects_within_world(world_object)
                self._move_flagged_objects_within_world(world_object)
                self.flagged_object_info_list = []
    
    #################
    ### BRENTILDA ###
    #################
    
    def _brentilda_main(self):
        '''Replaces the Brentildas with the egg and feather refills for the struct option ALL NOTES'''
        for setup_file in self.gruntildas_lair._setup_list:
            for item_search_string in Sequences.brentilda_list:
                setup_file._locate_item_index(item_search_string, "Brentilda", self.seed)
    
    ##################
    ### NOTE DOORS ###
    ##################
    
    def _note_doors_main(self):
        '''Removes the note doors for the setting FINAL NOTE DOOR'''
        if(self.grandmaster.final_note_door_var.get() == 1):
            for setup_file in self.gruntildas_lair._setup_list:
                for item_search_string in Sequences.note_door:
                    setup_file._locate_item_index(item_search_string, "Note_Door")
    
    #################
    ### SEQUENCE ###
    #################
    
    def _gather_sequence(self, sequence_list, sequence_type=None):
        '''Collects a sequence list per setup for the world'''
        self.curr_setup_file.sequence_index_list = []
        self.curr_setup_file.sequence_info_list = []
        for item_search_string in sequence_list:
            self.curr_setup_file._locate_sequence_index(item_search_string, sequence_type)
    
    def _shuffle_sequences_within_area(self):
        '''Shuffles the sequences found within the world'''
        self.sequence_info_list = []
        for sequence_info_list in self.curr_setup_file.sequence_info_list:
            self.sequence_info_list.append(sequence_info_list)
        self._shuffle_list(self.sequence_info_list)
    
    def _move_sequences(self):
        '''Places the randomized sequences list back into the world'''
        for list_index in range(len(self.curr_setup_file.sequence_index_list)):
            item_index = self.curr_setup_file.sequence_index_list[list_index]
            item_info = self.sequence_info_list[list_index]
            self.curr_setup_file._set_sequence(item_index, item_info)

    #######################
    ### CAMERA SEQUENCE ###
    #######################

    def _gather_camera_sequence(self, object_dict):
        '''Collects a sequence with cameras list per setup for the world'''
        self.curr_setup_file.sequence_index_list = []
        self.curr_setup_file.sequence_info_list = []
        for item_id in object_dict:
            object_search_string = object_dict[item_id]["Object"]
            camera_search_string = object_dict[item_id]["Camera"]
            self.curr_setup_file._locate_camera_sequence_index(object_search_string, camera_search_string)
    
    def _shuffle_camera_sequences_within_area(self):
        '''Shuffles the sequences with cameras found within the world'''
        self.sequence_info_list = []
        for sequence_info_list in self.curr_setup_file.sequence_info_list:
            self.sequence_info_list.append(sequence_info_list)
        self._shuffle_list(self.sequence_info_list)
    
    def _move_camera_sequences(self):
        '''Places the randomized sequences with cameras list back into the world'''
        for list_index in range(len(self.curr_setup_file.sequence_index_list)):
            obj_index = self.curr_setup_file.sequence_index_list[list_index][0]
            camera_index = self.curr_setup_file.sequence_index_list[list_index][1]
            obj_info = self.sequence_info_list[list_index][0]
            camera_info = self.sequence_info_list[list_index][1]
            self.curr_setup_file._set_camera_sequence(obj_index, obj_info, camera_index, camera_info)
    
    #######################
    ### SEQUENCE TUPLES ###
    #######################
    
    def _gather_sequence_tuple(self, sequence_list):
        '''Collects a sequence pair list per setup for the world'''
        self.curr_setup_file.sequence_index_list = []
        self.curr_setup_file.sequence_info_list = []
        for item_search_tuple in sequence_list:
            self.curr_setup_file._locate_sequence_tuple_index(item_search_tuple)
    
    def _center_x_z(self, sequence_list_index):
        '''Calculates the center x and center z coordinate of two objects'''
        # X
        flag1_x1 = leading_zeros(str(hex(self.curr_setup_file.sequence_info_list[sequence_list_index][0]["X_LOC1"]))[2:], 2)
        flag1_x2 = leading_zeros(str(hex(self.curr_setup_file.sequence_info_list[sequence_list_index][0]["X_LOC2"]))[2:], 2)
        flag1_x = possible_negative(int(flag1_x1 + flag1_x2, 16))
        flag2_x1 = leading_zeros(str(hex(self.curr_setup_file.sequence_info_list[sequence_list_index][1]["X_LOC1"]))[2:], 2)
        flag2_x2 = leading_zeros(str(hex(self.curr_setup_file.sequence_info_list[sequence_list_index][1]["X_LOC2"]))[2:], 2)
        flag2_x = possible_negative(int(flag2_x1 + flag2_x2, 16))
        center_x = fit_for_hex((flag1_x + flag2_x) // 2)
        center_hex_x = leading_zeros(str(hex(center_x))[2:], 4)
        center_hex_x1 = int(center_hex_x[:2], 16)
        center_hex_x2 = int(center_hex_x[2:], 16)
        # Z
        flag1_z1 = leading_zeros(str(hex(self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Z_LOC1"]))[2:], 2)
        flag1_z2 = leading_zeros(str(hex(self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Z_LOC2"]))[2:], 2)
        flag1_z = possible_negative(int(flag1_z1 + flag1_z2, 16))
        flag2_z1 = leading_zeros(str(hex(self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Z_LOC1"]))[2:], 2)
        flag2_z2 = leading_zeros(str(hex(self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Z_LOC2"]))[2:], 2)
        flag2_z = possible_negative(int(flag2_z1 + flag2_z2, 16))
        center_z = fit_for_hex((flag1_z + flag2_z) // 2)
        center_hex_z = leading_zeros(str(hex(center_z))[2:], 4)
        center_hex_z1 = int(center_hex_z[:2], 16)
        center_hex_z2 = int(center_hex_z[2:], 16)
        return (center_x, flag1_x, flag2_x, center_hex_x1, center_hex_x2, center_z, flag1_z, flag2_z, center_hex_z1, center_hex_z2)
    
    def _harder_boggy_race(self):
        '''Makes the Boggy race harder by making the flags move around'''
        self.sequence_info_list = []
        for sequence_info_list in self.curr_setup_file.sequence_info_list:
            self.sequence_info_list.append(sequence_info_list)
        shuffle_options = ["Tighter_Left", "Tighter_Right", "Higher", "Rotated"]
        for sequence_list_index in range(len(self.curr_setup_file.sequence_info_list)):
            random.seed(a=(self.seed + sequence_list_index))
            shuffle_option = random.choice(shuffle_options)
            if(shuffle_option == "Default"):
                continue
            elif(shuffle_option == "Tighter_Left"):
                (center_x, flag1_x, flag2_x, center_hex_x1, center_hex_x2, center_z, flag1_z, flag2_z, center_hex_z1, center_hex_z2) = self._center_x_z(sequence_list_index)
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["X_LOC1"] = center_hex_x1
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["X_LOC2"] = center_hex_x2
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Z_LOC1"] = center_hex_z1
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Z_LOC2"] = center_hex_z2
            elif(shuffle_option == "Tighter_Right"):
                (center_x, flag1_x, flag2_x, center_hex_x1, center_hex_x2, center_z, flag1_z, flag2_z, center_hex_z1, center_hex_z2) = self._center_x_z(sequence_list_index)
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["X_LOC1"] = center_hex_x1
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["X_LOC2"] = center_hex_x2
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Z_LOC1"] = center_hex_z1
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Z_LOC2"] = center_hex_z2
            elif(shuffle_option == "Rotated"):
                (center_x, flag1_x, flag2_x, center_hex_x1, center_hex_x2, center_z, flag1_z, flag2_z, center_hex_z1, center_hex_z2) = self._center_x_z(sequence_list_index)
                dist_from_center_x = abs(possible_negative(int(flag1_x)) - center_x)
                dist_from_center_z = abs(possible_negative(int(flag1_z)) - center_z)
                str_x1 = leading_zeros(str(hex(fit_for_hex(possible_negative(center_x) + dist_from_center_z)))[2:], 4)
                str_z1 = leading_zeros(str(hex(fit_for_hex(possible_negative(center_z) + dist_from_center_x)))[2:], 4)
                str_x2 = leading_zeros(str(hex(fit_for_hex(possible_negative(center_x) - dist_from_center_z)))[2:], 4)
                str_z2 = leading_zeros(str(hex(fit_for_hex(possible_negative(center_z) - dist_from_center_x)))[2:], 4)
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["X_LOC1"] = int(str_x1[:2], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["X_LOC2"] = int(str_x1[2:], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Z_LOC1"] = int(str_z1[:2], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Z_LOC2"] = int(str_z1[2:], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["X_LOC1"] = int(str_x2[:2], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["X_LOC2"] = int(str_x2[2:], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Z_LOC1"] = int(str_z2[:2], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Z_LOC2"] = int(str_z2[2:], 16)
            elif(shuffle_option == "Higher"):
                flag1_y1 = leading_zeros(str(hex(self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Y_LOC1"]))[2:], 2)
                flag1_y2 = leading_zeros(str(hex(self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Y_LOC2"]))[2:], 2)
                flag1_y = possible_negative(int(flag1_y1 + flag1_y2, 16))
                flag2_y1 = leading_zeros(str(hex(self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Y_LOC1"]))[2:], 2)
                flag2_y2 = leading_zeros(str(hex(self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Y_LOC2"]))[2:], 2)
                flag2_y = possible_negative(int(flag2_y1 + flag2_y2, 16))
                str_y1 = leading_zeros(str(hex(fit_for_hex(flag1_y - 200)))[2:], 4)
                str_y2 = leading_zeros(str(hex(fit_for_hex(flag2_y - 200)))[2:], 4)
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Y_LOC1"] = int(str_y1[:2], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Y_LOC2"] = int(str_y1[2:], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Y_LOC1"] = int(str_y2[:2], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Y_LOC2"] = int(str_y2[2:], 16)
            self.sequence_info_list.append((self.curr_setup_file.sequence_info_list[sequence_list_index][0], self.curr_setup_file.sequence_info_list[sequence_list_index][1]))
    
    def _move_sequence_tuple(self):
        '''Places the randomized sequences pairs list back into the world'''
        for list_index in range(len(self.curr_setup_file.sequence_index_list)):
            item_index1 = self.curr_setup_file.sequence_index_list[list_index][0]
            item_index2 = self.curr_setup_file.sequence_index_list[list_index][1]
            item_info1 = self.sequence_info_list[list_index][0]
            item_info2 = self.sequence_info_list[list_index][1]
            self.curr_setup_file._set_sequence_tuple(item_index1, item_info1, item_index2, item_info2)
            
    ######################
    ### SEQUENCE MAINS ###
    ######################
    
    def _shuffle_clanker_rings(self):
        '''Gathers, shuffles, and configures new Clanker ring order'''
        self.curr_setup_file = self.clankers_cavern._setup_list[1]
        self._gather_sequence(Sequences.clanker_rings_list, "Clanker_Rings")
        self._shuffle_sequences_within_area()
        self._move_sequences()

    def _shuffle_croctus(self):
        '''Gathers, shuffles, and configures new Croctus order'''
        self.curr_setup_file = self.bubblegloop_swamp._setup_list[0]
        self._gather_camera_sequence(Sequences.croctus_dict)
        self._shuffle_camera_sequences_within_area()
        self._move_camera_sequences()
    
    def _boggy_race_flags_main(self):
        '''Gathers, calculates new location, and configures new Clanker ring order'''
        self.curr_setup_file = self.freezeezy_peak._setup_list[0]
        self._gather_sequence_tuple(Sequences.boggy_race_flags)
        self._harder_boggy_race()
        self._move_sequence_tuple()
    
    def _shuffle_ancient_ones(self):
        '''Gathers, shuffles, and configures new Ancient Ones order'''
        self.curr_setup_file = self.gobis_valley._setup_list[0]
        self._gather_camera_sequence(Sequences.ancient_ones_dict)
        self._shuffle_camera_sequences_within_area()
        self._move_camera_sequences()
    
    def _shuffle_jinxy_heads(self):
        '''Gathers, shuffles, and configures new King Sandybutt Jinxy Heads order'''
        self.curr_setup_file = self.gobis_valley._setup_list[0]
        self._gather_camera_sequence(Sequences.jinxy_head_dict)
        self._shuffle_camera_sequences_within_area()
        self._move_camera_sequences()
    
    def _get_ccw_buttons(self):
        '''Gathers, shuffles, and configures new CCW Season order'''
        pass
    
    #############
    ### WARPS ###
    #############
    
    def _move_world_order_warps(self):
        '''PyDoc'''
        pass
    
    def _world_order_warps_main(self):
        '''Runs the world order warps options that are not NONE'''
        if((self.grandmaster.world_entrance_var == "Shuffle") and (self.grandmaster.move_bottles_locations_checkbutton)):
            self.world_order = World_Order_Bottles()
            self.world_order.world_order_dict
            self._move_world_order_warps()
            # self._move_bottles()
        elif(self.grandmaster.world_entrance_var == "Shuffle"):
            self.world_order = World_Order_Basic()
            self.world_order.world_order_dict
            self._move_world_order_warps()
    
    def _within_world_warps_main(self):
        '''Runs the within world warps options that are not NONE'''
        pass
    
    #####################
    ### MISCELLANEOUS ###
    #####################
    
    def _skip_furnace_fun(self):
        '''Takes a random entry point and turns it into a warp that leads to the next area'''
        for setup_file in self.gruntildas_lair._setup_list:
            if(setup_file.setup_name == "Furnace Fun"):
                object_search_string = "FFF900000A6F190C0001"
                replacement_dict = {
                    0: 0, # X1
                    1: 0, # X2
                    2: 0, # Y1
                    3: 0x10, # Y2
                    4: 0x8, # Z1
                    5: 0xFC, # Z2
                    6: 0x4B, # Radius
                    7: 0x6,
                    8: 0,
                    9: 0x77, # Warp ID
                    10: 0,
                    11: 0,
                    12: 0,
                    13: 0,
                    14: 0,
                    15: 0,
                    16: 0x6,
                    }
                setup_file._edit_object(object_search_string, replacement_dict)