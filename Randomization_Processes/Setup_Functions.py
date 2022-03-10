'''
Created on Aug 24, 2021

@author: Cyrus

    #################          #################
   #                 #       1 #               #
  #  PROGRESSION GUI  # -----> # SET UP FOLDER #
   #                 #    |    #               #
    #################     |    #################
                          |
                          |    ############
                          |  2 #          #
                          |--> # SET SEED #
                          |    #          #
                          |    ############
                          |
                          |    #################
                          |  3 #               #
                          |--> # MAKE ROM COPY #
                               #               #
                               #################

'''

######################
### PYTHON IMPORTS ###
######################

import os
import shutil
from random import randint

#################
### FUNCTIONS ###
#################

def setup_tmp_folder(file_dir):
    """Creates temporary folder that'll be used to store bin files and the randomized ROM."""
    rando_rom_folder = f"{file_dir}Randomized_ROM\\"
    if(not os.path.isdir(rando_rom_folder)):
        os.mkdir(rando_rom_folder)
    else:
        for filename in os.listdir(rando_rom_folder):
            file_path = os.path.join(rando_rom_folder, filename)
            try:
                if(os.path.isfile(file_path) or os.path.islink(file_path)):
                    os.unlink(file_path)
                elif(os.path.isdir(file_path)):
                    shutil.rmtree(file_path)
            except Exception:# as e:
                #logger.error('Failed to delete %s. Reason: %s' % (file_path, e))
                pass

def set_seed(seed_val=None):
    """If seed was not provided, generates a seed value."""
    if((seed_val == None) or (seed_val == "")):
        seed_val = randint(10000000, 19940303)
    return int(seed_val)

def make_copy_of_rom(seed_val, file_dir, original_rom):
    """Creates a copy of the rom that will be used for randomization"""
    randomized_rom_file = f"{file_dir}Randomized_ROM\\Banjo-Kazooie_Randomized_Seed_{str(seed_val)}.z64"
    shutil.copyfile(original_rom, randomized_rom_file)
    return randomized_rom_file

if __name__ == '__main__':
    pass