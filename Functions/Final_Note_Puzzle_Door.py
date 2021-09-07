def modify_bottles_unskipable_text(file_dir, new_bottles_text):
    '''Modifies the Bottles text at the beginning of the game'''
    # 5) Able to modify 5C9AF8/CF90.bin
    # (PRESS A IF YOU WANT ME TO TEACH YOU SOME BASIC MOVES, OR PRESS B IF YOU THINK YOU'RE ALREADY GOOD ENOUGH!)
    # "WELCOME TO BANJO KAZOOIE RANDOMIZER V. 0.7.6! THIS GENERATED SEED NEEDS 000 NOTES 000 JIGGIES" + also_add
    # "YOU'LL NEED 000 NOTES TO PASS THE FINAL NOTE DOOR! PRESS A FOR LESSONS OR PRESS B TO SKIP MY NOTES! HAHA!"
    # "YOU'LL NEED 000 JIGGIES TO PASS THE FINAL PUZZLE DOOR! PRESS B TO GO OR PRESS A IF YOU'RE PUZZLED!"
    # "WELCOME TO BANJO-KAZOOIE RANDOMIZER VERSION 0.7.6!!! HOPE YOU ENJOY THE GENERATED SEED!!" + also_add
    
    with open(file_dir + tmp_folder + "CF90-Decompressed.bin", "r+b") as decomp_file:
        mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
        text_index_start = mm_decomp.find(bytes.fromhex("50524553532041"))
        count = 0
        for char in new_bottles_text:
            mm_decomp[text_index_start + count] = ord(char)
            count += 1
        for index in range(text_index_start + len(new_bottles_text), len(mm_decomp)):
            mm_decomp[index] = mm_decomp[index]

def final_note_door_mode(file_dir, seed_val, final_note_score_lower, final_note_score_upper):
    '''Sets the requirements of every note door to zero except for the note door proceeding the final battle'''
    # Find location of note doors
    # 00 32 00 B4 01 04 01 5E 01 C2 02 80 02 FD 03 2A 03 3C 03 4E 03 60 03 72
    # Every 2 are a note door
    # Edit each note door with zeros
    # Max Notes Is 900
    if((final_note_score_lower < 0) or (final_note_score_lower == "")):
        final_note_score_lower = 0
    if((final_note_score_upper > 900) or (final_note_score_upper == "")):
        final_note_score_upper = 900
    if(final_note_score_upper <= 0):
        final_note_score = 0
    elif(final_note_score_lower >= 900):
        final_note_score = 900
    else:
        random.seed(a=seed_val)
        final_note_score = random.randint(final_note_score_lower, final_note_score_upper)
    with open(file_dir + tmp_folder + "FCF698-Decompressed.bin", "r+b") as decomp_file:
        mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
        #                                                      0 1 2 3 4 5 6 7 8 91011121314151617181920212223
        note_door_index_start = mm_decomp.find(bytes.fromhex("003200B40104015E01C2028002FD032A033C034E03600372"))
        for offset in range(14):
            mm_decomp[note_door_index_start + offset] = 0
        for offset in range(16, 24):
            mm_decomp[note_door_index_start + offset] = 0
        final_note_score_hex = leading_zeros(str(hex(final_note_score))[2:], 4)
        mm_decomp[note_door_index_start + 14] = int(final_note_score_hex[:2], 16)
        mm_decomp[note_door_index_start + 15] = int(final_note_score_hex[2:], 16)
    return final_note_score

def modify_world_puzzle_requirements(file_dir, seed_val, final_puzzle_lower, final_puzzle_upper):
    '''Sets the requirements of every puzzle to zero except for the puzzle proceeding the final battle'''
    # Find location of world puzzles
    # 00 00 01 01 00 5D 02 02 00 5E 05 03 00 60 07 03 00 63 08 04 00 66 09 04 00 6A 0A 04 00 6E 0C 04 00 72 0F 04 00 76 19 05 00 7A 04 03
    # Every 4 is a note door, with the third value being the one you have to change
    if((final_puzzle_lower < 0) or (final_puzzle_lower == "")):
        final_puzzle_lower = 0
    if((final_puzzle_upper > 99) or (final_puzzle_upper == "")):
        final_puzzle_upper = 99
    if(final_puzzle_upper <= 0):
        final_puzzle_score = 0
    elif(final_puzzle_lower >= 99):
        final_puzzle_score = 99
    else:
        random.seed(a=seed_val)
        final_puzzle_score = random.randint(final_puzzle_lower, final_puzzle_upper)
    with open(file_dir + tmp_folder + "FCF698-Decompressed.bin", "r+b") as decomp_file:
        mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
        #                                                      0 1 2 3 4 5 6 7 8 910111213141516171819202122232425262728293031323334353637383940414243
        note_door_index_start = mm_decomp.find(bytes.fromhex("00000101005D0202005E0503006007030063080400660904006A0A04006E0C0400720F0400761905007A0403"))
        for offset in range(0, 37, 4):
            mm_decomp[note_door_index_start + offset + 2] = 0
        mm_decomp[note_door_index_start + 38] = final_puzzle_score
        honeycomb_puzzle_count = 100 - final_puzzle_score
        if(honeycomb_puzzle_count > 4):
            honeycomb_puzzle_count = 4
        mm_decomp[note_door_index_start + 42] = honeycomb_puzzle_count
    return final_puzzle_score

