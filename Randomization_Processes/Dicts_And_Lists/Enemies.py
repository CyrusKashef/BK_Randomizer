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
            "190C0056", # Shrapnel
            "190C0124", # Snowman
            "190C01C6", # Grimlet
            ],
        "Wall": [
            "190C013B", # Flotsam
            "190C01CC", # Chompa
            "190C029F", # Clucker
            "190C0289", # Vent
            ],
        "Flying": [
            "190C0380", # Scabby
            "190C00CA", # Tee-Hee
            "078C034D", # Bees
            "008C030F", # Whipcrack
            "190C028A", # Whiplash
#             "190C03C1", # Purple Tee-Hee
            ],
        "Misc_Enemies": [
#             "190C000A", # Piranha Fish
#             "190C0068", # Snacker
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
            "190C0152", # Lockup
            ],
        },
    "Clanker's Cavern": {
        "Ground": [
            "190C00F5", # Mutant Snippet
            ],
        },
    "Bubblegloop Swamp": {
        "Ground": [
            "190C0133", # Flibbit
            "190C0137", # Gold Flibbit
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
        "008C00C7", # Ripper (Credits)
        "190C03C2", # Ripper (MMM Entrance)
        "010C037D", # Ice Cube (FP)
        "008C01C6", # Grimlet
        "190C02A4", # TNT 1 (Provide 1-up)
        ],
    "Wall": [
        "008C029F", # Clucker
        "198C0381", # Portrait Chompa
        "1A0C0381", # Portrait Chompa
        "1A8C0381", # Portrait Chompa
        "1B0C0381", # Portrait Chompa
        ],
    "Flying": [
        "078C034D", # Nibbly (Credits)
        ],
    "Misc_Enemies": [
        ]
    }

enemy_id_dict["Click Clock Wood"] = {}
for area in ["Lobby", "Spring", "Summer", "Fall", "Winter"]:
    for enemy_type in enemy_id_dict[f"Click Clock Wood - {area}"]:
        enemy_id_dict["Click Clock Wood"][enemy_type] = enemy_id_dict[f"Click Clock Wood - {area}"][enemy_type]

master_enemy_dict = {
    "Bull": ["190C0004"],
    "Ticker": ["190C0005"],
    "Beehive": ["190C0012"],
    "Snippet": ["190C0067", "008C0067"],
    "Ripper": ["190C00C7", "008C00C7", "190C03C2"],
    "Limbo": ["190C034E"],
    "Mum-mum": ["190C034F"],
    "Seaman Grublin": ["190C0350"],
    "Ice Cube": ["190C037D", "010C037D"],
    "Flotsam": ["190C013B"],
    "Chompa": ["190C01CC"],
    "Clucker": ["190C029F"],
    "Scabby": ["190C0380"],
    "Tee-Hee": ["190C00CA"],
    "Bees": ["078C034D"],
    "Gruntling (Red)": ["190C0367"],
    "Gruntling (Blue)": ["190C03BF"],
    "Gruntling (Black)": ["190C03C0"],
    "Grimlet*": ["190C01C6", "008C01C6"],
    "Buzzbomb": ["190C0134"],
    "Bawl": ["190C036E"],
    "Topper": ["190C036F"],
    "Coliwobble": ["190C036D"],
    "Grublin": ["190C0006"],
    "Yum-Yum": ["190C0069"],
    "Black Snippet": ["190C00F2"],
    "Flibbit (Red)": ["190C0133"],
    "Grublin Hood": ["190C0375"],
    "Portrait Chompa": ["190C0381"],
    "Nibbly": ["190C0163", "078C034D"],
    "Shrapnel": ["190C0056"],
    "Sir Slush*": ["190C0124"],
    "Flibbit (Yellow)*": ["190C0137"],
    "TNT": ["190C02A4", "190C030D"],
    "Vent": ["190C0289"],
    "Snarebear*": ["190C01E9"],
    "Snarebear (Dead)*": ["190C037E"],
    "Snippet (Mutie)*": ["190C00F5", "008C00F5"],
    "Lockup*": ["050C0153", "190C0152"],
    "Whipcrack*": ["008C030F"],
    "Whiplash*": ["190C028A"],
    }