croctus_list = [
    "008C01FA",
    "010C01FA",
    "018C01FA",
    "020C01FA",
    "028C01FA",
    ]

clanker_rings_list = [
    "190C00F9",
    "190C00FA",
    "190C00FB",
    "190C00FC",
    "190C00FD",
    "190C00FE",
    "190C00FF",
    "190C0100",
    ]

ancient_ones_list = [
    "008C0147",
    "010C0147",
    "018C0147",
    "020C0147",
    "028C0147",
    ]

jinxy_head_list = [
    "190C0285",
    "190C0286",
    "190C0287",
    ]

boggy_race_flags = []
for val in range(0x8C, 0x138C, 0x100):
    boggy_flag_id1 = str(hex(val))[2:]
    for count in range(4-len(boggy_flag_id1)):
        boggy_flag_id1 = "0" + boggy_flag_id1
    boggy_flag_id2 = str(hex(val+0x80))[2:]
    for count in range(4-len(boggy_flag_id2)):
        boggy_flag_id2 = "0" + boggy_flag_id2
    boggy_race_flags.append((f"0162{boggy_flag_id1}",f"0162{boggy_flag_id2}"))

other_setup_pointer_list = [
    "9BD0", "9AC0", "9AC8", "9AD0", "9B00", "9AE8", "9AF0", "9B40",
    "9C10", "9AD8", "9AE0", "9AF8", "9B08", "9B18", "9B20", "9B28",
    "9B30", "9B38", "9B48", "9B78", "9BE8", "9BF8", "9870", "9868",
    "9C00", "9B50", "9B60", "9B58", "9BA8", "9BC0", "9B80", "9BA0",
    "9BB0", "9BB8", "9C18", "9C20", "9C28", "9C30", "9C38", "9C40",
    "9878", "9B88", "9B90",
    ]

skip_these_setup_pointer_list = [
    "9BF0", # Sharkfood Island
    "9C08", # GV SNS Egg Room
    ]