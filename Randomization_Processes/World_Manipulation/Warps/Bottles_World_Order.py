'''
Created on Sep 23, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

from random import seed, choice

############
### DICT ###
############

learnable_moves_dict = {
    "Talon_Trot": "060C037A",
    "Beak_Buster": "058C037A",
    "Shock_Jump_Pad": "068C037A",
    "Eggs": "050C037A",
    "Fly": "070C037A",
    "Wonderwing": "078C037A",
    "Wading_Boots": "080C037A",
    "Beak_Bomb": "048C037A",
    "Turbo_Talon_Trot": "088C037A"
    }

#########################
### WORLD ORDER CLASS ###
#########################

class World_Order_Bottles():
    def __init__(self, bottles_world_warp_dict, extra_flagged_object_flags, seed_val=0, max_hp="One Health Only", final_puzzle_option=0, world_exit_option="Exit From World You Were Just In", removed_detransformations=0, free_transformations="Base Game Costs"):
        '''Initializes the World Order Bottles Class'''
        self.bottles_world_warp_dict = bottles_world_warp_dict
        self.extra_flagged_object_flags = extra_flagged_object_flags
        self.seed_val = seed_val
        self.remaining_moves = [move for move in learnable_moves_dict]
        self.learned_moves = []
        self.temp_learned_moves = {}
        self.remaining_worlds = [world for world in bottles_world_warp_dict]
        self.world_order_list = []
        self.world_order_dict = {}
        self.collected_jiggy_list = []
        self.collected_mumbo_token_list = []
        self.increment = 0
        if(max_hp in ["Normal Health", "Four Health Only"]):
            self.max_hp = False
        else:
            self.max_hp = True
        if(final_puzzle_option == 0):
            self._required_jiggies = [3, 8, 15, 23, 32, 42, 54, 69, 0]
        else:
            self._required_jiggies = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.world_exit_option = world_exit_option
        self.removed_detransformations = removed_detransformations
        self.free_transformations = free_transformations
        self._create_transformation_cost_dict()
        self.restart_count = 0

    def _create_transformation_cost_dict(self):
        '''Sets up the transformation cost dict for known values'''
        self.transform_cost_dict = {}
        if(self.free_transformations == "Base Game Costs"):
            self.transform_cost_dict["Termite"] = 5
            self.transform_cost_dict["Crocodile"] = 10
            self.transform_cost_dict["Walrus"] = 15
            self.transform_cost_dict["Pumpkin"] = 20
            self.transform_cost_dict["Bee"] = 25
        elif(self.free_transformations == "Free Transformations"):
            self.transform_cost_dict["Termite"] = 0
            self.transform_cost_dict["Crocodile"] = 0
            self.transform_cost_dict["Walrus"] = 0
            self.transform_cost_dict["Pumpkin"] = 0
            self.transform_cost_dict["Bee"] = 0
    
    def _progression_requirements(self, world_name):
        '''Calculates the progression requirements for the world number, based on lair progression and Jiggies needed to open the worlds'''
        world_count = len(self.world_order_list)
        required_move_list = []
        # Exiting MM -> Going To TTC
        if(world_count == 0):
            required_jiggy_count = self._required_jiggies[0]
            if(self.world_exit_option == "Exit From World You Were Just In"):
                if(world_name == "Mumbo's Mountain"):
                    required_move_list = ["Talon_Trot"]
                elif((world_name == "Freezeezy Peak") and (self.max_hp)):
                    required_move_list = ["Talon_Trot", "Fly"]
            else:
                required_move_list = ["Talon_Trot"]
        # Exiting TTC -> Going To CC
        elif(world_count == 1):
            required_jiggy_count = self._required_jiggies[1]
            if(self.world_exit_option == "Exit From World You Were Just In"):
                if((world_name != "Clanker's Cavern") and ("Clanker's Cavern" not in self.world_order_list)):
                    # You Can Enter World If Leaving It
                    # Shock_Jump_Pad For Puzzle, Beak_Buster For Pipes
                    required_move_list = ["Shock_Jump_Pad", "Beak_Buster"]
            else:
                required_move_list = ["Shock_Jump_Pad", "Beak_Buster"]
        # Exiting CC -> Going To BGS
        elif(world_count == 2):
            required_jiggy_count = self._required_jiggies[2]
            if(self.world_exit_option == "Exit From World You Were Just In"):
                if((world_name == "Bubblegloop Swamp") or ("Bubblegloop Swamp" in self.world_order_list)):
                    # You Can Enter World If Leaving It; Beak_Buster For Puzzle
                    required_move_list = ["Beak_Buster"]
                else:
                    # Talon_Trot To Get To BGS; Beak_Buster For Puzzle
                    required_move_list = ["Talon_Trot", "Beak_Buster"]
        # Exiting BGS -> Going To FP
        elif(world_count == 3):
            required_jiggy_count = self._required_jiggies[3]
            if(self.world_exit_option == "Exit From World You Were Just In"):
                if((world_name == "Freezeezy Peak") or ("Freezeezy Peak" in self.world_order_list)):
                    # You Can Enter World If Leaving It
                    required_move_list = []
                elif(world_name not in ["Gobi's Valley", "Mad Monster Mansion", "Rusty Bucket Bay", "Click Clock Wood"]):
                    possible_world_found = False
                    for possible_world in ["Gobi's Valley", "Mad Monster Mansion", "Rusty Bucket Bay", "Click Clock Wood"]:
                        if(possible_world in self.world_order_list):
                            possible_world_found = True
                            break
                    if(possible_world_found):
                        if(self.max_hp):
                            # Get To Puzzle Without Taking Damage
                            required_move_list = ["Wading_Boots"]
                    else:
                        if(self.max_hp):
                            required_move_list = ["Shock_Jump_Pad", "Wading_Boots"]
                        else:
                            # Get To 260 Note Door; Get To Puzzle Without Taking Damage
                            required_move_list = ["Shock_Jump_Pad"]
                else:
                    if(self.max_hp):
                        required_move_list = ["Wading_Boots"]
            else:
                if(self.max_hp):
                    required_move_list = ["Wading_Boots"]
        # Exiting FP -> Going To GV
        elif(world_count == 4):
            required_jiggy_count = self._required_jiggies[4]
            if(self.world_exit_option == "Exit From World You Were Just In"):
                if((world_name != "Gobi's Valley") and ("Gobi's Valley" not in self.world_order_list)):
                    # Get To GV Without Taking Damage
                    if(self.max_hp):
                        required_move_list = ["Wading_Boots"]
        # Exiting GV -> Going To MMM
        elif(world_count == 5):
            required_jiggy_count = self._required_jiggies[5]
            required_move_list = []
        # Exiting MMM -> Going To RBB
        elif(world_count == 6):
            required_jiggy_count = self._required_jiggies[6]
            # Raise The Water Level To Reach Puzzle
            if(self.world_exit_option == "Exit From World You Were Just In"):
                required_move_list = ["Beak_Buster"]
        # Exiting RBB -> Going To CCW
        elif(world_count == 7):
            required_jiggy_count = self._required_jiggies[7]
            # CCW Puzzle Button
            if(self.world_exit_option == "Exit From World You Were Just In"):
                required_move_list = ["Beak_Buster"]
        else:
            required_jiggy_count = self._required_jiggies[8]
        progress_move_list = []
        for required_move in required_move_list:
            if(required_move not in self.learned_moves):
                progress_move_list.append(required_move)
        return required_jiggy_count, progress_move_list
    
    def _possible_world_moves(self, world_name, progress_move_list, additional_learned_moves={}):
        '''Calculates the possible moves that can be learned in the level'''
        # Can you learn moves without learning other moves?
        available_bottles = []
        required_moves_for_additional_slot = []
        for possible_bottles in self.bottles_world_warp_dict[world_name]["Possible_Bottles"]:
            for requirement_list in self.bottles_world_warp_dict[world_name]["Possible_Bottles"][possible_bottles]:
                required_moves = []
                for requirement in requirement_list:
                    if((requirement not in self.learned_moves) and (requirement not in additional_learned_moves)):
                        required_moves.append(requirement)
                if((len(required_moves) == 0) and (possible_bottles not in additional_learned_moves)):
                    available_bottles.append(possible_bottles)
                    break
                elif(len(required_moves) == 1):
                    required_moves_for_additional_slot.append(required_moves[0])
        # Do you have enough spots to progress?
        if(len(progress_move_list) <= len(available_bottles)):
            for progress_move in progress_move_list:
                seed(a=(self.seed_val + self.increment))
                self.increment += 1
                selected_bottles = choice(available_bottles)
                self.temp_learned_moves[world_name]["New_Moves"][selected_bottles] = progress_move
                self.temp_learned_moves[world_name]["New_Moves_List"].append(progress_move)
                available_bottles.remove(selected_bottles)
            learnable_moves = []
            for move in self.remaining_moves:
                if((move not in list(additional_learned_moves.values())) and (move not in self.temp_learned_moves[world_name]["New_Moves_List"])):
                    learnable_moves.append(move)
            while((len(self.temp_learned_moves[world_name]["New_Moves"]) < 2) and (len(available_bottles) > 0) and (len(learnable_moves) > 0)):
                seed(a=(self.seed_val + self.increment))
                self.increment += 1
                if(len(required_moves_for_additional_slot) > 0):
                    selected_move = choice(required_moves_for_additional_slot)
                else:
                    selected_move = choice(learnable_moves)
                if(selected_move in required_moves_for_additional_slot):
                    required_moves_for_additional_slot.remove(selected_move)
                if(selected_move in learnable_moves):
                    learnable_moves.remove(selected_move)
                seed(a=(self.seed_val + self.increment))
                self.increment += 1
                selected_bottles = choice(available_bottles)
                available_bottles.remove(selected_bottles)
                self.temp_learned_moves[world_name]["New_Moves"][selected_bottles] = selected_move
                self.temp_learned_moves[world_name]["New_Moves_List"].append(selected_move)
        # If not, can you make more spots to progress?
        elif((len(available_bottles) > 0) and (required_moves_for_additional_slot)):
            selected_move = max(set(required_moves_for_additional_slot), key=required_moves_for_additional_slot.count)
            seed(a=(self.seed_val + self.increment))
            self.increment += 1
            selected_bottles = choice(available_bottles)
            self.temp_learned_moves[world_name]["New_Moves"][selected_bottles] = selected_move
            self.temp_learned_moves[world_name]["New_Moves_List"].append(selected_move)
            self._possible_world_moves(world_name, progress_move_list, additional_learned_moves=self.temp_learned_moves[world_name]["New_Moves"])
        else:
            return False
        # Double Check
        for progress_move in progress_move_list:
            if(progress_move not in self.temp_learned_moves[world_name]["New_Moves_List"]):
                return False
        return True
    
    def _possible_world_transformation(self, world_name):
        '''Calculates whether a transformation can happen if this world is selected'''
        # How many Mumbo Tokens would you have if you collected all available tokens?
        transformation_tokens = []
        for flagged_object_flag in self.bottles_world_warp_dict[world_name]["Flagged_Object_Flags"]:
            object_type = self.bottles_world_warp_dict[world_name]["Flagged_Object_Flags"][flagged_object_flag]["Type"]
            object_id = self.bottles_world_warp_dict[world_name]["Flagged_Object_Flags"][flagged_object_flag]["ID"]
            if((object_type == "Mumbo Token") and 
               (object_id not in self.collected_mumbo_token_list) and 
               (object_id not in self.temp_learned_moves[world_name]["New_Mumbo_Tokens"])):
                for requirement_list in self.bottles_world_warp_dict[world_name]["Flagged_Object_Flags"][flagged_object_flag]["Requirements"]:
                    can_obtain = True
                    for requirement in requirement_list:
                        if((requirement not in self.learned_moves) and (requirement not in self.temp_learned_moves[world_name]["New_Moves_List"])):
                            if((requirement in ["Termite", "Crocodile", "Walrus", "Pumpkin", "Bee"]) and (len(requirement_list) == 1)):
                                transformation_tokens.append(object_id)
                            can_obtain = False
                            break
                    if(can_obtain):
                        self.temp_learned_moves[world_name]["New_Mumbo_Tokens"].append(object_id)
        # Is there a transformation here and can you afford it?
        current_mumbo_count = len(set(self.collected_mumbo_token_list)) + len(set(self.temp_learned_moves[world_name]["New_Mumbo_Tokens"]))
        for transformation_name in ["Termite", "Crocodile", "Walrus", "Pumpkin", "Bee"]:
            if(transformation_name in self.learned_moves):
                current_mumbo_count -= self.transform_cost_dict[transformation_name]
        if(self.free_transformations == "World Order Scaled Costs"):
            next_transform_cost = (len(self.transform_cost_dict) + 1) * 5
        else:
            if(world_name == "Mumbo's Mountain"):
                next_transform_cost = self.transform_cost_dict["Termite"]
            elif(world_name == "Bubblegloop Swamp"):
                next_transform_cost = self.transform_cost_dict["Crocodile"]
            elif(world_name == "Freezeezy Peak"):
                next_transform_cost = self.transform_cost_dict["Walrus"]
            elif(world_name == "Mad Monster Mansion"):
                next_transform_cost = self.transform_cost_dict["Pumpkin"]
            elif(world_name == "Click Clock Wood"):
                next_transform_cost = self.transform_cost_dict["Bee"]
        if(world_name == "Mumbo's Mountain"):
            if(("Termite" not in self.learned_moves) and (current_mumbo_count >= next_transform_cost)):
                self.temp_learned_moves[world_name]["New_Moves_List"].append("Termite")
        elif(world_name == "Bubblegloop Swamp"):
            if(("Crocodile" not in self.learned_moves) and (current_mumbo_count >= next_transform_cost)):
                self.temp_learned_moves[world_name]["New_Moves_List"].append("Crocodile")
        elif(world_name == "Freezeezy Peak"):
            if(("Walrus" not in self.learned_moves) and (current_mumbo_count >= next_transform_cost)):
                self.temp_learned_moves[world_name]["New_Moves_List"].append("Walrus")
        elif(world_name == "Mad Monster Mansion"):
            if(("Pumpkin" not in self.learned_moves) and (current_mumbo_count >= next_transform_cost)):
                self.temp_learned_moves[world_name]["New_Moves_List"].append("Pumpkin")
        elif(world_name == "Click Clock Wood"):
            if(("Bee" not in self.learned_moves) and (current_mumbo_count >= next_transform_cost)):
                self.temp_learned_moves[world_name]["New_Moves_List"].append("Bee")
        # Does the transformation get more tokens?
        for token_id in transformation_tokens:
            self.temp_learned_moves[world_name]["New_Mumbo_Tokens"].append(token_id)
    
    def _possible_world_jiggies(self, world_name):
        '''Calculates the number of Jiggies and Tolens available in the possible world'''
        # How many Jiggies would you have if you collected all available Jiggies?
        for flagged_object_flag in self.bottles_world_warp_dict[world_name]["Flagged_Object_Flags"]:
            object_type = self.bottles_world_warp_dict[world_name]["Flagged_Object_Flags"][flagged_object_flag]["Type"]
            object_id = self.bottles_world_warp_dict[world_name]["Flagged_Object_Flags"][flagged_object_flag]["ID"]
            if((object_type == "Jiggy") and 
               (object_id not in self.collected_jiggy_list) and 
               (object_id not in self.temp_learned_moves[world_name]["New_Jiggies"])):
                for requirement_list in self.bottles_world_warp_dict[world_name]["Flagged_Object_Flags"][flagged_object_flag]["Requirements"]:
                    can_obtain = True
                    for requirement in requirement_list:
                        if((requirement not in self.learned_moves) and (requirement not in self.temp_learned_moves[world_name]["New_Moves_List"])):
                            can_obtain = False
                            break
                    if(can_obtain):
                        self.temp_learned_moves[world_name]["New_Jiggies"].append(object_id)

    def _possible_lair_collectables(self, world_name):
        '''Calculates the number of Jiggies and Tokens available in the lair'''
        transformation_jiggies = []
        transformation_tokens = []
        for area_name in self.extra_flagged_object_flags:
            self.temp_learned_moves[area_name] = {}
            self.temp_learned_moves[area_name]["New_Jiggies"] = []
            self.temp_learned_moves[area_name]["New_Mumbo_Tokens"] = []
            for object_flag in self.extra_flagged_object_flags[area_name]:
                object_type = self.extra_flagged_object_flags[area_name][object_flag]["Type"]
                object_id = self.extra_flagged_object_flags[area_name][object_flag]["ID"]
                if((object_type == "Jiggy") and
                   (object_id not in self.collected_jiggy_list) and 
                   (object_id not in self.temp_learned_moves[world_name]["New_Jiggies"]) and
                   (object_id not in self.temp_learned_moves[area_name]["New_Jiggies"])):
                    for requirement_list in self.extra_flagged_object_flags[area_name][object_flag]["Requirements"]:
                        can_obtain = True
                        for requirement in requirement_list:
                            if((requirement not in self.learned_moves) and (requirement not in self.temp_learned_moves[world_name]["New_Moves_List"])):
                                if((requirement in ["Termite", "Crocodile", "Walrus", "Pumpkin", "Bee"]) and (len(requirement_list) == 1)):
                                    transformation_jiggies.append(object_id)
                                can_obtain = False
                                break
                        if((self.world_exit_option == 1) and ((len(self.world_order_list) + 1) < self.extra_flagged_object_flags[area_name][object_flag]["World_Count"])):
                            can_obtain = False
                        if(can_obtain):
                            self.temp_learned_moves[area_name]["New_Jiggies"].append(object_id)
                if((object_type == "Mumbo Token") and
                   (object_id not in self.collected_jiggy_list) and 
                   (object_id not in self.temp_learned_moves[world_name]["New_Mumbo_Tokens"]) and
                   (object_id not in self.temp_learned_moves[area_name]["New_Mumbo_Tokens"])):
                    for requirement_list in self.extra_flagged_object_flags[area_name][object_flag]["Requirements"]:
                        can_obtain = True
                        for requirement in requirement_list:
                            if((requirement not in self.learned_moves) and (requirement not in self.temp_learned_moves[world_name]["New_Moves_List"])):
                                if((requirement in ["Termite", "Crocodile", "Walrus", "Pumpkin", "Bee"]) and (len(requirement_list) == 1)):
                                    transformation_tokens.append(object_id)
                                can_obtain = False
                                break
                        if((self.world_exit_option == 1) and ((len(self.world_order_list) + 1) < self.extra_flagged_object_flags[area_name][object_flag]["World_Count"])):
                            can_obtain = False
                        if(can_obtain):
                            self.temp_learned_moves[area_name]["New_Mumbo_Tokens"].append(object_id)
    
    def _jiggies_from_past_worlds(self):
        '''Calculates the number of Jiggies obtainable from past worlds'''
        for world_name in self.world_order_list:
            self.temp_learned_moves[world_name] = {}
            self.temp_learned_moves[world_name]["New_Moves"] = {}
            self.temp_learned_moves[world_name]["New_Moves_List"] = [world_name]
            self.temp_learned_moves[world_name]["New_Mumbo_Tokens"] = []
            self.temp_learned_moves[world_name]["New_Jiggies"] = []
            self._possible_world_transformation(world_name)
            self._possible_world_jiggies(world_name)

    def _possible_next_worlds(self):
        '''Determines the next possible world list based on learning progressable moves and getting enough Jiggies. Also creates a backup for levels that allow you to progress'''
        possible_world_list = []
        for world_name in self.remaining_worlds:
            # Moves
            self.temp_learned_moves[world_name] = {}
            self.temp_learned_moves[world_name]["New_Moves"] = {}
            self.temp_learned_moves[world_name]["New_Moves_List"] = [world_name]
            self.temp_learned_moves[world_name]["New_Mumbo_Tokens"] = []
            self.temp_learned_moves[world_name]["New_Jiggies"] = []
            required_jiggy_count, progress_move_list = self._progression_requirements(world_name)
            move_progressable = self._possible_world_moves(world_name, progress_move_list)
            if(move_progressable):
                # Mumbo Tokens
                self._possible_world_transformation(world_name)
                # Jiggies
                self._possible_world_jiggies(world_name)
                self._jiggies_from_past_worlds()
                self._possible_lair_collectables(world_name)
                possible_total_jiggy_list = []
                for jiggy_id in self.collected_jiggy_list:
                    possible_total_jiggy_list.append(jiggy_id)
                for jiggy_id in self.temp_learned_moves[world_name]["New_Jiggies"]:
                    possible_total_jiggy_list.append(jiggy_id)
                for past_world_name in self.world_order_list:
                    for jiggy_id in self.temp_learned_moves[past_world_name]["New_Jiggies"]:
                        possible_total_jiggy_list.append(jiggy_id)
                for area_name in self.extra_flagged_object_flags:
                    for jiggy_id in self.temp_learned_moves[area_name]["New_Jiggies"]:
                        possible_total_jiggy_list.append(jiggy_id)
                if(len(set(possible_total_jiggy_list)) >= required_jiggy_count):
                    possible_world_list.append(world_name)
        return possible_world_list

    def _set_next_world(self, next_world):
        '''Finalizes the selected world and all additional changes'''
        # Remove from remaining worlds
        self.world_order_list.append(next_world)
        self.world_order_dict[next_world] = {}
        self.remaining_worlds.remove(next_world)
        # What moves did you learn in which location?
        self.world_order_dict[next_world]["Learned_Moves"] = {}
        for bottles_location in self.temp_learned_moves[next_world]["New_Moves"]:
            self.world_order_dict[next_world]["Learned_Moves"][bottles_location] = self.temp_learned_moves[next_world]["New_Moves"][bottles_location]
        for new_move in self.temp_learned_moves[next_world]["New_Moves_List"]:
            self.learned_moves.append(new_move)
            if(new_move in self.remaining_moves):
                self.remaining_moves.remove(new_move)
        # Transformations
        transformation_name = None
        if(next_world == "Mumbo's Mountain"):
            transformation_name = "Termite"
        elif(next_world == "Bubblegloop Swamp"):
            transformation_name = "Crocodile"
        elif(next_world == "Freezeezy Peak"):
            transformation_name = "Walrus"
        elif(next_world == "Mad Monster Mansion"):
            transformation_name = "Pumpkin"
        elif(next_world == "Click Clock Wood"):
            transformation_name = "Bee"
        if((transformation_name) and (transformation_name not in self.transform_cost_dict)):
            if(self.free_transformations == "Free Transformations"):
                self.transform_cost_dict[transformation_name] = 0
            elif(self.free_transformations == "World Order Scaled Costs"):
                self.transform_cost_dict[transformation_name] = (len(self.transform_cost_dict) + 1) * 5
        # What would your Mumbo Token list be?
        for world_name in self.world_order_list:
            for token_id in self.temp_learned_moves[world_name]["New_Mumbo_Tokens"]:
                self.collected_mumbo_token_list.append(token_id)
        # What would your Jiggy list be?
        for world_name in self.world_order_list:
            for jiggy_id in self.temp_learned_moves[world_name]["New_Jiggies"]:
                if(jiggy_id not in self.collected_jiggy_list):
                    self.collected_jiggy_list.append(jiggy_id)
                    
    def _remaining_moves(self):
        '''For each remaining move, assign them to a possible location'''
        for remaining_move in self.remaining_moves:
            available_bottles = {}
            for world_name in self.world_order_list:
                for possible_bottles in self.bottles_world_warp_dict[world_name]["Possible_Bottles"]:
                    if(possible_bottles not in self.world_order_dict[world_name]["Learned_Moves"]):
                        for requirement_list in self.bottles_world_warp_dict[world_name]["Possible_Bottles"][possible_bottles]:
                            required_moves = []
                            for requirement in requirement_list:
                                if(requirement not in self.learned_moves):
                                    required_moves.append(requirement)
                            if(len(required_moves) == 0):
                                available_bottles[possible_bottles] = world_name
                                break
            seed(a=(self.seed_val + self.increment))
            self.increment += 1
            selected_bottles = choice(list(available_bottles))
            self.world_order_dict[available_bottles[selected_bottles]]["Learned_Moves"][selected_bottles] = remaining_move
    
    def _restart(self, reason="Unknown"):
        '''Resets the variables to recalculations'''
        print(f"### RESTARTING REASON: {reason} ###")
        self.restart_count += 1
        if(self.restart_count > 6.9):
            raise SystemError("Restart Count Higher Than 10")
        self.remaining_moves = [move for move in learnable_moves_dict]
        self.learned_moves = []
        self.temp_learned_moves = {}
        self.remaining_worlds = [world for world in self.bottles_world_warp_dict]
        self.world_order_list = []
        self.world_order_dict = {}
        self.collected_jiggy_list = []
        self.collected_mumbo_token_list = []
        self._create_transformation_cost_dict()

    def _determine_world_order(self):
        '''Determines the world order based on accessibility'''
        try:
            while(self.remaining_worlds):
                # What can be the next world?
                next_world = None
                possible_world_list = self._possible_next_worlds()
                if((self.world_exit_option == "Exit From Entrance You Entered From")):
                    if(self.removed_detransformations == 0):
                        if(len(self.world_order_list) == 6):
                            if("Mad Monster Mansion" in possible_world_list):
                                next_world = "Mad Monster Mansion"
                            else:
                                self._restart(reason="No Mad Monster Mansion 1")
                        elif("Mad Monster Mansion" in possible_world_list):
                            possible_world_list.remove("Mad Monster Mansion")
                    elif(self.removed_detransformations == 1):
                        if((len(self.world_order_list) == 6) and ("Mad Monster Mansion" not in self.world_order_list)):
                            if("Mad Monster Mansion" in possible_world_list):
                                next_world = "Mad Monster Mansion"
                            else:
                                self._restart(reason="No Mad Monster Mansion 2")
                        elif((len(self.world_order_list) < 4) and ("Mad Monster Mansion" in possible_world_list)):
                            possible_world_list.remove("Mad Monster Mansion")
                # Select from possible worlds
                seed(a=(self.seed_val + self.increment))
                self.increment += 1
                if(next_world):
                    # Placed all of the calculations in the dictionary
                    self._set_next_world(next_world)
                elif(possible_world_list):
                    next_world = choice(possible_world_list)
                    # Placed all of the calculations in the dictionary
                    self._set_next_world(next_world)
                else:
                    self._restart(reason="No Next World Available")
            # Teach any remaining moves
            self._remaining_moves()
        except IndexError:
            self._restart(reason="Index Error")
            self._determine_world_order()
        except KeyError:
            self._restart(reason="Key Error")
            self._determine_world_order()

if __name__ == '__main__':
    pass
