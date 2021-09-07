'''
Created on Aug 24, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

import subprocess

####################
### FILE IMPORTS ###
####################

from .Dicts_And_Lists.Setups import setup_ids
from .Common_Functions import get_address_endpoints

#################
### FUNCTIONS ###
#################

def verify_original_header(file_bytes, address):
    """Verifies the start of an address by looking for 11 72"""
    #logger.info("Verify Original Header")
    if((file_bytes[address] != 17) or (file_bytes[address+1] != 114)):# or (file_bytes[address+2] != 0) or (file_bytes[address+3] != 0)):
        #logger.error("Error: Please verify ROM is v1.0")
        #error_window("Error During Randomization")
        raise SystemExit

def decompress_file(file_dir, compressed_file):
    """Decompresses the hex file that was extracted from the main ROM file"""
    #logger.info("Decompress File")
    cmd = f"{file_dir}GZIP.EXE -dc {file_dir}Randomized_ROM\\{compressed_file.upper()}-Compressed.bin > {file_dir}Randomized_ROM\\{compressed_file.upper()}-Decompressed.bin"
#     #logger.debug(cmd)
    subprocess.Popen(cmd.split(),shell=True).communicate()

def decompressor(file_dir, randomized_rom_path):
    """Extracts a chunk of hex values from the main ROM file into a new file and prepares the new file for decompression by providing the correct header and footer"""
    #logger.info("Decompressor")
    with open(randomized_rom_path, "rb") as file:
        file_bytes = file.read()
    address_dict = {}
    for location_name in setup_ids:
        address_list = []
        for (addr, header, footer, lead, tail) in setup_ids[location_name]:
            # Get Address Endpoints
            (address1, address2) = get_address_endpoints(file_bytes, addr)
            verify_original_header(file_bytes, address1)
            # Write Compressed File
            file_pointer = addr[2:]
            with open(f"{file_dir}Randomized_ROM\\{file_pointer}-Compressed.bin", "w+b") as comp_file:
                # Write Header
                for hex_val in header:
                    comp_file.write(bytes.fromhex(hex_val))
                # Grab Middle
#                 for index in range(address1+len(lead), address2-len(tail)):
                for index in range(address1+6, address2-len(tail)):
                    hex_string = str(hex(file_bytes[index]))[2:]
                    if(len(hex_string) < 2):
                        hex_string = "0" + hex_string
                    comp_file.write(bytes.fromhex(hex_string))
                # Write Footer
                for hex_val in footer:
                    comp_file.write(bytes.fromhex(hex_val))
            # Decompress File
            decompress_file(file_dir, file_pointer)
            address_list.append(file_pointer)
        address_dict[location_name] = address_list
    return address_dict

if __name__ == '__main__':
    pass