enemy_id_dict = {
    "Global": {
        "Ground": [
            "190C0004", # Bull
            "190C0005", # Ticker
            "190C0012", # Beehive
            "190C0067", # Snippet
            "190C00C7", # RIP Tombstone
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
            "190C0380", # Scabby
            "190C00CA", # Tee-Hee
            "078C034D", # Bees
            ],
        "Misc_Enemies": [
#             "190C000A", # Piranha Fish
#             "190C0068", # Snacker
#             "190C030F", # Whipcrack
#             "190C028A", # Underwater Whipcrack
#             "190C0056", # Shrapnel
#             "190C03C1", # Purple Tee-Hee
            ],
        },
    "Gruntilda's Lair": {
        "Ground": [
            "190C0367", # Gruntling
            "190C03BF", # Gruntling 2
            "190C03C0", # Gruntling 3
            "190C01C6", # Grimlet
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            ],
        },
    "Spiral Mountain": {
        "Ground": [
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
            "190C0069", # Yum Yum
            "190C00F2", # Black Snippet
            ],
        },
    "Clanker's Cavern": {
        "Ground": [
            ],
        },
    "Bubblegloop Swamp": {
        "Ground": [
            "190C0133", # Flibbit
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
            ],
        },
    "Mad Monster Mansion": {
        "Wall": [
            "190C0381", # Portrait Chompa
            ],
        "Flying": [
            "190C0163", # Nibbly
            ],
        },
    "Rusty Bucket Bay": {
        "Ground": [
            "190C030D", # TNT 2 (Seen Out In Open)
            ],
        },
    "Click Clock Wood - Lobby": {
        "Ground": [
            "190C0375", # Grublin Hood
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            ],
        },
    "Click Clock Wood - Spring": {
        "Ground": [
            "190C0375", # Grublin Hood
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            ],
        },
    "Click Clock Wood - Summer": {
        "Ground": [
            "190C0375", # Grublin Hood
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            ],
        },
    "Click Clock Wood - Fall": {
        "Ground": [
            "190C0375", # Grublin Hood
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            ],
        },
    "Click Clock Wood - Winter": {
        "Ground": [
            "190C0375", # Grublin Hood
            ],
        "Flying": [
            "190C0134", # Dragon Fly
            ],
        },
    }

additional_search_enemy_id_dict = {
    "Ground": [
        "008C0067", # Snippet (TTC)
        "008C00C7", # RIP Tombstone (Credits)
        "190C03C2", # RIP Tombstone (MMM Entrance)
        "010C037D", # Ice Cube (FP)
        ],
    "Wall": [
        "008C029F", # Clucker
        "198C0381", # Portrait Chompa
        "1A0C0381", # Portrait Chompa
        "1A8C0381", # Portrait Chompa
        "1B0C0381", # Portrait Chompa
        ],
    "Flying": [
        "078C034D", # Nibbly
        ],
    "Misc_Enemies": [
#         "008C030F", # Whipcrack
        ]
    }

softlock_enemy_id_list = {
    "Global": {
        "Ground": [
            "190C0056", # Shrapnel
            "190C00F5", # Mutant Snippet
            "190C0124", # Snowman
            ],
        "Wall": [
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
        "Ground": [
            "190C0137", # Gold Flibbit
            ],
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
            ]
        },
    "Click Clock Wood - Lobby": {
        "Ground": [
            "190C01E9", # Venus Flytrap
            "190C037E", # Dead Venus Flytrap
            ]
        },
    "Click Clock Wood - Spring": {
        "Ground": [
            "190C01E9", # Venus Flytrap
            "190C037E", # Dead Venus Flytrap
            ]
        },
    "Click Clock Wood - Summer": {
        "Ground": [
            "190C01E9", # Venus Flytrap
            "190C037E", # Dead Venus Flytrap
            ]
        },
    "Click Clock Wood - Fall": {
        "Ground": [
            "190C01E9", # Venus Flytrap
            "190C037E", # Dead Venus Flytrap
            ]
        },
    "Click Clock Wood - Winter": {
        "Ground": [
            "190C01E9", # Venus Flytrap
            "190C037E", # Dead Venus Flytrap
            ]
        },
    }

additional_softlock_enemy_id_list = {
    "Ground": [
        "050C0153", # Lockup
        "008C01C6", # Grimlet
        "190C02A4", # TNT 1 (Provide 1-up)
        ],
    "Wall": [
        ],
    "Flying": [
        ],
    }

beta_enemy_id_dict = {
    "Global": {
        "Ground": [
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
    }

for curr_dict in [enemy_id_dict, softlock_enemy_id_list, beta_enemy_id_dict]:
    curr_dict["Click Clock Wood"] = {}
    for area in ["Lobby", "Spring", "Summer", "Fall", "Winter"]:
        for enemy_type in curr_dict[f"Click Clock Wood - {area}"]:
            curr_dict["Click Clock Wood"][enemy_type] = curr_dict[f"Click Clock Wood - {area}"][enemy_type]