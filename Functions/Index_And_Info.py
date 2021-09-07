def create_mmap(file_dir, address):
    '''Creates an mmap that can read and write to a hex file'''
    logger.info("Create MMap")
    with open(file_dir + tmp_folder + address + "-Decompressed.bin", "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
    return mm

######################
### GET INDEX LIST ###
######################

def get_flagged_object_index_list(mm, flagged_object, start=0):
    '''Locates the flagged objects by index in the decompressed file'''
    logger.info("Get Flagged Object Index List")
    object_index = mm.find(bytes.fromhex(flagged_object), start)
    if(object_index == -1):
        return []
    else:
        new_start = int(object_index) + 1
        object_list = get_object_index_list(mm, flagged_object, start=new_start)
    object_list.append(object_index)
    return object_list

def get_object_index_list(mm, object_id, start=0):
    '''Locates the flagged objects by index in the decompressed file'''
    logger.info("Get Flagged Object Index List")
    object_index = mm.find(bytes.fromhex("190C" + object_id), start)
    if(object_index == -1):
        return []
    else:
        new_start = int(object_index) + 1
        object_list = get_object_index_list(mm, object_id, start=new_start)
    object_list.append(object_index)
    return object_list

def adjust_ttc_oob_egg(mm, index):
    '''Moves the out of bounds egg in TTC slightly higher'''
    obj_id1 = mm[index]
    obj_id2 = mm[index + 1]
    if((obj_id1 == 22) and (obj_id2 == 80)):
        x_loc1 = mm[index - 8]
        x_loc2 = mm[index - 7]
        y_loc1 = mm[index - 6]
        y_loc2 = mm[index - 5]
        z_loc1 = mm[index - 4]
        z_loc2 = mm[index - 3]
        # TTC OoB Blue Egg
        if((x_loc1 == 240) and (x_loc2 == 120) and #F078
           (y_loc1 == 4) and (y_loc2 == 30) and #041E
           (z_loc1 == 6) and (z_loc2 == 214)): #06D6
            print("Editing TTC OoB Blue Egg")
            mm[index - 6] = 4
            mm[index - 5] = 166

def get_struct_index_list(mm, struct_id, start=0):
    '''Locates the structs by index in the decompressed file'''
    logger.info("Get Struct Index List")
    struct_index = mm.find(bytes.fromhex(struct_id), start)
    if(struct_index == -1):
        return []
    else:
        new_start = int(struct_index) + 1
        struct_list = get_struct_index_list(mm, struct_id, start=new_start)
    adjust_ttc_oob_egg(mm, struct_index)
    struct_list.append(struct_index)
    return struct_list

def skip_ttc_grublin(mm, index):
    '''Skips randomizing the Grublin at the top of TTC'''
    obj_id1 = mm[index]
    obj_id2 = mm[index + 1]
    if((obj_id1 == 0) and (obj_id2 == 6)):
        x_loc1 = mm[index - 8]
        x_loc2 = mm[index - 7]
        y_loc1 = mm[index - 6]
        y_loc2 = mm[index - 5]
        z_loc1 = mm[index - 4]
        z_loc2 = mm[index - 3]
        # TTC Grublin
        if((x_loc1 == 4) and (x_loc2 == 238) and #04EE
           (y_loc1 == 20) and (y_loc2 == 97) and #1461
           (z_loc1 == 241) and (z_loc2 == 246)): #F1F6
            print("Editing TTC OoB Blue Egg")
            return False
    return True

def get_enemy_index_list(mm, enemy_id, start=0):
    '''Locates the enemies by index in the decompressed file'''
    logger.info("Get Enemy Index List")
    enemy_index = mm.find(bytes.fromhex(enemy_id), start)
    if(enemy_index == -1):
        return []
    else:
        new_start = int(enemy_index) + 1
        enemy_list = get_enemy_index_list(mm, enemy_id, start=new_start)
    if(skip_ttc_grublin(mm, enemy_index)):
        enemy_list.append(enemy_index)
    return enemy_list

def skip_non_ring(mm, index):
    '''Skips the first clanker's cavern ring in order to not be confused with another object'''
    # CC Non-Ring
    if(mm[index - 1] == 119):
        print("Skipping Non-Ring")
        return False
    return True

def get_sequence_index_list(mm, seq_search, start=0):
    '''Locates the sequence events by index in the decompressed file'''
    logger.info("Get Enemy Index List")
    seq_index = mm.find(bytes.fromhex(seq_search), start)
    if(seq_index == -1):
        return []
    else:
        new_start = int(seq_index) + 1
        seq_list = get_enemy_index_list(mm, seq_search, start=new_start)
    if(skip_non_ring(mm, seq_index)):
        seq_list.append(seq_index)
    return seq_list

########################
### OBTAIN LIST INFO ###
########################

def obtain_flagged_object_info(mm, obj_index):
    '''Gathers all of the information about the flagged object into a dict'''
    obj_dict = {}
    obj_dict["Index"] = obj_index
    hex_x1 = leading_zeros(str(hex(mm[obj_index]))[2:].upper(), 2)
    hex_x2 = leading_zeros(str(hex(mm[obj_index + 1]))[2:].upper(), 2)
    obj_dict["Hex_X"] = hex_x1 + hex_x2
    hex_y1 = leading_zeros(str(hex(mm[obj_index + 2]))[2:].upper(), 2)
    hex_y2 = leading_zeros(str(hex(mm[obj_index + 3]))[2:].upper(), 2)
    obj_dict["Hex_Y"] = hex_y1 + hex_y2
    hex_z1 = leading_zeros(str(hex(mm[obj_index + 4]))[2:].upper(), 2)
    hex_z2 = leading_zeros(str(hex(mm[obj_index + 5]))[2:].upper(), 2)
    obj_dict["Hex_Z"] = hex_z1 + hex_z2
    obj_dict["Script1"] = mm[obj_index + 6]
    obj_dict["Script2"] = mm[obj_index + 7]
    obj_dict["Obj_ID1"] = mm[obj_index + 8]
    obj_dict["Obj_ID2"] = mm[obj_index + 9]
    obj_dict["IDK1"] = mm[obj_index + 10]
    obj_dict["IDK2"] = mm[obj_index + 11]
    obj_dict["IDK3"] = mm[obj_index + 12]
    obj_dict["IDK4"] = mm[obj_index + 13]
    obj_dict["Rotation"] = mm[obj_index + 14]
    obj_dict["Size"] = mm[obj_index + 15]
    obj_dict["IDK5"] = mm[obj_index + 16]
    obj_dict["IDK6"] = mm[obj_index + 17]
    obj_dict["IDK7"] = mm[obj_index + 18]
    return obj_dict

def obtain_flag_info(mm, flag_index):
    '''Gathers all of the information about the flag into a dict'''
    flag_dict = {}
    flag_dict["Index"] = flag_index
    hex_x1 = leading_zeros(str(hex(mm[flag_index]))[2:].upper(), 2)
    hex_x2 = leading_zeros(str(hex(mm[flag_index + 1]))[2:].upper(), 2)
    flag_dict["Hex_X"] = hex_x1 + hex_x2
    hex_y1 = leading_zeros(str(hex(mm[flag_index + 2]))[2:].upper(), 2)
    hex_y2 = leading_zeros(str(hex(mm[flag_index + 3]))[2:].upper(), 2)
    flag_dict["Hex_Y"] = hex_y1 + hex_y2
    hex_z1 = leading_zeros(str(hex(mm[flag_index + 4]))[2:].upper(), 2)
    hex_z2 = leading_zeros(str(hex(mm[flag_index + 5]))[2:].upper(), 2)
    flag_dict["Hex_Z"] = hex_z1 + hex_z2
    flag_dict["Script1"] = mm[flag_index + 6]
    flag_dict["Script2"] = mm[flag_index + 7]
    flag_dict["Obj_ID1"] = mm[flag_index + 8]
    flag_dict["Obj_ID2"] = mm[flag_index + 9]
    flag_dict["IDK1"] = mm[flag_index + 10]
    flag_dict["IDK2"] = mm[flag_index + 11]
    flag_dict["IDK3"] = mm[flag_index + 12]
    flag_dict["IDK4"] = mm[flag_index + 13]
    flag_dict["Rotation"] = mm[flag_index + 14]
    flag_dict["Size"] = mm[flag_index + 15]
    flag_dict["IDK5"] = mm[flag_index + 16]
    flag_dict["IDK6"] = mm[flag_index + 17]
    flag_dict["IDK7"] = mm[flag_index + 18]
    return flag_dict

def obtain_no_flag_object_list_info(mm, no_flag_obj_index_list):
    '''Gathers all of the information about the non-flag object into a list'''
    logger.info("Obtain Non-Flag Object List Info")
    #X-Loc  Y-Loc  Z-Loc  script   ID     --   --   --   --   rot.  size  --    --
    #0E48   0153   1998   190C     0049   00   00   00   00   00    64    0C    10
    object_location_list = []
    for object_index in no_flag_obj_index_list:
        object_dict = {}
#         object_dict["Hex_X1"] = mm[object_index - 6]
#         object_dict["Hex_X2"] = mm[object_index - 5]
#         object_dict["Hex_Y1"] = mm[object_index - 4]
#         object_dict["Hex_Y2"] = mm[object_index - 3]
#         object_dict["Hex_Z1"] = mm[object_index - 2]
#         object_dict["Hex_Z2"] = mm[object_index - 1]
        object_dict["Script1"] = mm[object_index]
        object_dict["Script2"] = mm[object_index + 1]
        object_dict["Obj_ID1"] = mm[object_index + 2]
        object_dict["Obj_ID2"] = mm[object_index + 3]
#         object_dict["Rotation"] = mm[object_index + 8]
#         object_dict["Size"] = mm[object_index + 9]
        object_location_list.append(object_dict)
    return object_location_list

def obtain_struct_list_info(mm, struct_list_index_list):
    '''Gathers all of the information about the struct into a list'''
    logger.info("Obtain Struct List Info")
    #obj id  ????  x-loc  y-loc  z-loc  size  ??
    #1640    00B6  FA12   03C4   02C2   19    80
    struct_location_list = []
    for struct_index in struct_list_index_list:
        struct_dict = {}
        struct_dict["Index"] = struct_index
        struct_dict["Obj_ID1"] = mm[struct_index]
        struct_dict["Obj_ID2"] = mm[struct_index + 1]
        struct_dict["IDK1"] = mm[struct_index + 2]
        struct_dict["IDK2"] = mm[struct_index + 3]
#         struct_dict["Hex_X1"] = mm[struct_index + 4]
#         struct_dict["Hex_X2"] = mm[struct_index + 5]
#         struct_dict["Hex_Y1"] = mm[struct_index + 6]
#         struct_dict["Hex_Y2"] = mm[struct_index + 7]
#         struct_dict["Hex_Z1"] = mm[struct_index + 8]
#         struct_dict["Hex_Z2"] = mm[struct_index + 9]
        struct_dict["Size"] = mm[struct_index + 10]
#         struct_dict["IDK3"] = mm[struct_index + 11]
        struct_location_list.append(struct_dict)
    return struct_location_list

def obtain_enemy_list_info(mm, enemy_index_list):
    '''Gathers all of the information about the enemy into a list'''
    logger.info("Obtain Enemy List Info")
    #X-Loc  Y-Loc  Z-Loc  script   ID     --   --   --   --   rot.  size  --    --
    #0E48   0153   1998   190C     0049   00   00   00   00   00    64    0C    10
    enemy_location_list = []
    for enemy_index in enemy_index_list:
        enemy_dict = {}
#         enemy_dict["Hex_X1"] = mm[enemy_index - 6]
#         enemy_dict["Hex_X2"] = mm[enemy_index - 5]
#         enemy_dict["Hex_Y1"] = mm[enemy_index - 4]
#         enemy_dict["Hex_Y2"] = mm[enemy_index - 3]
#         enemy_dict["Hex_Z1"] = mm[enemy_index - 2]
#         enemy_dict["Hex_Z2"] = mm[enemy_index - 1]
#         enemy_dict["Script1"] = mm[enemy_index]
#         enemy_dict["Script2"] = mm[enemy_index + 1]
        enemy_dict["Obj_ID1"] = mm[enemy_index + 2]
        enemy_dict["Obj_ID2"] = mm[enemy_index + 3]
#         enemy_dict["Rotation"] = mm[enemy_index + 8]
#         enemy_dict["Size"] = mm[enemy_index + 9]
        enemy_location_list.append(enemy_dict)
    return enemy_location_list

def obtain_sequence_object_list_info(mm, sequence_obj_index_list):
    '''Gathers all of the information about the non-flag object into a list'''
    logger.info("Obtain Non-Flag Object List Info")
    #X-Loc  Y-Loc  Z-Loc  script   ID     --   --   --   --   rot.  size  --    --
    #0E48   0153   1998   190C     0049   00   00   00   00   00    64    0C    10
    object_location_list = []
    for object_index in sequence_obj_index_list:
        object_dict = {}
#         object_dict["Hex_X1"] = mm[object_index - 6]
#         object_dict["Hex_X2"] = mm[object_index - 5]
#         object_dict["Hex_Y1"] = mm[object_index - 4]
#         object_dict["Hex_Y2"] = mm[object_index - 3]
#         object_dict["Hex_Z1"] = mm[object_index - 2]
#         object_dict["Hex_Z2"] = mm[object_index - 1]
        object_dict["Script1"] = mm[object_index]
        object_dict["Script2"] = mm[object_index + 1]
        object_dict["Obj_ID1"] = mm[object_index + 2]
        object_dict["Obj_ID2"] = mm[object_index + 3]
#         object_dict["Rotation"] = mm[object_index + 4]
#         object_dict["Size"] = mm[object_index + 5]
        object_location_list.append(object_dict)
    return object_location_list

##################
### INDEX MAIN ###
##################

def enemy_get_lists(mm, location, allow_abnormalities_option=False, enemy_option=None):
    '''For each enemy type, runs the functions that grabs the list of objects and locations'''
    logger.info("Get Enemy Lists: " + location)
    index_dict = {}
    location_dict = {}
    for enemy_type in enemy_id_dict["Global"]:
        index_dict[enemy_type] = []
        location_dict[enemy_type] = []
        for enemy_id in enemy_id_dict["Global"][enemy_type]:
            index_dict[enemy_type] = index_dict[enemy_type] + get_enemy_index_list(mm, enemy_id)
        location_dict[enemy_type] = location_dict[enemy_type] + obtain_enemy_list_info(mm, index_dict[enemy_type])
    for enemy_type in enemy_id_dict[location]:
        for enemy_id in enemy_id_dict[location][enemy_type]:
            index_dict[enemy_type] = index_dict[enemy_type] + get_enemy_index_list(mm, enemy_id)
        location_dict[enemy_type] = location_dict[enemy_type] + obtain_enemy_list_info(mm, index_dict[enemy_type])
    for enemy_type in additional_enemy_id_dict:
        for enemy_id in additional_enemy_id_dict[enemy_type]:
            index_dict[enemy_type] = index_dict[enemy_type] + get_enemy_index_list(mm, enemy_id)
        location_dict[enemy_type] = location_dict[enemy_type] + obtain_enemy_list_info(mm, index_dict[enemy_type])
    if((allow_abnormalities_option) and (enemy_option == "Oh Whoops")):
        for enemy_type in additional_abnormal_enemy_id_dict:
            for enemy_id in additional_abnormal_enemy_id_dict[enemy_type]:
                index_dict[enemy_type] = index_dict[enemy_type] + get_enemy_index_list(mm, enemy_id)
            location_dict[enemy_type] = location_dict[enemy_type] + obtain_enemy_list_info(mm, index_dict[enemy_type])
    return (index_dict, location_dict)

def get_flagged_objects_dict(mm, flagged_object_dict, location, allow_abnormalities_option=None):
    '''Searches the location for every flagged object with their flag and returns their index and information'''
    flagged_object_index_list = []
    flagged_object_location_list = []
    for obj_id in flagged_object_dict[location]:
        obj_search = flagged_object_dict[location][obj_id]["Object"]
        flag_search = flagged_object_dict[location][obj_id]["Flag"]
        obj_index = mm.find(bytes.fromhex(obj_search))
        flag_index = mm.find(bytes.fromhex(flag_search))
        if((obj_index != -1) and (flag_index != -1)):
            flagged_object_index_list.append((obj_index, flag_index))
            flagged_object_location_list.append((obtain_flagged_object_info(mm, obj_index), obtain_flag_info(mm, flag_index)))
    if(allow_abnormalities_option != None):
        for obj_id in abnormal_flagged_object_dict[location]:
            obj_search = abnormal_flagged_object_dict[location][obj_id]["Object"]
            flag_search = abnormal_flagged_object_dict[location][obj_id]["Flag"]
            obj_index = mm.find(bytes.fromhex(obj_search))
            flag_index = mm.find(bytes.fromhex(flag_search))
            if((obj_index != -1) and (flag_index != -1)):
                flagged_object_index_list.append((obj_index, flag_index))
                flagged_object_location_list.append((obtain_flagged_object_info(mm, obj_index), obtain_flag_info(mm, flag_index)))
    return (flagged_object_index_list, flagged_object_location_list)

def generic_get_lists(mm, id_list):
    '''For each type of id list, runs the functions that grabs the list of objects and locations'''
    logger.info("Generic Get Lists")
    index_list = []
    for obj_id in id_list:
        if((id_list == obj_no_flag_id_list) or (id_list == (obj_no_flag_id_list + abnormal_obj_no_flag_id_list))):
            object_list = get_object_index_list(mm, obj_id)
        elif((id_list == collectable_struct_id_list) or (id_list == (collectable_struct_id_list + abnormal_collectable_struct_id_list))):
            object_list = get_struct_index_list(mm, obj_id)
        elif((id_list == croctus_list) or (id_list == clanker_rings_list) or
             (id_list == ancient_ones_list) or (id_list == jinxy_head_list) or
             (id_list == brentilda_list) or (id_list == combined_bottles_list)):
            object_list = get_sequence_index_list(mm, obj_id)
        else:
            logger.error("Invalid ID List")
            error_window("Developer Error During Randomization")
            raise SystemExit # exit(0)
        for item in object_list:
            index_list.append(item)
    if((id_list == obj_no_flag_id_list) or (id_list == (obj_no_flag_id_list + abnormal_obj_no_flag_id_list))):
        location_list = obtain_no_flag_object_list_info(mm, index_list)
    elif((id_list == collectable_struct_id_list) or (id_list == (collectable_struct_id_list + abnormal_collectable_struct_id_list))):
        location_list = obtain_struct_list_info(mm, index_list)
    elif((id_list == croctus_list) or (id_list == clanker_rings_list) or
         (id_list == ancient_ones_list) or (id_list == jinxy_head_list) or
         (id_list == brentilda_list) or (id_list == combined_bottles_list)):
        location_list = obtain_sequence_object_list_info(mm, index_list)
    else:
        logger.error("Invalid ID List")
        error_window("Developer Error During Randomization")
        raise SystemExit # exit(0)
    return (index_list, location_list)

def get_warp_lists(mm, location_warps_entry_dict, address, warp_entry_index_dict, warp_entry_location_dict):
    for shuffle_group in location_warps_entry_dict:
        if(shuffle_group not in warp_entry_index_dict):
            warp_entry_index_dict[shuffle_group] = {}
        if(shuffle_group not in warp_entry_location_dict):
            warp_entry_location_dict[shuffle_group] = {}
        for warp_id in location_warps_entry_dict[shuffle_group]:
            if(warp_id not in warp_entry_index_dict[shuffle_group]):
                warp_entry_index_dict[shuffle_group][warp_id] = {}
                warp_entry_index_dict[shuffle_group][warp_id]["Warps"] = []
            if(warp_id not in warp_entry_location_dict[shuffle_group]):
                warp_entry_location_dict[shuffle_group][warp_id] = {}
                warp_entry_location_dict[shuffle_group][warp_id]["Warps"] = []
            if(warp_entry_index_dict[shuffle_group][warp_id]["Warps"] == []):
                for warp_search in location_warps_entry_dict[shuffle_group][warp_id]:
                    warp_index = mm.find(bytes.fromhex(warp_search))
                    if(warp_index >= 0):
                        warp_entry_index_dict[shuffle_group][warp_id]["Warp_Address"] = address
                        (warp_entry_index_dict[shuffle_group][warp_id]["Warps"]).append(warp_index)
                        warp_dict = {
                            "Index": warp_index,
                            "Obj_ID1": mm[warp_index + 8],
                            "Obj_ID2": mm[warp_index + 9],
                            }
                        (warp_entry_location_dict[shuffle_group][warp_id]["Warps"]).append(warp_dict)
    return (warp_entry_index_dict, warp_entry_location_dict)

def get_grunty_lair_warp_index_list(file_dir, original_world):
    warp_index_list = []
    with open(file_dir + tmp_folder + world_order_warps_list[original_world]["Gruntilda's Lair Address"] + "-Decompressed.bin", "r+b") as decomp_file:
        mm_find = mmap.mmap(decomp_file.fileno(), 0)
        for warp_search in world_order_warps_list[original_world]["Gruntilda's Lair Warps"]:
            warp_index = mm_find.find(bytes.fromhex(warp_search))
            if(warp_index >= 0):
                warp_index_list.append(warp_index)
            else:
                logger.error("Error: Lair Warp Not Found")
                error_window("Error During Randomization")
                raise SystemExit
    return warp_index_list

# def get_original_warp_pad(file_dir, original_world):
#     with open(file_dir + tmp_folder + world_order_warps_list[original_world]["World Address"] + "-Decompressed.bin", "r+b") as decomp_file:
#         mm_find = mmap.mmap(decomp_file.fileno(), 0)
#         warp_pad_search = world_order_warps_list[original_world]["World Pad"]
#         warp_pad_index = mm_find.find(bytes.fromhex(warp_pad_search))
#     if(warp_pad_index < 0):
#         logger.error("Error: Couldn't Find Warp Pad")
#         error_window("Error During Randomization")
#         raise SystemExit
#     return warp_pad_index