def decompress_generic_individual_misc_file(file_dir, rom_file, file_type):
    """Extracts a chunk of hex values from the main ROM file into a new file and prepares the new file for decompression by providing the correct header and footer"""
    logger.info("Decompressor")
    # Get File Bytes
    file_bytes = get_file_bytes(file_dir, rom_file)
    (addr, header, footer, lead, tail) = misc_setup_ids[file_type][0]
    if(addr.startswith("0x")):
        # Get Address Endpoints
        (address1, address2) = get_address_endpoints(file_bytes, addr)
        verify_original_header(file_bytes, address1)
        # Write Compressed File
        file_pointer = addr[2:]
    else:
        # Get Address Endpoints
        address1 = int(addr.split(",")[0], 16)
        address2 = int(addr.split(",")[1], 16)
        verify_original_header(file_bytes, address1)
        file_pointer = addr.split(",")[0]
    # Write Compressed File
    with open(file_dir + tmp_folder + file_pointer + "-Compressed.bin", "w+b") as comp_file:
        # Write Header
        for hex_val in header:
            comp_file.write(bytes.fromhex(hex_val))
        # Grab Middle
#         for index in range(address1+len(lead), address2-len(tail)):
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

def compress_individual_misc_file(file_dir, rom_file, file_type):
    """Prepares the hex file that was extracted from the main ROM file for compression by providing the correct header and footer"""
    logger.info("Compressor")
    file_bytes = get_file_bytes(file_dir, rom_file)
    (addr, header, footer, lead, tail) = misc_setup_ids[file_type][0]
    if(addr.startswith("0x")):
        # Get Address Endpoints
        (address1, address2) = get_address_endpoints(file_bytes, addr)
        verify_original_header(file_bytes, address1)
        file_pointer = addr[2:]
    else:
        # Get Address Endpoints
        address1 = int(addr.split(",")[0], 16)
        file_pointer = addr.split(",")[0]
    with open(file_dir + tmp_folder + file_pointer + "-Decompressed.bin", "r+b") as rand_comp_file:
        mm_decomp = mmap.mmap(rand_comp_file.fileno(), 0)
        decomp_len = str(hex(len(mm_decomp)))[2:]
        decomp_len = leading_zeros(decomp_len, 8)
    # Compress File
    compress_file(file_dir, file_pointer)
    # Get Length Of Original Compressed File
    with open(file_dir + tmp_folder + file_pointer + "-New_Compressed.bin", "r+b") as comp_file:
        mm_comp = mmap.mmap(comp_file.fileno(), 0)
        comp_file_len = len(mm_comp)
        header_end = ""
        for header_val in header[-4:]:
            header_end += header_val
        header_end_index = mm_comp.find(bytes.fromhex(header_end)) + 4
        with open(file_dir + tmp_folder + file_pointer + "-Randomized_Compressed.bin", "w+b") as new_comp_file:
            new_comp_file.write(bytes.fromhex("1172"))
            new_comp_file.write(bytes.fromhex(decomp_len))
            new_comp_len = 6
            for index in range(header_end_index, comp_file_len-len(footer)):
                hex_string = str(hex(mm_comp[index]))[2:]
                hex_string = leading_zeros(hex_string, 2)
                new_comp_file.write(bytes.fromhex(hex_string))
                new_comp_len += 1
            if((new_comp_len % 8) != 0):
                needs_padding = 8 - (new_comp_len % 8)
                if(addr.startswith("0x")):
                    for index in range(new_comp_len, new_comp_len + needs_padding):
                        new_comp_file.write(bytes.fromhex("AA"))
                else:
                    for index in range(new_comp_len, new_comp_len + needs_padding):
                        new_comp_file.write(bytes.fromhex("00"))

