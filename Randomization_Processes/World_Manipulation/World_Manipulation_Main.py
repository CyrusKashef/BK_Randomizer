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

from random import randint, seed, shuffle, choice
import json
import mmap
from math import ceil, floor

####################
### FILE IMPORTS ###
####################

from .Generic_World import World
from .Generic_Setup_File import SetupFile
from ..Dicts_And_Lists import Structs, Non_Flagged_Objects, Enemies, Flagged_Objects, Sequences, World_Order_Warps
from ..Dicts_And_Lists.Misc_Dicts_And_Lists import note_door_texture_offsets, note_door_indices
from ..Dicts_And_Lists.Flagged_Object_Flags import bottles_world_warp_dict, extra_flagged_object_flags
from Randomization_Processes.World_Manipulation.Warps.Basic_World_Order import World_Order_Basic
from Randomization_Processes.World_Manipulation.Warps.Bottles_World_Order import World_Order_Bottles
from ..Common_Functions import leading_zeros, possible_negative, fit_for_hex
from Randomization_Processes.Misc_Manipulation.Texture_Data.Texture_Main import Texture_Class
from ..Misc_Manipulation.Speech_Data.Speech_Main import Speech_Manipulation_Class
from .Level_Model_Manip.Level_Models import Level_Model_Class
from Randomization_Processes.World_Manipulation.Warps import Within_World_Warps

################################
### WORLD MANIPULATION CLASS ###
################################

