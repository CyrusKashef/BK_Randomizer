'''
Created on Aug 24, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

import json
import subprocess

#################
### FUNCTIONS ###
#################

def leading_zeros(num, num_of_digits):
    '''Adds leading zeros to a string that's supposed to be a certain number of digits in length'''
    if(isinstance(num, int)):
        if(num < 0):
            num += 0x10000
        num = str(hex(num))[2:].upper()
    while (len(num) < num_of_digits):
        num = "0" + num
    return num

def read_json(json_file_dir):
    '''Reads contents of a JSON file into a dictionary and returns that dictionary'''
    with open(json_file_dir, "r") as jf:
        json_content = json.load(jf)
    return json_content

def dump_json(json_file_dir, use_this_dict):
    '''Reads contents of a JSON file into a dictionary and returns that dictionary'''
    with open(json_file_dir, "w+") as jf:
        json_content = json.dump(use_this_dict, jf, indent = 4)

# def apply_patch(xdelta_path, old_file_path, delta_file_path, new_file_path):
#     # xdelta -d -s old_file delta_file decoded_new_file
#     cmd = f"{xdelta_path}xdelta.exe -d -s {old_file_path} {delta_file_path} {new_file_path}"
#     print(cmd)
#     subprocess.Popen(cmd.split(), shell=True).communicate()
# 
# def create_patch(xdelta_path, old_file_path, new_file_path, delta_file_path):
#     # xdelta -e -s old_file new_file delta_file
#     cmd = f"{xdelta_path}xdelta.exe -e -s {old_file_path} {new_file_path} {delta_file_path}"
#     subprocess.Popen(cmd.split(), shell=True).communicate()

def possible_negative(int_val):
    '''If value would be a negative hex value (greater than 0x8000), converts to negative. Otherwise returns initial value'''
    if(int_val > 32768):
        int_val = int_val - 65536
    return int_val

def fit_for_hex(int_val):
    '''Prepares value for hex conversion'''
    while(int_val < 0):
        int_val = int_val + 65536
    while(int_val > 65536):
        int_val = int_val - 65536
    return int_val

def get_address_endpoints(file_bytes, addr):
    """Goes to address (found in Banjo's Backpack) and address 8 bytes after to find the start and end of a setup file"""
    byte_list = []
    for byte_num in range(16):
        byte_val = str(hex(file_bytes[int(addr, 16) + byte_num])[2:])
        if(len(str(byte_val)) < 2):
            byte_val = "0" + byte_val
        byte_list.append(byte_val)
    address1 = int("0x" + byte_list[0] + byte_list[1] + byte_list[2] + byte_list[3], 16) + int("0x10CD0", 16)
    address2 = int("0x" + byte_list[8] + byte_list[9] + byte_list[10] + byte_list[11], 16) + int("0x10CD0", 16)
    return (address1, address2)
