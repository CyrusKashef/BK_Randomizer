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

from Dicts_And_Lists.Warps import level_warps

#################
### FUNCTIONS ###
#################

def obtain_possible_next_worlds(remaining_worlds, learned_moves):
    possible_next_world = []
    for world_name in remaining_worlds:
        if(level_warps[world_name]["Prior_Moves"] == []):
            possible_next_world.append(world_name)
        for learnable_move in level_warps[world_name]["Prior_Moves"]:
            if(learnable_move in learned_moves):
                possible_next_world.append(world_name)
                break
    return possible_next_world

def learnable_moves(world_name, remaining_moves):
    learned_move_list = []
    for count in range(level_warps[world_name]["Bottles_Count"]):
        if(level_warps[world_name]["Must_Learn_Move"] in remaining_moves):
            learned_move = level_warps[world_name]["Must_Learn_Move"]
        else:
            learned_move = choice(remaining_moves)
        learned_move_list.append(learned_move)
        remaining_moves.remove(learned_move)
    return learned_move_list, remaining_moves

def world_order_with_moves():
    remaining_worlds = [world_name for world_name in level_warps]
    remaining_moves = ["Talon_Trot", "Beak_Buster", "Eggs", "Fly", "Shock_Jump_Pad", "Wonderwing", "Wading_Boots", "Turbo_Talon_Trot", "Beak_Bomb"]
    world_order = {}
    learned_moves = []
    first_worlds = True
    for world_num in range(len(level_warps)):
        if((world_num == 3) and first_worlds):
            possible_next_world = obtain_possible_next_worlds(["GV", "FP", "MMM", "RBB", "CCW"], learned_moves)
        else:
            possible_next_world = obtain_possible_next_worlds(remaining_worlds, learned_moves)
        next_world = choice(possible_next_world)
        if(next_world in ["GV", "FP", "MMM", "RBB", "CCW"]):
            first_worlds = False
        learned_move_list, remaining_moves = learnable_moves(next_world, remaining_moves)
        world_order[world_num] = {}
        world_order[world_num]["World_Name"] = next_world
        world_order[world_num]["Learned_Moves"] = learned_move_list
        remaining_worlds.remove(next_world)
        for learned_move in learned_move_list:
            learned_moves.append(learned_move)
    return world_order

if __name__ == '__main__':
    world_order = world_order_with_moves()
    for world_num in world_order:
        print("World Num: " + str(world_num))
        print("\tWorld: " + world_order[world_num]["World_Name"])
        print("\tLearn Moves: " + str(world_order[world_num]["Learned_Moves"]))