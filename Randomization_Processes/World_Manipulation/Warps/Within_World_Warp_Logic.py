'''
Created on Nov 27, 2021

@author: Cyrus
'''

import random

from Randomization_Processes.Dicts_And_Lists.In_World_Warps import warp_dict

class Within_World_Warps_Class():
    def __init__(self, warp_dict, seed=0, shuffle_by="World"):
        self.seed = seed
        self.warp_dict = {}
        self.warp_dict["Safe"] = {}
        self.warp_dict["Safe_Transform"] = {}
        self.warp_dict["Unsafe"] = {}
        self.warp_dict["Unsafe_Transform"] = {}
        if(shuffle_by == "World"):
            for warp in warp_dict["Safe"]:
                self.warp_dict["Safe"][warp] = warp_dict["Safe"][warp]
            for warp in warp_dict["Safe_Transform"]:
                self.warp_dict["Safe_Transform"][warp] = warp_dict["Safe_Transform"][warp]
            for warp in warp_dict["Unsafe"]:
                self.warp_dict["Unsafe"][warp] = warp_dict["Unsafe"][warp]
            for warp in warp_dict["Unsafe_Transform"]:
                self.warp_dict["Unsafe_Transform"][warp] = warp_dict["Unsafe_Transform"][warp]
        elif(shuffle_by == "Game"):
            for world in warp_dict:
                if("-" not in world):
                    for warp in warp_dict[world]["Safe"]:
                        self.warp_dict["Safe"][warp] = warp_dict[world]["Safe"][warp]
                    for warp in warp_dict[world]["Safe_Transform"]:
                        self.warp_dict["Safe_Transform"][warp] = warp_dict[world]["Safe_Transform"][warp]
                    for warp in warp_dict[world]["Unsafe"]:
                        self.warp_dict["Unsafe"][warp] = warp_dict[world]["Unsafe"][warp]
                    for warp in warp_dict[world]["Unsafe_Transform"]:
                        self.warp_dict["Unsafe_Transform"][warp] = warp_dict[world]["Unsafe_Transform"][warp]
        self.new_warp_dict = {}
        self.global_warp_dict = {}
        self.global_increment = 0
    
    def _choose_from_list(self, original_list):
        '''Selects an option from a list based on the current address and the number of increments, if applicable'''
        random.seed(a=(self.seed +self.global_increment))
        random_choice = random.choice(original_list)
        self.global_increment += 1
        return random_choice
    
    def _within_game_warp_dict(self):
        warp_list = []
        transform_warp_list = []
        for world in self.warp_dict:
            for item in self.warp_dict[world]["Safe"]:
                warp_list.append(item)
            for item in self.warp_dict[world]["Unsafe"]:
                warp_list.append(item)
            for item in self.warp_dict[world]["Safe_Transform"]:
                transform_warp_list.append(item)
            for item in self.warp_dict[world]["Unsafe_Transform"]:
                transform_warp_list.append(item)
        return warp_list, transform_warp_list
    
    def _all_warps_lists(self):
        warp_list = []
        for item in self.warp_dict["Safe"]:
            warp_list.append(item)
            self.global_warp_dict[item] = self.warp_dict["Safe"][item][0][16:20]
        for item in self.warp_dict["Unsafe"]:
            warp_list.append(item)
            self.global_warp_dict[item] = self.warp_dict["Unsafe"][item][0][16:20]
        transform_warp_list = []
        for item in self.warp_dict["Safe_Transform"]:
            transform_warp_list.append(item)
            self.global_warp_dict[item] = self.warp_dict["Safe_Transform"][item][0][16:20]
        for item in self.warp_dict["Unsafe_Transform"]:
            transform_warp_list.append(item)
            self.global_warp_dict[item] = self.warp_dict["Unsafe_Transform"][item][0][16:20]
        return warp_list, transform_warp_list

    def _find_a_loop(self, safe_warps, warp_list):
        safe_choice = self._choose_from_list(safe_warps)
        warps_loop = [safe_choice]
        warp_list.remove(safe_choice)
        warp_choice = self._choose_from_list(warp_list)
        warp_list.remove(warp_choice)
        warps_loop.append(warp_choice)
        if(warp_choice in safe_warps):
            safe_warps.remove(warp_choice)
        while((warp_choice != safe_choice) and (len(warp_list) > 1)):
            choice_list = [safe_choice] + warp_list
            warp_choice = self._choose_from_list(choice_list)
            warps_loop.append(warp_choice)
            if(warp_choice in warp_list):
                warp_list.remove(warp_choice)
            if(warp_choice in safe_warps):
                safe_warps.remove(warp_choice)
        if(warps_loop[-1] != safe_choice):
            warps_loop.append(safe_choice)
            safe_warps.remove(safe_choice)
        return warps_loop, warp_list, safe_warps
    
    def _safe_in_list(self, safe_warps, warp_list):
        for warp in warp_list:
            if(warp in safe_warps):
                return True
        return False
    
    def _last_loop(self, safety_warp, warp_list):
        warps_loop = [safety_warp]
        while(len(warp_list) > 0):
            warp_choice = self._choose_from_list(warp_list)
            warps_loop.append(warp_choice)
            warp_list.remove(warp_choice)
        warps_loop.append(safety_warp)
        return warps_loop
    
    def _new_warp_dict(self, loop_list):
        for warp_loop in loop_list:
            for list_index in range(len(warp_loop) - 1):
                if("Inside" in warp_loop[list_index]):
                    self.new_warp_dict[warp_loop[list_index].replace("Inside", "Outside")] = self.global_warp_dict[warp_loop[list_index + 1]]
                elif("Outside" in warp_loop[list_index]):
                    self.new_warp_dict[warp_loop[list_index].replace("Outside", "Inside")] = self.global_warp_dict[warp_loop[list_index + 1]]
        print(self.new_warp_dict)
    
    def _non_transformation_warps(self, warp_list):
        if(len(self.warp_dict["Safe"]) > 0):
            warp_loop_list = []
            safe_warps = []
            for items in self.warp_dict["Safe"]:
                safe_warps.append(items)
            safety_warp = self._choose_from_list(safe_warps)
            safe_warps.remove(safety_warp)
            warp_list.remove(safety_warp)
            self.warp_dict["Safe"].pop(safety_warp)
            safe_boolean = self._safe_in_list(safe_warps, warp_list)
            while(safe_boolean and (len(self.warp_dict) > 1)):
                warps_loop, warp_list, safe_warps = self._find_a_loop(safe_warps, warp_list)
                warp_loop_list.append(warps_loop)
                safe_boolean = self._safe_in_list(safe_warps, warp_list)
            warps_loop = self._last_loop(safety_warp, warp_list)
            warp_loop_list.append(warps_loop)
            print(f"Warps Loop List: {warp_loop_list}")
            self._new_warp_dict(warp_loop_list)
            
    def _transformation_warps(self, transform_warp_list):
        if(len(transform_warp_list) > 0):
            transformation_warp_loop_list = []
            safe_warps = []
            for item in self.warp_dict["Safe_Transform"]:
                safe_warps.append(item)
            safety_warp = self._choose_from_list(safe_warps)
            safe_warps.remove(safety_warp)
            transform_warp_list.remove(safety_warp)
            safe_boolean = self._safe_in_list(safe_warps, transform_warp_list)
            while(safe_boolean and (len(transform_warp_list) > 1)):
                warps_loop, transform_warp_list, safe_warps = self._find_a_loop(safe_warps, transform_warp_list)
                transformation_warp_loop_list.append(warps_loop)
                safe_boolean = self._safe_in_list(safe_warps, transform_warp_list)
            warps_loop = self._last_loop(safety_warp, transform_warp_list)
            transformation_warp_loop_list.append(warps_loop)
