brentilda_list = [
    "008C0348", # Brentilda (GL 2)
    "010C0348", # Brentilda (GL 3)
    "018C0348", # Brentilda (GL BGS)
    "020C0348", # Brentilda (GL 6)
    "028C0348", # Brentilda (GL Lava)
    "030C0348", # Brentilda (GL 5)
    "038C0348", # Brentilda (GL 4)
    "040C0348", # Brentilda (GL CCW)
    "048C0348", # Brentilda (GL MMM)
    "050C0348", # Brentilda (GL CC)
    ]

inventory_refills = [
    "190C01D8", # Blue Egg Upgrade
    "190C01D9", # Red Feather Upgrade
    "190C01DA", # Gold Feather Upgrade
    ]

croctus_dict = {
    "1": {
        "Object": "008C01FA",
        "Camera": "010024020201",
        },
    "2": {
        "Object": "010C01FA",
        "Camera": "010009020201",
        },
    "3": {
        "Object": "018C01FA",
        "Camera": "01000A020201",
        },
    "4": {
        "Object": "020C01FA",
        "Camera": "01000B020201",
        },
    "5": {
        "Object": "028C01FA",
        "Camera": "01000C020201",
        },
    }

ttc_x_list = [
    "190C0055",
    "3C080047",
    "3C080048",
    "3C080049",
    "3C08004A",
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

ancient_ones_dict = {
    "1": {
        "Object": "008C0147",
        "Camera": "01003B020201",
        },
    "2": {
        "Object": "010C0147",
        "Camera": "01000E020201",
        },
    "3": {
        "Object": "018C0147",
        "Camera": "01000F020201",
        },
    "4": {
        "Object": "020C0147",
        "Camera": "010010020201",
        },
    "5": {
        "Object": "028C0147",
        "Camera": "010011020201",
        },
    }

jinxy_head_dict = {
    "1": {
        "Object": "190C0285",
        "Camera": "010025020201",
    },
    "2": {
        "Object": "190C0286",
        "Camera": "010016020201",
        },
    "3": {
        "Object": "190C0287",
        "Camera": "010017020201",
        },
    }

boggy_race_flags = []
for val in range(0x8C, 0x138C, 0x80):
    boggy_flag_id1 = str(hex(val))[2:]
    for count in range(4-len(boggy_flag_id1)):
        boggy_flag_id1 = "0" + boggy_flag_id1
    boggy_flag_id2 = str(hex(val))[2:]
    for count in range(4-len(boggy_flag_id2)):
        boggy_flag_id2 = "0" + boggy_flag_id2
    boggy_race_flags.append((f"{boggy_flag_id1}0161",f"{boggy_flag_id2}0162"))

note_door = [
    "008C0203",
    "010C0203",
    "018C0203",
    "020C0203",
    "028C0203",
    "030C0203",
    "038C0203",
#     "040C0203", # DoG Note Door
    "048C0203",
    "050C0203",
    "058C0203",
    "060C0203",
    ]