'''
Created on Sep 23, 2021

@author: Cyrus
'''

import random

from Randomization_Processes.Dicts_And_Lists import World_Order_Warps

class World_Order_Bottles():
    def __init__(self, seed_val=0):
        self.seed_val = seed_val
        self.remaining_moves = [move for move in World_Order_Warps.learnable_moves_dict]
        self.learned_moves = []
        self.remaining_worlds = [world for world in World_Order_Warps.bottles_world_warp_dict]
        self.world_order_list = []
        self.world_order_dict = {}

    def _possible_next_worlds(self):
        '''PyDoc'''
        self.possible_next_world_list = []
        for world_name in self.remaining_worlds:
            # Does BK have the moves to even do anything in that world?
            if(len(World_Order_Warps.bottles_world_warp_dict[world_name]["Prior_Moves"]) > 0):
                use_this_world = False
                for prior_move_list in World_Order_Warps.bottles_world_warp_dict[world_name]["Prior_Moves"]:
                    know_prior_moves = True
                    for prior_move in prior_move_list:
                        if(prior_move not in self.learned_moves):
                            know_prior_moves = False
                    if(know_prior_moves):
                        use_this_world = True
                        break
                if(not use_this_world):
#                     print(f"{world_name} Doesn't Have Prior Moves")
                    continue
            # Are there enough possible move locations for BK to learn the moves they need?
            possible_bottles_count = 0
            for available_bottles_location in World_Order_Warps.bottles_world_warp_dict[world_name]["Available_Bottles"]:
                if(len(World_Order_Warps.bottles_world_warp_dict[world_name]["Possible_Bottles"][available_bottles_location]) == 0):
                    possible_bottles_count += 1
                    continue
                for prior_move_list in World_Order_Warps.bottles_world_warp_dict[world_name]["Possible_Bottles"][available_bottles_location]:
                    know_prior_moves = True
                    for prior_move in prior_move_list:
                        if(prior_move not in self.learned_moves):
                            know_prior_moves = False
                            break
                    if(know_prior_moves):
                        possible_bottles_count += 1
                        break
            for learned_move in self.learned_moves:
                if(learned_move in World_Order_Warps.bottles_world_warp_dict[world_name]["In_World_Moves"]):
                    World_Order_Warps.bottles_world_warp_dict[world_name]["In_World_Moves"].remove(learned_move)
            if(len(World_Order_Warps.bottles_world_warp_dict[world_name]["In_World_Moves"]) <= possible_bottles_count):
                self.possible_next_world_list.append(world_name)
#                 print(f"{world_name} Is A Possible Next World")
#             else:
#                 print(f"{world_name} Doesn't Have Enough Bottles Spots: {possible_bottles_count} < {len(World_Order_Warps.bottles_world_warp_dict[world_name]['In_World_Moves'])}")         

    def _next_world_moves(self, next_world):
        '''PyDoc'''
        self.world_order_dict[next_world]["Learned_Moves"] = {}
        for in_world_moves in World_Order_Warps.bottles_world_warp_dict[next_world]["In_World_Moves"]:
            if(type(in_world_moves) == type("")):
                selected_move = in_world_moves
            else:
                random.seed(a=self.seed_val)
                selected_move = random.choice(in_world_moves)
            if(selected_move in self.learned_moves):
                continue
            possible_bottles = []
            for available_bottles_location in World_Order_Warps.bottles_world_warp_dict[next_world]["Available_Bottles"]:
                if(len(World_Order_Warps.bottles_world_warp_dict[next_world]["Possible_Bottles"][available_bottles_location]) == 0):
                    possible_bottles.append(available_bottles_location)
                    continue
                for prior_move_list in World_Order_Warps.bottles_world_warp_dict[next_world]["Possible_Bottles"][available_bottles_location]:
                    know_prior_moves = True
                    for prior_move in prior_move_list:
                        if(prior_move not in self.learned_moves):
                            know_prior_moves = False
                            break
                    if(know_prior_moves):
                        possible_bottles.append(available_bottles_location)
                        break
            random.seed(a=self.seed_val)
            bottles_location = random.choice(sorted(possible_bottles))
            World_Order_Warps.bottles_world_warp_dict[next_world]["Available_Bottles"].remove(bottles_location)
            self.remaining_moves.remove(selected_move)
            self.learned_moves.append(selected_move)
            self.world_order_dict[next_world]["Learned_Moves"][bottles_location] = selected_move
        for move_num in range(len(World_Order_Warps.bottles_world_warp_dict[next_world]["Available_Bottles"]) - len(self.world_order_dict[next_world]["Learned_Moves"])):
            if(len(self.remaining_moves) == 0):
                break
            random.seed(a=self.seed_val)
            selected_move = random.choice(self.remaining_moves)
            possible_bottles = []
            for available_bottles_location in World_Order_Warps.bottles_world_warp_dict[next_world]["Available_Bottles"]:
                if(len(World_Order_Warps.bottles_world_warp_dict[next_world]["Possible_Bottles"][available_bottles_location]) == 0):
                    possible_bottles.append(available_bottles_location)
                    continue
                for prior_move_list in World_Order_Warps.bottles_world_warp_dict[next_world]["Possible_Bottles"][available_bottles_location]:
                    know_prior_moves = True
                    for prior_move in prior_move_list:
                        if(prior_move not in self.learned_moves):
                            know_prior_moves = False
                            break
                    if(know_prior_moves):
                        possible_bottles.append(available_bottles_location)
                        break
            if(len(possible_bottles) > 0):
                random.seed(a=self.seed_val)
                bottles_location = random.choice(sorted(possible_bottles))
                World_Order_Warps.bottles_world_warp_dict[next_world]["Available_Bottles"].remove(bottles_location)
                self.remaining_moves.remove(selected_move)
                self.learned_moves.append(selected_move)
                self.world_order_dict[next_world]["Learned_Moves"][bottles_location] = selected_move
            else:
                break

    def _determine_world_order(self):
        '''PyDoc'''
        for world_num in range(1, 10):
            self._possible_next_worlds()
            random.seed(a=self.seed_val)
            next_world = random.choice(sorted(self.possible_next_world_list))
#             print(next_world)
            self.world_order_list.append(next_world)
            self.world_order_dict[next_world] = {"Order": world_num}
            self.remaining_worlds.remove(next_world)
            self._next_world_moves(next_world)

if __name__ == '__main__':
    import pprint
    pp = pprint.PrettyPrinter(indent=0)
    world_order = World_Order_Bottles()
    world_order._determine_world_order()
    for world in world_order.world_order_list:
        print('#######################################################')
        print(f"World: {world}")
        pp.pprint(world_order.world_order_dict[world])