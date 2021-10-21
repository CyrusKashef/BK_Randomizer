'''
Created on Oct 10, 2021

@author: Cyrus
'''

import os
import shutil

class CleanUp():
    def __init__(self, file_dir):
        self._file_dir = file_dir
    
    def _remove_bin_files(self, it_errored=False):
        """Removes compressed and decompressed bin files created during the randomization"""
        randomized_rom_dir = f"{self._file_dir}Randomized_ROM\\"
        for filename in os.listdir(randomized_rom_dir):
            file_path = os.path.join(randomized_rom_dir, filename)
            try:
                if((os.path.isfile(file_path) or os.path.islink(file_path)) and file_path.endswith(".bin")):
                    os.remove(file_path)
                elif(os.path.isdir(file_path)):
                    shutil.rmtree(file_path)
                elif((os.path.isfile(file_path) or os.path.islink(file_path)) and file_path.endswith(".z64") and (it_errored)):
                    os.remove(file_path)
            except Exception:# as e:
                #logger.warning('Failed to delete %s. Reason: %s' % (file_path, e))
                pass