class World_Manipulation_Class():
    '''The world manipulation class makes changes within the world maps'''
    def __init__(self, grandmaster, seed):
        '''Initializes the world manipulation class'''
        self.grandmaster = grandmaster
        self._file_dir = self.grandmaster.cwd
        self.seed = seed
        self.world_list = []
        self.world_order = None
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
        seed(a=(self.seed + address))
        shuffle(original_list)
    
    def _choose_from_list(self, original_list, address=0, increment=0):
        '''Selects an option from a list based on the current address and the number of increments, if applicable'''
        seed(a=(self.seed + address + increment))
        random_choice = choice(original_list)
        return random_choice
    
    def _choose_random_integer(self, int_start=0, int_end=1, address=0, increment=0):
        seed(a=(self.seed + address + increment))
        random_int = randint(int_start, int_end)
        return random_int
    
    def _create_worlds(self):
        '''Creates every world using the generic world and generic setup file classes, including individual seasons for click clock wood, if applicable'''
        # MUMBOS MOUNTAIN
        self.mumbos_mountain = World("Mumbo's Mountain")
        self.mumbos_mountain._add_setup_file(SetupFile("9788", self.grandmaster.cwd, "Main Area"))
        self.mumbos_mountain._add_setup_file(SetupFile("97D8", self.grandmaster.cwd, "Ticker's Tower"))
        self.mumbos_mountain._add_setup_file(SetupFile("97E8", self.grandmaster.cwd, "Mumbo's Skull"))
        self.world_list.append(self.mumbos_mountain)
        # TREASURE TROVE COVE
        self.treasure_trove_cove = World("Treasure Trove Cove")
        self.treasure_trove_cove._add_setup_file(SetupFile("97B0", self.grandmaster.cwd, "Main Area"))
        self.treasure_trove_cove._add_setup_file(SetupFile("97A0", self.grandmaster.cwd, "Blubber's Ship"))
        self.treasure_trove_cove._add_setup_file(SetupFile("97A8", self.grandmaster.cwd, "Nipper's Shell"))
        self.treasure_trove_cove._add_setup_file(SetupFile("97C8", self.grandmaster.cwd, "Sandcastle"))
        self.world_list.append(self.treasure_trove_cove)
        # CLANKER'S CAVERN
        self.clankers_cavern = World("Clanker's Cavern")
        self.clankers_cavern._add_setup_file(SetupFile("97D0", self.grandmaster.cwd, "Main Area"))
        self.clankers_cavern._add_setup_file(SetupFile("9888", self.grandmaster.cwd, "Inside Clanker Mouth And Belly"))
        self.clankers_cavern._add_setup_file(SetupFile("9880", self.grandmaster.cwd, "Inside Clanker Blowhole Entrance"))
        self.clankers_cavern._add_setup_file(SetupFile("9890", self.grandmaster.cwd, "Inside Clanker Gold Feather Room"))
        self.world_list.append(self.clankers_cavern)
        # BUBBLEGLOOP SWAMP
        self.bubblegloop_swamp = World("Bubblegloop Swamp")
        self.bubblegloop_swamp._add_setup_file(SetupFile("97E0", self.grandmaster.cwd, "Main Area"))
        self.bubblegloop_swamp._add_setup_file(SetupFile("97F8", self.grandmaster.cwd, "Mr Vile"))
        self.bubblegloop_swamp._add_setup_file(SetupFile("9800", self.grandmaster.cwd, "Tiptup Choir"))
        self.bubblegloop_swamp._add_setup_file(SetupFile("99B0", self.grandmaster.cwd, "Mumbo's Skull"))
        self.world_list.append(self.bubblegloop_swamp)
        # FREEZEEZY PEAK
        self.freezeezy_peak = World("Freezeezy Peak")
        self.freezeezy_peak._add_setup_file(SetupFile("98B0", self.grandmaster.cwd, "Main Area"))
        self.freezeezy_peak._add_setup_file(SetupFile("9980", self.grandmaster.cwd, "Boggy's Igloo"))
        self.freezeezy_peak._add_setup_file(SetupFile("99B8", self.grandmaster.cwd, "Mumbo's Skull"))
        self.freezeezy_peak._add_setup_file(SetupFile("9A10", self.grandmaster.cwd, "Inside The Tree"))
        self.freezeezy_peak._add_setup_file(SetupFile("9B70", self.grandmaster.cwd, "Wozza's Cave"))
        self.world_list.append(self.freezeezy_peak)
        # GOBI'S VALLEY
        self.gobis_valley = World("Gobi's Valley")
        self.gobis_valley._add_setup_file(SetupFile("9808", self.grandmaster.cwd, "Main Area"))
        self.gobis_valley._add_setup_file(SetupFile("9810", self.grandmaster.cwd, "Puzzle Room"))
        self.gobis_valley._add_setup_file(SetupFile("9818", self.grandmaster.cwd, "King Sandybutt's Tomb"))
        self.gobis_valley._add_setup_file(SetupFile("9820", self.grandmaster.cwd, "Water Room"))
        self.gobis_valley._add_setup_file(SetupFile("9828", self.grandmaster.cwd, "Rupee"))
        self.gobis_valley._add_setup_file(SetupFile("9848", self.grandmaster.cwd, "Jinxy"))
        self.world_list.append(self.gobis_valley)
        # MAD MONSTER MANSION
        self.mad_monster_mansion = World("Mad Monster Mansion")
        self.mad_monster_mansion._add_setup_file(SetupFile("9850", self.grandmaster.cwd, "Main Area"))
        self.mad_monster_mansion._add_setup_file(SetupFile("9BE0", self.grandmaster.cwd, "Septic Tank (Inside Loggo)"))
        self.mad_monster_mansion._add_setup_file(SetupFile("9858", self.grandmaster.cwd, "Church"))
        self.mad_monster_mansion._add_setup_file(SetupFile("9860", self.grandmaster.cwd, "Cellar"))
        self.mad_monster_mansion._add_setup_file(SetupFile("9898", self.grandmaster.cwd, "Tumblar's Shed"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98A0", self.grandmaster.cwd, "Well"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98A8", self.grandmaster.cwd, "Dining Room"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98B8", self.grandmaster.cwd, "Egg Room"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98C0", self.grandmaster.cwd, "Note Room"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98C8", self.grandmaster.cwd, "Red Feather Room"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98D0", self.grandmaster.cwd, "Secret Church Room"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98D8", self.grandmaster.cwd, "Bathroom"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98E0", self.grandmaster.cwd, "Bedroom"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98E8", self.grandmaster.cwd, "Gold Feather Room"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98F0", self.grandmaster.cwd, "Drain Pipe"))
        self.mad_monster_mansion._add_setup_file(SetupFile("98F8", self.grandmaster.cwd, "Mumbo's Skull"))
        self.world_list.append(self.mad_monster_mansion)
        # RUSTY BUCKET BAY
        self.rusty_bucket_bay = World("Rusty Bucket Bay")
        self.rusty_bucket_bay._add_setup_file(SetupFile("9900", self.grandmaster.cwd, "Main Area"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9BD0", self.grandmaster.cwd, "Anchor Room"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9918", self.grandmaster.cwd, "Engine Room"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9920", self.grandmaster.cwd, "Big Fish Warehouse"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9928", self.grandmaster.cwd, "Boat Room"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9930", self.grandmaster.cwd, "First Blue Container (Chompas)"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9938", self.grandmaster.cwd, "Third Blue Container (Mini Kabooms)"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9940", self.grandmaster.cwd, "Sea-Grublin's Cabin"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9948", self.grandmaster.cwd, "Kaboom's Room"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9950", self.grandmaster.cwd, "Mini Kaboom's Room (Pipe)"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9958", self.grandmaster.cwd, "Kitchen"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9960", self.grandmaster.cwd, "Navigation Room"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9968", self.grandmaster.cwd, "Second Blue Container (Sea Grublins)"))
        self.rusty_bucket_bay._add_setup_file(SetupFile("9970", self.grandmaster.cwd, "Captain's Room"))
        self.world_list.append(self.rusty_bucket_bay)
        # CLICK CLOCK WOOD - Seasons
        if(self.grandmaster.ccw_var.get() == "Season"):
            self.click_clock_wood_lobby = World("Click Clock Wood - Lobby")
            self.click_clock_wood_lobby._add_setup_file(SetupFile("9978", self.grandmaster.cwd, "Lobby"))
            self.world_list.append(self.click_clock_wood_lobby)
            self.click_clock_wood_spring = World("Click Clock Wood - Spring")
            self.click_clock_wood_spring._add_setup_file(SetupFile("9990", self.grandmaster.cwd, "Spring Main Area"))
            self.click_clock_wood_spring._add_setup_file(SetupFile("99C8", self.grandmaster.cwd, "Spring Mumbo's Skull"))
            self.click_clock_wood_spring._add_setup_file(SetupFile("9A50", self.grandmaster.cwd, "Spring Beehive"))
            self.click_clock_wood_spring._add_setup_file(SetupFile("9A68", self.grandmaster.cwd, "Spring Nabnut's House"))
            self.click_clock_wood_spring._add_setup_file(SetupFile("9AA0", self.grandmaster.cwd, "Spring Whipcrack Room"))
            self.world_list.append(self.click_clock_wood_spring)
            self.click_clock_wood_summer = World("Click Clock Wood - Summer")
            self.click_clock_wood_summer._add_setup_file(SetupFile("9998", self.grandmaster.cwd, "Summer Main Area"))
            self.click_clock_wood_summer._add_setup_file(SetupFile("99D0", self.grandmaster.cwd, "Summer Mumbo's Skull"))
            self.click_clock_wood_summer._add_setup_file(SetupFile("9A48", self.grandmaster.cwd, "Summer Beehive"))
            self.click_clock_wood_summer._add_setup_file(SetupFile("9A70", self.grandmaster.cwd, "Summer Nabnut's House"))
            self.click_clock_wood_summer._add_setup_file(SetupFile("9AA8", self.grandmaster.cwd, "Summer Whipcrack Room"))
            self.world_list.append(self.click_clock_wood_summer)
            self.click_clock_wood_fall = World("Click Clock Wood - Fall")
            self.click_clock_wood_fall._add_setup_file(SetupFile("99A0", self.grandmaster.cwd, "Fall Main Area"))
            self.click_clock_wood_fall._add_setup_file(SetupFile("99D8", self.grandmaster.cwd, "Fall Mumbo's Skull"))
            self.click_clock_wood_fall._add_setup_file(SetupFile("9A58", self.grandmaster.cwd, "Fall Beehive"))
            self.click_clock_wood_fall._add_setup_file(SetupFile("9A78", self.grandmaster.cwd, "Fall Nabnut's House"))
            self.click_clock_wood_fall._add_setup_file(SetupFile("9A90", self.grandmaster.cwd, "Fall Nabnut's Attic"))
            self.click_clock_wood_fall._add_setup_file(SetupFile("9AB0", self.grandmaster.cwd, "Fall Whipcrack Room"))
            self.world_list.append(self.click_clock_wood_fall)
            self.click_clock_wood_winter = World("Click Clock Wood - Winter")
            self.click_clock_wood_winter._add_setup_file(SetupFile("99A8", self.grandmaster.cwd, "Winter Main Area"))
            self.click_clock_wood_winter._add_setup_file(SetupFile("99E0", self.grandmaster.cwd, "Winter Mumbo's Skull"))
            self.click_clock_wood_winter._add_setup_file(SetupFile("9A80", self.grandmaster.cwd, "Winter Nabnut's House"))
            self.click_clock_wood_winter._add_setup_file(SetupFile("9A88", self.grandmaster.cwd, "Winter Nabnut's Attic 1 (Nuts)"))
            self.click_clock_wood_winter._add_setup_file(SetupFile("9A98", self.grandmaster.cwd, "Winter Nabnut's Attic 2 (Water)"))
            self.click_clock_wood_winter._add_setup_file(SetupFile("9AB8", self.grandmaster.cwd, "Winter Whipcrack Room"))
            self.world_list.append(self.click_clock_wood_winter)
        # CLICK CLOCK WOOD - All
        elif(self.grandmaster.ccw_var.get() == "Within World"):
            self.click_clock_wood = World("Click Clock Wood")
            self.click_clock_wood._add_setup_file(SetupFile("9978", self.grandmaster.cwd, "Lobby"))
            self.click_clock_wood._add_setup_file(SetupFile("9990", self.grandmaster.cwd, "Spring Main Area"))
            self.click_clock_wood._add_setup_file(SetupFile("99C8", self.grandmaster.cwd, "Spring Mumbo's Skull"))
            self.click_clock_wood._add_setup_file(SetupFile("9A50", self.grandmaster.cwd, "Spring Beehive"))
            self.click_clock_wood._add_setup_file(SetupFile("9A68", self.grandmaster.cwd, "Spring Nabnut's House"))
            self.click_clock_wood._add_setup_file(SetupFile("9AA0", self.grandmaster.cwd, "Spring Whipcrack Room"))
            self.click_clock_wood._add_setup_file(SetupFile("9998", self.grandmaster.cwd, "Summer Main Area"))
            self.click_clock_wood._add_setup_file(SetupFile("99D0", self.grandmaster.cwd, "Summer Mumbo's Skull"))
            self.click_clock_wood._add_setup_file(SetupFile("9A48", self.grandmaster.cwd, "Summer Beehive"))
            self.click_clock_wood._add_setup_file(SetupFile("9A70", self.grandmaster.cwd, "Summer Nabnut's House"))
            self.click_clock_wood._add_setup_file(SetupFile("9AA8", self.grandmaster.cwd, "Summer Whipcrack Room"))
            self.click_clock_wood._add_setup_file(SetupFile("99A0", self.grandmaster.cwd, "Fall Main Area"))
            self.click_clock_wood._add_setup_file(SetupFile("99D8", self.grandmaster.cwd, "Fall Mumbo's Skull"))
            self.click_clock_wood._add_setup_file(SetupFile("9A58", self.grandmaster.cwd, "Fall Beehive"))
            self.click_clock_wood._add_setup_file(SetupFile("9A78", self.grandmaster.cwd, "Fall Nabnut's House"))
            self.click_clock_wood._add_setup_file(SetupFile("9A90", self.grandmaster.cwd, "Fall Nabnut's Attic"))
            self.click_clock_wood._add_setup_file(SetupFile("9AB0", self.grandmaster.cwd, "Fall Whipcrack Room"))
            self.click_clock_wood._add_setup_file(SetupFile("99A8", self.grandmaster.cwd, "Winter Main Area"))
            self.click_clock_wood._add_setup_file(SetupFile("99E0", self.grandmaster.cwd, "Winter Mumbo's Skull"))
            self.click_clock_wood._add_setup_file(SetupFile("9A80", self.grandmaster.cwd, "Winter Nabnut's House"))
            self.click_clock_wood._add_setup_file(SetupFile("9A88", self.grandmaster.cwd, "Winter Nabnut's Attic 1 (Nuts)"))
            self.click_clock_wood._add_setup_file(SetupFile("9A98", self.grandmaster.cwd, "Winter Nabnut's Attic 2 (Water)"))
            self.click_clock_wood._add_setup_file(SetupFile("9AB8", self.grandmaster.cwd, "Winter Whipcrack Room"))
            self.world_list.append(self.click_clock_wood)
        # GRUNTILDA'S LAIR
        self.gruntildas_lair = World("Gruntilda's Lair")
        self.gruntildas_lair._add_setup_file(SetupFile("9AC0", self.grandmaster.cwd, "Floor 1 MM Puzzle And Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AC8", self.grandmaster.cwd, "Floor 2 TTC and CC Puzzles"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AD0", self.grandmaster.cwd, "Floor 3 CCW Puzzle"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B00", self.grandmaster.cwd, "Floor 4 Giant Gruntilda Statue"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AE8", self.grandmaster.cwd, "Floor 5 Giant Urn and GV Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AF0", self.grandmaster.cwd, "Floor 6 Grunty's Head and FP Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B40", self.grandmaster.cwd, "Floor 7 CCW Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9C10", self.grandmaster.cwd, "Floor 8 Gruntilda Puzzle And Dingpot"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AD8", self.grandmaster.cwd, "Floor 3 Pipe Room"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AE0", self.grandmaster.cwd, "TTC Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9AF8", self.grandmaster.cwd, "CC Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B08", self.grandmaster.cwd, "BGS Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B18", self.grandmaster.cwd, "GV Puzzle"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B20", self.grandmaster.cwd, "MMM Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B28", self.grandmaster.cwd, "Floor 6 Water Switch Area"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B30", self.grandmaster.cwd, "RBB Entrance"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B38", self.grandmaster.cwd, "MMM and RBB Puzzles"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B48", self.grandmaster.cwd, "Coffin Room"))
        self.gruntildas_lair._add_setup_file(SetupFile("9B78", self.grandmaster.cwd, "Path To Quiz Show"))
        self.gruntildas_lair._add_setup_file(SetupFile("9BE8", self.grandmaster.cwd, "Furnace Fun"))
        self.gruntildas_lair._add_setup_file(SetupFile("9BF8", self.grandmaster.cwd, "Gruntilda Boss Fight"))
        self.world_list.append(self.gruntildas_lair)
        # SPIRAL MOUNTAIN
        self.spiral_mountain = World("Spiral Mountain")
        self.spiral_mountain._add_setup_file(SetupFile("9780", self.grandmaster.cwd, "Main Area"))
        self.spiral_mountain._add_setup_file(SetupFile("9BD8", self.grandmaster.cwd, "Banjo's House"))
        self.world_list.append(self.spiral_mountain)
    
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
    
    def _shuffle_structs_within_game(self):
        '''Shuffles the structs found within the world'''
        for world_object in self.world_list[:-2]:
            for setup_file in world_object._setup_list:
                for struct_info_list in setup_file.struct_info_list:
                    self.struct_info_list.append(struct_info_list)
        self._shuffle_list(self.struct_info_list)
    
    def _randomize_structs(self):
        '''Randomizes the value of each struct found'''
        struct_count = 0
        for world_object in self.world_list[:-2]:
            for setup_file in world_object._setup_list:
                struct_count += len(setup_file.struct_info_list)
        struct_list = [
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
        note_info = {
            "Obj_ID1": 0x16,
            "Obj_ID2": 0x40,
            "Unknown1": 0x0,
            "Unknown2": 0xB4,
            "Size": 0x0,
            }
        if(self.grandmaster.struct_var.get() == "All Notes"):
            max_note_count = 2000
        else:
            max_note_count = 900
        scaled_note_count = min(int(int(self.grandmaster.final_puzzle_val) // 0.9), max_note_count)
        if(scaled_note_count < 10):
            scaled_note_count = 0
        else:
            scaled_note_count -= 10
        self.struct_info_list = [note_info] * scaled_note_count
        for struct_count in range(struct_count - scaled_note_count):
            struct_info = self._choose_from_list(struct_list, struct_count)
            self.struct_info_list.append(struct_info)
        self._shuffle_list(self.struct_info_list)
    
    def _oh_whoops_all_notes(self):
        '''Turns all found structs into notes'''
        struct_count = 0
        for world_object in self.world_list[:-2]:
            for setup_file in world_object._setup_list:
                struct_count += len(setup_file.struct_info_list)
        note_info = {
            "Obj_ID1": 0x16,
            "Obj_ID2": 0x40,
            "Unknown1": 0x0,
            "Unknown2": 0xB4,
            "Size": 0x0,
            }
        self.struct_info_list = [note_info] * struct_count
    
    def _move_structs_within_world(self, world_object):
        '''Places the randomized struct list back into the world'''
        list_index_start = 0
        for setup_file in world_object._setup_list:
            setup_file.note_count = 0
            for list_index in range(len(setup_file.struct_index_list)):
                setup_file._set_struct(setup_file.struct_index_list[list_index], self.struct_info_list[list_index_start + list_index])
                if((self.struct_info_list[list_index_start + list_index]["Obj_ID1"] == 0x16) and (self.struct_info_list[list_index_start + list_index]["Obj_ID2"] == 0x40)):
                    setup_file.note_count += 1
            list_index_start += len(setup_file.struct_index_list)
    
    def _move_structs_within_game(self):
        '''Places the randomized struct list back into the world'''
        list_index_start = 0
        for world_object in self.world_list[:-2]:
            for setup_file in world_object._setup_list:
                setup_file.note_count = 0
                for list_index in range(len(setup_file.struct_index_list)):
                    setup_file._set_struct(setup_file.struct_index_list[list_index], self.struct_info_list[list_index_start + list_index])
                    if((self.struct_info_list[list_index_start + list_index]["Obj_ID1"] == 0x16) and (self.struct_info_list[list_index_start + list_index]["Obj_ID2"] == 0x40)):
                        setup_file.note_count += 1
    #             print(f"Setup Name: {setup_file.setup_name}   Note Count: {setup_file.note_count}")
                list_index_start += len(setup_file.struct_index_list)

    def _structs_main(self):
        '''Runs the struct options that are not NONE'''
        if(self.grandmaster.struct_var.get() == "Shuffle (World)"):
            for world_object in self.world_list:
                self._gather_structs(world_object)
                self._shuffle_structs_within_world(world_object)
                self._move_structs_within_world(world_object)
                self.struct_info_list = []
        elif(self.grandmaster.struct_var.get() == "Shuffle (Game)"):
            for world_object in self.world_list[:-2]:
                self._gather_structs(world_object)
            self._shuffle_structs_within_game()
            self._move_structs_within_game()
            self.struct_info_list = []
            self._gather_structs(self.world_list[-1])
            self._shuffle_structs_within_world(self.world_list[-1])
            self._move_structs_within_world(self.world_list[-1])
            self.struct_info_list = []
        elif(self.grandmaster.struct_var.get() == "Randomize"):
            for world_object in self.world_list:
                self._gather_structs(world_object)
            self._randomize_structs()
            self._move_structs_within_game()
            self.struct_info_list = []
        elif(self.grandmaster.struct_var.get() == "All Notes"):
            for world_object in self.world_list:
                self._gather_structs(world_object)
            self._oh_whoops_all_notes()
            self._move_structs_within_game()
            self.struct_info_list = []
            self._lair_refills_main()
    
    ###########################
    ### NON FLAGGED OBJECTS ###
    ###########################
    
    def _gather_non_flag_objects(self, world_object):
        '''Collects the non-flagged objects per setup for the world'''
        for setup_file in world_object._setup_list:
            for item_search_string in Non_Flagged_Objects.obj_no_flag_id_dict:
                setup_file._locate_item_index(item_search_string, "No_Flagged_Object")
            if(self.grandmaster.non_flagged_object_abnormalities_var.get() == 1):
                for item_search_string in Non_Flagged_Objects.abnormal_obj_no_flag_id_dict:
                    setup_file._locate_item_index(item_search_string, "No_Flagged_Object")
    
    def _gather_specific_non_flagged_objects(self, world_object, dictionary):
        '''Collects the non-flagged objects listed in the given dictionary (Used for Lit Pots)'''
        for setup_file in world_object._setup_list:
            setup_file.non_flag_object_index_list = []
            setup_file.non_flag_object_info_list = []
            for item_search_string in dictionary:
                setup_file._locate_item_index(item_search_string, "No_Flagged_Object")
    
    def _shuffle_non_flag_objects_within_world(self, world_object):
        '''Shuffles the non-flagged objects found within the world'''
        for setup_file in world_object._setup_list:
            for non_flag_object_info_list in setup_file.non_flag_object_info_list:
                self.non_flag_object_info_list.append(non_flag_object_info_list)
        self._shuffle_list(self.non_flag_object_info_list, setup_file.setup_address)
    
    def _avoid_main_area_shuffle(self, world_object, main_area_count=0):
        '''It shuffles a particular item from the main area into subareas (Used for Lit Pots)'''
        for setup_file in world_object._setup_list:
            for non_flag_object_info_list in setup_file.non_flag_object_info_list:
                self.non_flag_object_info_list.append(non_flag_object_info_list)
        includes_main_area = self.non_flag_object_info_list[:-main_area_count]
        from_non_main_area = self.non_flag_object_info_list[-main_area_count:]
        self._shuffle_list(includes_main_area, setup_file.setup_address)
        self.non_flag_object_info_list = from_non_main_area + includes_main_area
    
    def _move_non_flag_objects_within_world(self, world_object):
        '''Places the randomized non-flagged objects list back into the world'''
        list_index_start = 0
        for setup_file in world_object._setup_list:
            setup_file.non_flagged_obj_dict = {}
            for list_index in range(len(setup_file.non_flag_object_index_list)):
                setup_file._set_object(setup_file.non_flag_object_index_list[list_index], self.non_flag_object_info_list[list_index_start + list_index])
                object_str = (leading_zeros(self.non_flag_object_info_list[list_index_start + list_index]["Script1"], 2) +
                              leading_zeros(self.non_flag_object_info_list[list_index_start + list_index]["Script2"], 2) +
                              leading_zeros(self.non_flag_object_info_list[list_index_start + list_index]["Obj_ID1"], 2) +
                              leading_zeros(self.non_flag_object_info_list[list_index_start + list_index]["Obj_ID2"], 2)).upper()
                if(object_str in Non_Flagged_Objects.obj_no_flag_id_dict):
                    object_name = Non_Flagged_Objects.obj_no_flag_id_dict[object_str]
                elif(object_str in Non_Flagged_Objects.abnormal_obj_no_flag_id_dict):
                    object_name = Non_Flagged_Objects.abnormal_obj_no_flag_id_dict[object_str]
                if(object_name not in setup_file.non_flagged_obj_dict):
                    setup_file.non_flagged_obj_dict[object_name] = 1
                else:
                    setup_file.non_flagged_obj_dict[object_name] += 1
            list_index_start += len(setup_file.non_flag_object_index_list)
    
    def _move_specific_non_flag_objects_within_world(self, world_object, dictionary):
        '''Places the randomized non-flagged objects list back into the world'''
        list_index_start = 0
        for setup_file in world_object._setup_list:
            setup_file.non_flagged_obj_dict = {}
            for list_index in range(len(setup_file.non_flag_object_index_list)):
                setup_file._set_object(setup_file.non_flag_object_index_list[list_index], self.non_flag_object_info_list[list_index_start + list_index])
                object_str = (leading_zeros(self.non_flag_object_info_list[list_index_start + list_index]["Script1"], 2) +
                              leading_zeros(self.non_flag_object_info_list[list_index_start + list_index]["Script2"], 2) +
                              leading_zeros(self.non_flag_object_info_list[list_index_start + list_index]["Obj_ID1"], 2) +
                              leading_zeros(self.non_flag_object_info_list[list_index_start + list_index]["Obj_ID2"], 2)).upper()
                if(object_str in dictionary):
                    object_name = dictionary[object_str]
                if(object_name not in setup_file.non_flagged_obj_dict):
                    setup_file.non_flagged_obj_dict[object_name] = 1
                else:
                    setup_file.non_flagged_obj_dict[object_name] += 1
            list_index_start += len(setup_file.non_flag_object_index_list)

    def _non_flag_objects_main(self):
        '''Runs the non-flagged objects options that are not NONE'''
        if(self.grandmaster.non_flagged_object_var.get() == "Shuffle (World)"):
            for world_object in self.world_list:
                self._gather_non_flag_objects(world_object)
                self._shuffle_non_flag_objects_within_world(world_object)
                self._move_non_flag_objects_within_world(world_object)
                self.non_flag_object_info_list = []
        if(self.grandmaster.lit_pots_var.get() == 1):
            self._gather_specific_non_flagged_objects(self.mad_monster_mansion, Non_Flagged_Objects.lit_pots)
            self._avoid_main_area_shuffle(self.mad_monster_mansion, main_area_count=5)
            self._move_specific_non_flag_objects_within_world(self.mad_monster_mansion, Non_Flagged_Objects.lit_pots)

    ###############
    ### ENEMIES ###
    ###############
    
    def _adjust_enemy_dicts(self):
        '''Filters the enemy dicts based on the selected enemies'''
        enemy_filter_list = []
        for enemy in self.grandmaster.enemy_checkbox_dict:
            if(self.grandmaster.enemy_checkbox_dict[enemy].get() == 0):
                for enemy_id in Enemies.master_enemy_dict[enemy]:
                    enemy_filter_list.append(enemy_id)
        return enemy_filter_list
    
    def _skip_enemies(self, item_search_string, enemy_option, world_name=None, setup_name=None):
        '''Does not randomize enemies that provide Jiggies or cause issues'''
        # Sir Slush
        if((item_search_string == "190C0124") and (world_name == "Freezeezy Peak")):
            return False
        # Yellow Flibbit
        elif((item_search_string == "190C0137") and (world_name == "Bubblegloop Swamp")):
            return False
        # Don't shuffle Yum-Yums or Lockups
        elif((enemy_option == "Shuffle") and (item_search_string in ["050C0153", "190C0152", "190C0069"])):
            return False
        # Mutie Snippet, Whipcrack, Wiplash, Lockup
        elif(item_search_string in ["190C00F5", "008C00F5", "008C030F", "190C028A", "050C0153", "190C0152"]):
            return False
        elif(setup_name == "Nipper's Shell"):
            return False
        return True
    
    def _gather_enemies(self, world_object, enemy_option):
        '''Collects the enemies per setup for the world'''
        for setup_file in world_object._setup_list:
            for item_search_string in Enemies.enemy_id_dict["Global"]["Ground"]:
                if(self._skip_enemies(item_search_string, enemy_option, world_object._world_name)):
                    setup_file._locate_item_index(item_search_string, "Ground_Enemy")
            for item_search_string in Enemies.additional_search_enemy_id_dict["Ground"]:
                if(self._skip_enemies(item_search_string, enemy_option, world_object._world_name)):
                    setup_file._locate_item_index(item_search_string, "Ground_Enemy")
            if("Ground" in Enemies.enemy_id_dict[world_object._world_name]):
                for item_search_string in Enemies.enemy_id_dict[world_object._world_name]["Ground"]:
                    if(self._skip_enemies(item_search_string, enemy_option, world_object._world_name)):
                        setup_file._locate_item_index(item_search_string, "Ground_Enemy")
            for item_search_string in Enemies.enemy_id_dict["Global"]["Wall"]:
                if(self._skip_enemies(item_search_string, enemy_option, world_object._world_name)):
                    setup_file._locate_item_index(item_search_string, "Wall_Enemy")
            for item_search_string in Enemies.additional_search_enemy_id_dict["Wall"]:
                if(self._skip_enemies(item_search_string, enemy_option, world_object._world_name)):
                    setup_file._locate_item_index(item_search_string, "Wall_Enemy")
            if("Wall" in Enemies.enemy_id_dict[world_object._world_name]):
                for item_search_string in Enemies.enemy_id_dict[world_object._world_name]["Wall"]:
                    if(self._skip_enemies(item_search_string, enemy_option, world_object._world_name)):
                        setup_file._locate_item_index(item_search_string, "Wall_Enemy")
            for item_search_string in Enemies.enemy_id_dict["Global"]["Flying"]:
                if(self._skip_enemies(item_search_string, enemy_option, world_object._world_name)):
                    setup_file._locate_item_index(item_search_string, "Flying_Enemy")
            for item_search_string in Enemies.additional_search_enemy_id_dict["Flying"]:
                if(self._skip_enemies(item_search_string, enemy_option, world_object._world_name)):
                    setup_file._locate_item_index(item_search_string, "Flying_Enemy")
            if("Flying" in Enemies.enemy_id_dict[world_object._world_name]):
                for item_search_string in Enemies.enemy_id_dict[world_object._world_name]["Flying"]:
                    if(self._skip_enemies(item_search_string, enemy_option, world_object._world_name)):
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
    
    def _randomize_enemies(self, world_object, enemy_filter_list):
        '''Randomizes the value of each enemies found'''
        ground_enemy_list = []
        for enemy_id in Enemies.enemy_id_dict["Global"]["Ground"]:
            ground_enemy_list.append(enemy_id)
        if("Ground" in Enemies.enemy_id_dict[world_object._world_name]):
            for enemy_id in Enemies.enemy_id_dict[world_object._world_name]["Ground"]:
                ground_enemy_list.append(enemy_id)
        for enemy_id in enemy_filter_list:
            ground_enemy_list = list(filter((enemy_id).__ne__, ground_enemy_list))
        if(not ground_enemy_list):
            ground_enemy_list = ["190C0268"]
        wall_enemy_list = []
        for enemy_id in Enemies.enemy_id_dict["Global"]["Wall"]:
            wall_enemy_list.append(enemy_id)
        if("Wall" in Enemies.enemy_id_dict[world_object._world_name]):
            for enemy_id in Enemies.enemy_id_dict[world_object._world_name]["Wall"]:
                wall_enemy_list.append(enemy_id)
        for enemy_id in enemy_filter_list:
            wall_enemy_list = list(filter((enemy_id).__ne__, wall_enemy_list))
        if(not wall_enemy_list):
            wall_enemy_list = ["190C0268"]
        flying_enemy_list = []
        for enemy_id in Enemies.enemy_id_dict["Global"]["Flying"]:
            flying_enemy_list.append(enemy_id)
        if("Flying" in Enemies.enemy_id_dict[world_object._world_name]):
            for enemy_id in Enemies.enemy_id_dict[world_object._world_name]["Flying"]:
                flying_enemy_list.append(enemy_id)
        for enemy_id in enemy_filter_list:
            flying_enemy_list = list(filter((enemy_id).__ne__, flying_enemy_list))
        if(not flying_enemy_list):
            flying_enemy_list = ["190C0268"]
        for setup_file in world_object._setup_list:
            for item_count in range(len(setup_file.ground_enemy_info_list)):
                reroll = True
                additional_increase = 0
                while(reroll):
                    new_enemy = self._choose_from_list(ground_enemy_list, setup_file.setup_address, increment=(item_count+additional_increase))
                    if((setup_file.setup_name == "Nipper's Shell") and (new_enemy == "190C0069")):
                        additional_increase += 69
                    else:
                        reroll = False
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
                self._gather_enemies(world_object, "Shuffle")
                self._shuffle_enemies_within_world(world_object)
                self._move_enemies_within_world(world_object)
                self.ground_enemy_info_list = []
                self.flying_enemy_info_list = []
                self.wall_enemy_info_list = []
        elif(self.grandmaster.enemies_var.get() == "Randomize"):
            enemy_filter_list = self._adjust_enemy_dicts()
            for world_object in self.world_list:
                self._gather_enemies(world_object, "Randomize")
                self._randomize_enemies(world_object, enemy_filter_list)
                self._move_enemies_within_world(world_object)
                self.ground_enemy_info_list = []
                self.flying_enemy_info_list = []
                self.wall_enemy_info_list = []
        if(self.grandmaster.buttons_var.get() == 1):
            replacement_dict = {
                4: 0xFB, 5: 0xC8,
                }
            self.rusty_bucket_bay._setup_list[0]._edit_object("079EFECAFBB2190C01CC", replacement_dict)
    
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
            if(self.grandmaster.flagged_object_abnormalities_var.get() == 1):
                for item_id in Flagged_Objects.abnormal_flagged_object_dict[world_object._world_name]:
                    object_search_string = Flagged_Objects.abnormal_flagged_object_dict[world_object._world_name][item_id]["Object"]
                    flag_search_string = Flagged_Objects.abnormal_flagged_object_dict[world_object._world_name][item_id]["Flag"]
                    setup_file._locate_flagged_object_index(object_search_string, flag_search_string)
            if(self.grandmaster.flagged_object_softlock_var.get() == 1):
                for item_id in Flagged_Objects.softlock_flagged_object_dict[world_object._world_name]:
                    object_search_string = Flagged_Objects.softlock_flagged_object_dict[world_object._world_name][item_id]["Object"]
                    flag_search_string = Flagged_Objects.softlock_flagged_object_dict[world_object._world_name][item_id]["Flag"]
                    setup_file._locate_flagged_object_index(object_search_string, flag_search_string)
    
    def _shuffle_flagged_objects_within_world(self, world_object):
        '''Shuffles the flagged objects found within the world'''
        for setup_file in world_object._setup_list:
            for flagged_object_info_list in setup_file.flagged_object_info_list:
                self.flagged_object_info_list.append(flagged_object_info_list)
        self._shuffle_list(self.flagged_object_info_list)
    
    def _shuffle_flagged_objects_within_game(self):
        '''Shuffles the flagged objects found within the game'''
        for world_object in self.world_list:
            for setup_file in world_object._setup_list:
                for flagged_object_info_list in setup_file.flagged_object_info_list:
                    self.flagged_object_info_list.append(flagged_object_info_list)
        self._shuffle_list(self.flagged_object_info_list)
    
    def _move_flagged_objects_within_world(self, world_object):
        '''Places the randomized flagged objects list back into the world'''
        list_index_start = 0
        for setup_file in world_object._setup_list:
            setup_file.flagged_obj_dict = {}
            setup_file.jiggy_count = 0
            setup_file.empty_honeycomb_count = 0
            for list_index in range(len(setup_file.flagged_object_index_list)):
                obj_index = setup_file.flagged_object_index_list[list_index][0]
                flag_index = setup_file.flagged_object_index_list[list_index][1]
                obj_info = self.flagged_object_info_list[list_index+list_index_start][0]
                flag_info = self.flagged_object_info_list[list_index+list_index_start][1]
                setup_file._set_flagged_object(obj_index, obj_info, flag_index, flag_info)
                object_name = Flagged_Objects.obj_flagged_id_dict[leading_zeros(self.flagged_object_info_list[list_index_start + list_index][0]["Obj_ID2"], 4).upper()]
                if(object_name == "Jiggy"):
                    obj_id = leading_zeros(flag_info['Obj_ID1'], 2) + leading_zeros(flag_info['Obj_ID2'], 2)
                    setup_file.flagged_obj_dict[f"Jiggy (ID {int(obj_id, 16)})"] = f"From {Flagged_Objects.cheat_sheet_dict[obj_id.upper()]}"
                    setup_file.jiggy_count += 1
                elif(object_name == "Empty Honeycomb"):
                    obj_id = leading_zeros(flag_info['Obj_ID1'], 2) + leading_zeros(flag_info['Obj_ID2'], 2)
                    setup_file.flagged_obj_dict[f"Empty Honeycomb (ID {int(obj_id, 16)})"] = f"From {Flagged_Objects.cheat_sheet_dict[obj_id.upper()]}"
                    setup_file.empty_honeycomb_count += 1
                else:
                    if(object_name not in setup_file.flagged_obj_dict):
                        setup_file.flagged_obj_dict[object_name] = 1
                    else:
                        setup_file.flagged_obj_dict[object_name] += 1
            list_index_start += len(setup_file.flagged_object_index_list)
    
    def _move_flagged_objects_within_game(self):
        '''Places the randomized flagged objects list back into the world'''
        list_index_start = 0
        for world_object in self.world_list:
            for setup_file in world_object._setup_list:
                setup_file.flagged_obj_dict = {}
                for list_index in range(len(setup_file.flagged_object_index_list)):
                    obj_index = setup_file.flagged_object_index_list[list_index][0]
                    flag_index = setup_file.flagged_object_index_list[list_index][1]
                    obj_info = self.flagged_object_info_list[list_index+list_index_start][0]
                    flag_info = self.flagged_object_info_list[list_index+list_index_start][1]
                    setup_file._set_flagged_object(obj_index, obj_info, flag_index, flag_info)
                    object_name = Flagged_Objects.obj_flagged_id_dict[leading_zeros(self.flagged_object_info_list[list_index_start + list_index][0]["Obj_ID2"], 4).upper()]
                    if(object_name == "Jiggy"):
                        obj_id = leading_zeros(flag_info['Obj_ID1'], 2) + leading_zeros(flag_info['Obj_ID2'], 2)
                        setup_file.flagged_obj_dict[f"Jiggy (ID {int(obj_id, 16)})"] = f"From {Flagged_Objects.cheat_sheet_dict[obj_id.upper()]}"
                        setup_file.jiggy_count += 1
                    elif(object_name == "Empty Honeycomb"):
                        obj_id = leading_zeros(flag_info['Obj_ID1'], 2) + leading_zeros(flag_info['Obj_ID2'], 2)
                        setup_file.flagged_obj_dict[f"Empty Honeycomb (ID {int(obj_id, 16)})"] = f"From {Flagged_Objects.cheat_sheet_dict[obj_id.upper()]}"
                        setup_file.empty_honeycomb_count += 1
                    else:
                        if(object_name not in setup_file.flagged_obj_dict):
                            setup_file.flagged_obj_dict[object_name] = 1
                        else:
                            setup_file.flagged_obj_dict[object_name] += 1
                list_index_start += len(setup_file.flagged_object_index_list)
    
    def _flagged_objects_main(self):
        '''Runs the flagged objects options that are not NONE'''
        if(self.grandmaster.flagged_object_var.get() == "Shuffle (World)"):
            for world_object in self.world_list:
                self._gather_flagged_objects(world_object)
                self._shuffle_flagged_objects_within_world(world_object)
                self._move_flagged_objects_within_world(world_object)
                self.flagged_object_info_list = []
        if(self.grandmaster.flagged_object_var.get() == "Shuffle (Game)"):
            for world_object in self.world_list:
                self._gather_flagged_objects(world_object)
            self._shuffle_flagged_objects_within_game()
            self._move_flagged_objects_within_game()
            self.flagged_object_info_list = []
    
    ###############
    ### REFILLS ###
    ###############
    
    def _lair_refills_main(self):
        '''Replaces normally 1-up locations with the egg and feather refills for the struct option ALL NOTES'''
        egg_replace_dict = { # EGG
            6: 0x19, 7: 0x0C,
            8: 0x01, 9: 0xD8,
            }
        red_feather_replace_dict = { # RED FEATHERS
            6: 0x19, 7: 0x0C,
            8: 0x01, 9: 0xD9,
            }
        gold_feather_replace_dict = { # GOLD FEATHERS
            6: 0x19, 7: 0x0C,
            8: 0x01, 9: 0xDA,
            }
        # CCW Puzzle Room
        self.gruntildas_lair._setup_list[2]._edit_object("0E0FFE220978", egg_replace_dict)
        # FP Entrance
        self.gruntildas_lair._setup_list[5]._edit_object("0B8A04DF0064", gold_feather_replace_dict)
        # CCW Entrance
        self.gruntildas_lair._setup_list[6]._edit_object("00000640F18C", red_feather_replace_dict)
        # BGS Entrance
        self.gruntildas_lair._setup_list[11]._edit_object("F838036EF414", red_feather_replace_dict)
        # MMM Entrance
        self.gruntildas_lair._setup_list[13]._edit_object("DE0FF90BF388", egg_replace_dict)
        # MMM & RBB Puzzles
        self.gruntildas_lair._setup_list[16]._edit_object("FCBA079E0343", gold_feather_replace_dict)
    
    ##################
    ### NOTE DOORS ###
    ##################
    
    ### FINAL NOTE DOOR ###
    
    def _remove_note_doors(self, note_door_list=Sequences.note_door):
        '''Removes the note doors for the setting FINAL NOTE DOOR'''
        for setup_file in self.gruntildas_lair._setup_list:
            for item_search_string in note_door_list:
                setup_file._locate_item_index(item_search_string, "Note_Door")
    
    def _810_bottles_cutscene(self):
        '''Places Bottles at the 810 Note Door because note doors don't open unless you see that cutscene'''
        self.curr_setup_file = self.gruntildas_lair._setup_list[7]
        # Bottles Molehill
        replacement_dict = {
            0: 0xFE, 1: 0xB6,
            2: 0x00, 3: 0x00,
            4: 0x02, 5: 0x76,
            6: 0x09, 7: 0x0C,
            8: 0x03, 9: 0x7A,
            10: 0x00, 11: 0x00,
            12: 0x48, 13: 0x00,
            14: 0x00, 15: 0x64,
            }
        self.curr_setup_file._edit_object("FFCB0085044D5788", replacement_dict)
        # Camera Release
        replacement_dict = {
            0: 0xFF, 1: 0xBF,
            2: 0x00, 3: 0x82,
            4: 0x02, 5: 0x8A,
            6: 0x64, 7: 0x88,
            8: 0x00, 9: 0x2A,
            10: 0x00, 11: 0x00,
            12: 0x00, 13: 0x00,
            14: 0x00, 15: 0x00,
            }
        self.curr_setup_file._edit_object("FF88008504765788", replacement_dict)
        # Change Cameras
        replacement_dict = {
            2: 0x0E,
            }
        self.curr_setup_file._edit_object("01000B0202", replacement_dict)
        replacement_dict = {
            2: 0x0B,
            }
        self.curr_setup_file._edit_object("01000E0203", replacement_dict)

    def _click_clock_wood_item_count(self, world_object_list):
        '''Counts the number of items for CCW specifically'''
        note_count = 0
        for world_object in world_object_list:
            for setup_file in world_object._setup_list:
                note_count += setup_file.note_count
        return note_count

    def _note_count(self, world_object):
        '''Checks the note counts per world'''
        if(isinstance(world_object, list)):
            return self._click_clock_wood_item_count(world_object)
        note_count = 0
        for setup_file in world_object._setup_list:
            note_count += setup_file.note_count
        if(world_object._world_name in ["Mumbo's Mountain", "Bubblegloop Swamp"]):
            note_count += 5
        return note_count
    
    ### SCALING NOTE DOOR ###
    
    def _scale_note_doors(self, final_note_door_value):
        '''Scales the note doors based on world order and how many notes are in each world'''
        if(not self.world_order):
            world_order_list = ["Mumbo's Mountain", "Treasure Trove Cove", "Clanker's Cavern",
                                "Bubblegloop Swamp", "Freezeezy Peak", "Gobi's Valley",
                                "Mad Monster Mansion", "Rusty Bucket Bay", "Click Clock Wood"]
        else:
            world_order_list = self.world_order.world_order_list
        world_order_note_count = [0] * 9
        for world_object in self.world_list[-2:]:
            note_count = self._note_count(world_object)
            if(world_object._world_name.startswith("Click Clock Wood")):
                world_order_note_count[self.world_order.index("Click Clock Wood")] += note_count
            elif(world_object._world_name in world_order_list):
                world_order_note_count[self.world_order.index(world_object._world_name)] += note_count
        note_door_scaling = [50/810, 180/810, 260/810, 350/810, 450/810, 640/810, 765/810, 1, 0, 0, 0, 0]
        note_door_list = []
        for scaling in note_door_scaling:
            note_door_list.append(round(scaling * final_note_door_value))
        return note_door_list
    
    def _set_note_door_values(self, note_door_list):
        '''Sets the requirements of every note door to zero except for the note door proceeding the final battle'''
        # Find location of note doors
        # 00 32 00 B4 01 04 01 5E 01 C2 02 80 02 FD 03 2A 03 3C 03 4E 03 60 03 72
        # Every 2 are a note door
        # Edit each note door with zeros
        note_door_texture_obj = Texture_Class(self._file_dir, "8320", seed_val=self.seed)
        with open(f"{self._file_dir}Randomized_ROM/FCF698-Decompressed.bin", "r+b") as decomp_file:
            mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
            #                                                      0 1 2 3 4 5 6 7 8 91011121314151617181920212223
            note_door_index_start = mm_decomp.find(bytes.fromhex("003200B40104015E01C2028002FD032A033C034E03600372"))
            len_note_door_list = len(note_door_list)
            for note_index in range(len_note_door_list):
                hundreths = tenths = ones = None
                # New Note Door Value
                use_this_value = note_door_list[note_index]
                increment = 0
                if(note_index < 7):
                    has_nine = True
                    while(has_nine):
                        if("9" in str(use_this_value)):
                            if(note_index > 0):
                                seed(a=(self.seed + increment))
                                increment += 1
                                use_this_value = randint(note_door_list[note_index - 1], use_this_value)
                            else:
                                use_this_value -= 1
                        else:
                            has_nine = False
                    note_door_list[note_index] = use_this_value
                mm_decomp[note_door_index_start + (note_index * 2)] = int(leading_zeros(use_this_value, 4)[:2], 16)
                mm_decomp[note_door_index_start + (note_index * 2) + 1] = int(leading_zeros(use_this_value, 4)[2:], 16)
                if(note_index < 8):
                    if(use_this_value > 999):
                        hundreths = tenths = ones = 0
                    elif((note_index == 0) and (use_this_value > 99)):
                        hundreths = tenths = ones = 0
                    if(note_index > 0):
                        if(not hundreths):
                            hundreths = (use_this_value // 100) % 10
                        note_door_texture_obj.mm[note_door_indices[note_index][100]["Overlay_Textures"]] = int(note_door_texture_offsets[hundreths][:2], 16)
                        note_door_texture_obj.mm[note_door_indices[note_index][100]["Overlay_Textures"] + 1] = int(note_door_texture_offsets[hundreths][2:], 16)
                        if(hundreths == 9):
                            note_door_texture_obj._flip_texture(note_door_indices[note_index][100]["Door_Vertices"], x_axis=True, y_axis=True)
                    if(not tenths):
                        tenths = (use_this_value // 10) % 10
                    note_door_texture_obj.mm[note_door_indices[note_index][10]["Overlay_Textures"]] = int(note_door_texture_offsets[tenths][:2], 16)
                    note_door_texture_obj.mm[note_door_indices[note_index][10]["Overlay_Textures"] + 1] = int(note_door_texture_offsets[tenths][2:], 16)
                    if(tenths == 9):
                        note_door_texture_obj._flip_texture(note_door_indices[note_index][10]["Door_Vertices"], x_axis=True, y_axis=True)
                    if(not ones):
                        ones = use_this_value % 10
                    note_door_texture_obj.mm[note_door_indices[note_index][1]["Overlay_Textures"]] = int(note_door_texture_offsets[ones][:2], 16)
                    note_door_texture_obj.mm[note_door_indices[note_index][1]["Overlay_Textures"] + 1] = int(note_door_texture_offsets[ones][2:], 16)
                    if(ones == 9):
                        note_door_texture_obj._flip_texture(note_door_indices[note_index][1]["Door_Vertices"], x_axis=True, y_axis=True)
        self._remove_note_doors(note_door_list=Sequences.note_door[-4:])
    
    def _note_doors_main(self, final_note_door_value):
        '''Either scales or removes Note Doors'''
        if(self.grandmaster.final_note_door_var.get() == "Final Note Door Only"):
            self._remove_note_doors()
            self._810_bottles_cutscene()
            note_door_list = [0, 0, 0, 0, 0, 0, 0, int(self.grandmaster.final_note_door_val), 0, 0, 0, 0]
        elif(self.grandmaster.final_note_door_var.get() == "Scaling Note Doors"):
            note_door_list = self._scale_note_doors(final_note_door_value)
        else:
            note_door_list = [50, 180, 260, 350, 450, 640, 765, 810, 828, 846, 864, 882]
        self._set_note_door_values(note_door_list)
    
    ####################
    ### WORLD PUZZLE ###
    #################### 
    
    ### FINAL WORLD PUZZLE ###
    
    def _final_world_puzzle(self, final_puzzle_value):
        '''Sets the requirements of every puzzle to zero except for the puzzle proceeding the final battle'''
        # Find location of world puzzles
        # 00 00 01 01 00 5D 02 02 00 5E 05 03 00 60 07 03 00 63 08 04 00 66 09 04 00 6A 0A 04 00 6E 0C 04 00 72 0F 04 00 76 19 05 00 7A 04 03
        # Every 4 is a note door, with the third value being the one you have to change
        with open(f"{self._file_dir}Randomized_ROM\\FCF698-Decompressed.bin", "r+b") as decomp_file:
            mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
            #                                                      0 1 2 3 4 5 6 7 8 910111213141516171819202122232425262728293031323334353637383940414243
            note_door_index_start = mm_decomp.find(bytes.fromhex("00000101005D0202005E0503006007030063080400660904006A0A04006E0C0400720F0400761905007A0403"))
            for offset in range(0, 37, 4):
                mm_decomp[note_door_index_start + offset + 2] = 0
            mm_decomp[note_door_index_start + 38] = final_puzzle_value
            honeycomb_puzzle_count = 100 - final_puzzle_value
            if(honeycomb_puzzle_count > 4):
                honeycomb_puzzle_count = 4
            mm_decomp[note_door_index_start + 42] = honeycomb_puzzle_count
    
    ######################
    ### MAGIC BARRIERS ###
    ######################
    
    def _magic_barrier_main(self):
        '''Removes the note doors for the setting FINAL NOTE DOOR'''
        for setup_file in self.gruntildas_lair._setup_list:
            for item_search_string in Non_Flagged_Objects.magic_barriers:
                setup_file._locate_item_index(item_search_string, "Magic_Barrier")
        if(self.grandmaster.ccw_var.get() == "Season"):
            for world_object in [self.click_clock_wood_lobby, self.click_clock_wood_spring, self.click_clock_wood_summer, self.click_clock_wood_fall, self.click_clock_wood_winter]:
                for setup_file in world_object._setup_list:
                    for item_search_string in Non_Flagged_Objects.magic_barriers:
                        setup_file._locate_item_index(item_search_string, "Magic_Barrier")
        elif(self.grandmaster.ccw_var.get() == "Within World"):
            for setup_file in self.click_clock_wood._setup_list:
                for item_search_string in Non_Flagged_Objects.magic_barriers:
                    setup_file._locate_item_index(item_search_string, "Magic_Barrier")
    
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
        flag1_x1 = leading_zeros(self.curr_setup_file.sequence_info_list[sequence_list_index][0]["X_LOC1"], 2)
        flag1_x2 = leading_zeros(self.curr_setup_file.sequence_info_list[sequence_list_index][0]["X_LOC2"], 2)
        flag1_x = possible_negative(int(flag1_x1 + flag1_x2, 16))
        flag2_x1 = leading_zeros(self.curr_setup_file.sequence_info_list[sequence_list_index][1]["X_LOC1"], 2)
        flag2_x2 = leading_zeros(self.curr_setup_file.sequence_info_list[sequence_list_index][1]["X_LOC2"], 2)
        flag2_x = possible_negative(int(flag2_x1 + flag2_x2, 16))
        center_x = fit_for_hex((flag1_x + flag2_x) // 2)
        center_hex_x = leading_zeros(center_x, 4)
        center_hex_x1 = int(center_hex_x[:2], 16)
        center_hex_x2 = int(center_hex_x[2:], 16)
        # Z
        flag1_z1 = leading_zeros(self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Z_LOC1"], 2)
        flag1_z2 = leading_zeros(self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Z_LOC2"], 2)
        flag1_z = possible_negative(int(flag1_z1 + flag1_z2, 16))
        flag2_z1 = leading_zeros(self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Z_LOC1"], 2)
        flag2_z2 = leading_zeros(self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Z_LOC2"], 2)
        flag2_z = possible_negative(int(flag2_z1 + flag2_z2, 16))
        center_z = fit_for_hex((flag1_z + flag2_z) // 2)
        center_hex_z = leading_zeros(center_z, 4)
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
            shuffle_option = self._choose_from_list(shuffle_options, increment=sequence_list_index)
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
                str_x1 = leading_zeros(fit_for_hex(possible_negative(center_x) + dist_from_center_z), 4)
                str_z1 = leading_zeros(fit_for_hex(possible_negative(center_z) + dist_from_center_x), 4)
                str_x2 = leading_zeros(fit_for_hex(possible_negative(center_x) - dist_from_center_z), 4)
                str_z2 = leading_zeros(fit_for_hex(possible_negative(center_z) - dist_from_center_x), 4)
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["X_LOC1"] = int(str_x1[:2], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["X_LOC2"] = int(str_x1[2:], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Z_LOC1"] = int(str_z1[:2], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Z_LOC2"] = int(str_z1[2:], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["X_LOC1"] = int(str_x2[:2], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["X_LOC2"] = int(str_x2[2:], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Z_LOC1"] = int(str_z2[:2], 16)
                self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Z_LOC2"] = int(str_z2[2:], 16)
            elif(shuffle_option == "Higher"):
                flag1_y1 = leading_zeros(self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Y_LOC1"], 2)
                flag1_y2 = leading_zeros(self.curr_setup_file.sequence_info_list[sequence_list_index][0]["Y_LOC2"], 2)
                flag1_y = possible_negative(int(flag1_y1 + flag1_y2, 16))
                flag2_y1 = leading_zeros(self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Y_LOC1"], 2)
                flag2_y2 = leading_zeros(self.curr_setup_file.sequence_info_list[sequence_list_index][1]["Y_LOC2"], 2)
                flag2_y = possible_negative(int(flag2_y1 + flag2_y2, 16))
                str_y1 = leading_zeros(fit_for_hex(flag1_y - 200), 4)
                str_y2 = leading_zeros(fit_for_hex(flag2_y - 200), 4)
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

    def _shuffle_ttc_x(self):
        '''Gathers, shuffles, and configures new Croctus order'''
        self.curr_setup_file = self.treasure_trove_cove._setup_list[0]
        self._gather_sequence(Sequences.ttc_x_list, "TTC_X")
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
    
    #########################
    ### WORLD ORDER WARPS ###
    #########################
    
    ### COMMON WORLD ORDER FUNCTIONS ###
    def _gather_all_world_warps(self):
        '''Locates the index and info of all world warps'''
        gruntildas_lair_warp_setups = [0, 9, 10, 11, 5, 4, 13, 15, 6]
        world_order_count = 1
        for setup_num in gruntildas_lair_warp_setups:
            (self.gruntildas_lair._setup_list[setup_num]).warp_index_list = []
            (self.gruntildas_lair._setup_list[setup_num]).warp_info_list = []
            for warp in World_Order_Warps.world_order_warps_dict[str(world_order_count)]:
                (self.gruntildas_lair._setup_list[setup_num])._locate_item_index(warp, "Warp")
            world_order_count += 1
    
    def _move_world_order(self, shuffle_type="Simple"):
        '''Sets the world order'''
        world_order_nums = {
            "Mumbo's Mountain": "1",
            "Treasure Trove Cove": "2",
            "Clanker's Cavern": "3",
            "Bubblegloop Swamp": "4",
            "Freezeezy Peak": "5",
            "Gobi's Valley": "6",
            "Mad Monster Mansion": "7",
            "Rusty Bucket Bay": "8",
            "Click Clock Wood": "9"
        }
        gruntildas_lair_warp_setups = [0, 9, 10, 11, 5, 4, 13, 15, 6]
        if(shuffle_type == "Simple"):
            world_order_nums.pop("Mumbo's Mountain")
            gruntildas_lair_warp_setups.pop(0)
        curr_world_num = 0
        for setup_num in gruntildas_lair_warp_setups:
            self.curr_setup_file = self.gruntildas_lair._setup_list[setup_num]
            new_warp = World_Order_Warps.world_order_warps_dict[world_order_nums[self.world_order.world_order_list[curr_world_num]]][0]
            edit_dict = {
                8: int(new_warp[16:18], 16),
                9: int(new_warp[18:], 16),
            }
            for warp_index in self.curr_setup_file.warp_index_list:
                self.curr_setup_file._edit_object_index(warp_index, edit_dict)
            curr_world_num += 1
    
    def _gather_all_bottles_mounds(self):
        '''Gathers the bottles mound info and index'''
        for world_object in self.world_list:
            for setup_file in world_object._setup_list:
                setup_file.bottles_index_list = []
                setup_file.bottles_info_list = []
                for bottles_mound in World_Order_Warps.learnable_moves_dict:
                    setup_file._locate_item_index(World_Order_Warps.learnable_moves_dict[bottles_mound], "Bottles_Mound")
    
    def _new_move_camera(self, setup_file, new_move):
        '''Adjusts cameras in an area with a potential new move'''
        primary_camera = World_Order_Warps.bottles_moves_camera_dict[new_move]["Primary_Camera"]
        secondary_camera = World_Order_Warps.bottles_moves_camera_dict[new_move]["Secondary_Camera"]
        if(not setup_file._does_string_exist(primary_camera)):
            edit_dict = {
                2: int(primary_camera[4:6], 16),
                }
            setup_file._edit_object("01000102", edit_dict)
            replacement_dict = {
                2: int(primary_camera[4:6], 16),
                }
            setup_file._replace_all_in_area("1200010000000000", replacement_dict)
            setup_file._replace_all_in_area("9200010000000000", replacement_dict)
        if(secondary_camera and (not setup_file._does_string_exist(secondary_camera))):
            edit_dict = {
                2: int(secondary_camera[4:6], 16),
                }
            setup_file._edit_object("01000002", edit_dict)
            replacement_dict = {
                2: int(primary_camera[4:6], 16),
                }
            setup_file._replace_all_in_area("1200000000000000", replacement_dict)
            setup_file._replace_all_in_area("9200000000000000", replacement_dict)
    
    def _add_clankers_cavern_jump_pad(self):
        '''Adds a Shock Jump Pad to the inside of Clanker in order to make the logic easier and help prevent backtracking'''
        edit_dict ={
            0: 255, # FF
            1: 246, # F6
            2: 4, # 04
            3: 76, # 4C
            4: 244, # F4
            5: 224, # E0
            6: 25,
            7: 12,
            8: 0,
            9: 11,
            }
        (self.clankers_cavern._setup_list[1])._edit_object("FF1F07EDF8FD190C0354", edit_dict)
    
    def _world_entrance_signs(self, shuffle_type="Simple"):
        '''Edits the world entrance signs based on world order'''
        # 0x89B0 - 4306E0
        world_texture_dict = {
            "Mumbo's Mountain": 0,
            "Treasure Trove Cove": 2,
            "Clanker's Cavern": 4,
            "Bubblegloop Swamp": 6,
            "Freezeezy Peak": 8,
            "Gobi's Valley": 10,
            "Mad Monster Mansion": 12,
            "Rusty Bucket Bay": 14,
            "Click Clock Wood": 16,
            }
        if(shuffle_type == "Simple"):
            self.world_order.world_order_list.insert(0, "Mumbo's Mountain")
        new_order_dict = {}
        for curr_index in range(len(world_texture_dict)):
            new_order_dict[curr_index * 2] = world_texture_dict[self.world_order.world_order_list[curr_index]]
            new_order_dict[curr_index * 2 + 1] = world_texture_dict[self.world_order.world_order_list[curr_index]] + 1
        texture_obj = Texture_Class(self.grandmaster.cwd, "89B0")
        texture_obj._extract_header_info()
        texture_obj._extract_texture_setup_info()  
        texture_obj._rearrange_textures(new_order_dict)
    
    def _brentilda_world_order_hints(self, shuffle_type="Simple"):
        '''Adjusts Brentilda's hints to give hints for the randomizer'''
        world_object_list = []
        if(shuffle_type == "Simple"):
            world_object_list.append(self.mumbos_mountain)
        for world_name in self.world_order.world_order_list:
            if(world_name == "Click Clock Wood"):
                if(self.grandmaster.ccw_var.get() == "Season"):
                    world_object_list.append([self.click_clock_wood_lobby,
                                              self.click_clock_wood_spring, self.click_clock_wood_summer,
                                              self.click_clock_wood_fall, self.click_clock_wood_winter])
                elif(self.grandmaster.ccw_var.get() == "Within World"):
                    world_object_list.append(self.click_clock_wood)
            else:
                for world_object in self.world_list:
                    if(world_object._world_name == world_name):
                        world_object_list.append(world_object)
                        break
        speech_manip = Speech_Manipulation_Class(self.grandmaster, self.seed)
        speech_manip._brentilda_intro()
        speech_manip._brentilda_1_1(world_object_list[0])
        speech_manip._brentilda_1_2(world_object_list[0])
        speech_manip._brentilda_1_3(world_object_list[0])
        speech_manip._brentilda_2_1(world_object_list[1])
        speech_manip._brentilda_2_2(world_object_list[1])
        speech_manip._brentilda_2_3(world_object_list[1])
        speech_manip._brentilda_3_1(world_object_list[2])
        speech_manip._brentilda_3_2(world_object_list[2])
        speech_manip._brentilda_3_3(world_object_list[2])
        speech_manip._brentilda_4_1(world_object_list[3])
        speech_manip._brentilda_4_2(world_object_list[3])
        speech_manip._brentilda_4_3(world_object_list[3])
        speech_manip._brentilda_5_1(world_object_list[4])
        speech_manip._brentilda_5_2(world_object_list[4])
        speech_manip._brentilda_5_3(world_object_list[4])
        speech_manip._brentilda_6_1(world_object_list[5])
        speech_manip._brentilda_6_2(world_object_list[5])
        speech_manip._brentilda_6_3(world_object_list[5])
        speech_manip._brentilda_7_1(world_object_list[6])
        speech_manip._brentilda_7_2(world_object_list[6])
        speech_manip._brentilda_7_3(world_object_list[6])
        speech_manip._brentilda_8_1(world_object_list[7])
        speech_manip._brentilda_8_2(world_object_list[7])
        speech_manip._brentilda_8_3(world_object_list[7])
        speech_manip._brentilda_9_1(world_object_list[8])
        speech_manip._brentilda_9_2(world_object_list[8])
        speech_manip._brentilda_9_3(world_object_list[8])
        speech_manip._brentilda_10_1(self.gruntildas_lair)
        speech_manip._brentilda_10_2(self.spiral_mountain)
        speech_manip._brentilda_10_3()
    
    ### BASIC SHUFFLE ###
    def _basic_calculate_new_world_order(self):
        '''Simple world order calculation'''
        self.world_order = World_Order_Basic(self.seed)
        self.world_order._world_order_main()
    
    def _basic_edit_bottles_mound(self):
        '''Edits bottles mounds for basic shuffle'''
        bottles_info_list = []
        for world_object in self.world_list:
            for setup_file in world_object._setup_list:
                for bottles_info in setup_file.bottles_info_list:
                    bottles_info_list.append(bottles_info)
        progression_moves = [
            {'Script1': 6, 'Script2': 12, 'Obj_ID1': 3, 'Obj_ID2': 122}, # Talon Trot
            {'Script1': 5, 'Script2': 140, 'Obj_ID1': 3, 'Obj_ID2': 122}, # Beak Buster
            {'Script1': 6, 'Script2': 140, 'Obj_ID1': 3, 'Obj_ID2': 122} # Shock Jump Pad
            ]
        increment = 0
        self.curr_setup_file = self.mumbos_mountain._setup_list[0]
        for bottles_index in self.curr_setup_file.bottles_index_list:
            chosen_move = self._choose_from_list(progression_moves, increment=increment)
            increment += 1
            replacement_dict = {
                0: chosen_move['Script1'],
                1: chosen_move['Script2'],
                2: chosen_move['Obj_ID1'],
                3: chosen_move['Obj_ID2'],
                }
            self.curr_setup_file._edit_object_index(bottles_index, replacement_dict)
            bottles_info_list.remove(chosen_move)
            progression_moves.remove(chosen_move)
        self._shuffle_list(bottles_info_list)
        for world_object in self.world_list[1:]:
            for setup_file in world_object._setup_list:
                for bottles_index in setup_file.bottles_index_list:
                    chosen_move = bottles_info_list[0]
                    replacement_dict = {
                        0: chosen_move['Script1'],
                        1: chosen_move['Script2'],
                        2: chosen_move['Obj_ID1'],
                        3: chosen_move['Obj_ID2'],
                        }
                    setup_file._edit_object_index(bottles_index, replacement_dict)
                    bottles_info_list.remove(chosen_move)
                    new_move = (leading_zeros(chosen_move['Script1'], 2) + 
                                leading_zeros(chosen_move['Script2'], 2) + 
                                leading_zeros(chosen_move['Obj_ID1'], 2) + 
                                leading_zeros(chosen_move['Obj_ID2'], 2)).upper()
                    self._new_move_camera(setup_file, new_move)
                    
    
    def _basic_world_order_shuffle_main(self):
        '''Runs the basic world order shuffle functions'''
        self._basic_calculate_new_world_order()
        self._move_world_order(shuffle_type="Simple")
        self._basic_edit_bottles_mound()
    
    ### BOTTLES SHUFFLE ###
    def _bottles_to_1_ups(self):
        '''Turns all Bottles mounds to 1-Ups to have them shuffle with non-flagged objects'''
        for world_object in self.world_list:
            for setup_file in world_object._setup_list:
                for bottles_mound in World_Order_Warps.learnable_moves_dict:
                    replacement_dict = {
                        0: 0x19, 1: 0x0C,
                        2: 0x0, 3: 0x49,
                        }
                    setup_file._edit_object(World_Order_Warps.learnable_moves_dict[bottles_mound], replacement_dict)
    
    def _determine_available_move_slots(self):
        '''Compares 1-Up locations to allowed potential bottles locations'''
        for world_object in self.world_list[:-2]:
            if((world_object._world_name).startswith("Click Clock Wood")):
                current_world_name = "Click Clock Wood"
            else:
                current_world_name = world_object._world_name
            available_bottles = []
            for setup_file in world_object._setup_list:
                for item_name in World_Order_Warps.possible_bottles_locations[current_world_name]:
                    if(setup_file._does_string_exist(f"{World_Order_Warps.possible_bottles_locations[current_world_name][item_name]}190C0049")):
                        available_bottles.append(item_name)
            for possible_bottles in list(bottles_world_warp_dict[current_world_name]["Possible_Bottles"]):
                if(possible_bottles not in available_bottles):
                    del bottles_world_warp_dict[current_world_name]["Possible_Bottles"][possible_bottles]
    
    def _bottles_new_world_order(self):
        '''Determines the new world order that also shuffles bottles around between the worlds'''
        for world_object in self.world_list[:-2]:
            if((world_object._world_name).startswith("Click Clock Wood")):
                world_name = "Click Clock Wood"
            else:
                world_name = world_object._world_name
            for flag_string in bottles_world_warp_dict[world_name]["Flagged_Object_Flags"]:
                if(flag_string.startswith("*")):
                    bottles_world_warp_dict[world_name]["Flagged_Object_Flags"][flag_string]["ID"] = flag_string
                else:
                    for setup_file in world_object._setup_list:
                        flag_id = setup_file._obtain_object_id_at_location(flag_string)
                        if(flag_id != -1):
                            if((flag_id >= 0x1) and flag_id <= 0x63):
                                bottles_world_warp_dict[world_name]["Flagged_Object_Flags"][flag_string]["Type"] = "Jiggy"
                            elif((flag_id >= 0x64) and flag_id <= 0x79):
                                bottles_world_warp_dict[world_name]["Flagged_Object_Flags"][flag_string]["Type"] = "Empty Honeycomb"
                            elif((flag_id >= 0xC8) and flag_id <= 0x13A):
                                bottles_world_warp_dict[world_name]["Flagged_Object_Flags"][flag_string]["Type"] = "Mumbo Token"
                            bottles_world_warp_dict[world_name]["Flagged_Object_Flags"][flag_string]["ID"] = flag_id
                            break
        for world_object in self.world_list[-2:]:
            world_name = world_object._world_name
            for flag_string in extra_flagged_object_flags[world_name]:
                if(flag_string.startswith("*")):
                    extra_flagged_object_flags[world_name][flag_string]["ID"] = flag_string
                else:
                    for setup_file in world_object._setup_list:
                        flag_id = setup_file._obtain_object_id_at_location(flag_string)
                        if(flag_id != -1):
                            if((flag_id >= 0x1) and flag_id <= 0x63):
                                extra_flagged_object_flags[world_name][flag_string]["Type"] = "Jiggy"
                            elif((flag_id >= 0x64) and flag_id <= 0x79):
                                extra_flagged_object_flags[world_name][flag_string]["Type"] = "Empty Honeycomb"
                            elif((flag_id >= 0xC8) and flag_id <= 0x13A):
                                extra_flagged_object_flags[world_name][flag_string]["Type"] = "Mumbo Token"
                            extra_flagged_object_flags[world_name][flag_string]["ID"] = flag_id
                            break
        self.world_order = World_Order_Bottles(bottles_world_warp_dict, extra_flagged_object_flags, seed_val=self.seed, one_hp=self.grandmaster.one_health_banjo_var.get())
        self.world_order._determine_world_order()
        if(self.grandmaster.cheat_sheet_var.get() == 1):
            world_cheat_sheet_str = ""
            for world in self.world_order.world_order_list:
                world_cheat_sheet_str += f"World: {world}\n"
                for move_location in self.world_order.world_order_dict[world]['Learned_Moves']:
                    world_cheat_sheet_str += f"Move: {self.world_order.world_order_dict[world]['Learned_Moves'][move_location]}    Location: {move_location}\n"
                world_cheat_sheet_str += "\n"
            with open(f"{self.grandmaster.cwd}Randomized_ROM/MOVES_CHEAT_SHEET_{self.seed}.txt", "w+") as world_entrance_cheat_sheet:
                world_entrance_cheat_sheet.write(world_cheat_sheet_str)
    
    def _bottles_set_new_moves(self):
        '''Replaces the 1-Ups with the calculated bottles hill'''
        for world_object in self.world_list[:-2]:
            world_name = world_object._world_name
            if("-" in world_name):
                world_name = world_name.split("-")[0][:-1]
            for setup_file in world_object._setup_list:
                for move_location in self.world_order.world_order_dict[world_name]["Learned_Moves"]:
                    replace_1_up = f"{World_Order_Warps.possible_bottles_locations[world_name][move_location]}190C0049"
                    if(setup_file._does_string_exist(replace_1_up)):
                        new_move = World_Order_Warps.learnable_moves_dict[self.world_order.world_order_dict[world_name]["Learned_Moves"][move_location]]
                        replacement_dict = {
                            6: int(new_move[:2], 16),
                            7: int(new_move[2:4], 16),
                            8: int(new_move[4:6], 16),
                            9: int(new_move[6:], 16),
                            }
                        setup_file._edit_object(replace_1_up, replacement_dict)
                        self._new_move_camera(setup_file, new_move)
    
    def _bottles_world_order_shuffle_main(self):
        '''Runs through the bottles world shuffle functions'''
        self.mumbos_mountain._setup_list[0]._check_for_orange()
        self._determine_available_move_slots()
        self._bottles_new_world_order()
        self._move_world_order(shuffle_type="Bottles")
        self._bottles_set_new_moves()
    
    def _remove_learning_move_warps(self):
        '''Removes placement warps for BK when a move is learned in TTC or GV'''
        replacement_dict = {
            6: 0x19, 7: 0x0C,
            8: 0x02, 9: 0x68,
            }
        self.treasure_trove_cove._setup_list[0]._edit_object("0A1F05ED0C5C190C0372", replacement_dict)
        self.treasure_trove_cove._setup_list[0]._edit_object("FF1608710456190C0372", replacement_dict)
        self.gobis_valley._setup_list[0]._edit_object("E7C90B0CFCCF190C0372", replacement_dict)
    
    ### WORLD ORDER WARPS MAIN ###
    def _world_order_warps_main(self):
        '''Runs the world order warps options that are not NONE'''
        self._gather_all_world_warps()
        self._gather_all_bottles_mounds()
        if(self.grandmaster.world_entrance_var.get() == "Basic Shuffle"):
            self._basic_world_order_shuffle_main()
            self._world_entrance_signs(shuffle_type="Simple")
            if(self.grandmaster.skip_furnace_fun_var.get() == 1):
                self._brentilda_world_order_hints(shuffle_type="Simple")
            self._add_clankers_cavern_jump_pad()
        elif(self.grandmaster.world_entrance_var.get() == "Bottles Shuffle"):
            self._bottles_world_order_shuffle_main()
            self._world_entrance_signs(shuffle_type="Bottles")
            self._remove_learning_move_warps()
            if(self.grandmaster.skip_furnace_fun_var.get() == 1):
                self._brentilda_world_order_hints(shuffle_type="Bottles")

    ##########################
    ### WITHIN WORLD WARPS ###
    ##########################
    
    def _set_world_warps_by_world(self, world_object, randomized_warp_dict):
        '''Sets the within world warps by world'''
        for warp in randomized_warp_dict:
            new_warp_string = warp.new_warp_search_strings[0]
            for warp_search_string in randomized_warp_dict[warp]:
                for setup_file in world_object._setup_list:
                    if(setup_file._edit_object(warp_search_string, {
                        7: int(new_warp_string[14:16], 16),
                        8: int(new_warp_string[16:18], 16), 9: int(new_warp_string[18:20], 16),
                        10: int(new_warp_string[20:22], 16), 11: int(new_warp_string[22:24], 16),
                        12: int(new_warp_string[24:26], 16), 13: int(new_warp_string[26:28], 16),
                        })):
                        break
    
    def _within_world_warps_by_world(self):
        '''Shuffles the within world warps within each world'''
        within_world_warps_obj = Within_World_Warps.Within_World_Warps_Class(self.seed, Within_World_Warps.Levels)
        for world_object in self.world_list[:-2]:
            within_world_warps_obj._randomize_by_world(world_object._world_name)
            self._set_world_warps_by_world(world_object, within_world_warps_obj._randomized_warp_dict)
        if(self.grandmaster.cheat_sheet_var.get() == 1):
            self._generate_within_world_warps_cheat_sheet(within_world_warps_obj._randomized_warp_cheat_sheet_dict)
 
    def _set_world_warps_by_game(self, randomized_warp_dict):
        '''Sets the within world warps by game'''
        for warp in randomized_warp_dict:
            new_warp_string = warp.new_warp_search_strings[0]
            for warp_search_string in randomized_warp_dict[warp]:
                string_found = False
                for world_object in self.world_list[:-2]:
                    for setup_file in world_object._setup_list:
                        if(setup_file._edit_object(warp_search_string, {
                            7: int(new_warp_string[14:16], 16),
                            8: int(new_warp_string[16:18], 16), 9: int(new_warp_string[18:20], 16),
                            10: int(new_warp_string[20:22], 16), 11: int(new_warp_string[22:24], 16),
                            12: int(new_warp_string[24:26], 16), 13: int(new_warp_string[26:28], 16),
                            })):
                            string_found = True
                            break
                    if(string_found):
                        break
 
    def _within_world_warps_by_game(self):
        '''Shuffles the within world warps within all 9 worlds'''
        within_world_warps_obj = Within_World_Warps.Within_World_Warps_Class(self.seed, Within_World_Warps.Levels)
        world_list = []
        for world_object in self.world_list[:-2]:
            world_list.append(world_object._world_name)
        within_world_warps_obj._randomize_by_game(world_list)
        self._set_world_warps_by_game(within_world_warps_obj._randomized_warp_dict)
        if(self.grandmaster.cheat_sheet_var.get() == 1):
            self._generate_within_world_warps_cheat_sheet(within_world_warps_obj._randomized_warp_cheat_sheet_dict)
    
    def _generate_within_world_warps_cheat_sheet(self, randomized_warp_cheat_sheet_dict):
        '''Creates a cheat sheet for within world warps'''
        cheat_sheet_text = "Original Warp -> Actually Goes To\n"
        for original_warp in randomized_warp_cheat_sheet_dict:
            cheat_sheet_text += f"{original_warp} -> {randomized_warp_cheat_sheet_dict[original_warp]}\n"
        config_file = f"{self.grandmaster.cwd}Randomized_ROM/WITHIN_WORLD_WARPS_CHEAT_SHEET_{self.seed}.txt"
        with open(config_file, "w+") as cheat_sheet_file: 
            cheat_sheet_file.write(cheat_sheet_text)
    
    def _within_world_warps_main(self):
        '''Runs the within world warps options that are not NONE'''
        if(self.grandmaster.within_world_warps_var.get() == "Shuffle By World"):
            self._within_world_warps_by_world()
        elif(self.grandmaster.within_world_warps_var.get() == "Shuffle By Game"):
            self._within_world_warps_by_game()
    
    ###################
    ### CHEAT SHEET ###
    ###################
    
    def _generate_cheat_sheet(self):
        '''PyDoc'''
        cheat_sheet_dict = {}
        for world_object in self.world_list:
            cheat_sheet_dict[world_object._world_name] = {}
            for setup_file in world_object._setup_list:
                cheat_sheet_dict[world_object._world_name][setup_file.setup_name] = {}
                if(self.grandmaster.struct_var.get() != "None"):
                    try:
                        cheat_sheet_dict[world_object._world_name][setup_file.setup_name]["Note_Count"] = setup_file.note_count
                    except AttributeError:
                        cheat_sheet_dict[world_object._world_name][setup_file.setup_name]["Note_Count"] = 0
                if(self.grandmaster.non_flagged_object_var.get() != "None"):
                    try:
                        cheat_sheet_dict[world_object._world_name][setup_file.setup_name]["Non_Flagged_Object_Dict"] = setup_file.non_flagged_obj_dict
                    except AttributeError:
                        pass
                if(self.grandmaster.flagged_object_var.get() != "None"):
                    try:
                        cheat_sheet_dict[world_object._world_name][setup_file.setup_name]["Flagged_Object_Dict"] = setup_file.flagged_obj_dict
                    except AttributeError:
                        pass
        config_file = f"{self.grandmaster.cwd}Randomized_ROM/OBJECT_CHEAT_SHEET_{self.seed}.json"
        with open(config_file, "w+") as json_file: 
            json.dump(cheat_sheet_dict, json_file, indent=4)
    
    ###########################
    ### HARDER FINAL BATTLE ###
    ###########################
    
    ### ENEMIES ###
    
    def _final_battle_sir_slush(self):
        '''PyDoc'''
        search_string_list = [
            "07C6000407C6", # +X +Z
            "07C80004F83A", # +X -Z
            "F839000407C7", # -X +Z
            "F83A0004F83A", # -X -Z
            ]
        replacement_dict_list = [
            { # +X +Z
                0: 0x04, 1: 0x97,
                2: 0x0, 3: 0x0,
                4: 0x04, 5: 0x97,
                6: 0x19, 7: 0x0C,
                8: 0x01, 9: 0x24,
                10: 0x0, 11: 0x0,
                12: 0x0, 13: 0x0,
                14: 0x0, 15: 0x64,
                },
            { # +X -Z
                0: 0x04, 1: 0x97,
                2: 0x0, 3: 0x0,
                4: 0xFB, 5: 0x69,
                6: 0x19, 7: 0x0C,
                8: 0x01, 9: 0x24,
                10: 0x0, 11: 0x0,
                12: 0x0, 13: 0x0,
                14: 0x0, 15: 0x64,
                },
            { # -X +Z
                0: 0xFB, 1: 0x69,
                2: 0x0, 3: 0x0,
                4: 0x04, 5: 0x97,
                6: 0x19, 7: 0x0C,
                8: 0x01, 9: 0x24,
                10: 0x0, 11: 0x0,
                12: 0x0, 13: 0x0,
                14: 0x0, 15: 0x64,
                },
            { # -X -Z
                0: 0xFB, 1: 0x69,
                2: 0x0, 3: 0x0,
                4: 0xFB, 5: 0x69,
                6: 0x19, 7: 0x0C,
                8: 0x01, 9: 0x24,
                10: 0x0, 11: 0x0,
                12: 0x0, 13: 0x0,
                14: 0x0, 15: 0x64,
                },
            ]
        self.curr_setup_file._replace_each_object_parameters(search_string_list, replacement_dict_list)
    
    def _final_battle_whipcrack(self):
        '''PyDoc'''
        search_string_list = [
            "080C0004044C", # +X +Z
            "FBB40004080C", # +X -Z
            "044C0000F7F3", # -X +Z
            "F7F30004FBB3", # -X -Z
            ]
        replacement_dict_list = [
            { # +X +Z
                0: 0x04, 1: 0x97,
                2: 0x0, 3: 0x0,
                4: 0x04, 5: 0x97,
                6: 0x19, 7: 0x0C,
                8: 0x03, 9: 0x0F,
                10: 0x0, 11: 0x0,
                12: 0x0, 13: 0x0,
                14: 0x0, 15: 0x50,
                },
            { # +X -Z
                0: 0x04, 1: 0x97,
                2: 0x0, 3: 0x0,
                4: 0xFB, 5: 0x69,
                6: 0x19, 7: 0x0C,
                8: 0x03, 9: 0x0F,
                10: 0x0, 11: 0x0,
                12: 0x0, 13: 0x0,
                14: 0x0, 15: 0x50,
                },
            { # -X +Z
                0: 0xFB, 1: 0x69,
                2: 0x0, 3: 0x0,
                4: 0x04, 5: 0x97,
                6: 0x19, 7: 0x0C,
                8: 0x03, 9: 0x0F,
                10: 0x0, 11: 0x0,
                12: 0x0, 13: 0x0,
                14: 0x0, 15: 0x50,
                },
            { # -X -Z
                0: 0xFB, 1: 0x69,
                2: 0x0, 3: 0x0,
                4: 0xFB, 5: 0x69,
                6: 0x19, 7: 0x0C,
                8: 0x03, 9: 0x0F,
                10: 0x0, 11: 0x0,
                12: 0x0, 13: 0x0,
                14: 0x0, 15: 0x50,
                },
            ]
        self.curr_setup_file._replace_each_object_parameters(search_string_list, replacement_dict_list)
    
    def _final_battle_ground_enemies(self):
        # Enemies
        ground_enemy_string_list = [
            "065F00000122", # +X +Z
            "01210000F9A2", # +X -Z
            "FEDE0000065E", # -X +Z
            "F9A20000FEDE", # -X -Z
            ]
        ground_replacement_dict_option_list = [
            { # Ticker
                8: 0x0, 9: 0x05,
                },
            { # Snippet
                8: 0x0, 9: 0x67,
                },
            { # Ripper
                8: 0x0, 9: 0xC7,
                },
            { # Limbo
                8: 0x03, 9: 0x4E,
                },
            { # Mum-mum
                8: 0x03, 9: 0x4F,
                },
            { # Seaman Grublin
                8: 0x03, 9: 0x50,
                },
            { # Ice Cube
                8: 0x03, 9: 0x7D,
                },
            { # Shrapnel
                8: 0x0, 9: 0x56,
                },
            ]
        if(self.grandmaster.enemies_var.get() == "All Toughies"):
            ground_replacement_dict_option_list = [
                { # Bull
                    8: 0x0, 9: 0x04,
                    },
                ]
        ground_enemy_location_replacement_dict = [
            { # +X +Z
                0: 0x01, 1: 0xF4,
                2: 0x0, 3: 0x0,
                4: 0x01, 5: 0xF4,
                },
            { # +X -Z
                0: 0x01, 1: 0xF4,
                2: 0x0, 3: 0x0,
                4: 0xFE, 5: 0x0C,
                },
            { # -X +Z
                0: 0xFE, 1: 0x0C,
                2: 0x0, 3: 0x0,
                4: 0x01, 5: 0xF4,
                },
            { # -X -Z
                0: 0xFE, 1: 0x0C,
                2: 0x0, 3: 0x0,
                4: 0xFE, 5: 0x0C,
                },
            ]
        ground_replacement_dict_list = []
        for enemy_num in range(len(ground_enemy_string_list)):
            ground_replacement_dict_list.append(self._choose_from_list(ground_replacement_dict_option_list, increment=enemy_num))
        self.curr_setup_file._replace_each_object_parameters(ground_enemy_string_list, ground_replacement_dict_list)
        self.curr_setup_file._replace_each_object_parameters(ground_enemy_string_list, ground_enemy_location_replacement_dict)
    
    def _final_battle_sky_enemies(self):
        '''PyDoc'''
        sky_enemy_string_list = [
            "011E0004065E", # +X +Z
            "065E0004FEDE", # +X -Z
            "F9A200040122", # -X +Z
            "FEDE0004F9A1", # -X -Z
            ]
        sky_replacement_dict_option_list = [
            { # Flotsam
                8: 0x01, 9: 0x3B,
                },
            { # Chompa
                8: 0x01, 9: 0xCC,
                },
            { # Clucker
                8: 0x02, 9: 0x9F,
                },
            ]
        if(self.grandmaster.enemies_var.get() == "All Toughies"):
            sky_replacement_dict_option_list = [
                { # Bee
                    6: 0x07, 7: 0x8C,
                    8: 0x03, 9: 0x4D,
                    },
                ]
        sky_enemy_location_replacement_dict = [
            { # +Z
                0: 0x0, 1: 0x0,
                2: 0x05, 3: 0x14,
                4: 0x02, 5: 0xBC,
                12: 0x00, 13: 0x00,
                },
            { # +X
                0: 0x02, 1: 0xBC,
                2: 0x05, 3: 0x14,
                4: 0x0, 5: 0x0,
                12: 0x2D, 13: 0x00,
                },
            { # -X
                0: 0xFD, 1: 0x44,
                2: 0x05, 3: 0x14,
                4: 0x0, 5: 0x0,
                12: 0x87, 13: 0x00,
                },
            { # -Z
                0: 0x0, 1: 0x0,
                2: 0x05, 3: 0x14,
                4: 0xFD, 5: 0x44,
                12: 0x5A, 13: 0x00,
                }
            ]
        replacement_dict_list = []
        for enemy_num in range(len(sky_enemy_string_list)):
            replacement_dict_list.append(self._choose_from_list(sky_replacement_dict_option_list, increment=enemy_num))
        self.curr_setup_file._replace_each_object_parameters(sky_enemy_string_list, replacement_dict_list)
        self.curr_setup_file._replace_each_object_parameters(sky_enemy_string_list, sky_enemy_location_replacement_dict)
    
    ### ENVIRONMENT ###
    
    def _final_battle_floor_is_missing(self):
        '''PyDoc'''
        search_string_list = [
#             "02AEF5C10FF5", # Lava
            "FFFDFF4203FC", # Entry
            "044D0000080D", # Jump Pad
            "080C0000FBB3", # Jump Pad
            "F7F30000044B", # Jump Pad
            "FBB50000F7F4", # Jump Pad
            "011E0004065E",
            "FEDE0000065E",
            "F9A200040122",
            "F9A20000FEDE",
            "FEDE0004F9A1",
            "01210000F9A2",
            "065E0004FEDE",
            "065F00000122",
            ]
        replacement_dict_list = [
#             { # Lava
#                 0: 0x0, 1: 0x0,
#                 2: 0x0, 3: 0x2,
#                 4: 0x0, 5: 0x0,
#                 },
            { # Entry
                0: 0x0, 1: 0x0A,
                2: 0x0, 3: 0x0A,
                4: 0x05, 5: 0x46,
                },
            { # Jump Pad +X +Z
                0: 0x0, 1: 0x0,
                2: 0xFF, 3: 0xD3,
                4: 0x04, 5: 0x4C,
                6: 0x19, 7: 0x0C,
                8: 0x0, 9: 0x0B,
                10: 0x0, 11: 0x0,
                12: 0x0, 13: 0x0,
                14: 0x0, 15: 0xFF,
                },
            { # Jump Pad +X -Z
                0: 0x04, 1: 0x4C,
                2: 0xFF, 3: 0xD3,
                4: 0x0, 5: 0x0,
                6: 0x19, 7: 0x0C,
                8: 0x0, 9: 0x0B,
                10: 0x0, 11: 0x0,
                12: 0x2D, 13: 0x0,
                14: 0x0, 15: 0xFF,
                },
            { # Jump Pad -X +Z
                0: 0xFB, 1: 0xB4,
                2: 0xFF, 3: 0xD3,
                4: 0x0, 5: 0x0,
                6: 0x19, 7: 0x0C,
                8: 0x0, 9: 0x0B,
                10: 0x0, 11: 0x0,
                12: 0x87, 13: 0x0,
                14: 0x0, 15: 0xFF,
                },
            { # Jump Pad -X -Z
                0: 0x0, 1: 0x0,
                2: 0xFF, 3: 0xD3,
                4: 0xFB, 5: 0xB4,
                6: 0x19, 7: 0x0C,
                8: 0x0, 9: 0x0B,
                10: 0x0, 11: 0x0,
                12: 0x5A, 13: 0x0,
                14: 0x0, 15: 0xFF,
                },
            { # Raise To 275
                2: 0x01, 3: 0x13,
                },
            { # Raise To 275
                2: 0x01, 3: 0x13,
                },
            { # Raise To 275
                2: 0x01, 3: 0x13,
                },
            { # Raise To 275
                2: 0x01, 3: 0x13,
                },
            { # Raise To 275
                2: 0x01, 3: 0x13,
                },
            { # Raise To 275
                2: 0x01, 3: 0x13,
                },
            { # Raise To 275
                2: 0x01, 3: 0x13,
                },
            { # Raise To 275
                2: 0x01, 3: 0x13,
                },
            ]
        self.curr_setup_file._replace_each_object_parameters(search_string_list, replacement_dict_list)
        final_battle_area = Level_Model_Class(self._file_dir, "10678")
        final_battle_area._grab_floors()
        vert_condition = lambda Vert1, Vert2, Vert3: ((final_battle_area._vertex_dict[Vert1]["Y"] < 1) and (final_battle_area._vertex_dict[Vert1]["Y"] > -6) and
                                                      (final_battle_area._vertex_dict[Vert2]["Y"] < 1) and (final_battle_area._vertex_dict[Vert2]["Y"] > -6) and 
                                                      (final_battle_area._vertex_dict[Vert3]["Y"] < 1) and (final_battle_area._vertex_dict[Vert3]["Y"] > -6))
        new_bytes = [0x0, 0x28, 0xFD, 0x79, 0xFD, 0x12]
        final_battle_area._change_floor_type_by_vert(vert_condition, new_bytes)
    
    def _final_battle_jinjo_pads(self):
        search_string_list = [
            "07C6000407C6", # +X +Z
            "07C80004F83A", # +X -Z
            "F839000407C7", # -X +Z
            "F83A0004F83A", # -X -Z
            ]
        replacement_dict_list = [
            { # +X +Z
                0: 0x03, 1: 0xB6,
                2: 0xFF, 3: 0xD3,
                4: 0x03, 5: 0xB6,
                6: 0x19, 7: 0x0C,
                8: 0x0, 9: 0x0B,
                10: 0x0, 11: 0x0,
                12: 0x16, 13: 0x0,
                14: 0x0, 15: 0xFF,
                },
            { # +X -Z
                0: 0x03, 1: 0xB6,
                2: 0xFF, 3: 0xD3,
                4: 0xFC, 5: 0x4A,
                6: 0x19, 7: 0x0C,
                8: 0x0, 9: 0x0B,
                10: 0x0, 11: 0x0,
                12: 0x43, 13: 0x0,
                14: 0x0, 15: 0xFF,
                },
            { # -X +Z
                0: 0xFC, 1: 0x4A,
                2: 0xFF, 3: 0xD3,
                4: 0x03, 5: 0xB6,
                6: 0x19, 7: 0x0C,
                8: 0x0, 9: 0x0B,
                10: 0x0, 11: 0x0,
                12: 0x9D, 13: 0x0,
                14: 0x0, 15: 0xFF,
                },
            { # -X -Z
                0: 0xFC, 1: 0x4A,
                2: 0xFF, 3: 0xD3,
                4: 0xFC, 5: 0x4A,
                6: 0x19, 7: 0x0C,
                8: 0x0, 9: 0x0B,
                10: 0x0, 11: 0x0,
                12: 0x70, 13: 0x0,
                14: 0x0, 15: 0xFF,
                },
            ]
        self.curr_setup_file._replace_each_object_parameters(search_string_list, replacement_dict_list)
    
    def _final_battle_jinjonator_floor(self):
        '''PyDoc'''
        search_string_list = [
            "080C0004044C", # +X +Z
            "FBB40004080C", # +X -Z
            "044C0000F7F3", # -X +Z
            "F7F30004FBB3", # -X -Z
            ]
        replacement_dict_list = [
            { # +X +Z
                0: 0x01, 1: 0x04,
                2: 0xFF, 3: 0xD3,
                4: 0x01, 5: 0x04,
                6: 0x19, 7: 0x0C,
                8: 0x0, 9: 0x0B,
                10: 0x0, 11: 0x0,
                12: 0x16, 13: 0x0,
                14: 0x0, 15: 0xFF,
                },
            { # +X -Z
                0: 0x01, 1: 0x04,
                2: 0xFF, 3: 0xD3,
                4: 0xFE, 5: 0xFC,
                6: 0x19, 7: 0x0C,
                8: 0x0, 9: 0x0B,
                10: 0x0, 11: 0x0,
                12: 0x43, 13: 0x0,
                14: 0x0, 15: 0xFF,
                },
            { # -X +Z
                0: 0xFE, 1: 0xFC,
                2: 0xFF, 3: 0xD3,
                4: 0x01, 5: 0x04,
                6: 0x19, 7: 0x0C,
                8: 0x0, 9: 0x0B,
                10: 0x0, 11: 0x0,
                12: 0x9D, 13: 0x0,
                14: 0x0, 15: 0xFF,
                },
            { # -X -Z
                0: 0xFE, 1: 0xFC,
                2: 0xFF, 3: 0xD3,
                4: 0xFE, 5: 0xFC,
                6: 0x19, 7: 0x0C,
                8: 0x0, 9: 0x0B,
                10: 0x0, 11: 0x0,
                12: 0x70, 13: 0x0,
                14: 0x0, 15: 0xFF,
                },
            ]
        self.curr_setup_file._replace_each_object_parameters(search_string_list, replacement_dict_list)
    
    ### GRUNTY SPECIFIC ###
    
    def _final_battle_grunty_size(self, new_size):
        '''Changes the final battle Gruntilda size'''
        search_string_list = [
            "190C038B", # Grunty
            ]
        replacement_dict_list = [
            { # Grunty
                9: new_size,
                },
            ]
        self.curr_setup_file._replace_each_object_parameters(search_string_list, replacement_dict_list)
        for item_num in range(len(search_string_list)):
            replacement_dict = self._choose_from_list(replacement_dict_list, increment=item_num)
            self.curr_setup_file._edit_object(search_string_list[item_num], replacement_dict)
    
    ### CAUSE I'M NICE ###
    
    def _pity_1_up(self):
        '''Puts a 1-Up where you spawn after failing the Gruntilda Fight'''
        replacement_dict = {
            6: 0x19, 7: 0x0C,
            8: 0x00, 9: 0x49,
            14: 0x0, 15: 0x64,
            }
        self.gruntildas_lair._setup_list[7]._edit_object("0C9201B001DE7D08002A000000000000", replacement_dict)

    ### MAIN ###
    
    def _harder_final_battle_main(self, difficulty_level):
        '''Runs the functions for determining and implementing the final battle changes'''
        # Miscellaneous
        self._pity_1_up()
        # Regular Harder Battle
        self.curr_setup_file = self.gruntildas_lair._setup_list[-1]
        final_battle_categories = []
        if(self.grandmaster.monster_house_var.get() == 1):
            final_battle_categories.append("Enemies")
        if(self.grandmaster.what_floor_var.get() == 1):
            final_battle_categories.append("Floor")
        if(self.grandmaster.grunty_size_var.get() == 1):
            final_battle_categories.append("Size")
        if(not final_battle_categories):
            return
        final_battle_category = self._choose_from_list(final_battle_categories)
#         print(f"Final Battle: {final_battle_category}")
        # Enemies
        if(final_battle_category == "Enemies"):
            # Layered
            self._final_battle_sir_slush()
            self._final_battle_whipcrack()
            if(difficulty_level > 1):
                self._final_battle_ground_enemies()
            if(difficulty_level > 2):
                self._final_battle_sky_enemies()
        # Environment
        elif(final_battle_category == "Floor"):
            # Reverse Layered
            self._final_battle_floor_is_missing()
            if(difficulty_level < 3):
                self._final_battle_jinjo_pads()
            if(difficulty_level < 2):
                self._final_battle_jinjonator_floor()
        # Size
        elif(final_battle_category == "Size"):
            if(difficulty_level == 1):
                self._final_battle_grunty_size(70)
            elif(difficulty_level == 2):
                self._final_battle_grunty_size(50)
            elif(difficulty_level == 3):
                self._final_battle_grunty_size(30)
        
    #########################
    ### SCATTERED STRUCTS ###
    #########################
    
    def _move_struct(self, item_index, level_collision_dict):
        '''Moves the structs on the map based on map collision'''
        curr_x = possible_negative(int(leading_zeros(self.curr_setup_file.mm[item_index + 4], 2) + leading_zeros(self.curr_setup_file.mm[item_index + 5], 2), 16))
        curr_y = possible_negative(int(leading_zeros(self.curr_setup_file.mm[item_index + 6], 2) + leading_zeros(self.curr_setup_file.mm[item_index + 7], 2), 16))
        curr_z = possible_negative(int(leading_zeros(self.curr_setup_file.mm[item_index + 8], 2) + leading_zeros(self.curr_setup_file.mm[item_index + 9], 2), 16))
        voxel_min_x = floor(curr_x / 1000) * 1000
        voxel_max_x = ceil(curr_x / 1000) * 1000
        voxel_min_y = floor(curr_y / 1000) * 1000
        voxel_max_y = ceil(curr_y / 1000) * 1000
        voxel_min_z = floor(curr_z / 1000) * 1000
        voxel_max_z = ceil(curr_z / 1000) * 1000
        selectable_x_z_list = []
        for possible_x in range(voxel_min_x, voxel_max_x, 100):
            for possible_z in range(voxel_min_z, voxel_max_z, 100):
                if(level_collision_dict[(possible_x, possible_z)] < voxel_max_y):
                    selectable_x_z_list.append((possible_x, possible_z))
        if(selectable_x_z_list):
            (new_x, new_z) = self._choose_from_list(selectable_x_z_list, address=self.curr_setup_file.setup_address, increment=item_index)
            new_y = self._choose_random_integer(max(voxel_min_y, level_collision_dict[(new_x, new_z)]), voxel_max_y, address=self.curr_setup_file.setup_address, increment=item_index)
            self.curr_setup_file.mm[item_index + 4] = int(leading_zeros(new_x, 4)[:2], 16)
            self.curr_setup_file.mm[item_index + 5] = int(leading_zeros(new_x, 4)[2:], 16)
            self.curr_setup_file.mm[item_index + 6] = int(leading_zeros(new_y, 4)[:2], 16)
            self.curr_setup_file.mm[item_index + 7] = int(leading_zeros(new_y, 4)[2:], 16)
            self.curr_setup_file.mm[item_index + 8] = int(leading_zeros(new_z, 4)[:2], 16)
            self.curr_setup_file.mm[item_index + 9] = int(leading_zeros(new_z, 4)[2:], 16)
    
    def _find_structs(self, level_collision_dict):
        '''Locates the structs on the map'''
        for struct_search_string in Structs.collectable_struct_id_list:
            item_index = 0
            while(item_index > -1):
                item_index = self.curr_setup_file.mm.find(bytes.fromhex(struct_search_string), item_index)
                if(item_index > -1):
                    self._move_struct(item_index, level_collision_dict)
                    item_index = item_index + 1
        for struct_search_string in Structs.adjusted_collectable_struct_id_list:
            item_index = 0
            while(item_index > -1):
                item_index = self.curr_setup_file.mm.find(bytes.fromhex(struct_search_string), item_index)
                if(item_index > -1):
                    self._move_struct(item_index, level_collision_dict)
                    item_index = item_index + 1
    
    def _scattered_structs_main(self):
        '''Runs the functions for having the structs scattered around the map within their original voxels'''
        ttc_level_model = Level_Model_Class(self._file_dir, "101F0")
        ttc_level_model._find_collision_height()
        self.curr_setup_file = self.treasure_trove_cove._setup_list[0]
        self._find_structs(ttc_level_model._collision_height_dict)
    
    #####################
    ### MISCELLANEOUS ###
    #####################
    
    def _skip_furnace_fun(self):
        '''Changes the warps after the 765 Note Door and after Furnace Fun to link with each other'''
        # Floor 7 To Floor 8
        self.curr_setup_file = self.gruntildas_lair._setup_list[6]
        replacement_dict = {8: 0x00, 9: 0x77}
        object_search_string = "0BA4039C047C64060117"
        self.curr_setup_file._edit_object(object_search_string, replacement_dict)
        object_search_string = "0B8B039C04C064060117"
        self.curr_setup_file._edit_object(object_search_string, replacement_dict)
        object_search_string = "0B76039C04FB64060117"
        self.curr_setup_file._edit_object(object_search_string, replacement_dict)
        object_search_string = "0BB6039C044564060117"
        self.curr_setup_file._edit_object(object_search_string, replacement_dict)
        # Floor 8 To Floor 7
        self.curr_setup_file = self.gruntildas_lair._setup_list[7]
        replacement_dict = {8: 0x01, 9: 0x16}
        object_search_string = "FD93FF8204028D060078"
        self.curr_setup_file._edit_object(object_search_string, replacement_dict)
    
    def _bigger_badder_mr_vile_main(self):
        '''Increases the size of Mr. Vile. Default size is 0x64 (100)'''
        self.curr_setup_file = self.bubblegloop_swamp._setup_list[1]
        object_search_string = "190C013A"
        replacement_dict = {
            8: 0x01,
            9: 0xF4,
            }
        self.curr_setup_file._edit_object(object_search_string, replacement_dict)
    
    def _tiptup_choir_main(self):
        '''Places the tiptup choir in semi-randomly placed positions to make the challenge harder'''
        self.curr_setup_file = self.bubblegloop_swamp._setup_list[2]
        object_search_string_list = ["190C027B", "190C027C", "190C027D", "190C027E", "190C027F", "190C0280"]
        possible_locations = [
            # Lowers To Head Only
            {-4: 0xFE, -3: 0xED},
            # Top Area
            {-6: 0x03, -5: 0xE8, -4: 0xFF, -3: 0x9C, -2: 0x0, -1: 0x0},
            {-6: 0x02, -5: 0xEE, -4: 0xFF, -3: 0x9C, -2: 0x02, -1: 0x8A},
            {-6: 0x03, -5: 0xB6, -4: 0xFF, -3: 0x9C, -2: 0x01, -1: 0x5E},
            {-6: 0x01, -5: 0xC2, -4: 0xFF, -3: 0x9C, -2: 0x03, -1: 0xB6},
            {-6: 0x0, -5: 0x0, -4: 0xFF, -3: 0x9C, -2: 0x03, -1: 0xE8},
            {-6: 0xFE, -5: 0x3E, -4: 0xFF, -3: 0x9C, -2: 0x03, -1: 0xB6},
            # Bottom Area
            {-6: 0xFF, -5: 0x6A, -4: 0xFE, -3: 0xD4, -2: 0xFF, -1: 0x06},
            {-6: 0x0, -5: 0x96, -4: 0xFE, -3: 0xD4, -2: 0xFF, -1: 0x06},
            {-6: 0xFF, -5: 0x06, -4: 0xFE, -3: 0xD4, -2: 0x0, -1: 0x32},
            {-6: 0x0, -5: 0xFA, -4: 0xFE, -3: 0xD4, -2: 0x0, -1: 0x32},
            {-6: 0x01, -5: 0x5E, -4: 0xFE, -3: 0xD4, -2: 0xFD, -1: 0xDA},
            {-6: 0xFE, -5: 0xA2, -4: 0xFE, -3: 0xD4, -2: 0xFD, -1: 0xDA},
            {-6: 0x0, -5: 0x0, -4: 0xFE, -3: 0xD4, -2: 0x01, -1: 0x90},
            ]
        increment = 0
        for object_search_string in object_search_string_list:
            replacement_dict = self._choose_from_list(possible_locations, self.curr_setup_file.setup_address, increment)
            self.curr_setup_file._edit_object(object_search_string, replacement_dict)
            if(replacement_dict != {-4: 0xFE, -3: 0xED}):
                possible_locations.remove(replacement_dict)
            increment += 1
