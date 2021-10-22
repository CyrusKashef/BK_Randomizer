'''
Created on Sep 23, 2021

@author: Cyrus
'''

from random import choice, randint

from ..Dicts_And_Lists.Warps import bottles_world_warp_dict

class World_Order_Bottles():
    def __init__(self, world_dict):
        self.remaining_moves = ["Talon_Trot", "Beak_Buster", "Eggs", "Fly", "Shock_Jump_Pad", "Wonderwing", "Wading_Boots", "Turbo_Talon_Trot", "Beak_Bomb"]
        self.learned_moves = []
        self.world_dict = world_dict
        self.remaining_worlds = [world for world in world_dict]
        self.world_order_list = []
        self.world_order_dict = {}

    def prior_moves_check(self):
        for world in self.remaining_worlds:
            if(self.world_dict[world]["Prior_Moves"] == []):
                self.possible_next_world_list.append(world)
            prior_moves_found = False
            for move in self.world_dict[world]["Prior_Moves"]:
                if(move in self.learned_moves):
                    self.possible_next_world_list.append(world)
                    prior_moves_found = True
                    break
            if(not prior_moves_found):
                for move in self.world_dict[world]["Prior_Moves"]:
                    if((move not in self.needed_world_moves) and (move in self.remaining_moves)):
                        self.needed_world_moves.append(move)
        return self.possible_next_world_list

    def available_bottles_locations(self):
        for world in self.possible_next_world_list:
            self.world_dict[world]["Possible_Location"] = []
            for location in self.world_dict[world]["Possible_Bottles"]:
                if(self.world_dict[world]["Possible_Bottles"][location] == []):
                    self.world_dict[world]["Possible_Location"] += [location]
                possible_requirements_met = False
                for possible_requirement in self.world_dict[world]["Possible_Bottles"][location]:
                    confirmed_move_location = True
                    for move in possible_requirement:
                        if(move in self.remaining_moves):
                            confirmed_move_location = False
                            break
                    if(confirmed_move_location):
                        self.world_dict[world]["Possible_Location"] += [location]
                        possible_requirements_met = True
                        break
                if(not possible_requirements_met):
                    for possible_requirement in self.world_dict[world]["Possible_Bottles"][location]:
                        for move in possible_requirement:
                            if((move not in self.needed_bottles_moves) and (move in self.remaining_moves)):
                                self.needed_bottles_moves.append(move)

    def enough_available_slots(self):
        possible_next_world_list = [world for world in self.possible_next_world_list]
        for world in self.possible_next_world_list:
            available_slots = len(self.world_dict[world]['Possible_Location'])
            needed_slots = len(self.world_dict[world]['In_World_Moves'])
            if(needed_slots > available_slots):
                possible_next_world_list.remove(world)
        self.possible_next_world_list = possible_next_world_list

    def in_world_moves(self, num_of_moves):
        for move in self.world_dict[self.next_world]['In_World_Moves']:
            if(move in self.remaining_moves):
                move_location = choice(self.world_dict[self.next_world]['Possible_Location'])
                self.world_order_dict[self.next_world]['Selected_Locations'].append(move_location)
                self.world_order_dict[self.next_world]['Learned_Moves'].append(move)
                self.world_dict[self.next_world]['Possible_Location'].remove(move_location)
                self.learned_moves.append(move)
                self.remaining_moves.remove(move)
                if(move in self.needed_bottles_moves):
                    self.needed_bottles_moves.remove(move)
                num_of_moves -= 1
        return num_of_moves

    def next_world_moves(self, num_of_moves):
        possible_remaining_worlds = []
        for world in self.remaining_worlds:
            needed_moves_count = 0
            for move in self.world_dict[world]["Prior_Moves"]:
                if(move in self.remaining_moves):
                    needed_moves_count += 1
            if(len(self.world_dict[self.next_world]['Possible_Location']) >= needed_moves_count):
                possible_remaining_worlds.append(world)
        next_world = choice(possible_remaining_worlds)
        for move in self.world_dict[next_world]["Prior_Moves"]:
            if(move in self.remaining_moves):
                move_location = choice(self.world_dict[self.next_world]['Possible_Location'])
                self.world_order_dict[self.next_world]['Selected_Locations'].append(move_location)
                self.world_order_dict[self.next_world]['Learned_Moves'].append(move)
                self.world_dict[self.next_world]['Possible_Location'].remove(move_location)
                self.learned_moves.append(move)
                self.remaining_moves.remove(move)
                if(move in self.needed_bottles_moves):
                    self.needed_bottles_moves.remove(move)
                num_of_moves -= 1
        return num_of_moves

    def possible_location_moves(self, num_of_moves):
        for move_count in range(min(num_of_moves, len(self.needed_bottles_moves))):
            move_location = choice(self.world_dict[self.next_world]['Possible_Location'])
            move = choice(self.needed_bottles_moves)
            self.world_order_dict[self.next_world]['Selected_Locations'].append(move_location)
            self.world_order_dict[self.next_world]['Learned_Moves'].append(move)
            self.world_dict[self.next_world]['Possible_Location'].remove(move_location)
            self.needed_bottles_moves.remove(move)
            self.learned_moves.append(move)
            self.remaining_moves.remove(move)
            if(move in self.needed_bottles_moves):
                self.needed_bottles_moves.remove(move)
            num_of_moves -= 1
        return num_of_moves

    def random_moves(self, num_of_moves):
        for move_count in range(min(num_of_moves, len(self.remaining_moves))):
            move_location = choice(self.world_dict[self.next_world]['Possible_Location'])
            move = choice(self.remaining_moves)
            self.world_order_dict[self.next_world]['Selected_Locations'].append(move_location)
            self.world_order_dict[self.next_world]['Learned_Moves'].append(move)
            self.world_dict[self.next_world]['Possible_Location'].remove(move_location)
            self.learned_moves.append(move)
            self.remaining_moves.remove(move)
            if(move in self.needed_bottles_moves):
                self.needed_bottles_moves.remove(move)
            num_of_moves -= 1
        return num_of_moves

    def world_learnable_moves(self):
        self.world_order_dict[self.next_world]['Selected_Locations'] = []
        self.world_order_dict[self.next_world]['Learned_Moves'] = []
        num_of_moves = min(randint(len(self.world_dict[self.next_world]['In_World_Moves']), len(self.world_dict[self.next_world]['Possible_Location'])), self.world_dict[self.next_world]["Available_Slots"])
        if(len(self.learned_moves) == 9):
            return "" # Found All Moves
        if(len(self.world_dict[self.next_world]['In_World_Moves']) > 0):
            num_of_moves = self.in_world_moves(num_of_moves)
        if((len(self.possible_next_world_list) == 1) and (len(self.remaining_worlds) > 0)):
            num_of_moves = self.next_world_moves(num_of_moves)
        if((num_of_moves > 0) and (len(self.needed_bottles_moves) > 0)):
            num_of_moves = self.possible_location_moves(num_of_moves)
        elif(num_of_moves > 0):
            self.random_moves(num_of_moves)

    def determine_world_order(self):
        shock_jump_pad_removed = False
        beak_buster_removed = False
        talon_trot_removed = False
        first_four_worlds = ["MM", "TTC", "CC", "BGS"]
        removed_level = None
        for order_count in range(1,10):
            if(order_count == 3):
                if("Shock_Jump_Pad" in self.remaining_moves):
                    self.remaining_moves.remove("Shock_Jump_Pad")
                    shock_jump_pad_removed = True
                if("Beak_Buster" in self.remaining_moves):
                    self.remaining_moves.remove("Beak_Buster")
                    beak_buster_removed = True
                if("Talon_Trot" in self.remaining_moves):
                    self.remaining_moves.remove("Talon_Trot")
                    talon_trot_removed = True
            elif(order_count == 4):
                if(shock_jump_pad_removed):
                    self.remaining_moves.append("Shock_Jump_Pad")
                if(beak_buster_removed):
                    self.remaining_moves.append("Beak_Buster")
                if(talon_trot_removed):
                    self.remaining_moves.append("Talon_Trot")
                if(len(first_four_worlds) == 1):
                    removed_level = first_four_worlds[0]
                    self.remaining_worlds.remove(removed_level)
            elif(order_count == 5):
                if(removed_level):
                    self.remaining_worlds.append(removed_level)
            self.needed_world_moves = []
            self.needed_bottles_moves = []
            self.possible_next_world_list = []
            self.prior_moves_check()
            self.available_bottles_locations()
            self.enough_available_slots()
            self.next_world = choice(self.possible_next_world_list)
            if(self.next_world in first_four_worlds):
                first_four_worlds.remove(self.next_world)
            self.remaining_worlds.remove(self.next_world)
            self.world_order_dict[self.next_world] = {}
            self.world_learnable_moves()
            self.world_order_list.append(self.next_world)

# import pprint
# pp = pprint.PrettyPrinter(indent=0)
# 
# world_order = World_Order_Bottles(bottles_world_warp_dict)
# world_order.determine_world_order()
# for world in world_order.world_order_list:
#     print('#######################################################')
#     print(f"World: {world}")
#     pp.pprint(world_order.world_order_dict[world])

# print("Start")
# for count in range(500):
#     world_order = World_Order_Bottles(bottles_world_warp_dict)
#     world_order.determine_world_order()
# print("Done")