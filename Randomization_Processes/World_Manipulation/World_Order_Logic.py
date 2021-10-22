'''
Created on Aug 23, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

from random import choice

####################
### FILE IMPORTS ###
####################

from ..Dicts_And_Lists.Warps import basic_world_warp_dict

#################
### FUNCTIONS ###
#################

class World_Order_Basic():
    def __init__(self):
        self.remaining_worlds = [world_name for world_name in basic_world_warp_dict]
        self.remaining_moves = ["Talon_Trot", "Beak_Buster", "Eggs", "Fly", "Shock_Jump_Pad", "Wonderwing", "Wading_Boots", "Turbo_Talon_Trot", "Beak_Bomb"]
        self.world_order_dict = {}
        self.learned_moves = []
        self.first_worlds = True
    
    def _obtain_possible_next_worlds(self, temp_list=None):
        if(temp_list):
            world_list = temp_list
        else:
            world_list = self.remaining_worlds
        possible_next_world = []
        for world_name in world_list:
            if(basic_world_warp_dict[world_name]["Prior_Moves"] == []):
                possible_next_world.append(world_name)
            for learnable_move in basic_world_warp_dict[world_name]["Prior_Moves"]:
                if(learnable_move in self.learned_moves):
                    possible_next_world.append(world_name)
                    break
        return possible_next_world

    def _learnable_moves(self, world_name):
        learned_move_list = []
        for count in range(basic_world_warp_dict[world_name]["Bottles_Count"]):
            if(basic_world_warp_dict[world_name]["Must_Learn_Move"] in self.remaining_moves):
                learned_move = basic_world_warp_dict[world_name]["Must_Learn_Move"]
            else:
                learned_move = choice(self.remaining_moves)
            learned_move_list.append(learned_move)
            self.remaining_moves.remove(learned_move)
        return learned_move_list

    def _world_order_with_moves(self):
        for world_num in range(1, len(basic_world_warp_dict)+1):
            if((world_num == 3) and self.first_worlds):
                possible_next_world = self._obtain_possible_next_worlds(["GV", "FP", "MMM", "RBB", "CCW"])
            else:
                possible_next_world = self._obtain_possible_next_worlds()
            next_world = choice(possible_next_world)
            if(next_world in ["GV", "FP", "MMM", "RBB", "CCW"]):
                self.first_worlds = False
            learned_move_list = self._learnable_moves(next_world)
            self.world_order_dict[world_num] = {}
            self.world_order_dict[world_num]["World_Name"] = next_world
            self.world_order_dict[world_num]["Learned_Moves"] = learned_move_list
            self.remaining_worlds.remove(next_world)
            for learned_move in learned_move_list:
                self.learned_moves.append(learned_move)

# world_order = World_Order_Basic()
# world_order._world_order_with_moves()
# for world_num in world_order.world_order_dict:
#     print("World Num: " + str(world_num))
#     print("\tWorld: " + world_order.world_order_dict[world_num]["World_Name"])
#     print("\tLearn Moves: " + str(world_order.world_order_dict[world_num]["Learned_Moves"]))