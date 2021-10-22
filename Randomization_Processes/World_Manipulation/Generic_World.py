'''
Created on Aug 30, 2021

@author: Cyrus
'''

###########################
### GENERIC WORLD CLASS ###
###########################

class World():
    '''Generic World Class'''
    def __init__(self, world_name=None):
        '''Initializes world class'''
        self._world_name = world_name
        self._setup_list = []
    
    def _add_setup_file(self, setup_object):
        '''Adds a setup file to the world'''
        self._setup_list.append(setup_object)