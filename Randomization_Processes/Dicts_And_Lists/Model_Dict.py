'''
Created on Oct 14, 2021

@author: Cyrus
'''

model_dict = {
    "BK_Model1": {
        "Banjo_Fur": {
            "Model_List": [(0xB410,0xC9F0),(0xE210,0xF0B0),(0x11A90,0x11EA0),(0x13500,0x13F70),(0x140D0,0x142B0)],
            "Color_Check": lambda red, green, blue, alpha: (((red > 0x25) and (red > (2.2*green)) and (red < (3*green)) and (red > (10*blue)))
                                                             or ((red == 0x55) and (green == 0x3) and (blue == 0x55)))
                                                             and (alpha == 0xFF),
            },
        "Banjo_Skin": {
            "Model_List": [(0xB130,0xB640),(0xB6B0,0xB730),(0xB750,0xB750),(0xB770,0xBC80),(0xBCF0,0xBD70),(0xBD90,0xBD90),
                           (0xBDB0,0xBE80),(0xBF20,0xBF70),(0xBFE0,0xCD70),(0xCE70,0xD7B0),(0xD8C0,0xEF20),(0x118D0,0x123F0),
                           (0x124F0,0x12C70),(0x12D70,0x13D60),(0x14060,0x144D0)],
            "Color_Check": lambda red, green, blue, alpha: (((red > 0x25) and (red > green) and (red < (4.2*green)) and (red > (1.1*blue)) and (red < (10*blue)))
                                                             or ((green > red) and (green > blue) and (red == blue))
                                                             or ((red == 0xFF) and (green == 0xFF) and (blue == 0xFF))
                                                             or ((red == 0xA7) and (green == 0xA7) and (blue == 0xA7)))
                                                             and (alpha == 0xFF),
            },
        "Banjo_Toes": {
            "Model_List": None,
            "Texture": {
                "Foot1": {
                    "Map": [0x5F0, 0x5F4, 0x5F6, 0x5F8, 0x5FA, 0x5FC, 0x5FE, 0x600, 0x602, 0x604, 0x606, 0x608, 0x60A, 0x60C, 0x60E],
                    },
                "Foot2": {
                    "Map": [0xF10, 0xF12, 0xF14, 0xF16, 0xF18, 0xF1A, 0xF1C, 0xF1E, 0xF20, 0xF22, 0xF24, 0xF26, 0xF28, 0xF2A, 0xF2C, 0xF2E],
                    },
                },
            },
        "Banjo_Shorts": {
            "Model_List": [(0xB5D0,0xBF70),(0x11B50,0x12130)],
            "Color_Check": lambda red, green, blue, alpha: (((red > 0x25) and (red > (1.1*green)) and (red < (5.5*green)) and (red > (10*blue)))
                                                            or ((red == green) and (green >= blue))
                                                            or ((green > red) and (red == blue)))
                                                            and (alpha == 0xFF),
            "Texture": {
                "Pants1": {
                    "Map": [0xAD0, 0xAD6, 0xADA, 0xADC, 0xADE, 0xAE0, 0xAE4, 0xAE6, 0xAE8, 0xAEA, 0xAEC, 0xAEE],
                    },
                "Pants2": {
                    "Map": [0xCF0, 0xCF2, 0xCF6, 0xCFA, 0xCFC, 0xCFE, 0xD00, 0xD04, 0xD06, 0xD0A, 0xD0E],
                    },
                },
            },
        "Kazooie_Feathers": {
            "Model_List": [(0xF0C0, 0xF270),(0xF570,0xF6C0),(0xF840,0xF8E0),(0x11490,0x118C0),(0x14060,0x18790)],
            "Color_Check": lambda red, green, blue, alpha: (red > 0x50) and (red > (2.6*green)) and (blue < 0x5) and (alpha == 0xFF),
            "Texture": {
                "Wing": {
                    "Map": [0x1570,0x157C,0x1582,0x1586,0x1588,0x158A],
                    },
                },
            },
        "Kazooie_Spots": {
            "Model_List": [(0xF0C0,0x11860),(0x140D0,0x14110),(0x144D0,0x144D0),(0x145F0,0x14980)],
            "Color_Check": lambda red, green, blue, alpha: (red > 0xC8) and (red > (1.1*green)) and (red < (2.5*green)) and (red > (10*blue)) and (alpha == 0xFF),
            },
        "Backpack": {
            "Model_List": [(0xB190,0xB940),(0xE8D0,0xFA80),(0x119B0,0x11D10),(0x13F80,0x144C0)],
            "Color_Check": lambda red, green, blue, alpha: (blue > 0x25) and (blue > (1.1*green)) and (blue > (1.1*red)) and (alpha == 0xFF),
            },
        },
#     "BK_Model2": {
#         "Banjo_Fur": {
#             "Model_List": [(0x10B90,0x13050),(0x14A40,0x161F0),(0x194C0,0x1AE90),(0x1C6B0,0x1D540),(0x1FF90,0x226B0)],
#             "Color_Check": lambda red, green, blue, alpha: (red > 0x25) and (red > (2.2*green)) and (red < (3*green)) and (red > (10*blue)) and (alpha == 0xFF),
#             },
#         "Kazooie_Feathers": {
#             "Model_List": [(0x16760,0x16CB0),(0x16CE0,0x16D00),(0x16D70,0x16DB0),(0x16DE0,0x179F0),(0x19050,0x19480),(0x1D560,0x1E180),(0x22E10,0x22E70)],
#             "Color_Check": lambda red, green, blue, alpha: (red > 0x50) and (red > (2.6*green)) and (blue < 0x5) and (alpha == 0xFF),
#             "Texture": {
#                 "Wing": {
#                     "Map": [0x17A0,0x17AA,0x17AC,0x17B0,0x17B4,0x17B6,0x17B8,0x17BA,0x17BC,0x17BE],
#                     },
#                 },
#             },
#         "Kazooie_Spots": {
#             "Model_List": [(0x16760,0x1D6B0)],
#             "Color_Check": lambda red, green, blue, alpha: (red > 0xC8) and (red > (1.1*green)) and (red < (2.5*green)) and (red > (10*blue)) and (alpha == 0xFF),
#             },
#         },
    }