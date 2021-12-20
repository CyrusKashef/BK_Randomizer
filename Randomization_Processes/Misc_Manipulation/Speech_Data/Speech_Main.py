'''
Created on Oct 29, 2021

@author: Cyrus
'''

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
    def __init__(self, grandmaster, seed_val):
        self._grandmaster = grandmaster
        self._file_dir = grandmaster.cwd
        self._seed_val = seed_val
        self._spawned_count = {
            "Mumbo's Mountain": {
                "Notes": 5,
                "Jiggies": 6,
                "Empty Honeycombs": 0,
                },
            "Treasure Trove Cove": {
                "Notes": 0,
                "Jiggies": 4,
                "Empty Honeycombs": 0,
                },
            "Clanker's Cavern": {
                "Notes": 0,
                "Jiggies": 5,
                "Empty Honeycombs": 0,
                },
            "Bubblegloop Swamp": {
                "Notes": 5,
                "Jiggies": 10,
                "Empty Honeycombs": 0,
                },
            "Freezeezy Peak": {
                "Notes": 0,
                "Jiggies": 9,
                "Empty Honeycombs": 0,
                },
            "Gobi's Valley": {
                "Notes": 0,
                "Jiggies": 7,
                "Empty Honeycombs": 2,
                },
            "Mad Monster Mansion": {
                "Notes": 0,
                "Jiggies": 3,
                "Empty Honeycombs": 0,
                },
            "Rusty Bucket Bay": {
                "Notes": 0,
                "Jiggies": 3,
                "Empty Honeycombs": 1,
                },
            "Click Clock Wood": {
                "Notes": 0,
                "Jiggies": 4,
                "Empty Honeycombs": 0,
                },
            "Gruntilda's Lair": {
                "Notes": 0,
                "Jiggies": 6,
                "Empty Honeycombs": 0,
                },
            "Spiral Mountain": {
                "Notes": 0,
                "Jiggies": 0,
                "Empty Honeycombs": 2,
                },
        }

    #################
    ### BRENTILDA ###
    #################
    
    def _brentilda_intro(self):
        '''PyDoc'''
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
        if(object_name == "Bottles"):
            count = 0
            for world_object in world_object_list:
                for setup_file in world_object._setup_list:
                    for bottles_search in bottles_moves_camera_dict:
                        if(setup_file._does_string_exist(bottles_search)):
                            count += 1  
            return count
        elif(object_name == "Note"):
            count = 0
            for world_object in world_object_list:
                for setup_file in world_object._setup_list:
                    count += setup_file.note_count
            return count
        elif(object_name == "Flagged"):
            jiggy_count = 0
            honeycomb_count = 0
            for world_object in world_object_list:
                for setup_file in world_object._setup_list:
                    jiggy_count += setup_file.jiggy_counts
                    honeycomb_count += setup_file.empty_honeycomb_count
            return jiggy_count, honeycomb_count

    def _item_count(self, world_object, object_name):
        if(isinstance(world_object, list)):
            return self._click_clock_wood_item_count(world_object, object_name)
        if(object_name == "Bottles"):
            count = 0
            for setup_file in world_object._setup_list:
                for bottles_search in bottles_moves_camera_dict:
                    if(setup_file._does_string_exist(bottles_search)):
                        count += 1
            return count
        elif(object_name == "Note"):
            if(self._grandmaster.struct_var.get() == "None"):
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
            if(self._grandmaster.flagged_object_var.get() == "None"):
                if(world_object._world_name == "Spiral Mountain"):
                    return 0, 6
                elif(world_object._world_name == "Gruntilda's Lair"):
                    return 10, 0
                return 10, 2
            else:
                jiggy_count = 0
                honeycomb_count = 0
                for setup_file in world_object._setup_list:
                    jiggy_count += setup_file.jiggy_counts
                    honeycomb_count += setup_file.empty_honeycomb_count
                jiggy_count += self._spawned_count[world_object._world_name]["Jiggies"]
                honeycomb_count += self._spawned_count[world_object._world_name]["Empty Honeycombs"]
                return jiggy_count, honeycomb_count

    def _brentilda_1_1(self, world_object):
        '''PyDoc'''
        # 0xE2B0 - 5CF130
        # GRUNTY BRUSHES HER ROTTEN TEETH WITH ~ FLAVORED TOOTHPASTE!
        new_move_count = self._item_count(world_object, "Bottles")
        brentilda_text = Speech_File_Class(self._file_dir, "E2B0")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("4752554e5459", f"CLICK CLOCK WOOD HAS {new_move_count} NEW MOVES! ~")
        else:
            brentilda_text._replace_line("4752554e5459", f"{(world_object._world_name).upper()} HAS {new_move_count} NEW MOVES! ~")
    
    def _brentilda_1_2(self, world_object):
        '''PyDoc'''
        # 0xE2B8 - 5CF1A0
        # SHE ALSO WASHES HER HAIR WITH ~. YUK!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E2B8")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("53484520414c534f", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("53484520414c534f", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_1_3(self, world_object):
        '''PyDoc'''
        # 0xE2C0 - 5CF200
        # AND SHE GETS HER CLOTHES FROM ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E2C0")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("414e4420534845", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("414e4420534845", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_2_1(self, world_object):
        '''PyDoc'''
        # 0xE2C8 - 5CF270
        # UGLY GRUNTY'S NICKNAME WAS ~ AT WITCH SCHOOL!
        new_move_count = self._item_count(world_object, "Bottles")
        brentilda_text = Speech_File_Class(self._file_dir, "E2C8")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("55474c59204752554e5459", f"CLICK CLOCK WOOD HAS {new_move_count} NEW MOVES! ~")
        else:
            brentilda_text._replace_line("55474c59204752554e5459", f"{(world_object._world_name).upper()} HAS {new_move_count} NEW MOVES! ~")
    
    def _brentilda_2_2(self, world_object):
        '''PyDoc'''
        # 0xE2D0 - 5CF2D8
        # I ALSO KNOW THAT ~ IS HER FAVORITE SMELL!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E2D0")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("4920414c534f", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("4920414c534f", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_2_3(self, world_object):
        '''PyDoc'''
        # 0xE2D8 - 5CF348
        # AND THE OLD HAG'S FAVORITE COLOR IS ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E2D8")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("414e4420544845", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("414e4420544845", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_3_1(self, world_object):
        '''PyDoc'''
        # 0xE388 - 5CFD48
        # GRUNTY WEARS ~ UNDER THAT REPULSIVE DRESS OF HERS!
        new_move_count = self._item_count(world_object, "Bottles")
        brentilda_text = Speech_File_Class(self._file_dir, "E388")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("4752554e5459205745415253", f"CLICK CLOCK WOOD HAS {new_move_count} NEW MOVES! ~")
        else:
            brentilda_text._replace_line("4752554e5459205745415253", f"{(world_object._world_name).upper()} HAS {new_move_count} NEW MOVES! ~")
    
    def _brentilda_3_2(self, world_object):
        '''PyDoc'''
        # 0xE390 - 5CFDC0
        # SHE'S ALSO GOT THIS NASTY PET DOG WHOSE NAME IS ~!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E390")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("534845275320414c534f", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("534845275320414c534f", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_3_3(self, world_object):
        '''PyDoc'''
        # 0xE398 - 5CFE20
        # MY SISTER SINGS IN HER OWN BAND, ~. THEY'RE AWFUL!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E398")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("4d5920534953544552", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("4d5920534953544552", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_4_1(self, world_object):
        '''PyDoc'''
        # 0xE340 - 5CF910
        # MY LAZY SISTER OFTEN SLEEPS ~, THE DIRTY HAG!
        new_move_count = self._item_count(world_object, "Bottles")
        brentilda_text = Speech_File_Class(self._file_dir, "E340")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("4d59204c415a59", f"CLICK CLOCK WOOD HAS {new_move_count} NEW MOVES! ~")
        else:
            brentilda_text._replace_line("4d59204c415a59", f"{(world_object._world_name).upper()} HAS {new_move_count} NEW MOVES! ~")
    
    def _brentilda_4_2(self, world_object):
        '''PyDoc'''
        # 0xE348 - 5CF980
        # THE ONLY THING SHE'S EVER WON WAS THE ~ COMPETITION AT WITCH SCHOOL!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E348")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("544845204f4e4c59205448494e47", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("544845204f4e4c59205448494e47", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_4_3(self, world_object):
        '''PyDoc'''
        # 0xE350 - 5CF9F8
        # SHE OFTEN BOASTS OF APPEARING ON THE COVER OF FAT HAG MONTHLY, ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E350")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("534845204f4654454e20424f41535453", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("534845204f4654454e20424f41535453", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_5_1(self, world_object):
        '''PyDoc'''
        # 0xE2E0 - 5CF3B0
        # MY FAT OLD SISTER'S FAVORITE SPORT IS ~!
        new_move_count = self._item_count(world_object, "Bottles")
        brentilda_text = Speech_File_Class(self._file_dir, "E2E0")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("4d5920464154", f"CLICK CLOCK WOOD HAS {new_move_count} NEW MOVES! ~")
        else:
            brentilda_text._replace_line("4d5920464154", f"{(world_object._world_name).upper()} HAS {new_move_count} NEW MOVES! ~")
    
    def _brentilda_5_2(self, world_object):
        '''PyDoc'''
        # 0xE2E8 - 5CF420
        # ALTHOUGH SHE'S DIM, SHE ATTENDED ~!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E2E8")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("414c54484f554748", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("414c54484f554748", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_5_3(self, world_object):
        '''PyDoc'''
        # 0xE2F0 - 5CF490
        # YOU WON'T BELIEVE THAT GRUNTILDA'S PARTY TRICK IS ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E2F0")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("594f5520574f4e2754", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            print(f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
            brentilda_text._replace_line("594f5520574f4e2754", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_6_1(self, world_object):
        '''PyDoc'''
        # 0xE328 - 5CF7C8
        # GRUNTY'S BEST FRIEND AT WITCH SCHOOL WAS THE AWFUL ~!
        new_move_count = self._item_count(world_object, "Bottles")
        brentilda_text = Speech_File_Class(self._file_dir, "E328")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("4752554e54592753", f"CLICK CLOCK WOOD HAS {new_move_count} NEW MOVES! ~")
        else:
            brentilda_text._replace_line("4752554e54592753", f"{(world_object._world_name).upper()} HAS {new_move_count} NEW MOVES! ~")
    
    def _brentilda_6_2(self, world_object):
        '''PyDoc'''
        # 0xE330 - 5CF830
        # WHEN RELAXING, SHE USUALLY READS ~ MAGAZINE!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E330")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5748454e2052454c4158494e47", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("5748454e2052454c4158494e47", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_6_3(self, world_object):
        '''PyDoc'''
        # 0xE338 - 5CF8A0
        # WHILE SIPPING A GLASS OF HER FAVORITE ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E338")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5748494c452053495050494e47", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("5748494c452053495050494e47", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_7_1(self, world_object):
        '''PyDoc'''
        # 0xE2F8 - 5CF520
        # THE DISGUSTING GRUNTILDA HAS ~ FOR BREAKFAST!
        new_move_count = self._item_count(world_object, "Bottles")
        brentilda_text = Speech_File_Class(self._file_dir, "E2F8")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5448452044495347555354494e47", f"CLICK CLOCK WOOD HAS {new_move_count} NEW MOVES! ~")
        else:
            print(f"{(world_object._world_name).upper()} HAS {new_move_count} NEW MOVES! ~")
            brentilda_text._replace_line("5448452044495347555354494e47", f"{(world_object._world_name).upper()} HAS {new_move_count} NEW MOVES! ~")
    
    def _brentilda_7_2(self, world_object):
        '''PyDoc'''
        # 0xE300 - 5CF590
        # THEN SHE USUALLY HAS ~ FOR DINNER. YUK!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E300")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5448454e20534845", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("5448454e20534845", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_7_3(self, world_object):
        '''PyDoc'''
        # 0xE308 - 5CF5F8
        # WARTBAGS THEN FINISHES WITH ~ FOR DESSERT. HOW HORRID!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E308")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5741525442414753", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("5741525442414753", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_8_1(self, world_object):
        '''PyDoc'''
        # 0xE310 - 5CF670
        # REVOLTING GRUNTILDA'S BEDROOM HAS ~ HANGING FROM THE CEILING!
        new_move_count = self._item_count(world_object, "Bottles")
        brentilda_text = Speech_File_Class(self._file_dir, "E310")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5245564f4c54494e47", f"CLICK CLOCK WOOD HAS {new_move_count} NEW MOVES! ~")
        else:
            brentilda_text._replace_line("5245564f4c54494e47", f"{(world_object._world_name).upper()} HAS {new_move_count} NEW MOVES! ~")
    
    def _brentilda_8_2(self, world_object):
        '''PyDoc'''
        # E318 - 5CF6E0
        # SHE ALSO HAS ~ GROWING IN A POT BESIDE HER BED! FILTHY OLD BAG!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E318")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("53484520414c534f", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("53484520414c534f", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_8_3(self, world_object):
        '''PyDoc'''
        # 0xE320 - 5CF758
        # AND YOU'D BE SICK IF YOU SAW HER ENORMOUS ~ UNDIES!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E320")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("414e4420594f552744", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("414e4420594f552744", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_9_1(self, world_object):
        '''PyDoc'''
        # 0xE370 - 5CFBD8
        # DID YOU KNOW WARTBAGS KEEPS ~ IN HER POCKET FOR LUCK?
        new_move_count = self._item_count(world_object, "Bottles")
        brentilda_text = Speech_File_Class(self._file_dir, "E370")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("44494420594f55", f"CLICK CLOCK WOOD HAS {new_move_count} NEW MOVES! ~")
        else:
            brentilda_text._replace_line("44494420594f55", f"{(world_object._world_name).upper()} HAS {new_move_count} NEW MOVES! ~")
    
    def _brentilda_9_2(self, world_object):
        '''PyDoc'''
        # 0xE378 - 5CFC50
        # I'VE ALSO SEEN MY SISTER CUDDLING ~ IN BED AT NIGHT!
        note_count = self._item_count(world_object, "Note")
        brentilda_text = Speech_File_Class(self._file_dir, "E378")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("4927564520414c534f", f"CLICK CLOCK WOOD HAS {note_count} NOTES! ~")
        else:
            brentilda_text._replace_line("4927564520414c534f", f"{(world_object._world_name).upper()} HAS {note_count} NOTES! ~")
    
    def _brentilda_9_3(self, world_object):
        '''PyDoc'''
        # 0xE380 - 5CFCC8
        # SHE'S REALLY PROUD OF HER BROOMSTICK. IT'S A TOP OF THE RANGE ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E380")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5348452753205245414c4c59", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("5348452753205245414c4c59", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_10_1(self, world_object):
        '''PyDoc'''
        # 0xE358 - 5CFA80
        # GRUESOME GRUNTILDA'S FAVORITE PASTIME IS ~!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E358")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("47525545534f4d45", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("47525545534f4d45", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_10_2(self, world_object):
        '''PyDoc'''
        # 0xE360 - 5CFAF8
        # THIS POOR GUY CALLED ~, WAS HER FIRST AND ONLY BOYFRIEND!
        jiggy_count, honeycomb_count = self._item_count(world_object, "Flagged")
        brentilda_text = Speech_File_Class(self._file_dir, "E360")
        if(isinstance(world_object, list)):
            brentilda_text._replace_line("5448495320504f4f5220475559", f"CLICK CLOCK WOOD HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
        else:
            brentilda_text._replace_line("5448495320504f4f5220475559", f"{(world_object._world_name).upper()} HAS {jiggy_count} JIGGIES AND {honeycomb_count} EMPTY HONEYCOMBS! ~")
    
    def _brentilda_10_3(self):
        '''PyDoc'''
        # 0xE368 - 5CFB68
        # WHEN SHE WAS YOUNGER, GRUNTY USED TO HAVE ~ AS A PET!
        brentilda_text = Speech_File_Class(self._file_dir, "E368")
        brentilda_text._replace_line("5748454e2053484520574153", f"CHECK UP ON YOUR FRIENDS, BEFORE YOU MISS YOUR CHANCE... ~")
    
    ######################
    ### INTRO CUTSCENE ###
    ######################
    
    def _intro_cutscene_1(self):
        '''PyDoc'''
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
        '''PyDoc'''
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
        '''PyDoc'''
        # 0xD160 - 5CAA88
        # GRUNTILDA: WELL...WE'LL SEE ABOUT THAT!
        pass
    
    def _intro_cutscene_4(self):
        '''PyDoc'''
        # 0xD168 - 5CAAB8
        # BOTTLES: HI THERE TOOTY, WHAT ARE YOU GOING TO DO TODAY?
        # TOOTY: WHEN MY BIG LAZY BROTHER WAKES UP, WE'RE GOING ON AN ADVENTURE!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D168")
#         intro_cutscene_text._replace_line("4849205448455245", "")
        intro_cutscene_text._replace_line("5748454e204d59", "I'M GOING TO WATCH MY BROTHER SPEEDRUN THE GAME HAHA!")

    def _intro_cutscene_5(self):
        '''PyDoc'''
        # 0xD170 - 5CAB30
        # KAZOOIE: WAKE UP, I WANT TO GO ON AN ADVENTURE TOO...
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D170")
        intro_cutscene_text._replace_line("57414b45205550", "WAKE UP, I WANT TO GET UNDER 2 HOURS!")
    
    def _intro_cutscene_6(self):
        '''PyDoc'''
        # 0xD178 - 5CAB70
        # GRUNTILDA: IF TOOTY THINKS SHE'S FAIRER THAN ME,
        # GRUNTILDA: I'LL STEAL HER LOOKS AND UGLY SHE'LL BE!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D178")
        intro_cutscene_text._replace_line("494620544f4f5459", "IF PLAYERS THINK THEY KNOW THE GAME WELL,")
        intro_cutscene_text._replace_line("49274c4c20535445414c", "I'LL CHANGE THE GAME WITH MY RANDOIZE SPELL!")
    
    def _intro_cutscene_7(self):
        '''PyDoc'''
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
        '''PyDoc'''
        # 0xD188 - 5CAC38
        # TOOTY: I DON'T THINK SO. WHO IS THAT?
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D188")
        intro_cutscene_text._replace_line("4920444f4e2754", "OH NO... THAT'S A BAD SEED!")
    
    def _intro_cutscene_9(self):
        '''PyDoc'''
        # 0xD190 - 5CAC70
        # GRUNTILDA: COME TO ME, MY LITTLE PRETTY,
        # GRUNTILDA: YOU'LL SOON BE UGLY, WHAT A PITY!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D190")
        intro_cutscene_text._replace_line("434f4d4520544f204d45", "ONCE I MOVE SOME THINGS AROUND,")
        intro_cutscene_text._replace_line("594f55274c4c20534f4f4e", "NO COLLECTABLES WILL BE FOUND!")
    
    def _intro_cutscene_10(self):
        '''PyDoc'''
        # 0xD198 - 5CACC0
        # TOOTY: LET ME GO, YOU UGLY OLD HAG!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D198")
        intro_cutscene_text._replace_line("4c4554204d4520474f", "PUT THAT BACK, YOU UGLY OLD HAG!")
    
    def _intro_cutscene_11(self):
        '''PyDoc'''
        # 0xD1A0 - 5CACF8
        # GRUNTILDA: DON'T SCRATCH AND BITE, MY LITTLE BEAR,
        # GRUNTILDA: YOU'LL SOON NEED BIGGER UNDERWEAR!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D1A0")
        intro_cutscene_text._replace_line("444f4e27542053435241544348", "I'LL PUT THIS HERE, I'LL PUT THAT THERE,")
        intro_cutscene_text._replace_line("594f55274c4c20534f4f4e", "NOW THERE ARE NEW THINGS EVERYWHERE!")
    
    def _intro_cutscene_12(self):
        '''PyDoc'''
        # 0xD1A8 - 5CAD58
        # BOTTLES: OH NO, SHE'S GOT HER! SOMEBODY......HELP!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D1A8")
        intro_cutscene_text._replace_line("4f48204e4f2c", "I CAN'T TELL, IS THIS WORLD RECORD PACE?")
    
    def _intro_cutscene_13(self):
        '''PyDoc'''
        # 0xD1B0 - 5CAD98
        # KAZOOIE: BANJO! WAKE UP......NOW!
#         intro_cutscene_text = Speech_File_Class(self._file_dir, "D1B0")
#         intro_cutscene_text._replace_line("42414e4a4f21", "")
        pass
    
    def _intro_cutscene_14(self):
        '''PyDoc'''
        # 0xD1B8 - 5CADC8
        # BANJO: YAWN...WHAT DO YOU WANT KAZOOIE?
#         intro_cutscene_text = Speech_File_Class(self._file_dir, "")
#         intro_cutscene_text._replace_line("", "")
        pass
    
    def _intro_cutscene_15(self):
        '''PyDoc'''
        # 0xD1C0 - 5CAE00
        # KAZOOIE: LET'S GET OUTSIDE, THERE'S TROUBLE!
#         intro_cutscene_text = Speech_File_Class(self._file_dir, "")
#         intro_cutscene_text._replace_line("", "")
        pass
    
    ###########################
    ### ENTER LAIR CUTSCENE ###
    ###########################
    
    def _enter_lair_cutscene(self):
        '''PyDoc'''
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
    
    ###############################
    ### BASE GAME PROGRESS TEXT ###
    ###############################
    
    def _bottles_50_notes(self):
        '''PyDoc'''
        # 0xDA38 - 5CC5C8
        # YIPPEE! YOU'VE COLLECTED ENOUGH NOTES TO BREAK THE FIRST NOTE DOOR SPELL!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA38")
        intro_cutscene_text._replace_line("59495050454521", "REMEMBER TO STAY HYDRATED!")
    
    def _bottles_enter_mm_moves(self):
        '''PyDoc'''
        # 0xD9D8 - 5CC1B0
        # THERE ARE THREE NEW MOVES TO LEARN IN THIS WORLD. FIND MY MOLEHILLS AND I'LL EXPLAIN.
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D9D8")
        intro_cutscene_text._replace_line("544845524520415245", "BEAR AND BIRD FIND MOLE AND LEARN MOVES!")
    
    def _bottles_learned_mm_moves(self):
        '''PyDoc'''
        # 0xB908 - 5C4350
        # WOAAA, BANJO! THERE'S NOTHING MORE I CAN TEACH YOU ON THIS WORLD!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "B908")
        intro_cutscene_text._replace_line("574f4141412c", "EEKUM BOKUM!")
    
    def _bottles_enter_ttc_moves(self):
        '''PyDoc'''
        # 0xD9E0 - 5CC210
        # AHOY THERE! THIS BE TREASURE TROVE COVE. THAR BE TWO NEW MOVES FOR YE TO FIND.
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D9E0")
        intro_cutscene_text._replace_line("41484f5920544845524521", "REMEMBER CAP'N BLACKEYE? ME NEITHER!")
    
    def _bottles_learned_ttc_moves(self):
        '''PyDoc'''
        # 0xAFD0 - 5C2BC0
        # NICE GOING, YOU'VE LEARNED ALL THE COVE'S NEW MOVES!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "AFD0")
        intro_cutscene_text._replace_line("4e49434520474f494e47", "THE REAL LOOT BE THE SCALLYWAGS WE MADE ALONG THE WAY!")
    
    def _bottles_enter_cc_moves(self):
        '''PyDoc'''
        # 0xD9E8 - 5CC268
        # JUST THE ONE NEW MOVE TO FIND THIS TIME, BUT IT'S HIDDEN WELL!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D9E8")
        intro_cutscene_text._replace_line("4a55535420544845", "WHAT IS CLANKER ANYWAY? A SHARK? A WHALE?")
    
    def _bottles_learned_cc_moves(self):
        '''PyDoc'''
        # 0xC850 - 5C7818
        # YOU'VE LEARNED ALL MY NEW MOVES FOR THIS WORLD, THE REST IS UP TO YOU!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "C850")
        intro_cutscene_text._replace_line("594f55275645", "IS ANYONE REALLY FREE WHEN CHAINED TO SOCIETY?")
    
    def _bottles_enter_bgs_moves(self):
        '''PyDoc'''
        # 0xD9F0 - 5CC2B8
        # KEEP YOUR EYES OPEN FOR YOUR NEW MOVE, BEAK FACE!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D9F0")
        intro_cutscene_text._replace_line("4b45455020594f5552", "WHAT ARE YEW DOIN' IN MY SWAMP?!")
    
    def _bottles_learned_bgs_moves(self):
        '''PyDoc'''
        # 0xC2E8 - 5C6358
        # GREAT, NOW YOU KNOW ALL THE SWAMP'S NEW MOVES!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "C2E8")
        intro_cutscene_text._replace_line("47524541542c", "IT SMELLS LIKE A VIDEO GAME CHAMPIONSHIP HERE...")
    
    def _bottles_enter_fp_moves(self):
        '''PyDoc'''
        # 0xD9F8 - 5CC300
        # THE PEAK'S GOT ANOTHER NEW MOVE WAITING FOR YOU IF YOU CAN FIND IT!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "D9F8")
        intro_cutscene_text._replace_line("544845205045414b", "WHAT'S THIS? DROPS OF RAIN FROZEN INTO ICE CRYSTALS? I SHALL HARNESS THEIR ENERGY AND RULE THE WORLD!")
    
    def _bottles_learned_fp_moves(self):
        '''PyDoc'''
        # 0xBFE8 - 5C5680
        # YOU'VE LEARNED ALL THE MOVES I CAN TEACH YOU ON THIS WORLD NOW!
        intro_cutscene_text = Speech_File_Class(self._file_dir, "BFE8")
        intro_cutscene_text._replace_line("594f55275645", "HAPPY WALRUS NOISES!")
    
    def _bottles_enter_gv_moves(self):
        '''PyDoc'''
        # 0xDA00 - 5CC350
        # YOU'LL FIND ONE MORE MOVE IN HERE, BANJO.
        intro_cutscene_text = Speech_File_Class(self._file_dir, "DA00")
        intro_cutscene_text._replace_line("594f55274c4c", "I DON'T LIKE SAND. IT'S COARSE AND ROUGH AND IRRITATING AND IT GETS EVERYWHERE.")
    
    def _bottles_learned_gv_moves(self):
        '''PyDoc'''
        # 0xB2C8 - 5C33E8
        # WELL, I'M AFRAID THAT'S IT FOR NEW MOVES IN GOBI'S VALLEY.
        intro_cutscene_text = Speech_File_Class(self._file_dir, "B2C8")
        intro_cutscene_text._replace_line("57454c4c2c", "CHILI DOGS!")
    
    def _bottles_this_is_a_mod(self):
        '''PyDoc'''
        # DID YOU GET ALL OF THE NEW MOVES? OH WAIT, THIS IS A MOD, I CAN'T REMEMBER HOW MANY MOVES THERE ARE IN EACH LEVEL...
        pass
    
    #####################
    ### INTRO BOTTLES ###
    #####################
    
    def _bottles_introduction_text(self):
        '''PyDoc'''
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
        # ORIGINAL: "PRESS A IF YOU WANT ME TO TEACH YOU SOME BASIC MOVES, OR PRESS B IF YOU THINK YOU'RE ALREADY GOOD ENOUGH!"
        # BOTH:     "YOU'LL NEED 000 NOTES AND 99 JIGGIES TO REACH GRUNTY. PRESS A FOR THE TUTORIAL OR PRESS B TO GET GOING!"
        # NOTES:    "YOU'LL NEED 000 NOTES. JIGGY REQUIREMENT IS THE SAME AS BASE GAME. PRESS A FOR TUTORIAL OR B TO SKIP."
        # JIGGIES:  "YOU'LL NEED 00 JIGGIES. NOTES REQUIREMENT IS THE SAME AS BASE GAME. PRESS A FOR TUTORIAL OR B TO SKIP."
        # NONE:     "YOU'LL NEED THE SAME NOTES AND JIGGY REQUIREMENTS AS BASE GAME. PRESS A FOR TUTORIAL OR B TO SKIP."
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
    
    #####################
    ### MISCELLANEOUS ###
    #####################
    
    def _copyright_info(self):
        # 0xECD8 - 5D3100
        # COPYRIGHT 1998
        # NINTENDO-RARE LTD
        # GAME BY RARE TM
        # PRODUCED BY RARE
        # PRESENTED BY NINTENDO
        pass