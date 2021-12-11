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

furnace_fun_questions_pointer_list = [pointer for pointer in range(0xEF38, 0xFFB8 + 1, 0x8)]
furnace_fun_questions_pointer_list.append(0xECE8)

rbb_pipes_grimlets = {
    "Pipes": {
        # Pipes themselves are structs?
        # Formatted AAAA BBBB XXXX YYYY ZZZZ?
        # "Location": {
        #     "Search_Text": XYZ,
        #     "Warp": XYZ,
        #     "Entry": XYZ,
        #     },
        "Front": {
            "Search_Text": "EE080000FC7D",
            "Warp": "EE08001EFC7D",
            "Entry": "ED4200AFFC7A",
            },
        "Center": {
            "Search_Text": "002CFE700359",
            "Warp": "002BFE6F0350",
            "Entry": "FFAEFF1F03D0",
            },
        "Rear": {
            "Search_Text": "1A5EFCE0FDDA",
            "Warp": "1A5EFCFEFDDA",
            "Entry": "1B35FD8FFDDA",
            },
        },
    "Grimlet": {
        # "Location": {
        #     "Search_Text": SCRIPT + OBJECT_ID,
        #     },
        "Front": {
            "Search_Text": "008C01C6",
            },
        "Center": {
            "Search_Text": "190C01C6",
            },
        "Rear": {
            "Search_Text":  "190C01C6",
            },
        },
    }

gv_matching_puzzle_pictures = {
    # TILE: START HEX
    0x0190: 0x15304, 0x0191: 0x153C4, 0x0192: 0x154C4, 0x0193: 0x155C4,
    0x0194: 0x15504, 0x0195: 0x15784, 0x0196: 0x15844, 0x0197: 0x15604,
    0x0198: 0x15884, 0x0199: 0x15A84, 0x019A: 0x15B84, 0x019B: 0x152C4,
    0x019C: 0x15B44, 0x019D: 0x15404, 0x019E: 0x15A44, 0x019F: 0x15744
    }

note_door_texture_offsets = {
    0: "1820",
    1: "3040",
    2: "4040",
    3: "5040",
    4: "6040",
    5: "7040",
    6: "8040", 
    7: "9040",
    8: "A040",
    9: "8040",
    }

note_door_indices = {
    0: {
        10: {
            "Door_Textures": [0xBE5C, 0xBE6C, 0xBE7C, 0xBE8C],
            "Overlay_Textures": 0xB2CE,
            },
        1: {
            "Door_Textures": [0xBE9C, 0xBEAC, 0xBEBC, 0xBECC],
            "Overlay_Textures": 0xB326,
            },
        },
    1: {
        100: {
            "Door_Textures": [0xBEDC, 0xBEEC, 0xBEFC, 0xBF0C],
            "Overlay_Textures": 0xB376,
            },
        10: {
            "Door_Textures": [0xBF1C, 0xBF2C, 0xBF3C, 0xBF4C],
            "Overlay_Textures": 0xB3CE,
            },
        1: {
            "Door_Textures": [0xBF5C, 0xBF6C, 0xBF7C, 0xBF8C],
            "Overlay_Textures": 0xB3FE,
            },
        },
    2: {
        100: {
            "Door_Textures": [0xBF9C, 0xBFAC, 0xBFBC, 0xBFCC],
            "Overlay_Textures": 0xB44E,
            },
        10: {
            "Door_Textures": [0xBFDC, 0xBFEC, 0xBFFC, 0xC00C],
            "Overlay_Textures": 0xB4A6,
            },
        1: {
            "Door_Textures": [0xC01C, 0xC02C, 0xC03C, 0xC04C],
            "Overlay_Textures": 0xB4D6,
            },
        },
    3: {
        100: {
            "Door_Textures": [0xC05C, 0xC06C, 0xC07C, 0xC08C],
            "Overlay_Textures": 0xB526,
            },
        10: {
            "Door_Textures": [0xC09C, 0xC0AC, 0xC0BC, 0xC0CC],
            "Overlay_Textures": 0xB57E,
            },
        1: {
            "Door_Textures": [0xC0DC, 0xC0EC, 0xC0FC, 0xC10C],
            "Overlay_Textures": 0xB5AE,
            },
        },
    4: {
        100: {
            "Door_Textures": [0xC11C, 0xC12C, 0xC13C, 0xC14C],
            "Overlay_Textures": 0xB5FE,
            },
        10: {
            "Door_Textures": [0xC15C, 0xC16C, 0xC17C, 0xC18C],
            "Overlay_Textures": 0xB656,
            },
        1: {
            "Door_Textures": [0xC19C, 0xC1AC, 0xC1BC, 0xC1CC],
            "Overlay_Textures": 0xB686,
            },
        },
    5: {
        100: {
            "Door_Textures": [0xC1DC, 0xC1EC, 0xC1FC, 0xC20C],
            "Overlay_Textures": 0xB6D6,
            },
        10: {
            "Door_Textures": [0xC21C, 0xC22C, 0xC23C, 0xC24C],
            "Overlay_Textures": 0xB72E,
            },
        1: {
            "Door_Textures": [0xC25C, 0xC26C, 0xC27C, 0xC28C],
            "Overlay_Textures": 0xB75E,
            },
        },
    6: {
        100: {
            "Door_Textures": [0xC29C, 0xC2AC, 0xC2BC, 0xC2CC],
            "Overlay_Textures": 0xB7AE,
            },
        10: {
            "Door_Textures": [0xC2DC, 0xC2EC, 0xC2FC, 0xC30C],
            "Overlay_Textures": 0xB806,
            },
        1: {
            "Door_Textures": [0xC31C, 0xC32C, 0xC33C, 0xC34C],
            "Overlay_Textures": 0xB836,
            },
        },
    7: {
        100: {
            "Door_Textures": [0xC35C, 0xC36C, 0xC37C, 0xC38C],
            "Overlay_Textures": 0xB886,
            },
        10: {
            "Door_Textures": [0xC39C, 0xC40C, 0xC41C, 0xC42C],
            "Overlay_Textures": 0xB8DE,
            },
        1: {
            "Door_Textures": [0xC43C, 0xC44C, 0xC45C, 0xC46C],
            "Overlay_Textures": 0xB90E,
            },
        },
    8: {
        100: {
            "Overlay_Textures": 0xB886,
            },
        10: {
            "Overlay_Textures": 0xB8DE,
            },
        1: {
            "Overlay_Textures": 0xB90E,
            },
        },
    9: {
        100: {
            "Overlay_Textures": 0xB886,
            },
        10: {
            "Overlay_Textures": 0xB8DE,
            },
        1: {
            "Overlay_Textures": 0xB90E,
            },
        },
    10: {
        100: {
            "Overlay_Textures": 0xB886,
            },
        10: {
            "Overlay_Textures": 0xB8DE,
            },
        1: {
            "Overlay_Textures": 0xB90E,
            },
        },
    11: {
        100: {
            "Overlay_Textures": 0xB886,
            },
        10: {
            "Overlay_Textures": 0xB8DE,
            },
        1: {
            "Overlay_Textures": 0xB90E,
            },
        },
    }