#             print(f"Transformation Warps Loop List: {transformation_warp_loop_list}")
            self._new_warp_dict(transformation_warp_loop_list)
    
    def _main(self):
        warp_list, transform_warp_list = self._all_warps_lists()
        self._non_transformation_warps(warp_list)
        self._transformation_warps(transform_warp_list)
        
if __name__ == '__main__':
    print("Mumbo's Mountain")
    within_world_warps_class = Within_World_Warps_Class(warp_dict["Mumbo's Mountain"], seed=14767031)
    within_world_warps_class._main()
#     print("##############################")
#     print("Treasure Trove Cove")
#     within_world_warps_class = Within_World_Warps_Class(warp_dict["Treasure Trove Cove"])
#     within_world_warps_class._main()
#     print("##############################")
#     print("Clanker's Cavern")
#     within_world_warps_class = Within_World_Warps_Class(warp_dict["Clanker's Cavern"])
#     within_world_warps_class._main()
#     print("##############################")
#     print("Bubblegloop Swamp")
#     within_world_warps_class = Within_World_Warps_Class(warp_dict["Bubblegloop Swamp"])
#     within_world_warps_class._main()
#     print("##############################")
#     print("Freezeezy Peak")
#     within_world_warps_class = Within_World_Warps_Class(warp_dict["Freezeezy Peak"])
#     within_world_warps_class._main()
#     print("##############################")
#     print("Gobi's Valley")
#     within_world_warps_class = Within_World_Warps_Class(warp_dict["Gobi's Valley"])
#     within_world_warps_class._main()
#     print("##############################")
#     print("Mad Monster Mansion")
#     within_world_warps_class = Within_World_Warps_Class(warp_dict["Mad Monster Mansion"])
#     within_world_warps_class._main()
#     print("##############################")
#     print("Rusty Bucket Bay")
#     within_world_warps_class = Within_World_Warps_Class(warp_dict["Rusty Bucket Bay"])
#     within_world_warps_class._main()
#     print("##############################")
#     print("Click Clock Wood Spring")
#     within_world_warps_class = Within_World_Warps_Class(warp_dict["Click Clock Wood - Spring"])
#     within_world_warps_class._main()
#     print("##############################")
#     print("Click Clock Wood")
#     within_world_warps_class = Within_World_Warps_Class(warp_dict["Click Clock Wood"])
#     within_world_warps_class._main()
#     print("##############################")
#     print("Shuffle By Game")
#     within_world_warps_class = Within_World_Warps_Class(warp_dict, shuffle_by="Game")
#     within_world_warps_class._main()