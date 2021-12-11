'''
Created on Aug 29, 2021

@author: Cyrus
'''

warp_dict = {
    "Mumbo's Mountain": {
        "Safe": {
            "MM_To_Skull_Outside": [
                "0000005103A94B0600170000000063A9",
                ],
            "MM_To_Lower_Ticker_Outside": [
                "008E003CFCB83206001900000006118B",
                "0124003CFCB93206001900000006118C",
                ],
            },
        "Unsafe": {
            "MM_To_Skull_Inside": [
                "1579098CF47532060016000000000000",
                "159D098DF49232060016000000000662",
                "15C1098CF4AE32060016000000000663",
                "15E0098EF4CB32060016000000000000",
                ],
            "MM_To_Lower_Ticker_Inside": [
                "03DC0663FC384E06001800000001071A",
                ],
            "MM_To_Upper_Ticker_Inside": [
                "011F0E1AFD224586001A000000000000",
                "01670E13FCE74886001A000000017972",
                "01D30E10FCC73A06001A00000006815B",
                ],
            "MM_To_Upper_Ticker_Outside": [
                "FDC608DCFD662586001B00000006784B",
                "FD9C08CCFD932586001B000000067856",
                "FD6A08DCFDC62586001B00000006784A",
                "FD60090EFD5F2586001B000000000000",
                ],
            },
        "Safe_Transform": {
            },
        "Unsafe_Transform": {
            },
        },
    "Treasure Trove Cove": {
        "Safe": {
            "TTC_To_Sandcastle_Outside": [
                "FFF9007805E25A860072000000000000",
                ],
            "TTC_To_Nipper_Outside": [
                "FCEC0045FC3D3206000B000000000000",
                "FD0B0045FC6F3206000B000000000000",
                "FD2E0045FC9D3206000B000000000000",
                "FD570045FCD93206000B00000014A1C7",
                "FD770045FD0B3206000B000000000000",
                "FD980045FD393206000B000000000064",
                "FDC3006FFD3F1906000B000000000000",
                "FDE90018FD3B1906000B000000000000",
                ],
            "TTC_To_Ship_Lower_Outside": [
                "FD73FDCD026C36860076000000000000",
                ],
            "TTC_To_Ship_Upper_Outside": [
                "01F5015DFFFD29860075000000000000",
                ],
            },
        "Unsafe": {
            "TTC_To_Sandcastle_Inside": [
                "09B5000011E45786006B000000000000",
                ],
            "TTC_To_Nipper_Inside": [
                "E89E0346109E31060047000000001B6E",
                "E894034C100F2B060047000000001E45",
                "E89903920F931F060047000000000000",
                "E899032D0F9317860047000000000000",
                ],
            "TTC_To_Ship_Lower_Inside": [
                "FDC0017A03D34D86006F000000000000",
                ],
            "TTC_To_Ship_Upper_Inside": [
                "00E802B503DF3F86006E000000000000",
                ],
            "TTC_To_Alcove": [
                "0AD20A72F6C77A86006D000000000000",
                "0ADE0A72F5747A86006D000000000000",
                ],
            "TTC_To_Top_Of_Mountain": [
                "063E12B6F87B8686006C000000000000",
                ],
            "TTC_To_Lighthouse_Bottom": [
                "020C1B4AF58F2B860071000000000000",
                "02031B4AF56125060071000000000064",
                "01E01B4DF54428060071000000000000",
                ],
            "TTC_To_Lighthouse_Top": [
                "01C21E77F57639060070000000012E61",
                ],
            },
        "Safe_Transform": [
            ],
        "Unsafe_Transform": [
            ],
        },
    "Clanker's Cavern": {
        "Safe": {
#                 "Left_Gill",
#                 "Right_Gill",
#                 "Gold_Feather_Room"
            },
        "Unsafe": {
#                 "Left_Tooth",
#                 "Right_Tooth",
#                 "Blowhole_To_Belly",
#                 "Blowhole_To_Mouth",
#                 "From_Gold_Feather_Room"
            },
        "Safe_Transform": [
            ],
        "Unsafe_Transform": [
            ],
        },
    "Bubblegloop Swamp": {
        "Safe": {
            "BGS_To_Skull_Outside": [
                "0000005103A94B06000A00000002E875",
                ],
            "BGS_To_Tanktup_Outside": [
                "FFF000000764960600680000000095A1",
                ],
            },
        "Unsafe": {
            "BGS_To_Skull_Inside": [
                "E62A0450EAD539860009000000000000",
                "E64D0454EAB33986000900000009EC1C",
                "E6660455EA963986000900000009EC1C",
                "E6890456EA78398600090000000522DF",
                ],
            "BGS_To_Tanktup_Inside": [
                "0F6800C004E41906004600000000A21F",
                "0F6500FF04E419060046000000000000",
                ]
            },
        "Safe_Transform": {
            "BGS_To_Left_Croc_Nostril_Outside": [
                "FC7F0082F1B125860067000000000000",
                "FC9C007AF1C82586006700000001C4DF",
                "FCB30079F1EA25860067000000000000",
                ],
            "BGS_To_Right_Croc_Nostril_Outside": [
                "FBA70081F32032060066000000000000",
                "FBC50064F3323206006600000001AC8C",
                "FBE70064F34632060066000000000000",
                ]
            },
        "Unsafe_Transform": {
            "BGS_To_Left_Croc_Nostril_Inside": [
                "FE0E00BEF7312D06006A000000000000",
                "FE3200BEF71C2D06006A000000000000",
                "FE5700BDF7062D06006A000000000000",
                "FE7900BDF6F52D06006A000000000000",
                "FE9A00BDF6E22D06006A000000000064",
                ],
            "BGS_To_Right_Croc_Nostril_Inside": [
                "016B00BEF6ED2D060069000000000064",
                "002D0000000000640580004000100142",
                "01D900BEF72032060069000000000000",
                "01F400BEF73C2D060069000000000000",
                ],
            },
        },
    "Freezeezy Peak": {
        "Safe": {
            "FP_To_Igloo_Outside": [
                "0007008603D25006004400000011FFB7",
                ],
            "FP_To_Skull_Outside": [
                "0000005103A94B060043000000000064",
                ]
            },
        "Unsafe": {
            "FP_To_Igloo_Inside": [
                "01C20DF924EE2F86004100000000D45D",
                ],
            "FP_To_Skull_Inside": [
                "1B7C02BAF30E32060040000000000000",
                "1B9C02BAF356320600400000000128B5",
                "1BC002BAF38F32060040000000000000",
                ],
            "FP_To_Tree_Inside": [
                "EE1803A718684C060042000000000000",
                ],
            "FP_To_Cave_Inside": [
                "E6CB0396F0F1898600FD000000000064",
                "E6E90396F156898600FD000000000000",
                "E7080396F1A5898600FD000000000000",
                "E72A0396F1EF898600FD000000000000",
                ],
            "FP_To_Tree_Outside": [
                "0017FDA6FFE599860045000000000F84",
                ],
            "FP_To_Cave_Outside": [
                "031B0066F9F0640600FC000000000000",
                "03590066FA0B640600FC000000000064",
                "03970066FA33640600FC00000000F9BA",
                "03D80066FA58640600FC000000000000",
                ]
            },
        "Safe_Transform": {
            },
        "Unsafe_Transform": {
            },
        },
    "Gobi's Valley": {
        "Safe": {
            "GV_To_Jinxy_Outside": [
                "0B73004EFFCF50060006000000000000",
                ],
            "GV_To_Rupee_Pyramid_Outside": [
                "000F00A306417D860064000000000064",
                ],
            "GV_To_King_Sandybutt_Maze_Start_Outside": [
                "1825008C015E63860062000000000064",
                ],
            "GV_To_King_Sandybutt_Maze_End_Outside": [
                "EA94006B046C460600DE000000000064",
                "EACB006B0486460600DE000000000000",
                "EB0B006B04A4460600DE000000000000",
                ],
            "GV_To_Matching_Pyramid_Outside": [
                "FA91015000236406006100002B000064",
                ],
            "GV_To_Water_Pyramid_Bottom_Outside": [
                "0006011406D48D060063000000000000",
                ],
            },
        "Unsafe": {
            "GV_To_Matching_Pyramid_Inside": [
                "0F3F09DF01432A86005C000000000000",
                ],
            "GV_To_King_Sandybutt_Maze_Start_Inside": [
                "00460A0A028D5186005D00000000FF49",
                ],
            "GV_To_Water_Pyramid_Top_Inside": [
                "000610A2EED56386005E000000000000",
                ],
            "GV_To_Water_Pyramid_Bottom_Inside": [
                "FF1C0BCBF20D6406005F000000029226",
                ],
            "GV_To_Rupee_Pyramid_Inside": [
                "F09E0B4C02A443860060000000000000",
                ],
            "GV_To_Jinxy_Inside": [
                "F06D05D317103E860005000000000000",
                ],
            },
        "Safe_Transform": {
            },
        "Unsafe_Transform": {
            },
        },
    "Mad Monster Mansion": {
        "Safe": {
            "MMM_Outside_Dining_Room": [
                "0000009F0C1954860088000000000000",
                ],
            "MMM_First_Floor_1": [
                "000B00C6FDBD4F860092000000000000",
                ],
            "MMM_First_Floor_2": [
                "000000AAFD754C860091000000000000",
                ],
            "MMM_Second_Floor_1": [
                "000800E7FD3475860094000000000000",
                ],
            "MMM_Second_Floor_2": [
                "FFFB00F0FD2161060093000000000000",
                ],
            "MMM_Well_Top_Exit": [
                "000008E400003986008A000000000000",
                ],
            "MMM_Outside_Tumblar": [
                "0000009105F75506008B00000000094E",
                ],
            "MMM_Outside_Church_Secret_Room": [
                "FE240183FCC74306008D000000000000",
                "FEC70185FCC64306008D000000000000",
                "FFD0018FFCC44106008D000000000000",
                "FFCF0092FCC44506008D000000000000",
                "FEC50094FCC34506008D000000000000",
                "FE210099FCC54306008D000000000000",
                ],
            "MMM_Outside_Cellar": [
                "FD2F01ACFAB33E860090000000000378",
                ],
            "MMM_Outside_Mumbo_Skull": [
                "00010051039D4B0600990000000EED9F",
                ],
            },
        "Unsafe": {
#             "MMM_Inside_Church": [
#                 "F6E5014DF6336B06007D000000001951",
#                 ],
            "MMM_Inside_Cellar": [
                "FD2EFF1F00EF53860081000000000000",
                ],
            "MMM_Inside_Tumblar": [
                "06C601D8EE944486007C000000019DFB",
                ],
            "MMM_Well_Top_Entrance": [
                "1645FF45F2EE3C06007B000000000000",
                ],
            "MMM_Inside_Dining_Room": [
                "03E70148045C53860079000000000F6A",
                ],
            "MMM_Inside_Egg_Room": [
                "026F015E04A734060082000000000000",
                ],
            "MMM_Inside_Note_Room": [
                "03F906F2FD9A59060086000000000000",
                ],
            "MMM_Inside_Feather_Room": [
                "056F0156FCC838860083000000000000",
                ],
            "MMM_Inside_Church_Secret_Room": [
                "F23701A1F58E5486007E000000000B8A",
                ],
            "MMM_Inside_Bathroom": [
                "0665053FFF224D060087000000000000",
                ],
            "MMM_Inside_Bedroom": [
                "03D406EC04495D860084000000000000",
                ],
            "MMM_Inside_Gold_Feather_Room": [
                "0665053FFF224D060087000000000000",
                ],
            "MMM_Inside_Mumbo_Skull": [
                "FE0900E9ED202586009A000000007230",
                "FE2200E4ED382586009A00000000B11C",
                "FE3800E5ED512586009A00000000B11E",
                "FE5600E8ED6E2586009A000000000000",
                ],
            "MMM_Inside_Third_Floor_1": [
                "03D406EC04495D860084000000000000",
                ],
            "MMM_Outside_Third_Floor_1": [
                "000200BEFDC248860096000000000000",
                ],
            "MMM_Inside_Third_Floor_2": [
                "03F906F2FD9A59060086000000000000",
                ],
            "MMM_Outside_Third_Floor_2": [
                "000200F2FD1D66860095000000000000",
                ],
            "MMM_Chimney": [
                "03EA094F00F81D86007A000000000000",
                ],
#             "MMM_Outside_Church_Door": [
#                 "FF9000EE1A509606008C000000000000",
#                 "004E00EE1A4E9606008C000000000000",
#                 ],
            "MMM_Church_Tower_Lower": [
                "F51505EBFA1044060097000000000000",
                ],
            "MMM_Chuch_Tower_Upper": [
                "F510084FF9872586009800000001DE34",
                ],
            },
        "Safe_Transform": {
            "MMM_Outside_Gutter_Lower": [
                "FFF9005802073306008F00000006D0F8",
                ],
            "MMM_Outside_Well_Bottom": [
                "024E001F01E11106011F000000000064",
                ],
            },
        "Unsafe_Transform": {
            "MMM_Outside_Loggo": [
                "001C017505A447060120000000001A3F"
                ],
            "MMM_Inside_Gutter_Lower": [
                "09970021071A1906008000000006DC62",
                ],
            "MMM_Inside_Well_Bottom": [
                "159AFE4DF3711906011E000000000000",
                "15BBFE4DF38F1906011E000000000000",
                ]
            },
        },
    "Rusty Bucket Bay": {
        "Safe": {
#             Kept softlocking, but also don't have destination on BB?
#             "RBB_Outside_Big_Fish_Warehouse_Side": [
#                 "064FFD1102BCFA0600BA000000000000",
#                 "0702FD860062C08600BA000000000000",
#                 ],
            "RBB_Outside_Boat_Room": [
                "F7CEFD85003D750600B3000000001882",
                ],
            "RBB_Outside_Left_Blue_Container": [
                "FFEB00E50599998600B4000000000000",
                "FE13011F0575BC8600B4000000000000",
                ],
            "RBB_Outside_Middle_Blue_Container": [
                "000303C402C24D8600B5000000000000",
                ],
            "RBB_Outside_Right_Blue_Container": [
                "002D005003E0578600B6000000000000",
                "002D00E603E0578600B6000000000000",
                "0125009F0391680600B6000000000000",
                ],
            "RBB_Outside_Kitchen": [
                "FCC4026CFB97368600AF000000000000",
                ],
            "RBB_Outside_Navigation_Room": [
                "03BC016C01142D0600B0000000000000",
                "03BC015702A92D0600B0000000000064",
                "03BC00C601142D0600B0000000000000",
                "03BC00C602A92D0600B0000000000000",
                "03A10008018E3E8600B0000000000000",
                "03A1000802363E8600B0000000000074",
                "04CB00E501E88F0600B0000000000064",
                ],
            "RBB_Outside_Captain_Room": [
                "FDE900DFFDE1278600AC000000000000",
                "FE070003FDF93C8600AC000000000000",
                ],
            "RBB_Outside_Middle_Pipe": [
                "01FE0326FC85780600B1000000014A2C",
                ],
            "RBB_Outside_Bedroom": [
                "014C00DBFD573C0600AD000000000000",
                "FFFC00E3FC5E8F8600AD000000000000",
                "FEDA00DBFD563C0600AD000000000000",
                "008B0000FD41420600AD000000000000",
                "FFA20000FD43420600AD000000000000",
                ],
            "RBB_Outside_Main_Engine_Room": [
                "FFF40A270FE33B8600B200000016CD8A",
                ],
            "RBB_Outside_Big_Boombox_Room": [
                "FAD205B90000858600B7000000000000",
                ],
            "RBB_Outside_Machine_Control_Room": [
                "F2AF01B0F0F2F40600AE000000000000",
                "EF9601E0F24EFA0600AE000000000000",
                "EFEA01B0F564FA0600AE000000000064",
                "EFB70425F013FA0600AE000000000064",
                "EDC504C1F382CF0600AE000000000064",
                "F03A0640F1CE4A0600AE000000000064",
                "EEDC06A2F2797E0600AE000000000064",
                "F07F0655F304560600AE000000000000",
                ],
            "RBB_Outside_Anchor_Room": [
                "FC00FF42FFD99406011C000000000000",
                ],
            },
        "Unsafe": {
            "RBB_Inside_Big_Fish_Warehouse_Top": [
                "E890FBC60DC8748600A7000000000000",
                ],
            "RBB_Inside_Big_Fish_Warehouse_Side": [
                "E911FA210DB8FA0600B9000000000000",
                "E911F7B30DB8FA0600B9000000000000",
                ],
            "RBB_Inside_Boat_Room": [
                "E05BF7ED043BBC8600A80000000020AA",
                ],
            "RBB_Inside_Left_Blue_Container": [
                "FBD2FDD5F2977F0600A9000000000000",
                ],
            "RBB_Inside_Middle_Blue_Container": [
                "FE73FDCCF2575B8600AA000000000000",
                ],
            "RBB_Inside_Right_Blue_Container": [
                "0102FDCBF28B7E8600AB000000000000",
                ],
            "RBB_Inside_Kitchen": [
                "EE08001EFC7D190600A3000000000064",
                ],
            "RBB_Inside_Navigation_Room": [
                "F1F100A603B7348600A4000000000000",
                "F1F4000003F2288600A4000000000000",
                ],
            "RBB_Inside_Captain_Room": [
                "F38800A2FC4E330600A0000000000000",
                "F38FFFE2FC25340600A0000000000000",
                ],
            "RBB_Inside_Middle_Pipe": [
                "002BFE6F03501A0600A5000000000000",
                ],
            "RBB_Inside_Bedroom": [
                "0199FF19FD2F3C8600A1000000000000",
                "0185FE21FCE32F8600A1000000000000",
                ],
            "RBB_Inside_Main_Engine_Room": [
                "056A002B00BB1C8600A6000000000064",
                "054F003200DE1C8600A6000000000064",
                "0530003501061C0600A6000000000064",
                "05120032012D1C8600A6000000000000",
                ],
            "RBB_Inside_Big_Boombox_Room": [
                "1008FB500062D00600B8000000000000",
                "0FFEFB50FF83D00600B8000000000000",
                ],
            "RBB_Inside_Machine_Control_Room": [
                "1A5EFCFEFDDA190600A2000000000064",
                ],
            "RBB_Inside_Anchor_Room": [
                "ECEEFA4A00D05006011D000000000000",
                "EC9AFA58007F5006011D000000000000",
                "EC48FA5800345006011D000000000000",
                ],
            },
        "Safe_Transform": {
            },
        "Unsafe_Transform": {
            },
        },
    "Click Clock Wood - Lobby": {
        "Safe": {
            },
        "Unsafe": {
            "CCW_Lobby_Spring_Entrance": [
                "000000610EF14B0600DB000000000000",
                ],
            "CCW_Lobby_Summer_Entrance": [
                "F10F005E00004B0600DC000000000000",
                ],
            "CCW_Lobby_Fall_Entrance": [
                "00000061F10F4B0600DD000000000000",
                ],
            "CCW_Lobby_Winter_Entrance": [
                "0EF100DD00004B0600DA000000000000",
                ],
            },
        "Safe_Transform": {
            },
        "Unsafe_Transform": {
            },
        },
    "Click Clock Wood - Spring": {
        "Safe": {
#             "Spring_Warp_From_Lobby": [
#                 "000000610EF14B0600DB000000000000",
#                 ],
            "CCW_Spring_Outside_Mumbo_Skull": [
                "0000005103A94B0600DF000000063B96",
                ],
            "CCW_Spring_Outside_Nabnut_Door": [
                "00000064036B5A0600EB0000000F5A7B",
                ],
            "CCW_Spring_Outside_Nabnut_Window": [
                "FEA300D503524B060127000000000000",
                ],
            "CCW_Spring_Outside_Whipcrack_Room": [
                "00000070FB356B860058000000003DB3",
                ],
            },
        "Unsafe": {
#             "CCW_Spring_Warp_To_Lobby": [
#                 "000000771E917D0600D700000000ABF3",
#                 ],
            "CCW_Spring_Inside_Mumbo_Skull": [
                "E53402D000004B0600E30000000E1592",
                ],
            "CCW_Spring_Inside_Nabnut_Door": [
                "FFFC11B10894640600E7000000000000",
                ],
            "CCW_Spring_Inside_Nabnut_Window": [
                "FEB111DF09AB32060123000000000000",
                ],
            "CCW_Spring_Inside_Whipcrack_Room": [
                "000016B1F81757860012000000000000",
                ],
            },
        "Safe_Transform": {
#             "Spring_Outside_Beehive",
            },
        "Unsafe_Transform": {
#             "Spring_Inside_Beehive",
            },
        },
    "Click Clock Wood - Summer": {
        "Safe": {
#             "Summer_Warp_From_Lobby": [
#                 "F10F005E00004B0600DC000000000000",
#                 ],
            "CCW_Summer_Outside_Mumbo_Skull": [
                "0000005103A94B0600E0000000004FEE",
                ],
            "CCW_Summer_Outside_Nabnut_Door": [
                "00000064036B5A0600EC00000000918F",
                ],
            "CCW_Summer_Outside_Nabnut_Window": [
                "FEA200D503524B060128000000000000",
                ],
            "CCW_Summer_Outside_Whipcrack_Room": [
                "00000070FB356B860059000000000000",
                ],
            "CCW_Summer_Outside_Beehive": [
                "FF2A05D6FBE84F860111000000000000",
                ],
            },
        "Unsafe": {
#             "Summer_Warp_To_Lobby": [],
            "CCW_Summer_Inside_Mumbo_Skull": [
                "E57F02D000004B0600E4000000040EC9",
                ],
            "CCW_Summer_Inside_Nabnut_Door": [
                "FFDA11B10886640600E8000000000000",
                ],
            "CCW_Summer_Inside_Nabnut_Window": [
                "FEB111DF09AB32060124000000000000",
                ],
            "CCW_Summer_Inside_Whipcrack_Room": [
                "000016B1F81757860013000000000064",
                ],
            "CCW_Summer_Inside_Beehive": [
                "0E2AEED53386010E00000000000001B0",
                ],
            },
        "Safe_Transform": {
            },
        "Unsafe_Transform": {
            },
        },
    "Click Clock Wood - Fall": {
        "Safe": {
#             "Fall_Warp_From_Lobby": [
#                 "00000061F10F4B0600DD000000000000",
#                 ],
            "CCW_Fall_Outside_Mumbo_Skull": [
                "0000005103A94B0600E1000000000064",
                ],
            "CCW_Fall_Outside_Nabnut_Door": [
                "00000064036B5A0600ED000000000000",
                ],
            "CCW_Fall_Outside_Nabnut_Window": [
                "FEA200D503524B060129000000000000",
                ],
            "CCW_Fall_Outside_Whipcrack_Room": [
                "00000070FB356B86005A00000000C75E",
                ],
            "CCW_Fall_Outside_Attic_1": [
                "000000C0FB693A86002D000000000000",
                ],
            "CCW_Fall_Outside_Beehive": [
                "FF2A05D6FBE84F860112000000000000",
                ],
            },
        "Unsafe": {
#             "CCW_Fall_Warp_To_Lobby": [],
            "CCW_Fall_Inside_Mumbo_Skull": [
                "E54802D000004B0600E500000004276B",
                ],
            "CCW_Fall_Inside_Nabnut_Door": [
                "000011B10894640600E9000000000000",
                ],
            "CCW_Fall_Inside_Nabnut_Window": [
                "FEB211DF09AC32060125000000000000",
                ],
            "CCW_Fall_Inside_Whipcrack_Room": [
                "000016B1F81757860014000000000000",
                ],
            "CCW_Fall_Inside_Attic_1": [
                "04E113E3084B3206002A000000000000",
                "051E13E3082A3206002A000000000000",
                ],
            "CCW_Fall_Inside_Beehive": [
                "00000E2AEEC93386010F000000000000",
                ],
            },
        "Safe_Transform": {
            },
        "Unsafe_Transform": {
            },
        },
    "Click Clock Wood - Winter": {
        "Safe": {
            "CCW_Winter_Warp_From_Lobby": [
                "0EF100DD00004B0600DA000000000000",
                ],
            "CCW_Winter_Outside_Mumbo_Skull": [
                "0000005103A94B0600E2000000000064",
                ],
            "CCW_Winter_Outside_Nabnut_Window": [
                "FEA200D503534B06012A000000000000",
                ],
            "CCW_Winter_Outside_Whipcrack_Room": [
                "00000070FB356B86005B000000000000",
                ],
            "CCW_Winter_Outside_Attic_1": [
                "000001F0FAB55786002C000000000000",
                ],
            "CCW_Winter_Outside_Attic_2": [
                "000000C0FB693A86002E000000000000",
                ],
            },
        "Unsafe": {
#             "Winter_Warp_To_Lobby": [],
            "CCW_Winter_Inside_Mumbo_Skull": [
                "E53402D000004B0600E6000000095742",
                ],
            "CCW_Winter_Inside_Nabnut_Window": [
                "FEB111DB09AB31860126000000000000",
                ],
            "CCW_Winter_Inside_Whipcrack_Room": [
                "FFFF16B1F8174B060015000000000000",
                ],
            "CCW_Winter_Inside_Attic_1": [
                "04E713E308523206002B000000000000",
                "051B13E308343206002B000000000000",
                ],
            "CCW_Winter_Inside_Attic_2": [
                "FF2E13DB0AAA2C060029000000143FF2",
                ],
            },
        "Safe_Transform": {
            },
        "Unsafe_Transform": {
            },
        },
    "Click Clock Wood": {
        "Safe": {
            "CCW_Spring_Warp_To_Lobby": [
                "000000771E917D0600D700000000ABF3"
                ],
            },
        "Unsafe": {
#             "CCW_Summer_Warp_To_Lobby": [
#                 "000000771E917D0600D8000000000000"
#                 ],
#             "CCW_Fall_Warp_To_Lobby": [
#                 "000000771E917D0600D9000000000000"
#                 ],
#             "CCW_Winter_Warp_To_Lobby": [
#                 "000000771E917D0600D6000000000000"
#                 ],
            "CCW_Spring_Inside_Mumbo_Skull": [
                "E53402D000004B0600E30000000E1592",
                ],
            "CCW_Spring_Inside_Nabnut_Door": [
                "FFFC11B10894640600E7000000000000",
                ],
            "CCW_Spring_Inside_Nabnut_Window": [
                "FEB111DF09AB32060123000000000000",
                ],
            "CCW_Spring_Inside_Whipcrack_Room": [
                "000016B1F81757860012000000000000",
                ],
            "CCW_Summer_Inside_Mumbo_Skull": [
                "E57F02D000004B0600E4000000040EC9",
                ],
            "CCW_Summer_Inside_Nabnut_Door": [
                "FFDA11B10886640600E8000000000000",
                ],
            "CCW_Summer_Inside_Nabnut_Window": [
                "FEB111DF09AB32060124000000000000",
                ],
            "CCW_Summer_Inside_Whipcrack_Room": [
                "000016B1F81757860013000000000064",
                ],
            "CCW_Summer_Inside_Beehive": [
                "0E2AEED53386010E00000000000001B0",
                ],
            "CCW_Fall_Inside_Mumbo_Skull": [
                "E54802D000004B0600E500000004276B",
                ],
            "CCW_Fall_Inside_Nabnut_Door": [
                "000011B10894640600E9000000000000",
                ],
            "CCW_Fall_Inside_Nabnut_Window": [
                "FEB211DF09AC32060125000000000000",
                ],
            "CCW_Fall_Inside_Whipcrack_Room": [
                "000016B1F81757860014000000000000",
                ],
            "CCW_Fall_Inside_Attic_1": [
                "04E113E3084B3206002A000000000000",
                "051E13E3082A3206002A000000000000",
                ],
            "CCW_Fall_Inside_Beehive": [
                "00000E2AEEC93386010F000000000000",
                ],
            "CCW_Winter_Inside_Mumbo_Skull": [
                "E53402D000004B0600E6000000095742",
                ],
            "CCW_Winter_Inside_Nabnut_Window": [
                "FEB111DB09AB31860126000000000000",
                ],
            "CCW_Winter_Inside_Whipcrack_Room": [
                "FFFF16B1F8174B060015000000000000",
                ],
            "CCW_Winter_Inside_Attic_1": [
                "04E713E308523206002B000000000000",
                "051B13E308343206002B000000000000",
                ],
            "CCW_Winter_Inside_Attic_2": [
                "FF2E13DB0AAA2C060029000000143FF2",
                ],
            "CCW_Lobby_Spring_Entrance": [
                "000000610EF14B0600DB000000000000"
                ],
            "CCW_Lobby_Summer_Entrance": [
                "F10F4B0600DD00000000000000800040"
                ],
            "CCW_Lobby_Fall_Entrance": [
                "00000061F10F4B0600DD000000000000"
                ],
            "CCW_Lobby_Winter_Entrance": [
                "0EF100DD00004B0600DA000000000000"
                ],
            "CCW_Spring_Outside_Mumbo_Skull": [
                "E53402D000004B0600E30000000E1592",
                ],
            "CCW_Spring_Outside_Nabnut_Door": [
                "FFFC11B10894640600E7000000000000",
                ],
            "CCW_Spring_Outside_Nabnut_Window": [
                "FEB111DF09AB32060123000000000000",
                ],
            "CCW_Spring_Outside_Whipcrack_Room": [
                "000016B1F81757860012000000000000",
                ],
            "CCW_Summer_Outside_Mumbo_Skull": [
                "E57F02D000004B0600E4000000040EC9",
                ],
            "CCW_Summer_Outside_Nabnut_Door": [
                "FFDA11B10886640600E8000000000000",
                ],
            "CCW_Summer_Outside_Nabnut_Window": [
                "FEB111DF09AB32060124000000000000",
                ],
            "CCW_Summer_Outside_Whipcrack_Room": [
                "000016B1F81757860013000000000064",
                ],
            "CCW_Summer_Outside_Beehive": [
                "0E2AEED53386010E00000000000001B0",
                ],
            "CCW_Fall_Outside_Mumbo_Skull": [
                "0000005103A94B0600E1000000000064",
                ],
            "CCW_Fall_Outside_Nabnut_Door": [
                "00000064036B5A0600ED000000000000",
                ],
            "CCW_Fall_Outside_Nabnut_Window": [
                "FEA200D503524B060129000000000000",
                ],
            "CCW_Fall_Outside_Whipcrack_Room": [
                "00000070FB356B86005A00000000C75E",
                ],
            "CCW_Fall_Outside_Attic_1": [
                "000000C0FB693A86002D000000000000",
                ],
            "CCW_Fall_Outside_Beehive": [
                "FF2A05D6FBE84F860112000000000000",
                ],
            "CCW_Winter_Outside_Mumbo_Skull": [
                "0000005103A94B0600E2000000000064",
                ],
            "CCW_Winter_Outside_Nabnut_Window": [
                "FEA200D503534B06012A000000000000",
                ],
            "CCW_Winter_Outside_Whipcrack_Room": [
                "00000070FB356B86005B000000000000",
                ],
            "CCW_Winter_Outside_Attic_1": [
                "000001F0FAB55786002C000000000000",
                ],
            "CCW_Winter_Outside_Attic_2": [
                "000000C0FB693A86002E000000000000",
                ],
            },
        "Safe_Transform": {
#         "Spring_Outside_Beehive",
            },
        "Unsafe_Transform": {
#         "Spring_Inside_Beehive",
            },
        }
    }