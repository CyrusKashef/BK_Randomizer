'''
Created on Aug 30, 2021

@author: Cyrus
'''

class World():
    def __init__(self, world_name=None):
        self._world_name = world_name
        self._setup_list = []
    
    def _add_setup_file(self, setup_object):
        self._setup_list.append(setup_object)