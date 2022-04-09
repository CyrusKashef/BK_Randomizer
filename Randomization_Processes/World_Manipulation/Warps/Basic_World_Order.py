'''
Created on Aug 23, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

import random

#################
### FUNCTIONS ###
#################

class World_Order_Basic():
    def __init__(self, seed_val=0, world_exits="Exit From World You Were Just In", removed_detransformations=0):
        self._seed_val = seed_val
        self._world_exits = world_exits
        self.transform_cost_dict = {}
        self.removed_detransformations = removed_detransformations

    def _determine_world_order_normal(self):
        '''Creates a random order for the worlds'''
        self.world_order_list = ["Treasure Trove Cove", "Clanker's Cavern", "Bubblegloop Swamp", "Freezeezy Peak", "Gobi's Valley", "Mad Monster Mansion", "Rusty Bucket Bay", "Click Clock Wood"]
        random.seed(a=self._seed_val)
        random.shuffle(self.world_order_list)
        self.world_order_list.insert(0, "Mumbo's Mountain")

    def _determine_world_order_adjusted(self):
        '''Creates a random order for the worlds'''
        self.world_order_list = ["Treasure Trove Cove", "Clanker's Cavern", "Bubblegloop Swamp", "Freezeezy Peak", "Gobi's Valley", "Rusty Bucket Bay", "Click Clock Wood"]
        random.seed(a=self._seed_val)
        random.shuffle(self.world_order_list)
        self.world_order_list.insert(0, "Mumbo's Mountain")
        self.world_order_list.insert(6, "Mad Monster Mansion")

    def _transformation_costs(self):
        '''PyDoc'''
        for transformation_name in ["Termite", "Crocodile", "Walrus", "Pumpkin", "Bee"]:
            self.transform_cost_dict[transformation_name] = 0
        if(self.removed_detransformations == 0):
            transformation_cost = 5
            for world in self.world_order_list:
                if(world == "Mumbo's Mountain"):
                    self.transform_cost_dict["Termite"] = transformation_cost
                    transformation_cost += 5
                elif(world == "Bubblegloop Swamp"):
                    self.transform_cost_dict["Crocodile"] = transformation_cost
                    transformation_cost += 5
                elif(world == "Freezeezy Peak"):
                    self.transform_cost_dict["Walrus"] = transformation_cost
                    transformation_cost += 5
                elif(world == "Mad Monster Mansion"):
                    self.transform_cost_dict["Pumpkin"] = transformation_cost
                    transformation_cost += 5
                elif(world == "Click Clock Wood"):
                    self.transform_cost_dict["Bee"] = transformation_cost
                    transformation_cost += 5

    def _world_order_main(self):
        '''Main function to shuffle the world entrance warps within the lair'''
        if(self._world_exits == "Exit From World You Were Just In"):
            self._determine_world_order_normal()
            self._transformation_costs()
        elif(self._world_exits == "Exit From Entrance You Entered From"):
            self._determine_world_order_adjusted()
            self._transformation_costs()
        else:
            print("Basic World Entrance Mode?")
            raise SystemError
