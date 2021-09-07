'''
Created on Aug 24, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

import random

#######################
### TESTING IMPORTS ###
#######################

from Dicts_And_Lists.In_World_Warps import *

#################
### FUNCTIONS ###
#################

def all_warps_lists(warps_dict):
    warp_list = warps_dict["Safe"] + warps_dict["Unsafe"]
    transform_warp_list = warps_dict["Safe_Transform"] + warps_dict["Unsafe_Transform"]
    return warp_list, transform_warp_list

def find_a_loop(safe_warps, warp_list):
    safe_choice = random.choice(safe_warps)
    warps_loop = [safe_choice]
#     print(f"Warp List: {warp_list}")
    warp_list.remove(safe_choice)
    warp_choice = random.choice(warp_list)
    warp_list.remove(warp_choice)
    warps_loop.append(warp_choice)
    if(warp_choice in safe_warps):
        safe_warps.remove(warp_choice)
    while((warp_choice != safe_choice) and (len(warp_list) > 1)):
        choice_list = [safe_choice] + warp_list
        warp_choice = random.choice(choice_list)
        warps_loop.append(warp_choice)
        if(warp_choice in warp_list):
            warp_list.remove(warp_choice)
        if(warp_choice in safe_warps):
            safe_warps.remove(warp_choice)
    if(warps_loop[-1] != safe_choice):
        warps_loop.append(safe_choice)
        safe_warps.remove(safe_choice)
#     print(f"Warps Loop: {warps_loop}")
#     print(f"Warp List:  {warp_list}")
#     print(f"Safe Warps: {safe_warps}")
    return warps_loop, warp_list, safe_warps

def safe_in_list(safe_warps, warp_list):
    for warp in warp_list:
        if(warp in safe_warps):
            return True
    return False

def last_loop(safety_warp, warp_list):
    warps_loop = [safety_warp]
    while(len(warp_list) > 0):
        warp_choice = random.choice(warp_list)
        warps_loop.append(warp_choice)
        warp_list.remove(warp_choice)
    warps_loop.append(safety_warp)
    return warps_loop

def in_world_warp_logic_main(warps_dict):
    warp_list, transform_warp_list = all_warps_lists(warps_dict)
    if(len(warp_list) > 0):
        warp_loop_list = []
        safe_warps = warps_dict["Safe"]
        safety_warp = random.choice(safe_warps)
#         print(f"Safety Warp: {safety_warp}")
        safe_warps.remove(safety_warp)
        warp_list.remove(safety_warp)
        safe_boolean = safe_in_list(safe_warps, warp_list)
        while(safe_boolean and (len(warp_list) > 1)):
#             print(f"Warp List: {warp_list}")
            warps_loop, warp_list, safe_warps = find_a_loop(safe_warps, warp_list)
#             print(f"Warp Loop: {warps_loop}")
            warp_loop_list.append(warps_loop)
            safe_boolean = safe_in_list(safe_warps, warp_list)
        warps_loop = last_loop(safety_warp, warp_list)
        warp_loop_list.append(warps_loop)
        print(f"Warps Loop List: {warp_loop_list}")
    if(len(transform_warp_list) > 0):
        transformation_warp_loop_list = []
        safe_warps = warps_dict["Safe_Transform"]
        safety_warp = random.choice(safe_warps)
#         print(f"Safety Warp: {safety_warp}")
        safe_warps.remove(safety_warp)
        transform_warp_list.remove(safety_warp)
        safe_boolean = safe_in_list(safe_warps, transform_warp_list)
        while(safe_boolean and (len(transform_warp_list) > 1)):
            warps_loop, transform_warp_list, safe_warps = find_a_loop(safe_warps, transform_warp_list)
            transformation_warp_loop_list.append(warps_loop)
            safe_boolean = safe_in_list(safe_warps, transform_warp_list)
        warps_loop = last_loop(safety_warp, transform_warp_list)
        transformation_warp_loop_list.append(warps_loop)
        print(f"Transformation Warps Loop List: {transformation_warp_loop_list}")

if __name__ == '__main__':
    in_world_warp_logic_main(mm_warps_dict)
    in_world_warp_logic_main(ttc_warps_dict)
    in_world_warp_logic_main(cc_warps_dict)
    in_world_warp_logic_main(bgs_warps_dict)
    in_world_warp_logic_main(fp_warps_dict)
    in_world_warp_logic_main(gv_warps_dict)
    in_world_warp_logic_main(mmm_warps_dict)
    in_world_warp_logic_main(rbb_warps_dict)
    in_world_warp_logic_main(ccw_spring_warps_dict)
    in_world_warp_logic_main(ccw_summer_warps_dict)
    in_world_warp_logic_main(ccw_fall_warps_dict)
    in_world_warp_logic_main(ccw_winter_warps_dict)
    in_world_warp_logic_main(ccw_all_warps_dict)