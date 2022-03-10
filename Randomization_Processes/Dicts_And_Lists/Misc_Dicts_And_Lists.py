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
    0: { # 50
        10: {
            "Door_Vertices": [0xBE50, 0xBE60, 0xBE70, 0xBE80],
            "Overlay_Textures": 0xB2CE,
            },
        1: {
            "Door_Vertices": [0xBE90, 0xBEA0, 0xBEB0, 0xBEC0],
            "Overlay_Textures": 0xB326,
            },
        },
    1: { # 180
        100: {
            "Door_Vertices": [0xBED0, 0xBEE0, 0xBEF0, 0xBF00],
            "Overlay_Textures": 0xB376,
            },
        10: {
            "Door_Vertices": [0xBF10, 0xBF20, 0xBF30, 0xBF40],
            "Overlay_Textures": 0xB3CE,
            },
        1: {
            "Door_Vertices": [0xBF50, 0xBF60, 0xBF70, 0xBF80],
            "Overlay_Textures": 0xB3FE,
            },
        },
    2: { # 260
        100: {
            "Door_Vertices": [0xBF90, 0xBFA0, 0xBFB0, 0xBFC0],
            "Overlay_Textures": 0xB44E,
            },
        10: {
            "Door_Vertices": [0xBFD0, 0xBFE0, 0xBFF0, 0xC000],
            "Overlay_Textures": 0xB4A6,
            },
        1: {
            "Door_Vertices": [0xC010, 0xC020, 0xC030, 0xC040],
            "Overlay_Textures": 0xB4D6,
            },
        },
    3: { # 350
        100: {
            "Door_Vertices": [0xC050, 0xC060, 0xC070, 0xC080],
            "Overlay_Textures": 0xB526,
            },
        10: {
            "Door_Vertices": [0xC090, 0xC0A0, 0xC0B0, 0xC0C0],
            "Overlay_Textures": 0xB57E,
            },
        1: {
            "Door_Vertices": [0xC0D0, 0xC0E0, 0xC0F0, 0xC100],
            "Overlay_Textures": 0xB5AE,
            },
        },
    4: { # 450
        100: {
            "Door_Vertices": [0xC110, 0xC120, 0xC130, 0xC140],
            "Overlay_Textures": 0xB5FE,
            },
        10: {
            "Door_Vertices": [0xC150, 0xC160, 0xC170, 0xC180],
            "Overlay_Textures": 0xB656,
            },
        1: {
            "Door_Vertices": [0xC190, 0xC1A0, 0xC1B0, 0xC1C0],
            "Overlay_Textures": 0xB686,
            },
        },
    5: { # 640
        100: {
            "Door_Vertices": [0xC1D0, 0xC1E0, 0xC1F0, 0xC200],
            "Overlay_Textures": 0xB6D6,
            },
        10: {
            "Door_Vertices": [0xC210, 0xC220, 0xC230, 0xC240],
            "Overlay_Textures": 0xB72E,
            },
        1: {
            "Door_Vertices": [0xC250, 0xC260, 0xC270, 0xC280],
            "Overlay_Textures": 0xB75E,
            },
        },
    6: { # 765
        100: {
            "Door_Vertices": [0xC290, 0xC2A0, 0xC2B0, 0xC2C0],
            "Overlay_Textures": 0xB7AE,
            },
        10: {
            "Door_Vertices": [0xC2D0, 0xC2E0, 0xC2F0, 0xC300],
            "Overlay_Textures": 0xB806,
            },
        1: {
            "Door_Vertices": [0xC310, 0xC320, 0xC330, 0xC340],
            "Overlay_Textures": 0xB836,
            },
        },
    7: { # 810
        100: {
            "Door_Vertices": [0xC350, 0xC360, 0xC370, 0xC380],
            "Overlay_Textures": 0xB886,
            },
        10: {
            "Door_Vertices": [0xC390, 0xC3A0, 0xC3B0, 0xC3C0],
            "Overlay_Textures": 0xB8DE,
            },
        1: {
            "Door_Vertices": [0xC3D0, 0xC3E0, 0xC3F0, 0xC400],
            "Overlay_Textures": 0xB90E,
            },
        },
    8: { # 828
        100: {
            "Door_Vertices": [0xC410, 0xC420, 0xC430, 0xC440],
            "Overlay_Textures": 0xB886,
            },
        10: {
            "Door_Vertices": [0xC450, 0xC460, 0xC470, 0xC480],
            "Overlay_Textures": 0xB8DE,
            },
        1: {
            "Door_Vertices": [0xC490, 0xC4A0, 0xC4B0, 0xC4C0],
            "Overlay_Textures": 0xB90E,
            },
        },
    9: { # 846
        100: {
            "Door_Vertices": [0xC4D0, 0xC4E0, 0xC4F0, 0xC500],
            "Overlay_Textures": 0xB886,
            },
        10: {
            "Door_Vertices": [0xC510, 0xC520, 0xC530, 0xC540],
            "Overlay_Textures": 0xB8DE,
            },
        1: {
            "Door_Vertices": [0xC550, 0xC560, 0xC570, 0xC580],
            "Overlay_Textures": 0xB90E,
            },
        },
    10: { # 864
        100: {
            "Door_Vertices": [0xC590, 0xC5A0, 0xC5B0, 0xC5C0],
            "Overlay_Textures": 0xB886,
            },
        10: {
            "Door_Vertices": [0xC5D0, 0xC5E0, 0xC5F0, 0xC600],
            "Overlay_Textures": 0xB8DE,
            },
        1: {
            "Door_Vertices": [0xC610, 0xC620, 0xC630, 0xC640],
            "Overlay_Textures": 0xB90E,
            },
        },
    11: { # 882
        100: {
            "Door_Vertices": [0xC650, 0xC660, 0xC670, 0xC680],
            "Overlay_Textures": 0xB886,
            },
        10: {
            "Door_Vertices": [0xC690, 0xC6A0, 0xC6B0, 0xC6C0],
            "Overlay_Textures": 0xB8DE,
            },
        1: {
            "Door_Vertices": [0xC6D0, 0xC6E0, 0xC6F0, 0xC700],
            "Overlay_Textures": 0xB90E,
            },
        },
    }