def randomize_list(seed_val, original_list, address=0):
    '''Shuffles a given list based on the seed value'''
    logger.info("Randomize List")
    random.seed(a=(seed_val + address))
    random.shuffle(original_list)
    return original_list

def move_flagged_objects(mm, obj_index_list, object_location_list):
    '''For each object, assign it a new script and object id based on randomized list'''
    logger.info("Move Flagged Objects")
    for (object_index, flag_index) in obj_index_list:
        mm[object_index + 6] = object_location_list[0][0]["Script1"]
        mm[object_index + 7] = object_location_list[0][0]["Script2"]
        mm[object_index + 8] = object_location_list[0][0]["Obj_ID1"]
        mm[object_index + 9] = object_location_list[0][0]["Obj_ID2"]
        mm[object_index + 10] = object_location_list[0][0]["IDK1"]
        mm[object_index + 11] = object_location_list[0][0]["IDK2"]
        mm[object_index + 12] = object_location_list[0][0]["IDK3"]
        mm[object_index + 13] = object_location_list[0][0]["IDK4"]
        mm[object_index + 14] = object_location_list[0][0]["Rotation"]
        mm[object_index + 15] = object_location_list[0][0]["Size"]
#         mm[object_index + 16] = object_location_list[0][0]["IDK5"]
#         mm[object_index + 17] = object_location_list[0][0]["IDK6"]
#         mm[object_index + 18] = object_location_list[0][0]["IDK7"]
        mm[flag_index + 6] = object_location_list[0][1]["Script1"]
        mm[flag_index + 7] = object_location_list[0][1]["Script2"]
        mm[flag_index + 8] = object_location_list[0][1]["Obj_ID1"]
        mm[flag_index + 9] = object_location_list[0][1]["Obj_ID2"]
        mm[flag_index + 10] = object_location_list[0][1]["IDK1"]
        mm[flag_index + 11] = object_location_list[0][1]["IDK2"]
        mm[flag_index + 12] = object_location_list[0][1]["IDK3"]
        mm[flag_index + 13] = object_location_list[0][1]["IDK4"]
        mm[flag_index + 14] = object_location_list[0][1]["Rotation"]
        mm[flag_index + 15] = object_location_list[0][1]["Size"]
#         mm[flag_index + 16] = object_location_list[0][1]["IDK5"]
#         mm[flag_index + 17] = object_location_list[0][1]["IDK6"]
#         mm[flag_index + 18] = object_location_list[0][1]["IDK7"]
        object_location_list.pop(0)
    return object_location_list

def move_no_flag_objects(mm, obj_index_list, object_location_list):
    '''For each object, assign it a new script and object id based on randomized list'''
    logger.info("Move Non-Flag Objects")
    for object_index in obj_index_list:
        mm[object_index] = object_location_list[0]["Script1"]
        mm[object_index + 1] = object_location_list[0]["Script2"]
        mm[object_index + 2] = object_location_list[0]["Obj_ID1"]
        mm[object_index + 3] = object_location_list[0]["Obj_ID2"]
        object_location_list.pop(0)
    return object_location_list

def move_structs(mm, struct_index_list, struct_location_list):
    '''For each struct, assign it a new script and object id based on randomized list'''
    logger.info("Move Local Structs")
    for struct_index in struct_index_list:
        mm[struct_index] = struct_location_list[0]["Obj_ID1"]
        mm[struct_index + 1] = struct_location_list[0]["Obj_ID2"]
#         mm[struct_index + 2] = struct_location_list[0]["IDK1"]
#         mm[struct_index + 3] = struct_location_list[0]["IDK2"]
        mm[struct_index + 2] = 0
        mm[struct_index + 3] = 160
        mm[struct_index + 10] = struct_location_list[0]["Size"]
        struct_location_list.pop(0)
    return struct_location_list

def oh_whoops_all_notes(mm, struct_index_list):
    '''For each struct, assign it to be a note'''
    logger.info("Move Local Structs")
    for struct_index in struct_index_list:
        mm[struct_index] = 22
        mm[struct_index + 1] = 64
#         mm[struct_index + 2] = struct_location_list[0]["IDK1"]
#         mm[struct_index + 3] = struct_location_list[0]["IDK2"]
        mm[struct_index + 2] = 0
        mm[struct_index + 3] = 160
        mm[struct_index + 10] = 69

def turn_brentildas_into_refills(mm, seed_val, address, brentilda_index_list, brentilda_location_list):
    seed_count = 0
    for brentilda_index in brentilda_index_list:
        random.seed(a=(seed_val + int(address, 16) + seed_count))
        refill_choice = random.choice(inventory_refills)
        mm[brentilda_index] = int(refill_choice[:2], 16)
        mm[brentilda_index + 1] = int(refill_choice[2:4], 16)
        mm[brentilda_index + 2] = int(refill_choice[4:6], 16)
        mm[brentilda_index + 3] = int(refill_choice[6:], 16)
        brentilda_location_list.pop(0)
        seed_count += len("I wonder if people will even care about me after I release the randomizer...")
    return brentilda_location_list

