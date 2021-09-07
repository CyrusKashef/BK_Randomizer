def get_index_main(file_dir, address_dict, seed_val, non_flag_option, flagged_option, struct_option, enemy_option, warp_option, croctus_option, clanker_rings_option, ancient_ones_option, jinxy_head_option, allow_abnormalities_option):
    '''For every location, grabs all of the non-flags, flagged, struct, and enemy indices and information, randomizes the lists, and assigns the new values'''
    logger.info("Get Index Main")
    warp_seed_addition = 0
    for location in address_dict:
        logger.debug("Location: " + str(location))
        address_index_dict = {}
        address_flagged_object_location_list = []
        address_no_flag_object_location_list = []
        address_struct_location_list = []
        address_brentilda_location_list = []
        address_bottles_location_list = []
        address_ground_enemy_location_list = []
        address_flying_enemy_location_list = []
        address_wall_enemy_location_list = []
        address_misc_enemy_location_list = []
        address_warp_entry_index_dict = {}
        address_warp_entry_location_dict = {}
        address_croctus_location_list = []
        address_clanker_rings_location_list = []
        address_ancient_ones_location_list = []
        address_jinxy_head_location_list = []
        for address in address_dict[location]:
            logger.debug("Address: " + str(address))
            address_index_dict[address] = {}
            address_index_dict[address]["Grounded_Enemies"] = []
            address_index_dict[address]["Flying_Enemies"] = []
            address_index_dict[address]["Wall_Enemies"] = []
            address_index_dict[address]["Misc_Enemies"] = []
            mm = create_mmap(file_dir, address)
            # Flagged Objects
            if(flagged_option != "None"):
                logger.info("Get Flagged Objects Index")
                if(allow_abnormalities_option == "0"):
                    (flagged_object_index_list, flagged_object_location_list) = get_flagged_objects_dict(mm, flagged_object_dict, location)
                else:
                    (flagged_object_index_list, flagged_object_location_list) = get_flagged_objects_dict(mm, flagged_object_dict, location, allow_abnormalities_option=abnormal_flagged_object_dict)
                for item in flagged_object_location_list:
                    address_flagged_object_location_list.append(item)
                address_index_dict[address]["Flagged_Objects"] = flagged_object_index_list
            # No Flag Objects
            if(non_flag_option != "None"):
                logger.info("Get Non-Flag Objects Index")
                if(allow_abnormalities_option == "0"):
                    (no_flag_obj_index_list, no_flag_object_location_list) = generic_get_lists(mm, obj_no_flag_id_list)
                else:
                    new_obj_no_flag_id_list = obj_no_flag_id_list + abnormal_obj_no_flag_id_list
                    (no_flag_obj_index_list, no_flag_object_location_list) = generic_get_lists(mm, new_obj_no_flag_id_list)
                for item in no_flag_object_location_list:
                    address_no_flag_object_location_list.append(item)
                address_index_dict[address]["No_Flag_Objects"] = no_flag_obj_index_list
            # Structs
            if(struct_option != "None"):
                logger.info("Get Structs Index")
                if(allow_abnormalities_option == "0"):
                    (struct_index_list, struct_location_list) = generic_get_lists(mm, collectable_struct_id_list)
                else:
                    new_struct_id_list = collectable_struct_id_list + abnormal_collectable_struct_id_list
                    (struct_index_list, struct_location_list) = generic_get_lists(mm, new_struct_id_list)
                for item in struct_location_list:
                    address_struct_location_list.append(item)
                address_index_dict[address]["Structs"] = struct_index_list
                if(struct_option == "Oh Whoops"):
                    (brentilda_index_list, brentilda_location_list) = generic_get_lists(mm, brentilda_list)
                    for item in brentilda_location_list:
                        address_brentilda_location_list.append(item)
                    address_index_dict[address]["Brentilda"] = brentilda_index_list
            # Enemies
            if(enemy_option != "None"):
                (index_dict, location_dict) = enemy_get_lists(mm, location, allow_abnormalities_option, enemy_option)
                # Grounded Enemies
                logger.info("Get Grounded Enemies Index")
                address_index_dict[address]["Grounded_Enemies"] = address_index_dict[address]["Grounded_Enemies"] + index_dict["Ground"]
                address_ground_enemy_location_list = address_ground_enemy_location_list + location_dict["Ground"]
                # Flying Enemies
                logger.info("Get Grounded Enemies Index")
                address_index_dict[address]["Flying_Enemies"] = address_index_dict[address]["Flying_Enemies"] + index_dict["Flying"]
                address_flying_enemy_location_list = address_flying_enemy_location_list + location_dict["Flying"]
                # Wall Enemies
                logger.info("Get Wall Enemies Index")
                address_index_dict[address]["Wall_Enemies"] = address_index_dict[address]["Wall_Enemies"] + index_dict["Wall"]
                address_wall_enemy_location_list = address_wall_enemy_location_list + location_dict["Wall"]
                if(enemy_option == "Oh Whoops"):
                    logger.info("Get Misc Enemies Index")
                    address_index_dict[address]["Misc_Enemies"] = address_index_dict[address]["Misc_Enemies"] + index_dict["Misc_Enemies"]
                    address_misc_enemy_location_list = address_misc_enemy_location_list + location_dict["Misc_Enemies"]
            # Warps
            if((warp_option == "In-World") or (warp_option == "Max Warps")):
                logger.info("In-World Warps")
                if(location in within_world_warps_list):
                    (address_warp_entry_index_dict, address_warp_entry_location_dict) = get_warp_lists(mm, within_world_warps_list[location], address, address_warp_entry_index_dict, address_warp_entry_location_dict)
            if((warp_option == "World Order") or (warp_option == "Max Warps")):
                logger.info("Lair Warps")
                (bottles_index_list, bottles_location_list) = generic_get_lists(mm, combined_bottles_list)
                for item in bottles_location_list:
                    address_bottles_location_list.append(item)
                address_index_dict[address]["Bottles"] = bottles_index_list
            # Misc Options
            if((croctus_option == "1") and (location == "Bubblegloop Swamp")):
                logger.info("Get Croctus Index")
                (croctus_index_list, croctus_location_list) = generic_get_lists(mm, croctus_list)
                for item in croctus_location_list:
                    address_croctus_location_list.append(item)
                address_index_dict[address]["Croctus"] = croctus_index_list
            if((clanker_rings_option == "1") and (location == "Clanker's Cavern")):
                logger.info("Get Clanker Rings Index")
                (clanker_rings_index_list, clanker_rings_location_list) = generic_get_lists(mm, clanker_rings_list)
                for item in clanker_rings_location_list:
                    address_clanker_rings_location_list.append(item)
                address_index_dict[address]["Clanker_Rings"] = clanker_rings_index_list
            if((ancient_ones_option == "1") and (location == "Gobi's Valley")):
                logger.info("Get Ancient Ones Index")
                (ancient_ones_index_list, ancient_ones_location_list) = generic_get_lists(mm, ancient_ones_list)
                for item in ancient_ones_location_list:
                    address_ancient_ones_location_list.append(item)
                address_index_dict[address]["Ancient_Ones"] = ancient_ones_index_list
            if((jinxy_head_option == "1") and (location == "Gobi's Valley")):
                logger.info("Get Ancient Ones Index")
                (jinxy_head_index_list, jinxy_head_location_list) = generic_get_lists(mm, jinxy_head_list)
                for item in jinxy_head_location_list:
                    address_jinxy_head_location_list.append(item)
                address_index_dict[address]["Jinxy_Head"] = jinxy_head_index_list
        
        ### Randomize The Lists
        logger.info("Randomizing Lists Section")
        if(flagged_option == "Shuffle"):
            address_flagged_object_location_list = randomize_list(seed_val, address_flagged_object_location_list)
        if(non_flag_option == "Shuffle"):
            address_no_flag_object_location_list = randomize_list(seed_val, address_no_flag_object_location_list)
        if(struct_option == "Shuffle"):
            address_struct_location_list = randomize_list(seed_val, address_struct_location_list)
        if(enemy_option == "Shuffle"):
            address_ground_enemy_location_list = randomize_list(seed_val, address_ground_enemy_location_list)
            address_flying_enemy_location_list = randomize_list(seed_val, address_flying_enemy_location_list)
            address_wall_enemy_location_list = randomize_list(seed_val, address_wall_enemy_location_list)
        if((warp_option == "In-World") or (warp_option == "Max Warps")):
            address_warp_entry_location_dict = shuffle_within_world_warp_entry_order(seed_val, warp_seed_addition, address_warp_entry_location_dict)
            warp_seed_addition += len("If you're reading this, please check up on your friends <3")
        if((croctus_option == "1") and (location == "Bubblegloop Swamp")):
            address_croctus_location_list = randomize_list(seed_val, address_croctus_location_list)
        if((clanker_rings_option == "1") and (location == "Clanker's Cavern")):
            address_clanker_rings_location_list = randomize_list(seed_val, address_clanker_rings_location_list)
        if((ancient_ones_option == "1") and (location == "Gobi's Valley")):
            address_ancient_ones_location_list = randomize_list(seed_val, address_ancient_ones_location_list)
        if((jinxy_head_option == "1") and (location == "Gobi's Valley")):
            address_jinxy_head_location_list = randomize_list(seed_val, address_jinxy_head_location_list)

        ### Move Everything
        logger.info("Moving Object/Structs/Enemies Section")
        for address in address_dict[location]:
            logger.debug(address)
            mm = create_mmap(file_dir, address)
            # Flagged Objects
            if(flagged_option == "None"):
                logger.info("Flagged Objects Randomization Off")
            elif(flagged_option == "Shuffle"):
                address_flagged_object_location_list = move_flagged_objects(mm, address_index_dict[address]["Flagged_Objects"], address_flagged_object_location_list)
            # No Flag Objects
            if(non_flag_option == "None"):
                logger.info("Non-Flag Objects Randomization Off")
            elif(non_flag_option == "Shuffle"):
                address_no_flag_object_location_list = move_no_flag_objects(mm, address_index_dict[address]["No_Flag_Objects"], address_no_flag_object_location_list)
            # Structs
            if(struct_option == "None"):
                logger.info("Struct Randomization Off")
            elif(struct_option == "Shuffle"):
                address_struct_location_list = move_structs(mm, address_index_dict[address]["Structs"], address_struct_location_list)
            elif(struct_option == "Oh Whoops"):
                oh_whoops_all_notes(mm, address_index_dict[address]["Structs"])
                address_brentilda_location_list = turn_brentildas_into_refills(mm, seed_val, address, address_index_dict[address]["Brentilda"], address_brentilda_location_list)
            # Enemies
            if(enemy_option == "None"):
                logger.info("Enemy Randomization Off")
            elif(enemy_option == "Shuffle"):
                # Grounded Enemies
                address_ground_enemy_location_list = move_local_enemies(mm, address_index_dict[address]["Grounded_Enemies"], address_ground_enemy_location_list)
                # Flying Enemies
                address_flying_enemy_location_list = move_local_enemies(mm, address_index_dict[address]["Flying_Enemies"], address_flying_enemy_location_list)
                # Wall Enemies
                address_wall_enemy_location_list = move_local_enemies(mm, address_index_dict[address]["Wall_Enemies"], address_wall_enemy_location_list)
            elif(enemy_option == "Randomize"):
                # Grounded Enemies
                move_randomized_enemies(mm, seed_val, address_index_dict[address]["Grounded_Enemies"], "Ground", location, address, allow_abnormalities_option)
                # Flying Enemies
                move_randomized_enemies(mm, seed_val, address_index_dict[address]["Flying_Enemies"], "Flying", location, address, allow_abnormalities_option)
                # Wall Enemies
                move_randomized_enemies(mm, seed_val, address_index_dict[address]["Wall_Enemies"], "Wall", location, address, allow_abnormalities_option)
            elif(enemy_option == "Oh Whoops"):
                oh_whoops_all_enemies(mm, seed_val, address_index_dict[address]["Grounded_Enemies"], "Ground", location, address, allow_abnormalities_option)
                oh_whoops_all_enemies(mm, seed_val, address_index_dict[address]["Flying_Enemies"], "Flying", location, address, allow_abnormalities_option)
                oh_whoops_all_enemies(mm, seed_val, address_index_dict[address]["Wall_Enemies"], "Wall", location, address, allow_abnormalities_option)
                oh_whoops_all_enemies(mm, seed_val, address_index_dict[address]["Misc_Enemies"], "Misc", location, address, allow_abnormalities_option)
            # Warps
            if((warp_option == "In-World") or (warp_option == "Max Warps")):
                logger.info("In-World Warps")
                move_within_world_warps_entries(mm, address, address_warp_entry_index_dict, address_warp_entry_location_dict)
            if((warp_option == "World Order") or (warp_option == "Max Warps")):
                logger.info("Lair Warps")
                address_bottles_location_list = move_bottles_mounds(mm, seed_val, address_index_dict[address]["Bottles"], address_bottles_location_list, progression_bottles_moves_mounds, non_progression_bottles_moves_mounds)
            # Croctus
            if((croctus_option == "1") and (location == "Bubblegloop Swamp")):
                address_croctus_location_list = move_no_flag_objects(mm, address_index_dict[address]["Croctus"], address_croctus_location_list)
            # Clanker Rings
            if((clanker_rings_option == "1") and (location == "Clanker's Cavern")):
                address_clanker_rings_location_list = move_no_flag_objects(mm, address_index_dict[address]["Clanker_Rings"], address_clanker_rings_location_list)
            # Ancient Ones
            if((ancient_ones_option == "1") and (location == "Gobi's Valley")):
                address_ancient_ones_location_list = move_no_flag_objects(mm, address_index_dict[address]["Ancient_Ones"], address_ancient_ones_location_list)
            # Jinxy Head
            if((jinxy_head_option == "1") and (location == "Gobi's Valley")):
                address_jinxy_head_location_list = move_no_flag_objects(mm, address_index_dict[address]["Jinxy_Head"], address_jinxy_head_location_list)
    if((warp_option == "World Order") or (warp_option == "Max Warps")):
        shuffle_world_order_warps(file_dir, seed_val)