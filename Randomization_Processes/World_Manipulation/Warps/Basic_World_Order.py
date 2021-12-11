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
    def __init__(self, seed_val=0):
        self._seed_val = seed_val
        self.world_order_list = ["Treasure Trove Cove", "Clanker's Cavern", "Bubblegloop Swamp", "Freezeezy Peak", "Gobi's Valley", "Mad Monster Mansion", "Rusty Bucket Bay", "Click Clock Wood"]

    def _determine_world_order(self):
        '''Creates a random order for the worlds'''
        random.seed(a=self._seed_val)
        random.shuffle(self.world_order_list)

    def _world_order_main(self):
        '''Main function to shuffle the world entrance warps within the lair'''
        self._determine_world_order()