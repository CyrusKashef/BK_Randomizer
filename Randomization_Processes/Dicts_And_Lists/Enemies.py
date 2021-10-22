enemy_id_dict = {
    "Global": {
        "Ground": [
#             "190C0004", # Bull
            "190C0005", # Ticker
            "190C0012", # Beehive
            "190C0067", # Snippet
            "190C00C7", # RIP Tombstone
            #"190C00F5", # Mutant Snippet
#             "190C0124", # Snowman
            "190C034E", # Skeleton
            "190C034F", # Mummy
            "190C0350", # Sea Grublin
            "190C037D", # Ice Cube
            ],
        "Wall": [
            "190C013B", # Flotsam
            "190C01CC", # Chompa
            "190C029F", # Clucker
            ],
        "Flying": [
            "190C0380", # Beetle
            "190C00CA", # Tee-Hee
            "078C034D", # Bees
            ],
        "Misc_Enemies": [
#             "190C000A", # Piranha Fish
#             "190C0068", # Snacker
#             "190C030F", # Whipcrack
#             "190C028A", # Underwater Whipcrack
#             "190C0056", # Shrapnel
            #"190C03C1", # Purple Tee-Hee
            ],
        },
    "Gruntilda's Lair": {
        "Ground": [
            "190C0004", # Bull
            "190C0367", # Gruntling
            "190C03BF", # Gruntling 2
            "190C03C0", # Gruntling 3
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            ],
        },
    "Spiral Mountain": {
        "Ground": [
            "190C0004", # Bull
            "190C036E", # Bawl
            "190C036F", # Topper
            ],
        "Flying": [
            "190C036D", # Coliwobble
            ],
        },
    "Mumbo's Mountain": {
        "Ground": [
            "190C0006", # Grublin
            ],
        },
    "Treasure Trove Cove": {
        "Ground": [
            "190C0004", # Bull
            "190C0069", # Yum Yum
            #"190C00F2", # Black Snippet
#             "190C0124", # Snowman
#             "190C0152", # Lockup
            ],
        },
    "Clanker's Cavern": {
        "Ground": [
            ],
        },
    "Bubblegloop Swamp": {
        "Ground": [
            "190C0133", # Flibbit
            #"190C0137", # Gold Flibbit
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            ],
        },
    "Freezeezy Peak": {
        "Ground": [
            ],
        },
    "Gobi's Valley": {
        "Ground": [
            "190C0120", # Slappa
#             "190C0124", # Snowman
            ],
        },
    "Mad Monster Mansion": {
        "Wall": [
            "190C0381", # Portrait Chompa
            ],
        "Flying": [
            "190C0163", # Bat
            ],
        },
    "Rusty Bucket Bay": {
        "Ground": [
            #"190C02A4", # TNT 1 (Provide 1-up)
            "190C030D", # TNT 2 (Seen Out In Open)
            ],
        },
    "Click Clock Wood - Lobby": {
        "Ground": [
#             "190C01E9", # Venus Flytrap
            "190C0375", # Grublin Hood
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            #"190C029C", # Attacking Zubba
            ],
        },
    "Click Clock Wood - Spring": {
        "Ground": [
#             "190C01E9", # Venus Flytrap
            "190C0375", # Grublin Hood
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            #"190C029C", # Attacking Zubba
            ],
        },
    "Click Clock Wood - Summer": {
        "Ground": [
#             "190C01E9", # Venus Flytrap
            "190C0375", # Grublin Hood
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            #"190C029C", # Attacking Zubba
            ],
        },
    "Click Clock Wood - Fall": {
        "Ground": [
#             "190C01E9", # Venus Flytrap
            "190C0375", # Grublin Hood
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            #"190C029C", # Attacking Zubba
            ],
        },
    "Click Clock Wood - Winter": {
        "Ground": [
#             "190C0124", # Snowman
#             "190C01E9", # Venus Flytrap
            "190C0375", # Grublin Hood
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            #"190C029C", # Attacking Zubba
            ],
        },
    }

additional_enemy_id_dict = {
    "Ground": [
#         "190C0153", # Lockup
        "008C0067", # Snippet (TTC)
        "190C03C2", # RIP Tombstone (MMM Entrance)
        "010C037D", # Ice Cube (FP)
        ],
    "Wall": [
        "198C0381", # Portrait Chompa
        "1A0C0381", # Portrait Chompa
        "1A8C0381", # Portrait Chompa
        "1B0C0381", # Portrait Chompa
        ],
    "Flying": [
        ],
    }

abnormal_enemy_id_list = {
    "Global": {
        "Ground": [
            "190C0056", # Shrapnel
#             "190C0124", # Snowman
            ],
        "Wall": [
            "190C0289", # Vent
            ],
        "Flying": [
            ],
        },
    "Gruntilda's Lair": {
        },
    "Spiral Mountain": {
        },
    "Mumbo's Mountain": {
        },
    "Treasure Trove Cove": {
        "Ground": [
            "190C0152", # Lockup
            ],
        },
    "Clanker's Cavern": {
        },
    "Bubblegloop Swamp": {
        },
    "Freezeezy Peak": {
        },
    "Gobi's Valley": {
        },
    "Mad Monster Mansion": {
        },
    "Rusty Bucket Bay": {
        "Ground": [
            "190C01C6", # Grimlet
            "190C02A4", # TNT 1 (Provide 1-up)
            "190C030D", # TNT 2 (Seen Out In Open)
            ]
        },
    "Click Clock Wood - Lobby": {
            "190C01E9", # Venus Flytrap
            "190C037E", # Dead Venus Flytrap
        },
    "Click Clock Wood - Spring": {
            "190C01E9", # Venus Flytrap
            "190C037E", # Dead Venus Flytrap
        },
    "Click Clock Wood - Summer": {
            "190C01E9", # Venus Flytrap
            "190C037E", # Dead Venus Flytrap
        },
    "Click Clock Wood - Fall": {
            "190C01E9", # Venus Flytrap
            "190C037E", # Dead Venus Flytrap
        },
    "Click Clock Wood - Winter": {
            "190C01E9", # Venus Flytrap
            "190C037E", # Dead Venus Flytrap
        },
    }

additional_abnormal_enemy_id_dict = {
    "Ground": [
        ],
    "Wall": [
        "190C0368", # Mumbo Token Sign
        "190C0369", # Mumbo Token Sign
        "190C036A", # Mumbo Token Sign
        "190C036B", # Mumbo Token Sign
        "190C0382", # Portrait
        "190C0387", # Portrait
        ],
    "Flying": [
        ],
    }