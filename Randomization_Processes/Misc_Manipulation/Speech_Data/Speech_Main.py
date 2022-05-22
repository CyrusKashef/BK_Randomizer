'''
Created on Oct 29, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

from random import seed, choice

####################
### FILE IMPORTS ###
####################

from Randomization_Processes.Misc_Manipulation.Speech_Data.Speech_File import Speech_File_Class
from Randomization_Processes.Dicts_And_Lists.World_Order_Warps import bottles_moves_camera_dict
from Randomization_Processes.Common_Functions import read_json
from builtins import isinstance

#################################
### SPEECH MANIPULATION CLASS ###
#################################

class Speech_Manipulation_Class():
    '''Handles all of the text related changes'''
    def __init__(self, grandmaster, seed_val):
        self._grandmaster = grandmaster
        self._file_dir = grandmaster.cwd
        self._seed_val = seed_val
        self._spawned_count = {
            "Mumbo's Mountain": {
                "Notes": 5,
                "Jiggies": 6,
                "Abnormal Jiggies": 0,
                "Softlock Jiggies": 0,
                "Empty Honeycombs": 0,
                "Abnormal Empty Honeycombs": 0,
                "Softlock Empty Honeycombs": 2,
                },
            "Treasure Trove Cove": {
                "Notes": 0,
                "Jiggies": 4,
                "Abnormal Jiggies": 1,
                "Softlock Jiggies": 0,
                "Empty Honeycombs": 0,
                "Abnormal Empty Honeycombs": 0,
                "Softlock Empty Honeycombs": 0,
                },
            "Clanker's Cavern": {
                "Notes": 0,
                "Jiggies": 5,
                "Abnormal Jiggies": 0,
                "Softlock Jiggies": 0,
                "Empty Honeycombs": 0,
                "Abnormal Empty Honeycombs": 0,
                "Softlock Empty Honeycombs": 0,
                },
            "Bubblegloop Swamp": {
                "Notes": 5,
                "Jiggies": 10,
                "Abnormal Jiggies": 0,
                "Softlock Jiggies": 0,
                "Empty Honeycombs": 0,
                "Abnormal Empty Honeycombs": 0,
                "Softlock Empty Honeycombs": 0,
                },
            "Freezeezy Peak": {
                "Notes": 0,
                "Jiggies": 9,
                "Abnormal Jiggies": 0,
                "Softlock Jiggies": 0,
                "Empty Honeycombs": 0,
                "Abnormal Empty Honeycombs": 0,
                "Softlock Empty Honeycombs": 0,
                },
            "Gobi's Valley": {
                "Notes": 0,
                "Jiggies": 6,
                "Abnormal Jiggies": 0,
                "Softlock Jiggies": 1,
                "Empty Honeycombs": 2,
                "Abnormal Empty Honeycombs": 0,
                "Softlock Empty Honeycombs": 0,
                },
            "Mad Monster Mansion": {
                "Notes": 0,
                "Jiggies": 3,
                "Abnormal Jiggies": 0,
                "Softlock Jiggies": 2,
                "Empty Honeycombs": 0,
                "Abnormal Empty Honeycombs": 0,
                "Softlock Empty Honeycombs": 1,
                },
            "Rusty Bucket Bay": {
                "Notes": 0,
                "Jiggies": 3,
                "Abnormal Jiggies": 1,
                "Softlock Jiggies": 0,
                "Empty Honeycombs": 1,
                "Abnormal Empty Honeycombs": 0,
                "Softlock Empty Honeycombs": 0,
                },
            "Click Clock Wood": {
                "Notes": 0,
                "Jiggies": 4,
                "Abnormal Jiggies": 1,
                "Softlock Jiggies": 1,
                "Empty Honeycombs": 0,
                "Abnormal Empty Honeycombs": 0,
                "Softlock Empty Honeycombs": 0,
                },
            "Gruntilda's Lair": {
                "Notes": 0,
                "Jiggies": 6,
                "Abnormal Jiggies": 0,
                "Softlock Jiggies": 1,
                "Empty Honeycombs": 0,
                "Abnormal Empty Honeycombs": 0,
                "Softlock Empty Honeycombs": 0,
                },
            "Spiral Mountain": {
                "Notes": 0,
                "Jiggies": 0,
                "Abnormal Jiggies": 0,
                "Softlock Jiggies": 0,
                "Empty Honeycombs": 2,
                "Abnormal Empty Honeycombs": 0,
                "Softlock Empty Honeycombs": 0,
                },
        }

    #################
    ### BRENTILDA ###
    #################
    
    def _brentilda_intro(self):
        '''Modifies Brentilda's intro text'''
        # 0xE3A0 - 5CFEA0
        # HELLO THERE, YOUNG ONES! I'M BRENTILDA, GRUNTILDA'S NICER SISTER. I'VE CREPT DOWN HERE TO HELP YOU DEFEAT THE OLD HAG, IT'S ABOUT TIME SHE WAS TAUGHT A LESSON!
        # I KNOW ALL OF GRUNTY'S DISGUSTING SECRETS, AND I'LL TELL YOU THREE OF THEM EVERY TIME YOU FIND ME.
        # REMEMBER THEM WELL, YOUNG ONES, AS THEY WILL HELP YOU AVOID A FIERY FATE!
        # PRESS B IF YOU'D LIKE TO HEAR THEM!
        brentilda_text = Speech_File_Class(self._file_dir, "E3A0")
        brentilda_text._replace_line("48454c4c4f205448455245", f"HELLO! I'M BRENTILDA!")
        brentilda_text._replace_line("49204b4e4f5720414c4c", f"I KNOW GRUNTY'S RANDOMIZER SPELL AND I'LL TELL YOU 3 HINTS FOR THE SEED EVERY TIME YOU FIND ME.")
        brentilda_text._replace_line("52454d454d424552205448454d", f"I'LL ALSO WARP YOU PAST HER FURNACE FUN.")

    def _click_clock_wood_item_count(self, world_object_list, object_name):
        '''Counts all of the moves, notes, and flagged objects in click clock wood'''
        if(object_name == "Bottles"):
            move_list = []
            for world_object in world_object_list:
                for setup_file in world_object._setup_list:
                    for bottles_search in bottles_moves_camera_dict:
                        if(setup_file._does_string_exist(bottles_search)):
                            move_list.append(bottles_moves_camera_dict[bottles_search]["Move_Name"])
            return move_list
        elif(object_name == "Note"):
            count = 0
            for world_object in world_object_list:
                for setup_file in world_object._setup_list:
                    count += setup_file.note_count
            return count
        elif(object_name == "Flagged"):
            if(self._grandmaster.remove_floating_jiggies_var.get() == 1):
                return self._spawned_count["Click Clock Wood"]["Jiggies"], self._spawned_count["Click Clock Wood"]["Empty Honeycombs"]
            if(self._grandmaster.flagged_object_var.get() in ["No Shuffle", "Shuffle (World)"]):
                return 10, 2
            else:
                jiggy_list = []
                honeycomb_list = []
                for world_object in world_object_list:
                    for setup_file in world_object._setup_list:
                        for flagged_object in setup_file.flagged_obj_dict:
                            if(flagged_object.startswith("Jiggy")):
                                jiggy_list.append(flagged_object)
                            elif(flagged_object.startswith("Empty Honeycomb")):
                                honeycomb_list.append(flagged_object)
                jiggy_count = len(set(jiggy_list)) + self._spawned_count["Click Clock Wood"]["Jiggies"]
                honeycomb_count = len(set(honeycomb_list)) + self._spawned_count["Click Clock Wood"]["Empty Honeycombs"]
                if(self._grandmaster.flagged_object_abnormalities_var.get() == 0):
                    jiggy_count += self._spawned_count["Click Clock Wood"]["Abnormal Jiggies"]
                    honeycomb_count += self._spawned_count["Click Clock Wood"]["Abnormal Empty Honeycombs"]
                if(self._grandmaster.flagged_object_softlock_var.get() == 0):
                    jiggy_count += self._spawned_count["Click Clock Wood"]["Softlock Jiggies"]
                    honeycomb_count += self._spawned_count["Click Clock Wood"]["Softlock Empty Honeycombs"]
                return jiggy_count, honeycomb_count

    def _item_count(self, world_object, object_name):
        '''Counts all of the moves, notes, and flagged objects'''
        if(isinstance(world_object, list)):
            return self._click_clock_wood_item_count(world_object, object_name)
        if(object_name == "Bottles"):
            move_list = []
            for setup_file in world_object._setup_list:
                for bottles_search in bottles_moves_camera_dict:
                    if(setup_file._does_string_exist(bottles_search)):
                        move_list.append(bottles_moves_camera_dict[bottles_search]["Move_Name"])
            return move_list
        elif(object_name == "Note"):
            if(self._grandmaster.struct_var.get() in ["No Shuffle", "Shuffle (World)"]):
                if(world_object._world_name in ["Gruntilda's Lair", "Spiral Mountain"]):
                    return 0
                return 100
            else:
                count = 0
                for setup_file in world_object._setup_list:
                    count += setup_file.note_count
                count += self._spawned_count[world_object._world_name]["Notes"]
                return count
        elif(object_name == "Flagged"):
            if(self._grandmaster.remove_floating_jiggies_var.get() == 1):
                return self._spawned_count[world_object._world_name]["Jiggies"], self._spawned_count[world_object._world_name]["Empty Honeycombs"]
            if(self._grandmaster.flagged_object_var.get() in ["No Shuffle", "Shuffle (World)"]):
                if(world_object._world_name == "Spiral Mountain"):
                    return 0, 6
                elif(world_object._world_name == "Gruntilda's Lair"):
                    return 10, 0
                return 10, 2
            else:
                jiggy_list = []
                honeycomb_list = []
                for setup_file in world_object._setup_list:
                    for flagged_object in setup_file.flagged_obj_dict:
                        if(flagged_object.startswith("Jiggy")):
                            jiggy_list.append(flagged_object)
                        elif(flagged_object.startswith("Empty Honeycomb")):
                            honeycomb_list.append(flagged_object)
                jiggy_count = len(set(jiggy_list))
                honeycomb_count = len(set(honeycomb_list))
                jiggy_count += self._spawned_count[world_object._world_name]["Jiggies"]
                honeycomb_count += self._spawned_count[world_object._world_name]["Empty Honeycombs"]
                if(self._grandmaster.flagged_object_abnormalities_var.get() == 0):
                    jiggy_count += self._spawned_count[world_object._world_name]["Abnormal Jiggies"]
                    honeycomb_count += self._spawned_count[world_object._world_name]["Abnormal Empty Honeycombs"]
                if(self._grandmaster.flagged_object_softlock_var.get() == 0):
                    jiggy_count += self._spawned_count[world_object._world_name]["Softlock Jiggies"]
                    honeycomb_count += self._spawned_count[world_object._world_name]["Softlock Empty Honeycombs"]
                return jiggy_count, honeycomb_count

    def _generate_brentilda_move_string(self, move_list):
        '''Provides the response for the Brentilda move hint'''
        if(len(move_list) == 0):
            move_string = "NO NEW MOVES"
        elif(len(move_list) == 1):
            move_string = move_list[0]
        elif(len(move_list) == 2):
            move_string = f"{move_list[0]} and {move_list[1]}"
        else:
            move_string = ""
            for move_name in move_list[:-1]:
                move_string += f"{move_name}, "
            move_string += f"AND {move_list[-1]}"


    def _brentilda_1_1(self, world_object, detailed=False):
        '''Brentilda move hint for the first world'''
        # 0xE2B0 - 5CF130
        # GRUNTY BRUSHES HER ROTTEN TEETH WITH ~ FLAVORED TOOTHPASTE!
        brentilda_text = Speech_File_Class(self._file_dir, "E2B0")
        move_list = self._item_count(world_object, "Bottles")
        if(isinstance(world_object, list)):
            world_name = "CLICK CLOCK WOOD"
        else:
            world_name = (world_object._world_name).upper()
        if(detailed):
            move_string = self._generate_brentilda_move_string(move_list)
            brentilda_text._replace_line("4752554e5459", f"WORLD 1, {world_name}, HAS {move_string}! ~")
        else:
            brentilda_text._replace_line("4752554e5459", f"WORLD 1, {world_name} HAS {len(move_list)} NEW MOVES! ~")
    
    def _brentilda_1_2(self, world_object):
        '''Brentilda note count for the first world'''
        # 0xE2B8 - 5CF1A0
        # SHE ALSO WASHES HER HAIR WITH ~. YUK!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E2B8")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("53484520414c534f", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("53484520414c534f", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_1_3(self, world_object):
        '''Brentilda flagged object count for the first world'''
        # 0xE2C0 - 5CF200
        # AND SHE GETS HER CLOTHES FROM ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E2C0")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("414e4420534845", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("414e4420534845", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_2_1(self, world_object, detailed=False):
        '''Brentilda move hint for the second world'''
        # 0xE2C8 - 5CF270
        # UGLY GRUNTY'S NICKNAME WAS ~ AT WITCH SCHOOL!
        brentilda_text = Speech_File_Class(self._file_dir, "E2C8")
        move_list = self._item_count(world_object, "Bottles")
        if(isinstance(world_object, list)):
            world_name = "CLICK CLOCK WOOD"
        else:
            world_name = (world_object._world_name).upper()
        if(detailed):
            move_string = self._generate_brentilda_move_string(move_list)
            brentilda_text._replace_line("55474c59204752554e5459", f"WORLD 2, {world_name}, HAS {move_string}! ~")
        else:
            brentilda_text._replace_line("55474c59204752554e5459", f"WORLD 2, {world_name} HAS {len(move_list)} NEW MOVES! ~")
    
    def _brentilda_2_2(self, world_object):
        '''Brentilda note count for the second world'''
        # 0xE2D0 - 5CF2D8
        # I ALSO KNOW THAT ~ IS HER FAVORITE SMELL!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E2D0")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("4920414c534f", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("4920414c534f", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_2_3(self, world_object):
        '''Brentilda flagged object count for the second world'''
        # 0xE2D8 - 5CF348
        # AND THE OLD HAG'S FAVORITE COLOR IS ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E2D8")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("414e4420544845", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("414e4420544845", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_3_1(self, world_object, detailed=False):
        '''Brentilda move hint for the third world'''
        # 0xE388 - 5CFD48
        # GRUNTY WEARS ~ UNDER THAT REPULSIVE DRESS OF HERS!
        brentilda_text = Speech_File_Class(self._file_dir, "E388")
        move_list = self._item_count(world_object, "Bottles")
        if(isinstance(world_object, list)):
            world_name = "CLICK CLOCK WOOD"
        else:
            world_name = (world_object._world_name).upper()
        if(detailed):
            move_string = self._generate_brentilda_move_string(move_list)
            brentilda_text._replace_line("4752554e5459205745415253", f"WORLD 3, {world_name}, HAS {move_string}! ~")
        else:
            brentilda_text._replace_line("4752554e5459205745415253", f"WORLD 3, {world_name} HAS {len(move_list)} NEW MOVES! ~")
    
    def _brentilda_3_2(self, world_object):
        '''Brentilda note count for the third world'''
        # 0xE390 - 5CFDC0
        # SHE'S ALSO GOT THIS NASTY PET DOG WHOSE NAME IS ~!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E390")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("534845275320414c534f", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("534845275320414c534f", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_3_3(self, world_object):
        '''Brentilda flagged object count for the third world'''
        # 0xE398 - 5CFE20
        # MY SISTER SINGS IN HER OWN BAND, ~. THEY'RE AWFUL!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E398")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("4d5920534953544552", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("4d5920534953544552", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_4_1(self, world_object, detailed=False):
        '''Brentilda move hint for the fourth world'''
        # 0xE340 - 5CF910
        # MY LAZY SISTER OFTEN SLEEPS ~, THE DIRTY HAG!
        brentilda_text = Speech_File_Class(self._file_dir, "E340")
        move_list = self._item_count(world_object, "Bottles")
        if(isinstance(world_object, list)):
            world_name = "CLICK CLOCK WOOD"
        else:
            world_name = (world_object._world_name).upper()
        if(detailed):
            move_string = self._generate_brentilda_move_string(move_list)
            brentilda_text._replace_line("4d59204c415a59", f"WORLD 4, {world_name}, HAS {move_string}! ~")
        else:
            brentilda_text._replace_line("4d59204c415a59", f"WORLD 4, {world_name} HAS {len(move_list)} NEW MOVES! ~")
    
    def _brentilda_4_2(self, world_object):
        '''Brentilda note count for the fourth world'''
        # 0xE348 - 5CF980
        # THE ONLY THING SHE'S EVER WON WAS THE ~ COMPETITION AT WITCH SCHOOL!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E348")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("544845204f4e4c59205448494e47", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("544845204f4e4c59205448494e47", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_4_3(self, world_object):
        '''Brentilda flagged object count for the fourth world'''
        # 0xE350 - 5CF9F8
        # SHE OFTEN BOASTS OF APPEARING ON THE COVER OF FAT HAG MONTHLY, ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E350")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("534845204f4654454e20424f41535453", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("534845204f4654454e20424f41535453", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_5_1(self, world_object, detailed=False):
        '''Brentilda move hint for the fifth world'''
        # 0xE2E0 - 5CF3B0
        # MY FAT OLD SISTER'S FAVORITE SPORT IS ~!
        brentilda_text = Speech_File_Class(self._file_dir, "E2E0")
        move_list = self._item_count(world_object, "Bottles")
        if(isinstance(world_object, list)):
            world_name = "CLICK CLOCK WOOD"
        else:
            world_name = (world_object._world_name).upper()
        if(detailed):
            move_string = self._generate_brentilda_move_string(move_list)
            brentilda_text._replace_line("4d5920464154", f"WORLD 5, {world_name}, HAS {move_string}! ~")
        else:
            brentilda_text._replace_line("4d5920464154", f"WORLD 5, {world_name} HAS {len(move_list)} NEW MOVES! ~")
    
    def _brentilda_5_2(self, world_object):
        '''Brentilda note count for the fifth world'''
        # 0xE2E8 - 5CF420
        # ALTHOUGH SHE'S DIM, SHE ATTENDED ~!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E2E8")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("414c54484f554748", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("414c54484f554748", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_5_3(self, world_object):
        '''Brentilda flagged object count for the fifth world'''
        # 0xE2F0 - 5CF490
        # YOU WON'T BELIEVE THAT GRUNTILDA'S PARTY TRICK IS ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E2F0")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("594f5520574f4e2754", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("594f5520574f4e2754", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_6_1(self, world_object, detailed=False):
        '''Brentilda move hint for the sixth world'''
        # 0xE328 - 5CF7C8
        # GRUNTY'S BEST FRIEND AT WITCH SCHOOL WAS THE AWFUL ~!
        brentilda_text = Speech_File_Class(self._file_dir, "E328")
        move_list = self._item_count(world_object, "Bottles")
        if(isinstance(world_object, list)):
            world_name = "CLICK CLOCK WOOD"
        else:
            world_name = (world_object._world_name).upper()
        if(detailed):
            move_string = self._generate_brentilda_move_string(move_list)
            brentilda_text._replace_line("4752554e54592753", f"WORLD 6, {world_name}, HAS {move_string}! ~")
        else:
            brentilda_text._replace_line("4752554e54592753", f"WORLD 6, {world_name} HAS {len(move_list)} NEW MOVES! ~")
    
    def _brentilda_6_2(self, world_object):
        '''Brentilda note count for the sixth world'''
        # 0xE330 - 5CF830
        # WHEN RELAXING, SHE USUALLY READS ~ MAGAZINE!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E330")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5748454e2052454c4158494e47", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("5748454e2052454c4158494e47", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_6_3(self, world_object):
        '''Brentilda flagged object count for the sixth world'''
        # 0xE338 - 5CF8A0
        # WHILE SIPPING A GLASS OF HER FAVORITE ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E338")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5748494c452053495050494e47", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("5748494c452053495050494e47", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_7_1(self, world_object, detailed=False):
        '''Brentilda move hint for the seventh world'''
        # 0xE2F8 - 5CF520
        # THE DISGUSTING GRUNTILDA HAS ~ FOR BREAKFAST!
        brentilda_text = Speech_File_Class(self._file_dir, "E2F8")
        move_list = self._item_count(world_object, "Bottles")
        if(isinstance(world_object, list)):
            world_name = "CLICK CLOCK WOOD"
        else:
            world_name = (world_object._world_name).upper()
        if(detailed):
            move_string = self._generate_brentilda_move_string(move_list)
            brentilda_text._replace_line("5448452044495347555354494e47", f"WORLD 7, {world_name}, HAS {move_string}! ~")
        else:
            brentilda_text._replace_line("5448452044495347555354494e47", f"WORLD 7, {world_name} HAS {len(move_list)} NEW MOVES! ~")
    
    def _brentilda_7_2(self, world_object):
        '''Brentilda note count for the seventh world'''
        # 0xE300 - 5CF590
        # THEN SHE USUALLY HAS ~ FOR DINNER. YUK!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E300")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5448454e20534845", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("5448454e20534845", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_7_3(self, world_object):
        '''Brentilda flagged object count for the seventh world'''
        # 0xE308 - 5CF5F8
        # WARTBAGS THEN FINISHES WITH ~ FOR DESSERT. HOW HORRID!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E308")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5741525442414753", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("5741525442414753", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_8_1(self, world_object, detailed=False):
        '''Brentilda move hint for the eigth world'''
        # 0xE310 - 5CF670
        # REVOLTING GRUNTILDA'S BEDROOM HAS ~ HANGING FROM THE CEILING!
        brentilda_text = Speech_File_Class(self._file_dir, "E310")
        move_list = self._item_count(world_object, "Bottles")
        if(isinstance(world_object, list)):
            world_name = "CLICK CLOCK WOOD"
        else:
            world_name = (world_object._world_name).upper()
        if(detailed):
            move_string = self._generate_brentilda_move_string(move_list)
            brentilda_text._replace_line("5245564f4c54494e47", f"WORLD 8, {world_name}, HAS {move_string}! ~")
        else:
            brentilda_text._replace_line("5245564f4c54494e47", f"WORLD 8, {world_name} HAS {len(move_list)} NEW MOVES! ~")
    
    def _brentilda_8_2(self, world_object):
        '''Brentilda note count for the eigth world'''
        # E318 - 5CF6E0
        # SHE ALSO HAS ~ GROWING IN A POT BESIDE HER BED! FILTHY OLD BAG!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E318")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("53484520414c534f", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("53484520414c534f", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_8_3(self, world_object):
        '''Brentilda flagged object count for the eigth world'''
        # 0xE320 - 5CF758
        # AND YOU'D BE SICK IF YOU SAW HER ENORMOUS ~ UNDIES!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E320")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("414e4420594f552744", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("414e4420594f552744", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_9_1(self, world_object, detailed=False):
        '''Brentilda move hint for the ninth world'''
        # 0xE370 - 5CFBD8
        # DID YOU KNOW WARTBAGS KEEPS ~ IN HER POCKET FOR LUCK?
        brentilda_text = Speech_File_Class(self._file_dir, "E370")
        move_list = self._item_count(world_object, "Bottles")
        if(isinstance(world_object, list)):
            world_name = "CLICK CLOCK WOOD"
        else:
            world_name = (world_object._world_name).upper()
        if(detailed):
            move_string = self._generate_brentilda_move_string(move_list)
            brentilda_text._replace_line("44494420594f55", f"WORLD 9, {world_name}, HAS {move_string}! ~")
        else:
            brentilda_text._replace_line("44494420594f55", f"WORLD 9, {world_name} HAS {len(move_list)} NEW MOVES! ~")
    
    def _brentilda_9_2(self, world_object):
        '''Brentilda note count for the ninth world'''
        # 0xE378 - 5CFC50
        # I'VE ALSO SEEN MY SISTER CUDDLING ~ IN BED AT NIGHT!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E378")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("4927564520414c534f", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("4927564520414c534f", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_9_3(self, world_object):
        '''Brentilda flagged object count for the ninth world'''
        # 0xE380 - 5CFCC8
        # SHE'S REALLY PROUD OF HER BROOMSTICK. IT'S A TOP OF THE RANGE ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E380")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5348452753205245414c4c59", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("5348452753205245414c4c59", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_10_1(self, world_object):
        '''Brentilda flagged object hint for the Gruntilda's Lair'''
        # 0xE358 - 5CFA80
        # GRUESOME GRUNTILDA'S FAVORITE PASTIME IS ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E358")
        brentilda_text._replace_line("47525545534f4d45", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_10_2(self, world_object):
        '''Brentilda flagged object hint for the Spiral Mountain'''
        # 0xE360 - 5CFAF8
        # THIS POOR GUY CALLED ~, WAS HER FIRST AND ONLY BOYFRIEND!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E360")
        brentilda_text._replace_line("5448495320504f4f5220475559", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_10_3(self):
        '''I hope this makes someone call their mom and tell her they love her'''
        # 0xE368 - 5CFB68
        # WHEN SHE WAS YOUNGER, GRUNTY USED TO HAVE ~ AS A PET!
        brentilda_text = Speech_File_Class(self._file_dir, "E368")
        last_brentilda_list = [
            "CHECK UP ON YOUR FRIENDS, BEFORE YOU MISS YOUR CHANCE... ~",
            "IT'S NICE THAT PEOPLE ARE TALKING TO ME NOW, I THOUGHT EVERYONE FORGOT ME... ~",
            "HAS ANYONE TOLD YOU HOW PROUD THEY ARE OF YOU RECENTLY? WELL I'M PROUD! ~"
        ]
        seed(a=self._seed_val)
        brentilda_speech = choice(last_brentilda_list)
        brentilda_text._replace_line("5748454e2053484520574153", brentilda_speech)
    
    ######################
    ### INTRO CUTSCENE ###
    ######################
    
    def _intro_cutscene_1(self):
        '''Edits Intro Cutscene 1'''
        # 0xD150 - 5CA8F8
        # GRUNTILDA: DINGPOT, DINGPOT BY THE BENCH,
        # GRUNTILDA: WHO IS THE NICEST LOOKING WENCH?
        # DINGPOT:   WHY IT'S GRUNTY ANY DAY,
        # DINGPOT:   SHE REALLY TAKES MY BREATH AWAY...COUGH!
        # GRUNTILDA: YES YOU'RE RIGHT, I'M RATHER PROUD,
        # GRUNTILDA: MY LOOKS STAND ME OUT FROM THE CROWD!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D150")
        intro_cutscene_text._replace_line("44494e47504f54", "DINGPOT, DINGPOT THAT I CLAIM,")
        intro_cutscene_text._replace_line("57484f20495320544845", "WHO HAS THE TOUGHEST GAME?")
        intro_cutscene_text._replace_line("5748592049542753", "WHY IT'S GRUNTY'S ANY DAY,")
        intro_cutscene_text._replace_line("534845205245414c4c59", "HER LEVELS TAKE PLAYERS' LIVES AWAY...COUGH!")
        intro_cutscene_text._replace_line("59455320594f55275245", "YES YOU'RE RIGHT, I'M RATHER PROUD,")
        intro_cutscene_text._replace_line("4d59204c4f4f4b53", "MY WORLDS STAND ME OUT FROM THE CROWD!")
    
    def _intro_cutscene_2(self):
        '''Edits Intro Cutscene 2'''
        # 0xD158 - 5CA9B0
        # DINGPOT: ERR...BUT THERE IS THIS GIRL...
        # GRUNTILDA: WHAT D'YOU MEAN, THIS CANNOT BE,
        # GRUNTILDA: THERE'S NO ONE PRETTIER THAN ME!
        # DINGPOT: WHY, IT'S TOOTY, YOUNG AND SMALL,
        # DINGPOT: SHE'S THE PRETTIEST GIRL OF ALL!
        # GRUNTILDA: NO NO NO YOU MUST BE MAD,
        # GRUNTILDA: NICER BEAUTY CAN'T BE HAD!
        # DINGPOT: UNFORTUNATELY I THINK YOU'LL FIND,
        # DINGPOT: IT'S TOOTY, SHE'S CUTE AND KIND!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D158")
        intro_cutscene_text._replace_line("4552522e2e2e425554", "ERR...BUT MOST HAVE BEATEN IT...")
        intro_cutscene_text._replace_line("57484154204427594f55", "WHAT D'YOU MEAN, THIS CANNOT BE,")
        intro_cutscene_text._replace_line("54484552452753204e4f", "THE LAST TWO WORLDS AREN'T EASY!")
        intro_cutscene_text._replace_line("5748592c204954275320544f4f5459", "PLAYERS MEMORIZED EVERY SPOT,")
        intro_cutscene_text._replace_line("53484527532054484520505245545449455354", "THEY MOVE QUICKLY IN TALON TROT.")
        intro_cutscene_text._replace_line("4e4f204e4f204e4f", "NO NO NO YOU MUST BE MAD,")
        intro_cutscene_text._replace_line("4e4943455220424541555459", "HARDER GAMEPLAY CAN'T BE HAD!")
        intro_cutscene_text._replace_line("554e464f5254554e4154454c59", "I THINK YOU'LL COME TO KNOW,")
        intro_cutscene_text._replace_line("4954275320544f4f5459", "THERE'S A ROUTE PLAYERS LIKE TO GO.")
    
    def _intro_cutscene_3(self):
        '''Unused'''
        # 0xD160 - 5CAA88
        # GRUNTILDA: WELL...WE'LL SEE ABOUT THAT!
        pass
    
    def _intro_cutscene_4(self):
        '''Edits Intro Cutscene 4'''
        # 0xD168 - 5CAAB8
        # BOTTLES: HI THERE TOOTY, WHAT ARE YOU GOING TO DO TODAY?
        # TOOTY: WHEN MY BIG LAZY BROTHER WAKES UP, WE'RE GOING ON AN ADVENTURE!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D168")
#         intro_cutscene_text._replace_line("4849205448455245", "")
        intro_cutscene_text._replace_line("5748454e204d59", "I'M GOING TO WATCH MY BROTHER SPEEDRUN THE GAME HAHA!")

    def _intro_cutscene_5(self):
        '''Edits Intro Cutscene 5'''
        # 0xD170 - 5CAB30
        # KAZOOIE: WAKE UP, I WANT TO GO ON AN ADVENTURE TOO...
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D170")
        intro_cutscene_text._replace_line("57414b45205550", "WAKE UP, I WANT TO GET UNDER 2 HOURS!")
    
    def _intro_cutscene_6(self):
        '''Edits Intro Cutscene 6'''
        # 0xD178 - 5CAB70
        # GRUNTILDA: IF TOOTY THINKS SHE'S FAIRER THAN ME,
        # GRUNTILDA: I'LL STEAL HER LOOKS AND UGLY SHE'LL BE!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D178")
        intro_cutscene_text._replace_line("494620544f4f5459", "IF PLAYERS THINK THEY KNOW THE GAME WELL,")
        intro_cutscene_text._replace_line("49274c4c20535445414c", "I'LL CHANGE THE GAME WITH MY RANDOMIZE SPELL!")
    
    def _intro_cutscene_7(self):
        '''Unused'''
        # 0xD180 - 5CABD0
        # BOTTLES: IS THAT YOUR BROTHER?
        # BOTTLES: UP THERE IN THE SKY!
        # TOOTY: WHERE, MR. MOLE? I CAN'T SEE HIM...
#         intro_cutscene_text = Speech_File_Class(self._file_dir, "D180")
#         intro_cutscene_text._replace_line("4953205448415420594f5552", "")
#         intro_cutscene_text._replace_line("5550205448455245", "")
#         intro_cutscene_text._replace_line("57484552452c204d52", "")
        pass
    
    def _intro_cutscene_8(self):
        '''Edits Intro Cutscene 8'''
        # 0xD188 - 5CAC38
        # TOOTY: I DON'T THINK SO. WHO IS THAT?
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D188")
        intro_cutscene_text._replace_line("4920444f4e2754", "OH NO... THAT'S A BAD SEED!")
    
    def _intro_cutscene_9(self):
        '''Edits Intro Cutscene 9'''
        # 0xD190 - 5CAC70
        # GRUNTILDA: COME TO ME, MY LITTLE PRETTY,
        # GRUNTILDA: YOU'LL SOON BE UGLY, WHAT A PITY!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D190")
        intro_cutscene_text._replace_line("434f4d4520544f204d45", "ONCE I MOVE SOME THINGS AROUND,")
        intro_cutscene_text._replace_line("594f55274c4c20534f4f4e", "NO COLLECTABLES WILL BE FOUND!")
    
    def _intro_cutscene_10(self):
        '''Edits Intro Cutscene 10'''
        # 0xD198 - 5CACC0
        # TOOTY: LET ME GO, YOU UGLY OLD HAG!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D198")
        intro_cutscene_text._replace_line("4c4554204d4520474f", "PUT THAT BACK, YOU UGLY OLD HAG!")
    
    def _intro_cutscene_11(self):
        '''Edits Intro Cutscene 11'''
        # 0xD1A0 - 5CACF8
        # GRUNTILDA: DON'T SCRATCH AND BITE, MY LITTLE BEAR,
        # GRUNTILDA: YOU'LL SOON NEED BIGGER UNDERWEAR!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D1A0")
        intro_cutscene_text._replace_line("444f4e27542053435241544348", "I'LL PUT THIS HERE, I'LL PUT THAT THERE,")
        intro_cutscene_text._replace_line("594f55274c4c20534f4f4e", "NOW THERE ARE NEW THINGS EVERYWHERE!")
    
    def _intro_cutscene_12(self):
        '''Edits Intro Cutscene 12'''
        # 0xD1A8 - 5CAD58
        # BOTTLES: OH NO, SHE'S GOT HER! SOMEBODY......HELP!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D1A8")
        intro_cutscene_text._replace_line("4f48204e4f2c", "I CAN'T TELL, IS THIS WORLD RECORD PACE?")
    
    def _intro_cutscene_13(self):
        '''Unused'''
        # 0xD1B0 - 5CAD98
        # KAZOOIE: BANJO! WAKE UP......NOW!
#         intro_cutscene_text = Speech_File_Class(self._file_dir, "D1B0")
#         intro_cutscene_text._replace_line("42414e4a4f21", "")
        pass
    
    def _intro_cutscene_14(self):
        '''Unused'''
        # 0xD1B8 - 5CADC8
        # BANJO: YAWN...WHAT DO YOU WANT KAZOOIE?
#         intro_cutscene_text = Speech_File_Class(self._file_dir, "")
#         intro_cutscene_text._replace_line("", "")
        pass
    
    def _intro_cutscene_15(self):
        '''Unused'''
        # 0xD1C0 - 5CAE00
        # KAZOOIE: LET'S GET OUTSIDE, THERE'S TROUBLE!
#         intro_cutscene_text = Speech_File_Class(self._file_dir, "")
#         intro_cutscene_text._replace_line("", "")
        pass
    
    ###########################
    ### ENTER LAIR CUTSCENE ###
    ###########################
    
    def _enter_lair_cutscene(self):
        '''Edits Enter Lair Cutscene'''
        # 0xD1C8 - 5CAE38
        # GRUNTY: THIS FINE CONTRAPTION SO I'M TOLD,
        # GRUNTY: WILL MAKE ME YOUNG AND TOOTY OLD!
        # TOOTY: LET ME GO, YOU FAT HAG! MY BROTHER WILL COME
        # TOOTY: AND KICK YOUR BUTT!
        # GRUNTY: RESCUE YOU HE WILL NOT DARE,
        # GRUNTY: THERE'S MANY DANGERS IN MY LAIR!
        # GRUNTY: HURRY KLUNGO, PUSH THAT SWITCH,
        # GRUNTY: I'M TIRED OF BEING AN UGLY WITCH!
        # KLUNGO: YESSS MISSSTRESSS GRUNTY! POWER ISSS ON, SSSOON BE READY...
        # TOOTY: BANJO............HELP!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D1C8")
        intro_cutscene_text._replace_line("544849532046494e45", "WITH EVERYTHING JUMBLED, I'LL HAVE MORE TIME,")
        intro_cutscene_text._replace_line("57494c4c204d414b45", "TO STEAL YOUR BEAUTY AND BE AT MY PRIME!")
        intro_cutscene_text._replace_line("4c4554204d4520474f", "MY BROTHER BEAT YOU BEFORE,")
        intro_cutscene_text._replace_line("414e44204b49434b", "HE WILL BEAT YOU AGAIN!")
        intro_cutscene_text._replace_line("52455343554520594f55", "THERE IS NO GUIDE FOR RNG,")
        intro_cutscene_text._replace_line("54484552452753204d414e59", "I DOUBT HE EVEN OPENED THE README!")
        intro_cutscene_text._replace_line("4855525259204b4c554e474f2c", "NOW HURRY KLUNGO, IT'S TIME TO START,")
        intro_cutscene_text._replace_line("49274d205449524544", "I WANT TO LOOK LIKE ALL MY FAN ART!")
        intro_cutscene_text._replace_line("5945535353204d49535353545245535353", "YESSS MISSSTRESSS GRUNTY!")
        intro_cutscene_text._replace_line("42414e4a4f2e2e2e", "THIS IS SO NOT WAHAY...")
    
    ##########################
    ### GAME OVER CUTSCENE ###
    ##########################

    def _game_over_cutscene(self):
        '''Edits Game Over Cutscene'''
        # 0xD1D0 - 5CAF48
        # GRUNTY: BANJO'S GAME ENDS IN MY TOWER,
        # GRUNTY: TURN IT UP I NEED FULL POWER!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D1D0")
        intro_cutscene_text._replace_line("42414E4A4F27532047414D4520454E44", "THE PLAYER IS NOW REGRETTING,")
        intro_cutscene_text._replace_line("5455524E2049542055502049204E4545", "TURNING ON A HARDER SETTING!")
        # 0xD1D8 - 5CAF98
        # KLUNGO: YESSS YOUR GRUNTYSSSHIP, TRANSSSFORMATION SSSOON BE COMPLETE...
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D1D8")
        intro_cutscene_text._replace_line("594553535320594F5552204752554E54", "GEE GEE EASSSY, AMAZZZING CHESSST AHEAD...")
        # 0xD1E0 - 5CAFE8
        # KLUNGO: BEAR AND BIRD FINISSSHED, GRUNTY WINSSS!
        # TOOTY: ýhHELP ýhME ýhBANJO, ýhI ýhFEEL ýhALL ýhFUNNY...ýl
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D1E0")
        intro_cutscene_text._replace_line("4245415220414E442042495244204649", "TRANSSSFORMATION ISSS SSSUCCESSSSFUL!")
        intro_cutscene_text._replace_line("FD6848454C5020FD684D4520FD684241", "ýhOH ýhNO! ýhTHERE'S ýhA ýhYUM-YUM ýhIN ýhHERE!ýl")
        # 0xD1E8 - 5CB058
        # GRUNTY: LOOK AT GRUNTY SHE'S A BEAUTY,
        # GRUNTY: I'M MUCH PRETTIER THAN TOOTY!
        # KLUNGO: OH YOU ARE MISSSTRESSS!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D1E8")
        intro_cutscene_text._replace_line("4C4F4F4B204154204752554E54592053", "NOW THAT I AM SO MUCH HOTTER,")
        intro_cutscene_text._replace_line("49274D204D5543482050524554544945", "I CAN SELL MY CAULDRON WATER!")
        intro_cutscene_text._replace_line("4F4820594F5520415245204D49535353", "YASSS MISSSTRESSS! SSSLAY!")
        # 0xD230 - 5CB2C8
        # MUMBO: GRUNTY NICE, COME BACK TO MUMBO'S SKULL, YES?
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D230")
        intro_cutscene_text._replace_line("4752554E5459204E4943452C20434F4D", "MOMMY? SORRY, MOMMY? SORRY, MOMMY?...")
        # 0xD200 - 5CB100
        # TOOTY: BANJO! YOUR SISTER WANTS A WORD WITH YOU.........
        # TOOTY: NOW!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D200")
        intro_cutscene_text._replace_line("42414E4A4F2120594F55522053495354", "BANJO! YOUR SISTER HAS TWO WORDS FOR YOU...")
        intro_cutscene_text._replace_line("4E4F5721", "GIT GUD!")

    ###############################
    ### BASE GAME PROGRESS TEXT ###
    ###############################
    
    def _bottles_opened_first_world(self, world_object):
        '''Edits text that appears when opening the first world'''
        # 0xDA88 - 5CC988
        # Bottles: THAT'S IT! THE PICTURE'S COMPLETE AND THE DOOR TO MUMBO'S MOUNTAIN IS OPEN!
        # Gruntilda: THAT WAS SUCH AN EASY FIT,
        # Gruntilda: THE OTHERS MAY JUST TEST YOUR WIT!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA88")
        if(isinstance(world_object, list)):
            intro_cutscene_text._replace_line("54484154275320495421205448452050", f"THAT'S IT! THE PICTURE'S COMPLETE AND THE DOOR TO CLICK CLOCK WOOD IS OPEN!")
        else:
            intro_cutscene_text._replace_line("54484154275320495421205448452050", f"THAT'S IT! THE PICTURE'S COMPLETE AND THE DOOR TO {(world_object._world_name).upper()} IS OPEN!")

    def _bottles_this_is_first_world(self):
        '''Edits text that appears when approaching the first world'''
        # 0xDA90 - 5CCA10
        # THIS IS THE FIRST WORLD, MUMBO'S MOUNTAIN. TO OPEN THE DOOR YOU'LL NEED TO FIND THE JIGSAW PICTURE WITH AN IMAGE OF THIS AREA ON IT. HAVE A LOOK AROUND, IT CAN'T BE FAR AWAY.
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA90")
        intro_cutscene_text._replace_line("54484953204953205448452046495253", f"IS THIS YOUR FIRST TIME PLAYING BANJO-KAZOOIE? GO GET A JIGGY, 4HEAD!")

    def _bottles_this_is_first_puzzle(self):
        '''Edits text that appears when approaching the first puzzle'''
        # 0xDA98 - 5CCAA8
        # THIS IS THE FIRST WORLD, MUMBO'S MOUNTAIN. COMPLETE THE JIGSAW PICTURE TO OPEN THE DOOR.
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA98")
        intro_cutscene_text._replace_line("54484953204953205448452046495253", f"IS IT REALLY MUMBO'S MOUNTAIN? MAYBE THE PICTURES SHOULD BE UPDATED...")

    def _bottles_50_notes(self):
        '''Edits text that appears when approaching the first world'''
        # 0xDA38 - 5CC5C8
        # YIPPEE! YOU'VE COLLECTED ENOUGH NOTES TO BREAK THE FIRST NOTE DOOR SPELL!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA38")
        intro_cutscene_text._replace_line("59495050454521", "REMEMBER TO STAY HYDRATED!")

    def _bottles_slippery_slope(self):
        '''Edits text that appears when sliding down a slope in Mumbo's Mountain'''
        # 0xB900 - 5C42F0
        # THINGS A BIT SLIPPY, HUH? FIND ME AND I'LL TEACH YOU HOW TO GET UP STEEP SLOPES!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "B900")
        intro_cutscene_text._replace_line("5448494E475320412042495420534C49", "LMAO CAUGHT YOU SLIPPIN' IN 4K!")
    
    def _bottles_enter_mm_moves(self):
        '''Edits text for learning moves in Mumbo's Mountain'''
        # 0xD9D8 - 5CC1B0
        # THERE ARE THREE NEW MOVES TO LEARN IN THIS WORLD. FIND MY MOLEHILLS AND I'LL EXPLAIN.
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D9D8")
        intro_cutscene_text._replace_line("544845524520415245", "BEAR AND BIRD FIND MOLE AND LEARN MOVES!")
    
    def _bottles_learned_mm_moves(self):
        '''Edits text after learning all MM moves'''
        # 0xB908 - 5C4350
        # WOAAA, BANJO! THERE'S NOTHING MORE I CAN TEACH YOU ON THIS WORLD!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "B908")
        intro_cutscene_text._replace_line("574f4141412c", "EEKUM BOKUM!")
    
    def _bottles_leaving_mm_without_moves(self):
        '''Edits text for leaving Mumbo's Mountain without learning moves'''
        # 0xDA08 - 5CC390
        # WAIT! YOU DIDN'T LEARN ALL THE NEW MOVES IN MUMBO'S MOUNTAIN! YOU WON'T GET FAR WITHOUT THEM...
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA08")
        intro_cutscene_text._replace_line("574149542120594F55204449444E2754", "WHAT'S THE MATTER? DON'T LIKE BACKTRACKING? GUESS YOU WON'T LIKE TOOIE...")
    
    def _bottles_enter_ttc_moves(self):
        '''Edits text for learning moves in TTC'''
        # 0xD9E0 - 5CC210
        # AHOY THERE! THIS BE TREASURE TROVE COVE. THAR BE TWO NEW MOVES FOR YE TO FIND.
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D9E0")
        intro_cutscene_text._replace_line("41484f5920544845524521", "REMEMBER CAP'N BLACKEYE? ME NEITHER!")
    
    def _bottles_learned_ttc_moves(self):
        '''Edits text after learning all TTC moves'''
        # 0xAFD0 - 5C2BC0
        # NICE GOING, YOU'VE LEARNED ALL THE COVE'S NEW MOVES!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "AFD0")
        intro_cutscene_text._replace_line("4e49434520474f494e47", "THE REAL LOOT BE THE SCALLYWAGS WE MADE ALONG THE WAY!")
    
    def _bottles_leaving_ttc_without_moves(self):
        '''Edits text for leaving TTC without learning moves'''
        # 0xDA10 - 5CC3F8
        # HEY! THERE'S AT LEAST ONE NEW MOVE YOU MISSED. THAT'S THE REAL TREASURE!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA10")
        intro_cutscene_text._replace_line("48455921205448455245275320415420", "THE CAMERAS GET FUNKY WHEN YOU LEARN A MOVE NOT FROM THAT LEVEL!")
    
    def _bottles_enter_cc_moves(self):
        '''Edits text for learning moves in CC'''
        # 0xD9E8 - 5CC268
        # JUST THE ONE NEW MOVE TO FIND THIS TIME, BUT IT'S HIDDEN WELL!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D9E8")
        intro_cutscene_text._replace_line("4a55535420544845", "WHAT IS CLANKER ANYWAY? A SHARK? A WHALE?")
    
    def _bottles_learned_cc_moves(self):
        '''Edits text after learning move in CC'''
        # 0xC850 - 5C7818
        # YOU'VE LEARNED ALL MY NEW MOVES FOR THIS WORLD, THE REST IS UP TO YOU!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "C850")
        intro_cutscene_text._replace_line("594f55275645", "IS ANYONE REALLY FREE WHEN CHAINED TO SOCIETY?")
    
    def _bottles_leaving_cc_without_moves(self):
        '''Edits text after leaving CC without learning moves'''
        # 0xDA18 - 5CC450
        # YOU DIDN'T SPLASH AROUND ENOUGH TO FIND THE NEW MOVE IN THERE, DID YOU?
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA18")
        intro_cutscene_text._replace_line("594F55204449444E27542053504C4153", "BABY SHARK DO DO DO DO DO DO!")
    
    def _bottles_enter_bgs_moves(self):
        '''Edits text for learning moves in BGS'''
        # 0xD9F0 - 5CC2B8
        # KEEP YOUR EYES OPEN FOR YOUR NEW MOVE, BEAK FACE!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D9F0")
        intro_cutscene_text._replace_line("4b45455020594f5552", "WHAT ARE YEW DOIN' IN MY SWAMP?!")
    
    def _bottles_learned_bgs_moves(self):
        '''Edits text after learning move in BGS'''
        # 0xC2E8 - 5C6358
        # GREAT, NOW YOU KNOW ALL THE SWAMP'S NEW MOVES!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "C2E8")
        intro_cutscene_text._replace_line("47524541542c", "IT SMELLS LIKE A VIDEO GAME CHAMPIONSHIP HERE...")
    
    def _bottles_leaving_bgs_without_moves(self):
        '''Edits text after leaving BGS without learning move'''
        # 0xDA20 - 5CC4A8
        # WADE BACK IN THERE AND FIND THAT NEW MOVE YOU JUST MISSED IF YOU WANT TO BEAT GRUNTY!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA20")
        intro_cutscene_text._replace_line("57414445204241434B20494E20544845", "THESE BOOTS ARE MADE FOR WALKIN, THAT'S JUST WHAT THEY'LL DO...")
    
    def _bottles_enter_fp_moves(self):
        '''Edits text for learning move in FP'''
        # 0xD9F8 - 5CC300
        # THE PEAK'S GOT ANOTHER NEW MOVE WAITING FOR YOU IF YOU CAN FIND IT!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D9F8")
        intro_cutscene_text._replace_line("544845205045414b", "WHAT'S THIS? DROPS OF RAIN FROZEN INTO ICE CRYSTALS? I SHALL HARNESS THEIR ENERGY AND RULE THE WORLD!")
    
    def _bottles_learned_fp_moves(self):
        '''Edits text after learning move in FP'''
        # 0xBFE8 - 5C5680
        # YOU'VE LEARNED ALL THE MOVES I CAN TEACH YOU ON THIS WORLD NOW!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "BFE8")
        intro_cutscene_text._replace_line("594f55275645", "HAPPY WALRUS NOISES!")
    
    def _bottles_leaving_fp_without_moves(self):
        '''Edits text after leaving FP without learning move'''
        # 0xDA28 - 5CC508
        # HOLD IT, BANJO, HADN'T YOU BETTER SLIDE BACK IN AND FIND THAT NEW MOVE?
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA28")
        intro_cutscene_text._replace_line("484F4C442049542C2042414E4A4F2C20", "CHRISTMAS IS OVER, TIME FOR VALENTINES DAY DECORATIONS!")
    
    def _bottles_enter_gv_moves(self):
        '''Edits text for learning move in GV'''
        # 0xDA00 - 5CC350
        # YOU'LL FIND ONE MORE MOVE IN HERE, BANJO.
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA00")
        intro_cutscene_text._replace_line("594f55274c4c", "I DON'T LIKE SAND. IT'S COARSE AND ROUGH AND IRRITATING AND IT GETS EVERYWHERE.")
    
    def _bottles_learned_gv_moves(self):
        '''Edits text after learning move in GV'''
        # 0xB2C8 - 5C33E8
        # WELL, I'M AFRAID THAT'S IT FOR NEW MOVES IN GOBI'S VALLEY.
        intro_cutscene_text = Speech_File_Class(self._file_dir, "B2C8")
        intro_cutscene_text._replace_line("57454c4c2c", "CHILI DOGS!")
    
    def _bottles_leaving_gv_without_moves(self):
        '''Edits text after leaving GV without learning move'''
        # 0xDA30 - 5CC560
        # DON'T DESERT THE VALLEY WITHOUT FINDING THE NEW MOVE! I'M SURE YOU'LL BE NEEDING IT LATER...
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA30")
        intro_cutscene_text._replace_line("444F4E27542044455345525420544845", "THERE ARE SOME REALLY COOL IMAGES ON THE WALLS IN THE MAZE!")
    
    def _bottles_this_is_a_mod(self):
        '''Unused'''
        # DID YOU GET ALL OF THE NEW MOVES? OH WAIT, THIS IS A MOD, I CAN'T REMEMBER HOW MANY MOVES THERE ARE IN EACH LEVEL...
        pass
    
    #####################
    ### INTRO BOTTLES ###
    #####################
    
    def _bottles_introduction_text(self):
        '''Edits Bottle's introduction text'''
        # 0xCE30 - 5C85D8
        # BOTTLES: LISTEN UP! I'M BOTTLES, THE SHORT-SIGHTED MOLE.
        # BOTTLES: SURE IS A STRANGE LOOKING BUDDY BANJO, CAN IT TALK?
        # BOTTLES: THE UGLY WITCH GRUNTILDA SWOOPED DOWN OUT OF THE SKY AND GRABBED HER!
        # BOTTLES: SHE FLEW UP TO HER MOUNTAIN LAIR!
        # BOTTLES: IT'S REALLY DANGEROUS, SO YOU'LL PROBABLY NEED SOME TRAINING BEFORE YOU GO UP THERE.
        # BANJO:   I'M BANJO, AND THIS HERE'S MY BUDDY KAZOOIE.
        # KAZOOIE: BETTER THAN YOU CAN, GOGGLE BOY!
        # BANJO:   WHAT WAS ALL THAT NOISE ABOUT, WHERE'S MY SISTER TOOTY?
        # KAZOOIE: CALM DOWN, GEEKY, WE'LL GET HER BACK! WHERE DID SHE GO?
#         bottles_intro_text._replace_line("4c495354454e20555021", "WELCOME TO THE BANJO-KAZOOIE RANDOMIZER V2! PRESS L R B TO SKIP THIS TEXT!")
        bottles_intro_text = Speech_File_Class(self._file_dir, "CE30")
        bottles_intro_text._replace_line("4c495354454e20555021", "WELCOME TO THE RANDO, PRESS LRB TO SKIP MY TEXT.")
        bottles_intro_text._replace_line("49274d2042414e4a4f2c", "NOT THIS TIME, BOTTLES.")
        bottles_intro_text._replace_line("535552452049532041", "HUH?")
        bottles_intro_text._replace_line("424554544552205448414e", "WE CARE ABOUT YOUR DUMB BUTT.")
        bottles_intro_text._replace_line("574841542057415320414c4c", "AND THAT'S COMING FROM LOUD-MOUTH KAZOOIE HAHA!")
        bottles_intro_text._replace_line("5448452055474c59205749544348", "AW MAN, THAT REALLY MEANS A LOT... SNIFFLES...")
        bottles_intro_text._replace_line("43414c4d20444f574e", "WE GOTCHU, FOUR-EYES.")
        bottles_intro_text._replace_line("53484520464c4557205550", "IT'S JUST HARD TO TALK ABOUT.")
        bottles_intro_text._replace_line("49542753205245414c4c59", "ANYWAY, BACK TO THE GAME...")
    
    def _modify_bottles_unskippable_text(self, final_note_option, final_note_score, final_puzzle_option, final_puzzle_score):
        '''Modifies the Bottles text at the beginning of the game'''
        # 0xCF90 - 5C9AF8
        # ORIGINAL:   "PRESS A IF YOU WANT ME TO TEACH YOU SOME BASIC MOVES, OR PRESS B IF YOU THINK YOU'RE ALREADY GOOD ENOUGH!"
        # BOTH:       "YOU'LL NEED 000 NOTES AND 99 JIGGIES TO REACH GRUNTY. PRESS A FOR THE TUTORIAL OR PRESS B TO GET GOING!"
        # NOTES:      "YOU'LL NEED 000 NOTES. JIGGY REQUIREMENT IS THE SAME AS BASE GAME. PRESS A FOR TUTORIAL OR B TO SKIP."
        # JIGGIES:    "YOU'LL NEED 00 JIGGIES. NOTES REQUIREMENT IS THE SAME AS BASE GAME. PRESS A FOR TUTORIAL OR B TO SKIP."
        # NO SHUFFLE: "YOU'LL NEED THE SAME NOTES AND JIGGY REQUIREMENTS AS BASE GAME. PRESS A FOR TUTORIAL OR B TO SKIP."
        if((final_note_option == "Final Note Door Only") and final_puzzle_option):
            new_bottles_text = f"YOU'LL NEED {final_note_score} NOTES AND {final_puzzle_score} JIGGIES TO REACH GRUNTY. PRESS A FOR TUTORIAL OR B TO SKIP."
        elif(final_note_option == "Final Note Door Only"):
            new_bottles_text = f"YOU'LL NEED {final_note_score} NOTES. JIGGY REQUIREMENT IS THE SAME AS BASE GAME. PRESS A FOR TUTORIAL OR B TO SKIP."
        elif(final_puzzle_option):
            new_bottles_text = f"YOU'LL NEED {final_puzzle_score} JIGGIES AND {final_note_score} NOTES. NOTE DOORS MAY SCALE. PRESS A FOR TUTORIAL OR B TO SKIP."
        else:
            new_bottles_text = "YOU'LL NEED THE SAME NUMBER OF JIGGIES AS BASE GAME, BUT NOTE DOORS MAY SCALE. PRESS A FOR TUTORIAL OR B TO SKIP."
        bottles_unskippable_text = Speech_File_Class(self._file_dir, "CF90")
        bottles_unskippable_text._replace_line("50524553532041", new_bottles_text)
    
    def _shorten_bottles_secret_game_text(self):
        '''Shotens Bottles secret game text to create room'''
        # 0xCF98 - 5C9B60
        # BOTTLES: OH...I'M AFRAID I CAN'T TELL YOU ANYMORE ABOUT THIS HIDDEN FEATURE UNTIL YOU COLLECT THE JIGSAW FROM THE SANDCASTLE GAME IN TREASURE TROVE COVE.
        # KAZOOIE: TELL US NOW, BARREL BOY!
        # BOTTLES: NO! ONLY WHEN YOU'VE GOT THE SANDCASTLE JIGSAW.
        # BANJO: C'MON KAZOOIE, LET'S COME BACK LATER...
        secret_game_text = Speech_File_Class(self._file_dir, "CF98")
        secret_game_text._replace_line("4f482e2e2e49274d", "GO COLLECT THE SANDCASTLE JIGGY FIRST.")
        secret_game_text._replace_line("4e4f21204f4e4c59", "JUST GET THE JIGGY FIRST, BIRD BRAIN!")
        secret_game_text._replace_line("43274d4f4e204b415a4f4f4945", "C'MON KAZOOIE, LET'S COME BACK LATER.")

    #############################
    ### FURNACE FUN QUESTIONS ###
    #############################
    
    def _furnace_fun_questions_main(self, empty=True):
        '''Edits the furnace fun questions; Unused'''
        if(empty):
            furnace_fun_json = read_json(f"{self._file_dir}Randomization_Processes/Misc_Manipulation/Speech_Data/Furnace_Fun_Empty.json")
        else:
            furnace_fun_json = read_json(f"{self._file_dir}Randomization_Processes/Misc_Manipulation/Speech_Data/Furnace_Fun_Custom.json")
        for pointer_index_str in furnace_fun_json:
            furnace_fun_text = Speech_File_Class(self._file_dir, pointer_index_str[2:])
            furnace_fun_text._furnace_fun_question_format(furnace_fun_json[pointer_index_str]["Question_Part_1"],
                                                          furnace_fun_json[pointer_index_str]["Question_Part_2"],
                                                          furnace_fun_json[pointer_index_str]["Answer_1"],
                                                          furnace_fun_json[pointer_index_str]["Answer_2"],
                                                          furnace_fun_json[pointer_index_str]["Answer_3"])
    
    ###############################
    ### GRUNTILDA LAIR SPEECHES ###
    ###############################
    
    ### RANDOM SPEECHES ###
    
    def _gruntilda_lair_speech_1(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDAC8 - 5CCCE0
        # GRUNTILDA: Your feathered buddy, that you've brung, useless like a pile of dung!
        grunty_text = Speech_File_Class(self._file_dir, "DAC8")
        grunty_text._replace_line("594F5552204645415448455245442042", message1)
        grunty_text._replace_line("5553454C455353204C494B4520412050", message2)
    
    def _gruntilda_lair_speech_2(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDAD0 - 5CCD38
        # GRUNTILDA: Hey Banjo, you're looking glum, it must be hard, being so dumb!
        grunty_text = Speech_File_Class(self._file_dir, "DAD0")
        grunty_text._replace_line("4845592042414E4A4F2C20594F552752", message1)
        grunty_text._replace_line("4954204D55535420424520484152442C", message2)
    
    def _gruntilda_lair_speech_3(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDAD8 - 5CCD90
        # GRUNTILDA: Many tricks are up my sleeve, to save yourself you'd better leave!
        grunty_text = Speech_File_Class(self._file_dir, "DAD8")
        grunty_text._replace_line("4D414E5920545249434B532041524520", message1)
        grunty_text._replace_line("544F205341564520594F555253454C46", message2)
    
    def _gruntilda_lair_speech_4(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDAE0 - 5CCDE8
        # GRUNTILDA: I can see it's quite hard work, to lump around that squawking jerk!
        grunty_text = Speech_File_Class(self._file_dir, "DAE0")
        grunty_text._replace_line("492043414E2053454520495427532051", message1)
        grunty_text._replace_line("544F204C554D502041524F554E442054", message2)
    
    def _gruntilda_lair_speech_5(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDAE8 - 5CCE40
        # GRUNTILDA: How bright they are, your stupid shorts, a target for my dumb cohorts!
        grunty_text = Speech_File_Class(self._file_dir, "DAE8")
        grunty_text._replace_line("484F5720425249474854205448455920", message1)
        grunty_text._replace_line("412054415247455420464F52204D5920", message2)
    
    def _gruntilda_lair_speech_6(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDAF0 - 5CCE98
        # GRUNTILDA: Join me now and dump the bear, that little backpack then I'll wear!
        grunty_text = Speech_File_Class(self._file_dir, "DAF0")
        grunty_text._replace_line("4A4F494E204D45204E4F5720414E4420", message1)
        grunty_text._replace_line("54484154204C4954544C45204241434B", message2)
    
    def _gruntilda_lair_speech_7(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDAF8 - 5CCEF0
        # GRUNTILDA: That ugly bear, you feathered freak, is nothing but a stupid geek!
        grunty_text = Speech_File_Class(self._file_dir, "DAF8")
        grunty_text._replace_line("544841542055474C5920424541522059", message1)
        grunty_text._replace_line("4953204E4F5448494E47204255542041", message2)
    
    def _gruntilda_lair_speech_8(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB00 - 5CCF48
        # GRUNTILDA: It really does sound quite absurd, adventure of a bear and bird!
        grunty_text = Speech_File_Class(self._file_dir, "DB00")
        grunty_text._replace_line("4954205245414C4C5920444F45532053", message1)
        grunty_text._replace_line("414456454E54555245204F4620412042", message2)
    
    def _gruntilda_lair_speech_9(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB08 - 5CCFA0
        # GRUNTILDA: You side with Banjo but change tack, imagine you on Grunty's back!
        grunty_text = Speech_File_Class(self._file_dir, "DB08")
        grunty_text._replace_line("594F5520534944452057495448204241", message1)
        grunty_text._replace_line("494D4147494E4520594F55204F4E2047", message2)
    
    def _gruntilda_lair_speech_10(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB10 - 5CCFF8
        # GRUNTILDA: I'm still here, I watch you play, but I can't think of much to say!
        grunty_text = Speech_File_Class(self._file_dir, "DB10")
        grunty_text._replace_line("49274D205354494C4C20484552452C20", message1)
        grunty_text._replace_line("42555420492043414E2754205448494E", message2)
    
    def _gruntilda_lair_speech_11(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB18 - 5CD050
        # GRUNTILDA: When the back of Grunty's hand, whups your butt you'll hardly stand!
        grunty_text = Speech_File_Class(self._file_dir, "DB18")
        grunty_text._replace_line("5748454E20544845204241434B204F46", message1)
        grunty_text._replace_line("574855505320594F5552204255545420", message2)
    
    def _gruntilda_lair_speech_12(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB20 - 5CD0A8
        # GRUNTILDA: Your butt will tell you and you'll know, when my boot swings to and fro!
        grunty_text = Speech_File_Class(self._file_dir, "DB20")
        grunty_text._replace_line("594F555220425554542057494C4C2054", message1)
        grunty_text._replace_line("5748454E204D5920424F4F5420535749", message2)
    
    def _gruntilda_lair_speech_13(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB28 - 5CD100
        # GRUNTILDA: Monsters chase you, they're a hounding, then you'll get a Grunty pounding!
        grunty_text = Speech_File_Class(self._file_dir, "DB28")
        grunty_text._replace_line("4D4F4E53544552532043484153452059", message1)
        grunty_text._replace_line("5448454E20594F55274C4C2047455420", message2)
    
    def _gruntilda_lair_speech_14(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB30 - 5CD158
        # GRUNTILDA: Long of tooth and strong of arm, Grunty's got the lasting charm!
        grunty_text = Speech_File_Class(self._file_dir, "DB30")
        grunty_text._replace_line("4C4F4E47204F4620544F4F544820414E", message1)
        grunty_text._replace_line("4752554E5459275320474F5420544845", message2)
    
    def _gruntilda_lair_speech_15(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB38 - 5CD1A8
        # GRUNTILDA: If you think I'm rather soft, I'll be waiting in the loft!
        grunty_text = Speech_File_Class(self._file_dir, "DB38")
        grunty_text._replace_line("494620594F55205448494E4B2049274D", message1)
        grunty_text._replace_line("49274C4C2042452057414954494E4720", message2)
    
    def _gruntilda_lair_speech_16(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB40 - 5CD1F8
        # GRUNTILDA: Can't you get here any faster? Come and fight me, I'm the master!
        grunty_text = Speech_File_Class(self._file_dir, "DB40")
        grunty_text._replace_line("43414E275420594F5520474554204845", message1)
        grunty_text._replace_line("434F4D4520414E44204649474854204D", message2)
    
    def _gruntilda_lair_speech_17(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB48 - 5CD248
        # GRUNTILDA: Why do I talk all the time, it's really hard to make these rhyme!
        grunty_text = Speech_File_Class(self._file_dir, "DB48")
        grunty_text._replace_line("57485920444F20492054414C4B20414C", message1)
        grunty_text._replace_line("49542753205245414C4C592048415244", message2)
    
    def _gruntilda_lair_speech_18(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB50 - 5CD2A0
        # GRUNTILDA: I don't like stairs much in my lair, they always make me gasp for air!
        grunty_text = Speech_File_Class(self._file_dir, "DB50")
        grunty_text._replace_line("4920444F4E2754204C494B4520535441", message1)
        grunty_text._replace_line("5448455920414C57415953204D414B45", message2)
    
    def _gruntilda_lair_speech_19(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB58 - 5CD2F8
        # GRUNTILDA: My filthy bed gives me a rash, I never wash, I save my cash!
        grunty_text = Speech_File_Class(self._file_dir, "DB58")
        grunty_text._replace_line("4D592046494C54485920424544204749", message1)
        grunty_text._replace_line("49204E4556455220574153482C204920", message2)
    
    def _gruntilda_lair_speech_20(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB60 - 5CD348
        # GRUNTILDA: My belly's big, it's rather neat, it's years since I have seen my feet!
        grunty_text = Speech_File_Class(self._file_dir, "DB60")
        grunty_text._replace_line("4D592042454C4C592753204249472C20", message1)
        grunty_text._replace_line("495427532059454152532053494E4345", message2)
    
    def _gruntilda_lair_speech_21(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB68 - 5CD3A0
        # GRUNTILDA: I've learned this spell, it's really neat, I'll keep it later for your treat!
        grunty_text = Speech_File_Class(self._file_dir, "DB68")
        grunty_text._replace_line("49275645204C4541524E454420544849", message1)
        grunty_text._replace_line("49274C4C204B454550204954204C4154", message2)
    
    def _gruntilda_lair_speech_22(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB70 - 5CD400
        # GRUNTILDA: Grunty admits she's a hog, I really need a big hot dog!
        grunty_text = Speech_File_Class(self._file_dir, "DB70")
        grunty_text._replace_line("4752554E54592041444D495453205348", message1)
        grunty_text._replace_line("49205245414C4C59204E454544204120", message2)
    
    def _gruntilda_lair_speech_23(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB78 - 5CD450
        # GRUNTILDA: This stupid quest you should stop, you won't get to me at the top!
        grunty_text = Speech_File_Class(self._file_dir, "DB78")
        grunty_text._replace_line("54484953205354555049442051554553", message1)
        grunty_text._replace_line("594F5520574F4E27542047455420544F", message2)
    
    def _gruntilda_lair_speech_24(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB80 - 5CD4A0
        # GRUNTILDA: My next world is the hardest yet, and you will fail, on that I'll bet!
        grunty_text = Speech_File_Class(self._file_dir, "DB80")
        grunty_text._replace_line("4D59204E45585420574F524C44204953", message1)
        grunty_text._replace_line("414E4420594F552057494C4C20464149", message2)
    
    def _gruntilda_lair_speech_25(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB88 - 5CD4F8
        # GRUNTILDA: Tooty's fate is looking grim, it's because her brother's dim!
        grunty_text = Speech_File_Class(self._file_dir, "DB88")
        grunty_text._replace_line("544F4F54592753204641544520495320", message1)
        grunty_text._replace_line("49542753204245434155534520484552", message2)
    
    def _gruntilda_lair_speech_26(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB90 - 5CD548
        # GRUNTILDA: I've got this skirt so when I'm thinner, it really makes me look a winner!
        grunty_text = Speech_File_Class(self._file_dir, "DB90")
        grunty_text._replace_line("4927564520474F54205448495320534B", message1)
        grunty_text._replace_line("4954205245414C4C59204D414B455320", message2)
    
    def _gruntilda_lair_speech_27(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDB98 - 5CD5A0
        # GRUNTILDA: When Tooty is a big ole lump, I've got just the frock to hide her rump!
        grunty_text = Speech_File_Class(self._file_dir, "DB98")
        grunty_text._replace_line("5748454E20544F4F5459204953204120", message1)
        grunty_text._replace_line("49275645204A55535420544845204652", message2)
    
    def _gruntilda_lair_speech_28(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDBA0 - 5CD5F8
        # GRUNTILDA: Grunty's stomach and leg thins, goodbye to all those double chins!
        grunty_text = Speech_File_Class(self._file_dir, "DBA0")
        grunty_text._replace_line("4752554E54592753204C45475320414E", message1)
        grunty_text._replace_line("474F4F4442594520544F20414C4C2054", message2)
    
    def _gruntilda_lair_speech_29(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDBA8 - 5CD650
        # GRUNTILDA: When I'm nice and thin once more, burgers, fries, and chips galore!
        grunty_text = Speech_File_Class(self._file_dir, "DBA8")
        grunty_text._replace_line("5748454E2049274D204E49434520414E", message1)
        grunty_text._replace_line("425552474552532C2046524945532041", message2)
    
    def _gruntilda_lair_speech_30(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDBB0 - 5CD6A8
        # GRUNTILDA: Tooty says she's fine with me, if you go home I'll set her free!
        grunty_text = Speech_File_Class(self._file_dir, "DBB0")
        grunty_text._replace_line("544F4F54592053415953205348452753", message1)
        grunty_text._replace_line("494620594F5520474F20484F4D452049", message2)
    
    def _gruntilda_lair_speech_31(self, message1, message2):
        '''Edits one of gruntilda's lair speeches with an easter egg'''
        # 0xDBB8 - 5CD6F8
        # GRUNTILDA: Grunty's plan is rather cunning, when I'm thin, guys will be running!
        grunty_text = Speech_File_Class(self._file_dir, "DBB8")
        grunty_text._replace_line("4752554E5459275320504C414E204953", message1)
        grunty_text._replace_line("5748454E2049274D205448494E204755", message2)
    
    ### FIXED SPEECHES ###
    
    def _gruntilda_lair_speech_32(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: There he is, the fun begins, my tricks and traps will see who wins!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "THERE HE IS, THE FUN BEGINS, WITH THESE SETTINGS LET'S SEE WHO WINS!")
    
    def _gruntilda_lair_speech_33(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: That was such an easy fit, the others may just test your wit!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_34(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: You've found some notes but you need more, to break my spell and pass this door!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "YOU GOT SOME NOTES, THOUGHT YOU WERE STOCKED, BUT UNTIL THEN, GET SOFTLOCKED!")
    
    def _gruntilda_lair_speech_35(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: That door was easy you got past, unfortunately your first and last!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_36(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: When you open a world door, baddies escape and roam once more!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "WORLDS ARE NOT THE ONLY CHANGE, IN MY LAIR, THINGS GET STRANGE!")
    
    def _gruntilda_lair_speech_37(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Hey, book brain, what did you say? You'd better not give my spells away!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_38(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: If one more page I see you turn, then Grunty shall make Cheato burn!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_39(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: That traitor book has pushed its luck, so in the burning fire I'll chuck!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_40(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: It's not over stupid bear, see my picture over there!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_41(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: To fill it up is no mean feat, lots of Jiggies make it complete!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "GET ONE LAST LOOK AT MY PIC! IN A MOMENT, I WILL LOOK SLICK!")
    
    def _gruntilda_lair_speech_42(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Pieces that you've left behind, to battle me you must go find!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_43(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Don't be sure you silly pot, soon I'll have you nice and hot!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_44(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: See these filthy clothes I've got, when I've won you'll wash the lot!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_45(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Grunty's fate this should not be, so hurry, Klungo, rescue me!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_46(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Stop using cheats in my tower, you are getting all the power.
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_47(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Now I will erase your Game Pak, because you had the need to hack!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_48(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: That golden treasure was for me, now harder still the game will be!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_49(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: That lousy cheat for extra eggs, won't help bear and chicken legs!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_50(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: All my feathers, it makes me sick, fly to me, your butt I'll kick!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_51(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Golden Feathers you may have twenty, but bruises you'll still get plenty!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_52(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Stop this cheating Grunty says, or your Game Pak I'll erase!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_53(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: You didn't listen, I'm amazed, so now your Game Pak is erased!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_54(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: First you see it, now you don't, the fast one wins, the slow one won't!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_55(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: I'll be young and Tooty old, before you get Gruntilda's gold!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_56(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Grunty's race you cannot beat, until you find some faster feet!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_57(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Oh, those lovely thorns, how they've grown, music to my ears as you moan!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_58(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: I can't believe you went in there, wash your hands now, filthy bear!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_59(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: These two guests are rather dumb, let's make sure they're unwelcome!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_60(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Yes I'm mad, my boot I'll put, up your useless spooky butt!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_61(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Big oak door is very tough, stupid bear's not fast enough!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_62(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: My oily water, in you plunge, you'll lose air while in that gunge!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_63(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Under the scum you'll breathe your last, 'cuz air is used twice as fast!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_64(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Stupid bear, you'll have to learn, that red hot ovens tend to burn!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_65(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: A simple task you were sure, but Grunty's engines start once more!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_66(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: My bramble field makes you yelp, and loss of life it sure does help!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_67(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: You'll use your air up double fold, I've made this water double cold!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_68(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: Yes that's right, swim under there, icy water takes double air!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_69(self):
        '''Unused'''
        # 0x0000 - 000000
        # GRUNTILDA: What's wrong Banjo, is it tough? Let me know when you've had enough!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _gruntilda_lair_speech_70(self):
        '''Unused'''
        # 0xDBF8 - 5CDC40
        # GRUNTILDA: I'm sad to say down there you'll stop, 'cuz I'm safe here at the top!
        grunty_text = Speech_File_Class(self._file_dir, "")
        grunty_text._replace_line("", "")
    
    def _bk_first_death_gruntilda(self):
        '''Unused'''
        # 0xDAA0 - 5CCB08
        # Gruntilda: WHAT'S WRONG BANJO, IS IT TOUGH?
        #            TRYING TO GET THE GAME OVER SCREEN?
        # Gruntilda: LET ME KNOW WHEN YOU'VE HAD ENOUGH!
        #            YOU ARE LIKE A PERVERTED TEEN!
        grunty_text = Speech_File_Class(self._file_dir, "DAA0")
        grunty_text._replace_line("5748415427532057524F4E472042414E", "TRYING TO GET THE GAME OVER SCREEN?!")
        grunty_text._replace_line("4C4554204D45204B4E4F57205748454E", "YOU ARE LIKE A PERVERTED TEEN!")
    
    ##################
    ### SANDCASTLE ###
    ##################
    
    def _raised_maximum_blue_eggs_speech(self):
        '''Shortens text for cheato blue eggs'''
        # 0xDBD8 - 5CDA58
        # Cheato: 200 EGGS ARE NOW YOURS! NOW 200 IS MAXIMUM TOO!
        # Grunty: THAT LOUSY CHEAT FOR EXTRA EGGS,
        # Grunty: WON'T HELP BEAR AND CHICKEN LEGS!
        grunty_text = Speech_File_Class(self._file_dir, "DBD8")
        grunty_text._replace_line("323030204547475320415245204E4F57", "YOU CAN NOW CARRY MORE EGGS!")
    
    def _raised_maximum_red_feathers_speech(self):
        '''Shortens text for cheato red feathers'''
        # 0xDBE0 - 5CDAD0
        # Cheato: BEAR AND BIRD GET 100 RED FEATHERS. 100 MAXIMUM NOW IS!
        # Grunty: ALL MY FEATHERS, IT MAKES ME SICK,
        # Grunty: FLY TO ME, YOUR BUTT I'LL KICK!
        grunty_text = Speech_File_Class(self._file_dir, "DBE0")
        grunty_text._replace_line("4245415220414E442042495244204745", "YOU CAN NOW CARRY MORE RED FEATHERS!")
    
    def _raised_maximum_gold_feathers_speech(self):
        '''Shortens text for cheato gold feathers'''
        # 0xDBE8 - 5CDB50
        # Cheato: 20 GOLD FEATHERS YOU GET! NEW MAXIMUM 20 IS!
        # Grunty: GOLD FEATHERS YOU MAY HAVE TWENTY,
        # Grunty: BUT BRUISES YOU'LL STILL GET PLENTY!
        grunty_text = Speech_File_Class(self._file_dir, "DBE8")
        grunty_text._replace_line("323020474F4C44204645415448455253", "YOU CAN NOW CARRY MORE GOLD FEATHERS!")
    
    #####################
    ### MISCELLANEOUS ###
    #####################
    
    def _copyright_info(self):
        '''Unused'''
        # 0xECD8 - 5D3100
        # COPYRIGHT 1998
        # NINTENDO-RARE LTD
        # GAME BY RARE TM
        # PRODUCED BY RARE
        # PRESENTED BY NINTENDO
        pass
