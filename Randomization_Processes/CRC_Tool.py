'''
Created on Sep 13, 2021

@author: Cyrus
'''

import os
import subprocess

def run_crc_tool(seed_val, file_dir):
    '''Runs the CRC Tool that allows a modified game to run'''
    cmd =  f"{os.getcwd()}/rn64crc2/rn64crc.exe -u {os.getcwd()}/Randomized_ROM/Banjo-Kazooie_Randomized_Seed_{str(seed_val)}.z64"
    subprocess.Popen(cmd.split(),shell=True).communicate()