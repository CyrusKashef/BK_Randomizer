def get_address_endpoints(file_bytes, addr):
    """Goes to address (found in Banjo's Backpack) and address 8 bytes after to find the start and end of a setup file"""
    logger.info("Get Address Endpoints")
    byte_list = []
    for byte_num in range(16):
        byte_val = str(hex(file_bytes[int(addr, 16) + byte_num])[2:])
        if(len(str(byte_val)) < 2):
            byte_val = "0" + byte_val
        byte_list.append(byte_val)
    address1 = int("0x" + byte_list[0] + byte_list[1] + byte_list[2] + byte_list[3], 16) + int("0x10CD0", 16)
    address2 = int("0x" + byte_list[8] + byte_list[9] + byte_list[10] + byte_list[11], 16) + int("0x10CD0", 16)
    logger.debug("Address Start: " + str(hex(address1)))
    logger.debug("Address End: " + str(hex(address2)))
    return (address1, address2)

def verify_original_header(file_bytes, address):
    """Verifies the start of an address by looking for 11 72"""
    logger.info("Verify Original Header")
    if((file_bytes[address] != 17) or (file_bytes[address+1] != 114)):# or (file_bytes[address+2] != 0) or (file_bytes[address+3] != 0)):
        logger.error("Error: Please verify ROM is v1.0")
        error_window("Error During Randomization")
        raise SystemExit # exit(0)

def decompress_file(file_dir, compressed_file):
    """Decompresses the hex file that was extracted from the main ROM file"""
    logger.info("Decompress File")
    cmd = file_dir + "GZIP.EXE -dc " + file_dir + tmp_folder + compressed_file.upper() + "-Compressed.bin > " + file_dir + tmp_folder + compressed_file.upper() + "-Decompressed.bin"
#     logger.debug(cmd)
    subprocess.Popen(cmd.split(),shell=True).communicate()

def decompressor(file_dir, rom_file):
    """Extracts a chunk of hex values from the main ROM file into a new file and prepares the new file for decompression by providing the correct header and footer"""
    logger.info("Decompressor")
    # Get File Bytes
    file_bytes = get_file_bytes(file_dir, rom_file)
    address_dict = {}
    for location_name in setup_ids:
        address_list = []
        for (addr, header, footer, lead, tail) in setup_ids[location_name]:
            # Get Address Endpoints
            (address1, address2) = get_address_endpoints(file_bytes, addr)
            verify_original_header(file_bytes, address1)
            # Write Compressed File
            file_pointer = addr[2:]
            with open(file_dir + tmp_folder + file_pointer + "-Compressed.bin", "w+b") as comp_file:
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