def insert_misc_file_into_rom(seed_val, file_dir, rom_file, file_type):
    '''For every misc file, insert it back into the ROM file'''
    file_bytes = get_file_bytes(file_dir, rom_file)
    # For every compressed file in numerical order,
    with open(file_dir + tmp_folder + "Banjo-Kazooie_Randomized_Seed_" + str(seed_val) + ".z64", "r+b") as rand_rom:
        mm_rand_rom = mmap.mmap(rand_rom.fileno(), 0)
        (addr, header, footer, lead, tail) = misc_setup_ids[file_type][0]
        if(addr.startswith("0x")):
            # Get Address Endpoints
            (address1, address2) = get_address_endpoints(file_bytes, addr)
            verify_original_header(file_bytes, address1)
            file_pointer = addr[2:]
        else:
            # Get Address Endpoints
            address1 = int(addr.split(",")[0], 16)
            address2 = int(addr.split(",")[1], 16)
            file_pointer = addr.split(",")[0]
        with open(file_dir + tmp_folder + file_pointer + "-Randomized_Compressed.bin", "r+b") as setup_bin:
            setup_content = setup_bin.read()
            # Place It Where The Pointer Start Points To
            setup_count = 0
            for index in range(address1, address1 + len(setup_content)):
                mm_rand_rom[index] = setup_content[setup_count]
                setup_count += 1
    if(addr.startswith("0x")):
        pointer_start = ""
        for offset in range(4):
            pointer_start += leading_zeros(str(hex(mm_rand_rom[int(file_pointer, 16) + 8 + offset]))[2:], 2)
        with open(file_dir + tmp_folder + "Banjo-Kazooie_Randomized_Seed_" + str(seed_val) + ".z64", "r+b") as rand_rom:
            mm_rand_rom = mmap.mmap(rand_rom.fileno(), 0)
            for index in range(address1 + len(setup_content), address2):
                mm_rand_rom[index] = 170
    else:
        with open(file_dir + tmp_folder + "Banjo-Kazooie_Randomized_Seed_" + str(seed_val) + ".z64", "r+b") as rand_rom:
            mm_rand_rom = mmap.mmap(rand_rom.fileno(), 0)
            for index in range(address1 + len(setup_content), address2):
                mm_rand_rom[index] = 0

def unlockable_options(file_dir, rom_file, seed_val, seed_generated,
                       note_door_option, final_note_score_lower, final_note_score_upper,
                       puzzle_option, final_puzzle_lower, final_puzzle_upper,
                       ):
    '''Runs through the misc options'''
    logger.info("Unlockable Options")
    decompress_generic_individual_misc_file(file_dir, rom_file, "Requirements")
    decompress_generic_individual_misc_file(file_dir, rom_file, "Bottles Tutorial Confirmation")
    if((note_door_option == "1") and (puzzle_option == "1")):
        final_note_score = final_note_door_mode(file_dir, seed_val, final_note_score_lower, final_note_score_upper)
        final_puzzle_score = modify_world_puzzle_requirements(file_dir, seed_val, final_puzzle_lower, final_puzzle_upper)
        new_bottles_text = new_bottles_text = "YOU WILL NEED "+leading_zeros(str(final_note_score), 3)+ " NOTES AND "+leading_zeros(str(final_puzzle_score), 3)+" JIGGIES TO REACH THE TOP OF THE TOWER! PRESS B AND GET GOING!!!          "
    elif(note_door_option == "1"):
        final_note_score = final_note_door_mode(file_dir, seed_val, final_note_score_lower, final_note_score_upper)
        new_bottles_text = "YOU'LL NEED "+leading_zeros(str(final_note_score), 3)+" NOTES TO PASS THE FINAL NOTE DOOR! PRESS A FOR LESSONS OR PRESS B TO SKIP MY NOTES! HAHA!"
    elif(puzzle_option == "1"):
        final_puzzle_score = modify_world_puzzle_requirements(file_dir, seed_val, final_puzzle_lower, final_puzzle_upper)
        new_bottles_text = "YOU'LL NEED "+leading_zeros(str(final_puzzle_score), 3)+" JIGGIES TO PASS THE FINAL PUZZLE DOOR! PRESS B TO GO OR PRESS A IF YOU'RE PUZZLED!"
    new_bottles_text_len = len(new_bottles_text)
    for extra_space in range(new_bottles_text_len, 105):
        new_bottles_text += " "
    modify_bottles_unskipable_text(file_dir, new_bottles_text)
    compress_individual_misc_file(file_dir, rom_file, "Requirements")
    compress_individual_misc_file(file_dir, rom_file, "Bottles Tutorial Confirmation")
    insert_misc_file_into_rom(seed_val, file_dir, rom_file, "Requirements")
    insert_misc_file_into_rom(seed_val, file_dir, rom_file, "Bottles Tutorial Confirmation")