def move_local_enemies(mm, enemy_index_list, enemy_location_list):
    '''For each enemy, assign it a new script and object id based on randomized list'''
    logger.info("Move Local Enemies")
    for enemy_index in enemy_index_list:
#         mm[enemy_index] = enemy_location_list[enemy_count]["Script1"]
#         mm[enemy_index + 1] = enemy_location_list[enemy_count]["Script2"]
        mm[enemy_index + 2] = enemy_location_list[0]["Obj_ID1"]
        mm[enemy_index + 3] = enemy_location_list[0]["Obj_ID2"]
        enemy_location_list.pop(0)
    return enemy_location_list

def move_randomized_enemies(mm, seed_val, enemy_index_list, enemy_type, location, address, abnormal_option="0"):
    '''For each enemy, randomly assign it a new script and object id within the id list'''
    logger.info("Move Completely Randomized Enemies")
    if(enemy_type in enemy_id_dict[location]):
        enemy_id_list = enemy_id_dict["Global"][enemy_type] + enemy_id_dict[location][enemy_type]
    else:
        enemy_id_list = enemy_id_dict["Global"][enemy_type]
    if(abnormal_option == "1"):
        if(enemy_type in abnormal_enemy_id_list["Global"]):
            enemy_id_list = enemy_id_list + abnormal_enemy_id_list["Global"][enemy_type]
            if(location in abnormal_enemy_id_list):
                if(enemy_type in abnormal_enemy_id_list[location]):
                    enemy_id_list = enemy_id_list + abnormal_enemy_id_list[location][enemy_type]
    seed_count = 0
    for enemy_index in enemy_index_list:
        random.seed(a=(seed_val+seed_count+int(address, 16)))
        enemy_obj_id = random.choice(enemy_id_list)
        mm[enemy_index + 2] = int(enemy_obj_id[4:6], 16)
        mm[enemy_index + 3] = int(enemy_obj_id[6:], 16)
        if(enemy_obj_id == "190C0289"):
            rot_val = mm[enemy_index + 6]
            if(rot_val >= 45):
                mm[enemy_index + 6] = rot_val - 45
            else:
                mm[enemy_index + 6] = rot_val + 135
        seed_count += len("Everyone talks to me about what features should be in the randomizer without understanding the effort I put into coding this...")

def oh_whoops_all_enemies(mm, seed_val, enemy_index_list, enemy_type, location, address, abnormal_option="0"):
    '''For each enemy, randomly assign it a new script and object id within the id list'''
    logger.info("Move Completely Randomized Enemies")
    seed_count = 0
    for enemy_index in enemy_index_list:
        if(enemy_type == "Ground"):
            if((abnormal_option == "1") and (location == "Rusty Bucket Bay")):
                random.seed(a=(seed_val+seed_count+int(address, 16)))
                enemy_obj_id = random.choice(["190C0004", "190C01C6", "190C02A4", "190C030D"])
            else:
                enemy_obj_id = "190C0004"
        elif(enemy_type == "Wall"):
            if(abnormal_option == "1"):
                random.seed(a=(seed_val+seed_count+int(address, 16)))
                enemy_obj_id = random.choice(["190C013B", "190C0289"])
            else:
                enemy_obj_id = "190C013B"
        elif((enemy_type == "Flying") or (enemy_type == "Misc")):
            enemy_obj_id = "078C034D"
        mm[enemy_index] = int(enemy_obj_id[:2], 16)
        mm[enemy_index + 1] = int(enemy_obj_id[2:4], 16)
        mm[enemy_index + 2] = int(enemy_obj_id[4:6], 16)
        mm[enemy_index + 3] = int(enemy_obj_id[6:8], 16)
        if(enemy_obj_id == "190C0289"):
            rot_val = mm[enemy_index + 6]
            if(rot_val >= 45):
                mm[enemy_index + 6] = rot_val - 45
            else:
                mm[enemy_index + 6] = rot_val + 135
        seed_count += len("I waNt iT tOo bE chAlLenGinG :P")

def shuffle_within_world_warp_entry_order(seed_val, warp_seed_addition, warp_entry_location_dict):
    shuffled_warp_entry_location_dict = {}
    for shuffle_group in warp_entry_location_dict:
        warp_ids = sorted(list((warp_entry_location_dict[shuffle_group]).keys()))
        random.seed(a=(seed_val + warp_seed_addition))
        random.shuffle(warp_ids)
        shuffled_warp_entry_location_dict[shuffle_group] = {}
        for key in sorted(list((warp_entry_location_dict[shuffle_group]).keys())):
            shuffled_warp_entry_location_dict[shuffle_group][warp_ids[0]] = warp_entry_location_dict[shuffle_group][key]
            warp_ids.pop(0)
    return shuffled_warp_entry_location_dict

def determine_world_order(seed_val):
    original_world_order = ["Treasure Trove Cove", "Clanker's Cavern", "Bubblegloop Swamp", "Freezeezy Peak", "Gobi's Valley", "Rusty Bucket Bay", "Click Clock Wood - Lobby"]
    new_world_order = ["Treasure Trove Cove", "Clanker's Cavern", "Bubblegloop Swamp", "Freezeezy Peak", "Gobi's Valley", "Rusty Bucket Bay", "Click Clock Wood - Lobby"]
    random.seed(a=seed_val)
    random.shuffle(new_world_order)
