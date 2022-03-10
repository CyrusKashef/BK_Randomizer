'''
@author: Wizzard
'''

from warp import Warp

# Relevant information about the warps within each level
Levels = {
    #  0 - Main Area
    #  1 - Mumbo's Skull
    #  2 - Ticker's Tower
    #  3 - Top Of Ticker's Tower
    "Mumbo's Mountain": {
        # Coming outside from Mumbo's Skull
        Warp("Mumbo's Skull - Outside", 0x16, 0, 1, 0, 0, Warp.Termite): [
            "1579098CF47532060016000000000000",
            "159D098DF49232060016000000000662",
            "15C1098CF4AE32060016000000000663",
            "15E0098EF4CB32060016000000000000",
        ],
        # Coming inside to Mumbo's Skull
        Warp("Mumbo's Skull - Inside", 0x17, 1, 0): [
            "0000005103A94B0600170000000063A9",
        ],
        # Coming outside from the lower part of Ticker's Tower
        Warp("Ticker's Tower - Lower/Outside", 0x18, 0, 2): [
            "03DC0663FC384E06001800000001071A",
        ],
        # Coming inside to the lower part of Ticker's Tower
        Warp("Ticker's Tower - Lower/Inside", 0x19, 2, 0): [
            "008E003CFCB83206001900000006118B",
            "0124003CFCB93206001900000006118C",
        ],
        # Coming outside from the upper part of Ticker's Tower
        Warp("Ticker's Tower - Upper/Outside", 0x1A, 3, 2): [
            "011F0E1AFD224586001A000000000000",
            "01670E13FCE74886001A000000017972",
            "01D30E10FCC73A06001A00000006815B",
        ],
        # Coming inside to the upper part of Ticker's Tower
        Warp("Ticker's Tower - Upper/Inside", 0x1B, 2, 3): [
            "FDC608DCFD662586001B00000006784B",
            "FD9C08CCFD932586001B000000067856",
            "FD6A08DCFDC62586001B00000006784A",
            "FD60090EFD5F2586001B000000000000",
        ],
    },
    #  0 - Main Area
    #  1 - Blubber's Ship
    #  2 - Sandcastle
    #  3 - Nipper
    #  4 - Alcove Under Arch
    #  5 - Top Of Mountain/Bottom Of Lighthouse
    #  6 - Top Of Lighthouse
    "Treasure Trove Cove": {
    },
    "Clanker's Cavern": {
    },
    # 0 - Main Area
    # 1 - Mumbo's Skull
    # 2 - Tiptup Choir
    "Bubblegloop Swamp": {
    },
    # 0 - Main Area
    # 1 - Mumbo's Skull
    # 2 - Boggy's Igloo
    # 3 - Christmas Tree
    # 4 - Wozza's Cave
    "Freezeezy Peak": {
        # Coming outside from Mumbo's Skull
        Warp(debugName="Skull (Outside)", objectId=0x43, warpsTo=0, warpsFrom=1, flagsNeededToExit=0, flagsNeededToEnter=0, flagsForLearnedAbilities=Warp.Walrus): [
            "0000005103A94B060043000000000064",
        ],
        # Coming inside to Mumbo's Skull
        Warp("Skull (Inside)", 0x40, 1, 0): [
            "1B7C02BAF30E32060040000000000000",
            "1B9C02BAF356320600400000000128B5",
            "1BC002BAF38F32060040000000000000",
        ],
        # Coming outside from Igloo
        Warp("Igloo (Outside)", 0x44, 0, 2): [
            "0007008603D25006004400000011FFB7",
        ],
        # Coming inside to Igloo
        Warp("Igloo (Inside)", 0x41, 2, 0): [
            "01C20DF924EE2F86004100000000D45D",
        ],
        # Coming outside from Christmas Tree
        Warp("Tree (Outside)", 0x45, 0, 3): [
            "0017FDA6FFE599860045000000000F84",
        ],
        # Coming inside to Christmas Tree
        Warp("Tree (Inside)", 0x42, 3, 0): [
            "EE1803A718684C060042000000000000",
        ],
        # Coming outside from Cave
        Warp("Cave (Outside)", 0xFC, 0, 4): [
            "031B0066F9F0640600FC000000000000",
            "03590066FA0B640600FC000000000064",
            "03970066FA33640600FC00000000F9BA",
            "03D80066FA58640600FC000000000000",
        ],
        # Coming inside to Cave
        Warp("Cave (Inside)", 0xFD, 4, 0): [
            "E6CB0396F0F1898600FD000000000064",
            "E6E90396F156898600FD000000000000",
            "E7080396F1A5898600FD000000000000",
            "E72A0396F1EF898600FD000000000000",
        ],
    },
    # 0 - Main Area
    # 1 - Jinxy
    # 2 - Rupee
    # 3 - Matching Puzzle
    # 4 - Water Pyramid
    # 5 - King Sandybutt Maze
    "Gobi's Valley": {
        # Jinxy To Main
        Warp(debugName="Jinxy (To Main)", objectId=0x06, warpsTo=0, warpsFrom=1, flagsNeededToExit=0, flagsNeededToEnter=0): [
            "0B73004EFFCF50060006000000000000",
        ],
        # Main To Jinxy
        Warp(debugName="Jinxy (From Main)", objectId=0x05, warpsTo=1, warpsFrom=0, flagsNeededToExit=0, flagsNeededToEnter=0): [
            "F06D05D317103E860005000000000000",
        ],
        # Rupee To Main
        Warp(debugName="Rupee (To Main)", objectId=0x64, warpsTo=0, warpsFrom=2, flagsNeededToExit=0, flagsNeededToEnter=0): [
            "000F00A306417D860064000000000064",
        ],
        # Main To Rupee
        Warp(debugName="Rupee (From Main)", objectId=0x60, warpsTo=2, warpsFrom=0, flagsNeededToExit=0, flagsNeededToEnter=0): [
            "F09E0B4C02A443860060000000000000",
        ],
        # Matching Puzzle To Main
        Warp(debugName="Matching Puzzle (To Main)", objectId=0x61, warpsTo=0, warpsFrom=3, flagsNeededToExit=0, flagsNeededToEnter=0): [
            "FA91015000236406006100002B000064",
        ],
        # Main To Matching Puzzle
        Warp(debugName="Matching Puzzle (From Main)", objectId=0x5C, warpsTo=3, warpsFrom=0, flagsNeededToExit=0, flagsNeededToEnter=0): [
            "0F3F09DF01432A86005C000000000000",
        ],
        # Water Pyramid Bottom To Main
        Warp(debugName="Water Pyramid Bottom (To Main)", objectId=0x63, warpsTo=0, warpsFrom=4, flagsNeededToExit=0, flagsNeededToEnter=0): [
            "0006011406D48D060063000000000000",
        ],
        # Main To Water Pyramid Bottom
        Warp(debugName="Water Pyramid Bottom (From Main)", objectId=0x5F, warpsTo=4, warpsFrom=0, flagsNeededToExit=0, flagsNeededToEnter=0): [
            "FF1C0BCBF20D6406005F000000029226",
        ],
        # Main To Water Pyramid Top
        Warp(debugName="Water Pyramid Top (From Main)", objectId=0x5E, warpsTo=4, warpsFrom=0, flagsNeededToExit=0, flagsNeededToEnter=0): [
            "000610A2EED56386005E000000000000",
        ],
        # Main To King Sandybutt Start
        Warp(debugName="King Sandybutt Start (From Main)", objectId=0x5D, warpsTo=5, warpsFrom=0, flagsNeededToExit=0, flagsNeededToEnter=Warp.NeedsEggs): [
            "00460A0A028D5186005D00000000FF49",
        ],
        # King Sandybutt Start To Main
        Warp(debugName="King Sandybutt Start (To Main)", objectId=0x62, warpsTo=0, warpsFrom=5, flagsNeededToExit=0, flagsNeededToEnter=0): [
            "1825008C015E63860062000000000064",
        ],
        # King Sandybutt End To Main
        Warp(debugName="King Sandybutt End (From Main)", objectId=0xDE, warpsTo=0, warpsFrom=5, flagsNeededToExit=0, flagsNeededToEnter=0): [
                "EA94006B046C460600DE000000000064",
                "EACB006B0486460600DE000000000000",
                "EB0B006B04A4460600DE000000000000",
        ],
    },
    "Mad Monster Mansion": {
    },
    "Rusty Bucket Bay": {
    },
    "Click Clock Wood - Lobby": {
    },
    "Click Clock Wood - Spring": {
    },
    "Click Clock Wood - Summer": {
    },
    "Click Clock Wood - Fall": {
    },
    "Click Clock Wood - Winter": {
    },
    "Click Clock Wood": {
    },
}