#     new_world_order.insert(0, "Mumbo's Mountain")
#     new_world_order.insert(5, "Mad Monster Mansion")
    return (original_world_order, new_world_order)

def move_within_world_warps_entries(mm, address, address_warp_entry_index_dict, address_warp_entry_location_dict):
    for shuffle_group in address_warp_entry_index_dict:
        for warp_id in address_warp_entry_index_dict[shuffle_group]:
            if(address == address_warp_entry_index_dict[shuffle_group][warp_id]["Warp_Address"]):
                for warp_index in address_warp_entry_index_dict[shuffle_group][warp_id]["Warps"]:
                    mm[warp_index + 8] = address_warp_entry_location_dict[shuffle_group][warp_id]["Warps"][0]['Obj_ID1']
                    mm[warp_index + 9] = address_warp_entry_location_dict[shuffle_group][warp_id]["Warps"][0]['Obj_ID2']

def edit_grunty_lair_warps(file_dir, warp_index_list, original_world, new_world):
    # Replace it/them with new world warp
    mm_replace = create_mmap(file_dir, world_order_warps_list[original_world]["Gruntilda's Lair Address"])
    for warp_index in warp_index_list:
        first_new_warp = world_order_warps_list[new_world]["Gruntilda's Lair Warps"][0]
        mm_replace[warp_index + 8] = int(first_new_warp[16:18], 16)
        mm_replace[warp_index + 9] = int(first_new_warp[18:], 16)

# def edit_warp_pad(file_dir, warp_pad_index, original_world, new_world):
#     mm_replace = create_mmap(file_dir, world_order_warps_list[original_world]["World Address"])
#     new_warp_pad = world_order_warps_list[new_world]["World Pad"]
#     mm_replace[warp_pad_index] = int(new_warp_pad[:2], 16)
#     mm_replace[warp_pad_index + 1] = int(new_warp_pad[2:4], 16)
#     mm_replace[warp_pad_index + 2] = int(new_warp_pad[4:6], 16)
#     mm_replace[warp_pad_index + 3] = int(new_warp_pad[6:], 16)

def move_bottles_mounds(mm, seed_val, bottles_index_list, bottles_location_list, progression_bottles_moves_choices, non_progression_bottles_moves_choices):
    '''For each object, assign it a new script and object id based on randomized list'''
    logger.info("Move Non-Flag Objects")
    seed_count = 0
    for bottles_index in bottles_index_list:
        bottles_script_obj_id = (leading_zeros(str(hex(mm[bottles_index]))[2:], 2) +
                                 leading_zeros(str(hex(mm[bottles_index + 1]))[2:], 2) + 
                                 leading_zeros(str(hex(mm[bottles_index + 2]))[2:], 2) + 
                                 leading_zeros(str(hex(mm[bottles_index + 3]))[2:], 2)).upper()
        if(bottles_script_obj_id in ["050C037A", "058C037A", "060C037A"]):
            random.seed(a=(seed_val + seed_count))
            new_bottles_script_obj_id = random.choice(progression_bottles_moves_choices)
            progression_bottles_moves_choices.remove(new_bottles_script_obj_id)
        elif(bottles_script_obj_id in ["048C037A", "068C037A", "070C037A", "078C037A", "080C037A", "088C037A"]):
            random.seed(a=(seed_val + seed_count))
            new_bottles_script_obj_id = random.choice(non_progression_bottles_moves_choices)
            non_progression_bottles_moves_choices.remove(new_bottles_script_obj_id)
        else:
            logger.error("Error: Non-Bottles Mound Found")
            error_window("Error During Randomization")
            raise SystemExit
        mm[bottles_index] = int(new_bottles_script_obj_id[:2], 16)
        mm[bottles_index + 1] = int(new_bottles_script_obj_id[2:4], 16)
        mm[bottles_index + 2] = int(new_bottles_script_obj_id[4:6], 16)
        mm[bottles_index + 3] = int(new_bottles_script_obj_id[6:], 16)
        bottles_location_list.pop(0)
        seed_count += len("They ask you how you are, and you just have to say you're fine when you're not really fine, but you just can't get into it, because they would never understand.")
    return bottles_location_list

# def upgrade_water_level_button():
#     pass

def shuffle_world_order_warps(file_dir, seed_val):
    (original_world_order, new_world_order) = determine_world_order(seed_val)
    for world_index in range(len(original_world_order)):
        original_world = original_world_order[world_index]
        new_world = new_world_order[world_index]
        warp_index_list = get_grunty_lair_warp_index_list(file_dir, original_world)
        edit_grunty_lair_warps(file_dir, warp_index_list, original_world, new_world)
        #warp_pad_index = get_original_warp_pad(file_dir, original_world)
        #edit_warp_pad(file_dir, warp_pad_index, original_world, new_world)
        #upgrade_water_level_button()