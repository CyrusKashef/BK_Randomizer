'''
Created on Dec 20, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

from random import seed, choice

###################
### WARPS CLASS ###
###################

# Warps are the places gone to after transitioning out of a loading zone
class Warp:
    # Flags indicating what is needed to get back to the main entrance after using a warp
    Termite     = 1 << 0
    Crocodile   = 1 << 1
    Walrus      = 1 << 2
    Pumpkin     = 1 << 3
    Bee         = 1 << 4
    Banjo       = 1 << 5

    def __init__(self, debug_name, object_id, warps_to, warps_from, can_exit_from_room=63, can_enter_warp_zone=63, keep_in_same_setup=False, keep_in_same_world=False, warp_search_strings=[]):
        self.name = debug_name
        self.old_object_id = object_id
        self.new_object_id = object_id # Updated as warps are randomized
        self.warps_name = debug_name # This is the name of the warp that got replaced by this one
        self.warps_to = warps_to
        self.warps_from = warps_from # During randomization, this is updated to reflect that a warp comes from a different place
        self.can_exit_from_room = can_exit_from_room
        self.can_enter_warp_zone = can_enter_warp_zone
        self.keep_in_same_setup = keep_in_same_setup # Some events trigger from another area in the world, such as the sandcastle, and can therefore not be moved in order to allow 100%
        self.keep_in_same_world = keep_in_same_world # Some warps mess up when shuffling globally, so these need to be randomized within the world or not randomized at all for global only
        self.old_warp_search_strings = warp_search_strings
        self.new_warp_search_strings = warp_search_strings

    def SwapWarps(self, other):
        # New Object ID
        temp = self.new_object_id
        self.new_object_id = other.new_object_id
        other.new_object_id = temp
        # New Name
        temp = self.warps_name
        self.warps_name = other.warps_name
        other.warps_name = temp
        # New Warp From
        temp = self.warps_from
        self.warps_from = other.warps_from
        other.warps_from = temp
        # New Can Enter Warp Zone
        temp = self.can_enter_warp_zone
        self.can_enter_warp_zone = other.can_enter_warp_zone
        other.can_enter_warp_zone = temp
        # New Can Exit Warp Zone
#         temp = self.can_exit_from_room
#         self.can_exit_from_room = other.can_exit_from_room
#         other.can_exit_from_room = temp
        # Keep In Same Setup
        temp = self.keep_in_same_setup
        self.keep_in_same_setup = other.keep_in_same_setup
        other.keep_in_same_setup = temp
        # Keep In Same World
        temp = self.keep_in_same_world
        self.keep_in_same_world = other.keep_in_same_world
        other.keep_in_same_world = temp
        # Warp Strings
        temp = self.new_warp_search_strings
        self.new_warp_search_strings = other.new_warp_search_strings
        other.new_warp_search_strings = temp
        return self

##############
### LEVELS ###
##############

# Relevant information about the warps within each level
# Debug Name: Where the warp leads to
# Object ID: Warp's id value
# Warps To/From: ID given to area (We choose this. All main areas are divisible by 0x10
Levels = {
    "Mumbo's Mountain": [
        Warp(debug_name="MM Mumbo's Skull (Going Outside)", object_id=0x17, warps_to=0x100, warps_from=0x101, warp_search_strings=[
            "0000005103A94B0600170000000063A9",
            ]),
        Warp(debug_name="MM Mumbo's Skull (Coming Inside)", object_id=0x16, warps_to=0x101, warps_from=0x100, warp_search_strings=[
            "159D098DF49232060016000000000662",
            "15E0098EF4CB32060016000000000000",
            "1579098CF47532060016000000000000",
            "15C1098CF4AE32060016000000000663",
            ]),
        Warp(debug_name="MM Ticker's Tower (Going Outside - Lower)", object_id=0x19, warps_to=0x100, warps_from=0x102, warp_search_strings=[
            "0124003CFCB93206001900000006118C",
            "008E003CFCB83206001900000006118B",
            ]),
        Warp(debug_name="MM Ticker's Tower (Coming Inside - Lower)", object_id=0x18, warps_to=0x102, warps_from=0x100, warp_search_strings=[
            "03DC0663FC384E06001800000001071A",
            ]),
        Warp(debug_name="MM Ticker's Tower (Going Outside - Upper)", object_id=0x1B, warps_to=0x103, warps_from=0x102, warp_search_strings=[
            "FDC608DCFD662586001B00000006784B",
            "FD6A08DCFDC62586001B00000006784A",
            "FD60090EFD5F2586001B000000000000",
            "FD9C08CCFD932586001B000000067856",
            ]),
        Warp(debug_name="MM Ticker's Tower (Coming Inside - Upper)", object_id=0x1A, warps_to=0x102, warps_from=0x103, warp_search_strings=[
            "011F0E1AFD224586001A000000000000",
            "01670E13FCE74886001A000000017972",
            "01D30E10FCC73A06001A00000006815B",
            ]),
        ],
    "Treasure Trove Cove": [
        Warp(debug_name="TTC Nipper's Shell (Going Outside)", object_id=0x0B, warps_to=0x200, warps_from=0x201, warp_search_strings=[
            "FD980045FD393206000B000000000064",
            "FD770045FD0B3206000B000000000000",
            "FCEC0045FC3D3206000B000000000000",
            "FDE90018FD3B1906000B000000000000",
            "FD0B0045FC6F3206000B000000000000",
            "FDC3006FFD3F1906000B000000000000",
            "FD570045FCD93206000B00000014A1C7",
            "FD2E0045FC9D3206000B000000000000",
            ]),
        Warp(debug_name="TTC Nipper's Shell (Coming Inside)", object_id=0x47, warps_to=0x201, warps_from=0x200, can_enter_warp_zone=Warp.Banjo, keep_in_same_setup=True, warp_search_strings=[
            "E899032D0F9317860047000000000000",
            "E89903920F931F060047000000000000",
            "E894034C100F2B060047000000001E45",
            "E89E0346109E31060047000000001B6E",
            ]),
        Warp(debug_name="TTC Sandcastle (Going Outside)", object_id=0x72, warps_to=0x200, warps_from=0x202, warp_search_strings=[
            "FFF9007805E25A860072000000000000",
            ]),
        Warp(debug_name="TTC Sandcastle (Coming Inside)", object_id=0x6B, warps_to=0x202, warps_from=0x200, keep_in_same_world=True, can_exit_from_room=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Pumpkin), warp_search_strings=[
            "09B5000011E45786006B000000000000",
            ]),
        Warp(debug_name="TTC Salty Hippo (Going Outside - Top)", object_id=0x75, warps_to=0x200, warps_from=0x203, warp_search_strings=[
            "01F5015DFFFD29860075000000000000",
            ]),
        Warp(debug_name="TTC Salty Hippo (Coming Inside - Top)", object_id=0x6E, warps_to=0x203, warps_from=0x200, can_enter_warp_zone=Warp.Banjo,
                                                                                                          can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "00E802B503DF3F86006E000000000000",
            ]),
        Warp(debug_name="TTC Salty Hippo (Going Outside - Side)", object_id=0x76, warps_to=0x200, warps_from=0x204, warp_search_strings=[
            "FD73FDCD026C36860076000000000000",
            ]),
        Warp(debug_name="TTC Salty Hippo (Coming Inside - Side)", object_id=0x6F, warps_to=0x204, warps_from=0x200, can_enter_warp_zone=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Pumpkin),
                                                                                                           can_exit_from_room=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Pumpkin), warp_search_strings=[
            "FDC0017A03D34D86006F000000000000",
            ]),
        Warp(debug_name="TTC To Top Of The Mountain", object_id=0x6D, warps_to=0x206, warps_from=0x205, warp_search_strings=[
            "0AD20A72F6C77A86006D000000000000",
            "0ADE0A72F5747A86006D000000000000",
            ]),
        Warp(debug_name="TTC To Arch Under Alcove", object_id=0x6C, warps_to=0x205, warps_from=0x206, warp_search_strings=[
            "063E12B6F87B8686006C000000000000",
            ]),
        Warp(debug_name="TTC To Lighthouse Upper", object_id=0x71, warps_to=0x207, warps_from=0x206, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "020C1B4AF58F2B860071000000000000",
            "02031B4AF56125060071000000000064",
            "01E01B4DF54428060071000000000000",
            ]),
        Warp(debug_name="TTC To Lighthouse Lower", object_id=0x70, warps_to=0x206, warps_from=0x207, warp_search_strings=[
            "01C21E77F57639060070000000012E61",
            ]),
        ],
    "Clanker's Cavern": [
        Warp(debug_name="CC Left Gill To Outside", object_id=0x2F, warps_to=0x300, warps_from=0x301, keep_in_same_world=True, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "12D303E00000AF06002F000000000389",
            ]),
        Warp(debug_name="CC Right Gill To Outside", object_id=0x30, warps_to=0x300, warps_from=0x301, keep_in_same_world=True, can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "F2BB00650004CA860030000000000000",
            ]),
        Warp(debug_name="CC Left Tooth To Outside", object_id=0x31, warps_to=0x300, warps_from=0x302, keep_in_same_world=True, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "03A805DB1A9D3E860031000000000000",
            "035905FC1B023E86003100000001E994",
            "037805DB1ACE3E86003100000001E990",
            "032C05DB1B343E860031000000000000",
            "02FB05DB1B5E3E860031000000000064",
            ]),
        Warp(debug_name="CC Right Tooth To Outside", object_id=0x32, warps_to=0x300, warps_from=0x303, keep_in_same_world=True, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "FBBE05DA18964706003200000000217D",
            ]),
        Warp(debug_name="CC Gold Feather Room (Coming Outside)", object_id=0x9B, warps_to=0x304, warps_from=0x301, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "0008FE4609FA6406009B000000000000",
            ]),
        Warp(debug_name="CC Gold Feather Room (Going Inside)", object_id=0x9E, warps_to=0x301, warps_from=0x304, can_enter_warp_zone=(Warp.Banjo + Warp.Bee), can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "000D06E7EF427086009E000000000000",
            ]),
        Warp(debug_name="CC Blowhole To Mouth", object_id=0x9D, warps_to=0x301, warps_from=0x305, can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "0015FE8D0BA44586009D000000000000",
            ]),
        Warp(debug_name="CC Blowhole To Belly", object_id=0x9C, warps_to=0x301, warps_from=0x305, can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "0000FE7EF4244806009C000000000000",
            ]),
        ],
    "Bubblegloop Swamp": [
        Warp(debug_name="BGS Tanktup (Coming Outside)", object_id=0x68, warps_to=0x400, warps_from=0x401, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "FFF000000764960600680000000095A1",
            ]),
        Warp(debug_name="BGS Tanktup (Going Inside)", object_id=0x46, warps_to=0x401, warps_from=0x400, keep_in_same_setup=True, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "0F6800C004E41906004600000000A21F",
            "0F6500FF04E419060046000000000000",
            ]),
        Warp(debug_name="BGS Mumbo's Skull (Coming Outside)", object_id=0xA, warps_to=0x400, warps_from=0x402, can_enter_warp_zone=(Warp.Banjo + Warp.Termite + Warp.Walrus + Warp.Pumpkin + Warp.Bee), warp_search_strings=[
            "0000005103A94B06000A00000002E875",
            ]),
        Warp(debug_name="BGS Mumbo's Skull (Going Inside)", object_id=0x9, warps_to=0x402, warps_from=0x400, can_enter_warp_zone=(Warp.Banjo + Warp.Termite + Warp.Walrus + Warp.Pumpkin + Warp.Bee), 
                                                                                                             can_exit_from_room=Warp.Banjo,
             warp_search_strings=[
            "E62A0450EAD539860009000000000000",
            "E6660455EA963986000900000009EC1C",
            "E6890456EA78398600090000000522DF",
            "E64D0454EAB33986000900000009EC1C",
            ]),
        Warp(debug_name="BGS Croc Left Nostril (Going Outside)", object_id=0x67, warps_to=0x400, warps_from=0x403, can_enter_warp_zone=Warp.Crocodile, can_exit_from_room=Warp.Crocodile, warp_search_strings=[
            "FE0E00BEF7312D06006A000000000000",
            "FE3200BEF71C2D06006A000000000000",
            "FE5700BDF7062D06006A000000000000",
            "FE7900BDF6F52D06006A000000000000",
            "FE9A00BDF6E22D06006A000000000064",
            ]),
        Warp(debug_name="BGS Croc Left Nostril (Coming Inside)", object_id=0x6A, warps_to=0x403, warps_from=0x400, can_enter_warp_zone=Warp.Crocodile, can_exit_from_room=Warp.Crocodile, warp_search_strings=[
            "FC7F0082F1B125860067000000000000",
            "FC9C007AF1C82586006700000001C4DF",
            "FCB30079F1EA25860067000000000000",
            ]),
        Warp(debug_name="BGS Croc Right Nostril (Going Outside)", object_id=0x66, warps_to=0x400, warps_from=0x403, can_enter_warp_zone=Warp.Crocodile, can_exit_from_room=Warp.Crocodile, warp_search_strings=[
            "016B00BEF6ED2D060069000000000064",
            "01F400BEF73C2D060069000000000000",
            "01A900BEF7102D060069000000010755",
            "019500BEF6F632060069000000000000",
            "01D900BEF72032060069000000000000",
            ]),
        Warp(debug_name="BGS Croc Right Nostril (Coming Inside)", object_id=0x69, warps_to=0x403, warps_from=0x400, can_enter_warp_zone=Warp.Crocodile, can_exit_from_room=Warp.Crocodile, warp_search_strings=[
            "FBA70081F32032060066000000000000",
            "FBC50064F3323206006600000001AC8C",
            "FBE70064F34632060066000000000000",
            ]),
        ],
    "Freezeezy Peak": [
        Warp(debug_name="FP Mumbo's Skull (Going Outside)", object_id=0x43, warps_to=0x500, warps_from=0x501, can_enter_warp_zone=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Pumpkin + Warp.Bee), warp_search_strings=[
            "0000005103A94B060043000000000064",
            ]),
        Warp(debug_name="FP Mumbo's Skull (Coming Inside)", object_id=0x40, warps_to=0x501, warps_from=0x500, can_enter_warp_zone=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Pumpkin + Warp.Bee), 
                                                                                                              can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "1B7C02BAF30E32060040000000000000",
            "1B9C02BAF356320600400000000128B5",
            "1BC002BAF38F32060040000000000000",
            ]),
        Warp(debug_name="FP Boggy's Igloo (Going Outside)", object_id=0x44, warps_to=0x500, warps_from=0x502, warp_search_strings=[
            "0007008603D25006004400000011FFB7",
            ]),
        Warp(debug_name="FP Boggy's Igloo (Coming Inside)", object_id=0x41, warps_to=0x502, warps_from=0x500, warp_search_strings=[
            "01C20DF924EE2F86004100000000D45D",
            ]),
        Warp(debug_name="FP Christmas Tree (Going Outside)", object_id=0x45, warps_to=0x500, warps_from=0x503, warp_search_strings=[
            "0017FDA6FFE599860045000000000F84",
            ]),
        Warp(debug_name="FP Christmas Tree (Coming Inside)", object_id=0x42, warps_to=0x503, warps_from=0x500, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "EE1803A718684C060042000000000000",
            ]),
        Warp(debug_name="FP Wozza's Cave (Going Outside)", object_id=0xFC, warps_to=0x500, warps_from=0x504, can_exit_from_room=Warp.Walrus, warp_search_strings=[
            "031B0066F9F0640600FC000000000000",
            "03970066FA33640600FC00000000F9BA",
            "03590066FA0B640600FC000000000064",
            "03D80066FA58640600FC000000000000",
            ]),
        Warp(debug_name="FP Wozza's Cave (Coming Inside)", object_id=0xFD, warps_to=0x504, warps_from=0x500, can_enter_warp_zone=Warp.Walrus, warp_search_strings=[
            "E6CB0396F0F1898600FD000000000064",
            "E7080396F1A5898600FD000000000000",
            "E6E90396F156898600FD000000000000",
            "E72A0396F1EF898600FD000000000000",
            ]),
        ],
    "Gobi's Valley": [
        Warp(debug_name="GV Jinxy (Going Outside)", object_id=0x6, warps_to=0x600, warps_from=0x601, warp_search_strings=[
            "0B73004EFFCF50060006000000000000",
            ]),
        Warp(debug_name="GV Jinxy (Coming Inside)", object_id=0x5, warps_to=0x601, warps_from=0x600, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "F06D05D317103E860005000000000000",
            ]),
        Warp(debug_name="GV Rupee (Going Outside)", object_id=0x64, warps_to=0x600, warps_from=0x602, warp_search_strings=[
            "000F00A306417D860064000000000064",
            ]),
        Warp(debug_name="GV Rupee (Coming Inside)", object_id=0x60, warps_to=0x602, warps_from=0x600, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "F09E0B4C02A443860060000000000000",
            ]),
        Warp(debug_name="GV Matching Pyramid (Going Outside)", object_id=0x61, warps_to=0x600, warps_from=0x603, warp_search_strings=[
            "FA91015000236406006100002B000064",
            ]),
        Warp(debug_name="GV Matching Pyramid (Coming Inside)", object_id=0x5C, warps_to=0x603, warps_from=0x600, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "0F3F09DF01432A86005C000000000000",
            ]),
        Warp(debug_name="GV Water Pyramid (Going Outside)/Bottom", object_id=0x63, warps_to=0x600, warps_from=0x604, can_enter_warp_zone=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Pumpkin), warp_search_strings=[
            "0006011406D48D060063000000000000",
            ]),
        Warp(debug_name="GV Water Pyramid (Coming Inside)/Top", object_id=0x5E, warps_to=0x604, warps_from=0x600, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Pumpkin), warp_search_strings=[
            "000610A2EED56386005E000000000000",
            ]),
        Warp(debug_name="GV Water Pyramid (Coming Inside)/Bottom", object_id=0x5F, warps_to=0x604, warps_from=0x600, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Pumpkin), warp_search_strings=[
            "FF1C0BCBF20D6406005F000000029226",
            ]),
        Warp(debug_name="GV King Sandybutt (Going Outside)/Front", object_id=0x62, warps_to=0x600, warps_from=0x605, warp_search_strings=[
            "1825008C015E63860062000000000064",
            ]),
        Warp(debug_name="GV King Sandybutt (Going Outside)/Back", object_id=0xDE, warps_to=0x600, warps_from=0x605, warp_search_strings=[
            "EA94006B046C460600DE000000000064",
            "EACB006B0486460600DE000000000000",
            "EB0B006B04A4460600DE000000000000",
            ]),
        Warp(debug_name="GV King Sandybutt (Coming Inside)/Front", object_id=0x5D, warps_to=0x605, warps_from=0x600, keep_in_same_setup=True, warp_search_strings=[
            "00460A0A028D5186005D00000000FF49",
            ]),
        ],
    "Mad Monster Mansion": [
        Warp(debug_name="MMM Dining Room (Going Outside)", object_id=0x88, warps_to=0x700, warps_from=0x701, keep_in_same_world=True, warp_search_strings=[
            "0000009F0C1954860088000000000000",
            ]),
        Warp(debug_name="MMM Dining Room (Coming Inside)/Front", object_id=0x79, warps_to=0x701, warps_from=0x700, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "03E70148045C53860079000000000F6A",
            ]),
        Warp(debug_name="MMM Dining Room (Coming Inside)/Chimney", object_id=0x7A, warps_to=0x701, warps_from=0x700, can_enter_warp_zone=(Warp.Banjo + Warp.Bee), can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "03EA094F00F81D86007A000000000000",
            ]),
        Warp(debug_name="MMM First Floor 1 (Red Feather Room) (Going Outside)", object_id=0x91, warps_to=0x700, warps_from=0x702, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "000000AAFD754C860091000000000000",
            ]),
        Warp(debug_name="MMM First Floor 1 (Red Feather Room) (Coming Inside)", object_id=0x82, warps_to=0x702, warps_from=0x700, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "026F015E04A734060082000000000000",
            ]),
        Warp(debug_name="MMM First Floor 2 (Blue Egg Room) (Going Outside)", object_id=0x92, warps_to=0x700, warps_from=0x703, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "000B00C6FDBD4F860092000000000000",
            ]),
        # Can't Find Warp?
        Warp(debug_name="MMM First Floor 2 (Blue Egg Room) (Coming Inside)", object_id=0x83, warps_to=0x703, warps_from=0x700, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "056F0156FCC838860083000000000000",
            ]),
        Warp(debug_name="MMM Second Floor 1 (Empty Honeycomb Room) (Going Outside)", object_id=0x94, warps_to=0x700, warps_from=0x704, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "000800E7FD3475860094000000000000",
            ]),
        Warp(debug_name="MMM Second Floor 1 (Empty Honeycomb Room) (Coming Inside)", object_id=0x87, warps_to=0x704, warps_from=0x700, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "015C055400ED46060085000000000000",
            ]),
        Warp(debug_name="MMM Second Floor 2 (Bathroom) (Going Outside)", object_id=0x93, warps_to=0x700, warps_from=0x705, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "FFFB00F0FD2161060093000000000000",
            ]),
        Warp(debug_name="MMM Second Floor 2 (Bathroom) (Coming Inside)", object_id=0x87, warps_to=0x705, warps_from=0x700, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "0665053FFF224D060087000000000000",
            ]),
        Warp(debug_name="MMM Third Floor 1 (Bedroom) (Going Outside)", object_id=0x95, warps_to=0x700, warps_from=0x706, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "000200F2FD1D66860095000000000000",
            ]),
        Warp(debug_name="MMM Third Floor 1 (Bedroom) (Coming Inside)", object_id=0x86, warps_to=0x706, warps_from=0x700, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "03F906F2FD9A59060086000000000000",
            ]),
        Warp(debug_name="MMM Third Floor 2 (Note Room) (Going Outside)", object_id=0x96, warps_to=0x700, warps_from=0x707, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "000200BEFDC248860096000000000000",
            ]),
        Warp(debug_name="MMM Third Floor 2 (Note Room) (Coming Inside)", object_id=0x84, warps_to=0x707, warps_from=0x700, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "03D406EC04495D860084000000000000",
            ]),
        Warp(debug_name="MMM Well - Top/Outside", object_id=0x8A, warps_to=0x700, warps_from=0x708, warp_search_strings=[
            "000008E400003986008A000000000000",
            ]),
        Warp(debug_name="MMM Well - Top/Inside", object_id=0x7B, warps_to=0x708, warps_from=0x700, can_exit_from_room=(Warp.Banjo + Warp.Bee + Warp.Pumpkin), warp_search_strings=[
            "1645FF45F2EE3C06007B000000000000",
            ]),
        # Can't Find Warp?
        Warp(debug_name="MMM Tumblar's Shed (Going Outside)", object_id=0x8B, warps_to=0x700, warps_from=0x709, warp_search_strings=[
            "0000009105F75506008B00000000094E",
            ]),
        Warp(debug_name="MMM Tumblar's Shed (Coming Inside)", object_id=0x7C, warps_to=0x709, warps_from=0x700, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "06C601D8EE944486007C000000019DFB",
            ]),
        Warp(debug_name="MMM Church (Going Outside)", object_id=0x8C, warps_to=0x700, warps_from=0x70A, warp_search_strings=[
            "FF9000EE1A509606008C000000000000",
            "004E00EE1A4E9606008C000000000000",
            ]),
        # Because of the mechanics behind this warp, I'm removing it from randomizing
#         Warp(debug_name="MMM Church (Coming Inside)", object_id=0x7D, warps_to=0x70A, warps_from=0x700, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
#             "F6E5014DF6336B06007D000000001951",
#             ]),
        Warp(debug_name="MMM Church Secret Room (Going Outside)", object_id=0x8D, warps_to=0x700, warps_from=0x70B, warp_search_strings=[
            "FE240183FCC74306008D000000000000",
            "FEC70185FCC64306008D000000000000",
            "FFD0018FFCC44106008D000000000000",
            "FFCF0092FCC44506008D000000000000",
            "FEC50094FCC34506008D000000000000",
            "FE210099FCC54306008D000000000000",
            ]),
        Warp(debug_name="MMM Church Secret Room (Coming Inside)", object_id=0x7E, warps_to=0x70B, warps_from=0x700, warp_search_strings=[
            "F23701A1F58E5486007E000000000B8A",
            ]),
        Warp(debug_name="MMM Cellar (Going Outside)", object_id=0x90, warps_to=0x700, warps_from=0x70C, warp_search_strings=[
            "FD2F01ACFAB33E860090000000000378",
            ]),
        Warp(debug_name="MMM Cellar (Coming Inside)", object_id=0x81, warps_to=0x70C, warps_from=0x700, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "FD2EFF1F00EF53860081000000000000",
            ]),
        Warp(debug_name="MMM Church Tower Lower To Upper", object_id=0x97, warps_to=0x700, warps_from=0x70D, warp_search_strings=[
            "F51505EBFA1044060097000000000000",
            ]),
        Warp(debug_name="MMM Church Tower Upper To Lower", object_id=0x98, warps_to=0x70D, warps_from=0x700, warp_search_strings=[
            "F510084FF9872586009800000001DE34",
            ]),
        Warp(debug_name="MMM Mumbo's Skull (Going Outside)", object_id=0x99, warps_to=0x700, warps_from=0x70E, can_enter_warp_zone=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Walrus + Warp.Bee), warp_search_strings=[
            "00010051039D4B0600990000000EED9F",
            ]),
        Warp(debug_name="MMM Mumbo's Skull (Coming Inside)", object_id=0x9A, warps_to=0x70E, warps_from=0x700, can_enter_warp_zone=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Walrus + Warp.Bee), 
                                                                                                               can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "FE3800E5ED512586009A00000000B11E",
            "FE0900E9ED202586009A000000007230",
            "FE2200E4ED382586009A00000000B11C",
            "FE5600E8ED6E2586009A000000000000",
            ]),
        Warp(debug_name="MMM Gutter (Going Outside/Lower)", object_id=0x8F, warps_to=0x700, warps_from=0x70F, can_enter_warp_zone=Warp.Pumpkin, can_exit_from_room=Warp.Pumpkin, warp_search_strings=[
            "FFF9005802073306008F00000006D0F8",
            ]),
        Warp(debug_name="MMM Gutter (Coming Inside/Lower)", object_id=0x80, warps_to=0x70F, warps_from=0x700, can_enter_warp_zone=Warp.Pumpkin, can_exit_from_room=Warp.Pumpkin, warp_search_strings=[
            "09970021071A1906008000000006DC62",
            ]),
        Warp(debug_name="MMM Well (Going Outside/Lower)", object_id=0x11F, warps_to=0x700, warps_from=0x708, can_enter_warp_zone=Warp.Pumpkin, can_exit_from_room=Warp.Pumpkin, warp_search_strings=[
            "024E001F01E11106011F000000000064",
            ]),
        Warp(debug_name="MMM Well (Coming Inside/Lower)", object_id=0x11E, warps_to=0x708, warps_from=0x700, can_enter_warp_zone=Warp.Pumpkin, can_exit_from_room=Warp.Pumpkin, warp_search_strings=[
            "159AFE4DF3711906011E000000000000",
            "15BBFE4DF38F1906011E000000000000",
            ]),
        Warp(debug_name="MMM Loggo (Going Outside)", object_id=0x120, warps_to=0x704, warps_from=0x710, can_enter_warp_zone=Warp.Pumpkin, can_exit_from_room=Warp.Pumpkin, warp_search_strings=[
            "001C017505A447060120000000001A3F"
            ]),
        ],
    "Rusty Bucket Bay": [
        # Kept softlocking, but also don't have destination on BB?
#         Warp(debug_name="RBB Big Fish Warehouse (Going Outside)/Side", object_id=0xBA, warps_to=0x801, warps_from=0x800, warp_search_strings=[
#             "064FFD1102BCFA0600BA000000000000",
#             "0702FD860062C08600BA000000000000",
#             ]),
        Warp(debug_name="RBB Big Fish Warehouse (Coming Inside/Top)", object_id=0xA7, warps_to=0x801, warps_from=0x800, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "E890FBC60DC8748600A7000000000000",
            ]),
        Warp(debug_name="RBB Big Fish Warehouse (Coming Inside/Side)", object_id=0xB9, warps_to=0x801, warps_from=0x800, keep_in_same_world=True, warp_search_strings=[
            "E911F7B30DB8FA0600B9000000000000",
            "E911FA210DB8FA0600B9000000000000",
            ]),
        Warp(debug_name="RBB Boat Room (Going Outside)", object_id=0xB3, warps_to=0x800, warps_from=0x802, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "F7CEFD85003D750600B3000000001882",
            ]),
        # Can't Find Warp?
        Warp(debug_name="RBB Boat Room (Coming Inside)", object_id=0xA8, warps_to=0x802, warps_from=0x800, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "E05BF7ED043BBC8600A80000000020AA",
            ]),
        # Can't Find Warp?
        Warp(debug_name="RBB Left Blue Container (Going Outside)", object_id=0xB4, warps_to=0x800, warps_from=0x803, warp_search_strings=[
            "FE13011F0575BC8600B4000000000000",
            "FFEB00E50599998600B4000000000000",
            ]),
        Warp(debug_name="RBB Left Blue Container (Coming Inside)", object_id=0xA9, warps_to=0x803, warps_from=0x800, warp_search_strings=[
            "FBD2FDD5F2977F0600A9000000000000",
            ]),
        Warp(debug_name="RBB Middle Blue Container (Going Outside)", object_id=0xB5, warps_to=0x800, warps_from=0x804, warp_search_strings=[
            "000303C402C24D8600B5000000000000",
            ]),
        Warp(debug_name="RBB Middle Blue Container (Coming Inside)", object_id=0xAA, warps_to=0x804, warps_from=0x800, can_exit_from_room=(Warp.Banjo + Warp.Bee), warp_search_strings=[
            "FE73FDCCF2575B8600AA000000000000",
            ]),
        Warp(debug_name="RBB Right Blue Container (Going Outside)", object_id=0xB6, warps_to=0x800, warps_from=0x805, warp_search_strings=[
            "002D005003E0578600B6000000000000",
            "002D00E603E0578600B6000000000000",
            "0125009F0391680600B6000000000000",
            ]),
        Warp(debug_name="RBB Right Blue Container (Coming Inside)", object_id=0xAB, warps_to=0x805, warps_from=0x800, warp_search_strings=[
            "0102FDCBF28B7E8600AB000000000000",
            ]),
        Warp(debug_name="RBB Kitchen (Going Outside)", object_id=0xAF, warps_to=0x800, warps_from=0x806, warp_search_strings=[
            "FCC4026CFB97368600AF000000000000",
            ]),
        Warp(debug_name="RBB Kitchen (Coming Inside)", object_id=0xA3, warps_to=0x806, warps_from=0x800, warp_search_strings=[
            "EE08001EFC7D190600A3000000000064",
            ]),
        Warp(debug_name="RBB Navigation Room (Going Outside)", object_id=0xB0, warps_to=0x800, warps_from=0x807, warp_search_strings=[
            "03BC016C01142D0600B0000000000000",
            "03BC015702A92D0600B0000000000064",
            "03BC00C601142D0600B0000000000000",
            "03BC00C602A92D0600B0000000000000",
            "03A10008018E3E8600B0000000000000",
            "03A1000802363E8600B0000000000074",
            "04CB00E501E88F0600B0000000000064",
            ]),
        Warp(debug_name="RBB Navigation Room (Coming Inside)", object_id=0xA4, warps_to=0x807, warps_from=0x800, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "F1F100A603B7348600A4000000000000",
            "F1F4000003F2288600A4000000000000",
            ]),
        Warp(debug_name="RBB Captain's Room (Going Outside)", object_id=0xAC, warps_to=0x800, warps_from=0x808, warp_search_strings=[
            "FDE900DFFDE1278600AC000000000000",
            "FE070003FDF93C8600AC000000000000",
            ]),
        Warp(debug_name="RBB Captain's Room (Coming Inside)", object_id=0xA0, warps_to=0x808, warps_from=0x800, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "F38800A2FC4E330600A0000000000000",
            "F38FFFE2FC25340600A0000000000000",
            ]),
        Warp(debug_name="RBB Middle Pipe (Going Outside)", object_id=0xB1, warps_to=0x800, warps_from=0x809, warp_search_strings=[
            "01FE0326FC85780600B1000000014A2C",
            ]),
        Warp(debug_name="RBB Middle Pipe (Coming Inside)", object_id=0xA5, warps_to=0x809, warps_from=0x800, warp_search_strings=[
            "002BFE6F03501A0600A5000000000000",
            ]),
        Warp(debug_name="RBB Bedroom (Going Outside)", object_id=0xAD, warps_to=0x800, warps_from=0x80A, warp_search_strings=[
            "014C00DBFD573C0600AD000000000000",
            "FFFC00E3FC5E8F8600AD000000000000",
            "FEDA00DBFD563C0600AD000000000000",
            "008B0000FD41420600AD000000000000",
            "FFA20000FD43420600AD000000000000",
            ]),
        Warp(debug_name="RBB Bedroom (Coming Inside)", object_id=0xA1, warps_to=0x80A, warps_from=0x800, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "0199FF19FD2F3C8600A1000000000000",
            "0185FE21FCE32F8600A1000000000000",
            ]),
        Warp(debug_name="RBB Engine Room (Going Outside/Main)", object_id=0xB2, warps_to=0x800, warps_from=0x80B, warp_search_strings=[
            "FFF40A270FE33B8600B200000016CD8A",
            ]),
        Warp(debug_name="RBB Engine Room (Coming Inside/Main)", object_id=0xA6, warps_to=0x80B, warps_from=0x800, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=(Warp.Banjo + Warp.Bee), warp_search_strings=[
            "056A002B00BB1C8600A6000000000064",
            "054F003200DE1C8600A6000000000064",
            "0530003501061C0600A6000000000064",
            "05120032012D1C8600A6000000000000",
            ]),
        Warp(debug_name="RBB Engine Room (Coming Outside/Button)", object_id=0xAE, warps_to=0x800, warps_from=0x80C, warp_search_strings=[
            "F2AF01B0F0F2F40600AE000000000000",
            "EF9601E0F24EFA0600AE000000000000",
            "EFEA01B0F564FA0600AE000000000064",
            "EFB70425F013FA0600AE000000000064",
            "EDC504C1F382CF0600AE000000000064",
            "F03A0640F1CE4A0600AE000000000064",
            "EEDC06A2F2797E0600AE000000000064",
            "F07F0655F304560600AE000000000000",
            ]),
        Warp(debug_name="RBB Engine Room (Going Inside/Button)", object_id=0xA2, warps_to=0x80C, warps_from=0x800, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=(Warp.Banjo + Warp.Bee), warp_search_strings=[
            "1A5EFCFEFDDA190600A2000000000064",
            ]),
        Warp(debug_name="RBB Boombox Room (Going Outside)", object_id=0xB7, warps_to=0x800, warps_from=0x80D, warp_search_strings=[
            "FAD205B90000858600B7000000000000",
            ]),
        Warp(debug_name="RBB Boombox Room (Coming Inside)", object_id=0xB8, warps_to=0x80D, warps_from=0x800, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=(Warp.Banjo + Warp.Bee), warp_search_strings=[
            "1008FB500062D00600B8000000000000",
            "0FFEFB50FF83D00600B8000000000000",
            ]),
        Warp(debug_name="RBB Anchor Room (Going Outside)", object_id=0x11C, warps_to=0x800, warps_from=0x80E, warp_search_strings=[
            "FC00FF42FFD99406011C000000000000",
            ]),
        Warp(debug_name="RBB Anchor Room (Coming Inside)", object_id=0x11D, warps_to=0x80E, warps_from=0x800, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Pumpkin), warp_search_strings=[
            "ECEEFA4A00D05006011D000000000000",
            "EC9AFA58007F5006011D000000000000",
            "EC48FA5800345006011D000000000000",
            ]),
        ],
    "Click Clock Wood - Lobby": [
        # To randomize warps within just the lobby, you'd mess up the season buttons
        ],
    "Click Clock Wood - Spring": [
        Warp(debug_name="CCW Spring Mumbo's Skull (Going Outside)", object_id=0xDF, warps_to=0x900, warps_from=0x901, can_enter_warp_zone=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Pumpkin), 
                                                                                                                      can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "0000005103A94B0600DF000000063B96",
            ]),
        Warp(debug_name="CCW Spring Mumbo's Skull (Coming Inside)", object_id=0xE3, warps_to=0x901, warps_from=0x900, can_enter_warp_zone=(Warp.Banjo + Warp.Termite + Warp.Crocodile + Warp.Pumpkin), 
                                                                                                                      can_exit_from_room=Warp.Banjo, warp_search_strings=[
            "E53402D000004B0600E30000000E1592",
            ]),
        Warp(debug_name="CCW Spring Nabnut's Door (Going Outside)", object_id=0xEB, warps_to=0x900, warps_from=0x902, warp_search_strings=[
            "00000064036B5A0600EB0000000F5A7B",
            ]),
        Warp(debug_name="CCW Spring Nabnut's Door (Coming Inside)", object_id=0xE7, warps_to=0x902, warps_from=0x900, can_enter_warp_zone=(Warp.Banjo + Warp.Bee), warp_search_strings=[
            "FFFC11B10894640600E7000000000000",
            ]),
        Warp(debug_name="CCW Spring Nabnut's Window (Going Outside)", object_id=0x127, warps_to=0x900, warps_from=0x903, warp_search_strings=[
            "FEA300D503524B060127000000000000",
            ]),
        Warp(debug_name="CCW Spring Nabnut's Window (Coming Inside)", object_id=0x123, warps_to=0x903, warps_from=0x900, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "FEB111DF09AB32060123000000000000",
            ]),
        Warp(debug_name="CCW Spring Whipcrack Room (Going Outside)", object_id=0x58, warps_to=0x900, warps_from=0x904, warp_search_strings=[
            "00000070FB356B860058000000003DB3",
            ]),
        Warp(debug_name="CCW Spring Whipcrack Room (Coming Inside)", object_id=0x12, warps_to=0x904, warps_from=0x900, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "000016B1F81757860012000000000000",
            ]),
        Warp(debug_name="CCW Spring Zubba Hive (Going Outside)", object_id=0x110, warps_to=0x900, warps_from=0x905, can_enter_warp_zone=Warp.Bee, can_exit_from_room=Warp.Bee, warp_search_strings=[
            "00000258092D750601100000000017CF",
            ]),
        Warp(debug_name="CCW Spring Zubba Hive (Coming Inside)", object_id=0x10D, warps_to=0x905, warps_from=0x900, can_enter_warp_zone=Warp.Bee, can_exit_from_room=Warp.Bee, warp_search_strings=[
            "00000CE2EBE22706010D00000003E441",
            ]),
        ],
    "Click Clock Wood - Summer": [
        Warp(debug_name="CCW Summer Mumbo's Skull (Going Outside)", object_id=0xE0, warps_to=0x1000, warps_from=0x1001, warp_search_strings=[
            "0000005103A94B0600E0000000004FEE",
            ]),
        Warp(debug_name="CCW Summer Mumbo's Skull (Coming Inside)", object_id=0xE4, warps_to=0x1001, warps_from=0x1000, keep_in_same_world=True, warp_search_strings=[
            "E57F02D000004B0600E4000000040EC9",
            ]),
        Warp(debug_name="CCW Summer Zubba Hive (Going Outside)", object_id=0x111, warps_to=0x1000, warps_from=0x1002, warp_search_strings=[
            "FF2A05D6FBE84F860111000000000000",
            ]),
        Warp(debug_name="CCW Summer Zubba Hive (Coming Inside)", object_id=0x10E, warps_to=0x1002, warps_from=0x1000, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=(Warp.Banjo + Warp.Bee), warp_search_strings=[
            "00000E2AEED53386010E000000000000",
            ]),
        Warp(debug_name="CCW Summer Nabnut's Door (Going Outside)", object_id=0xEC, warps_to=0x1000, warps_from=0x1003, warp_search_strings=[
            "00000064036B5A0600EC00000000918F",
            ]),
        Warp(debug_name="CCW Summer Nabnut's Door (Coming Inside)", object_id=0xE8, warps_to=0x1003, warps_from=0x1000, can_enter_warp_zone=(Warp.Banjo + Warp.Bee), warp_search_strings=[
            "FFDA11B10886640600E8000000000000",
            ]),
        Warp(debug_name="CCW Summer Nabnut's Window (Going Outside)", object_id=0x128, warps_to=0x1000, warps_from=0x1004, warp_search_strings=[
            "FEA200D503524B060128000000000000",
            ]),
        Warp(debug_name="CCW Summer Nabnut's Window (Coming Inside)", object_id=0x124, warps_to=0x1004, warps_from=0x1000, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "FEB111DF09AB32060124000000000000",
            ]),
        Warp(debug_name="CCW Summer Whipcrack Room (Going Outside)", object_id=0x59, warps_to=0x1000, warps_from=0x1005, warp_search_strings=[
            "00000070FB356B860059000000000000",
            ]),
        Warp(debug_name="CCW Summer Whipcrack Room (Coming Inside)", object_id=0x13, warps_to=0x1005, warps_from=0x1000, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "000016B1F81757860013000000000064",
            ]),
        ],
    "Click Clock Wood - Fall": [
        Warp(debug_name="CCW Fall Mumbo's Skull (Going Outside)", object_id=0xE1, warps_to=0x1100, warps_from=0x1101, warp_search_strings=[
            "0000005103A94B0600E1000000000064",
            ]),
        Warp(debug_name="CCW Fall Mumbo's Skull (Coming Inside)", object_id=0xE5, warps_to=0x1101, warps_from=0x1100, warp_search_strings=[
            "E54802D000004B0600E500000004276B",
            ]),
        Warp(debug_name="CCW Fall Zubba Hive (Going Outside)", object_id=0x112, warps_to=0x1100, warps_from=0x1102, warp_search_strings=[
            "FF2A05D6FBE84F860112000000000000",
            ]),
        Warp(debug_name="CCW Fall Zubba Hive (Coming Inside)", object_id=0x10F, warps_to=0x1102, warps_from=0x1100, can_enter_warp_zone=Warp.Banjo, can_exit_from_room=(Warp.Banjo + Warp.Bee), warp_search_strings=[
            "00000E2AEEC93386010F000000000000",
            ]),
        Warp(debug_name="CCW Fall Nabnut's Door (Going Outside)", object_id=0xED, warps_to=0x1100, warps_from=0x1103, warp_search_strings=[
            "00000064036B5A0600ED000000000000",
            ]),
        Warp(debug_name="CCW Fall Nabnut's Door (Coming Inside)", object_id=0xE9, warps_to=0x1103, warps_from=0x1100, can_enter_warp_zone=(Warp.Banjo + Warp.Bee), warp_search_strings=[
            "000011B10894640600E9000000000000",
            ]),
        Warp(debug_name="CCW Fall Nabnut's Window (Going Outside)", object_id=0x129, warps_to=0x1100, warps_from=0x1104, warp_search_strings=[
            "FEA200D503524B060129000000000000",
            ]),
        Warp(debug_name="CCW Fall Nabnut's Window (Coming Inside)", object_id=0x125, warps_to=0x1104, warps_from=0x1100, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "FEB211DF09AC32060125000000000000",
            ]),
        Warp(debug_name="CCW Fall Nabnut's Attic 1 (Going Outside)", object_id=0x2D, warps_to=0x1100, warps_from=0x1105, warp_search_strings=[
            "000000C0FB693A86002D000000000000",
            ]),
        Warp(debug_name="CCW Fall Nabnut's Attic 1 (Coming Inside)", object_id=0x2A, warps_to=0x1105, warps_from=0x1100, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "04E113E3084B3206002A000000000000",
            "051E13E3082A3206002A000000000000",
            ]),
        Warp(debug_name="CCW Fall Whipcrack Room (Going Outside)", object_id=0x5A, warps_to=0x1100, warps_from=0x1106, warp_search_strings=[
            "00000070FB356B86005A00000000C75E",
            ]),
        Warp(debug_name="CCW Fall Whipcrack Room (Coming Inside)", object_id=0x14, warps_to=0x1106, warps_from=0x1100, keep_in_same_world=True, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "000016B1F81757860014000000000000",
            ]),
        ],
    "Click Clock Wood - Winter": [
        Warp(debug_name="CCW Winter Mumbo's Skull (Going Outside)", object_id=0xE2, warps_to=0x1200, warps_from=0x1201, warp_search_strings=[
            "0000005103A94B0600E2000000000064",
            ]),
        Warp(debug_name="CCW Winter Mumbo's Skull (Coming Inside)", object_id=0xE6, warps_to=0x1201, warps_from=0x1200, warp_search_strings=[
            "E53402D000004B0600E6000000095742",
            ]),
        Warp(debug_name="CCW Winter Nabnut's Window (Going Outside)", object_id=0x12A, warps_to=0x1200, warps_from=0x1202, warp_search_strings=[
            "FEA200D503534B06012A000000000000",
            ]),
        Warp(debug_name="CCW Winter Nabnut's Window (Coming Inside)", object_id=0x126, warps_to=0x1202, warps_from=0x1200, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "FEB111DB09AB31860126000000000000",
            ]),
        Warp(debug_name="CCW Winter Nabnut's Attic 1 (Going Outside)", object_id=0x2C, warps_to=0x1200, warps_from=0x1203, warp_search_strings=[
            "000001F0FAB55786002C000000000000",
            ]),
        Warp(debug_name="CCW Winter Nabnut's Attic 1 (Coming Inside)", object_id=0x2B, warps_to=0x1203, warps_from=0x1200, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "04E713E308523206002B000000000000",
            "051B13E308343206002B000000000000",
            ]),
        Warp(debug_name="CCW Winter Nabnut's Attic 2 (Going Outside)", object_id=0x2E, warps_to=0x1200, warps_from=0x1204, warp_search_strings=[
            "000000C0FB693A86002E000000000000",
            ]),
        Warp(debug_name="CCW Winter Nabnut's Attic 2 (Coming Inside)", object_id=0x29, warps_to=0x1204, warps_from=0x1200, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "FF2E13DB0AAA2C060029000000143FF2",
            ]),
        Warp(debug_name="CCW Winter Whipcrack Room (Going Outside)", object_id=0x5B, warps_to=0x1200, warps_from=0x1205, warp_search_strings=[
            "00000070FB356B86005B000000000000",
            ]),
        Warp(debug_name="CCW Winter Whipcrack Room (Coming Inside)", object_id=0x15, warps_to=0x1205, warps_from=0x1200, can_enter_warp_zone=Warp.Banjo, warp_search_strings=[
            "FFFF16B1F8174B060015000000000000",
            ]),
        ],
    "Click Clock Wood": [
        # Collect all the season warps and add the lobby warps (done in loop below)
        ],
    "Spiral Mountain": [
        Warp(debug_name="SM Banjo's House (Going Inside)", object_id=0x118, warps_to=0x1300, warps_from=0x1301, warp_search_strings=[
            "0F56FE571A694E860118000000002A7D",
            ]),
        Warp(debug_name="SM Banjo's House (Coming Outside)", object_id=0x118, warps_to=0x1301, warps_from=0x1300, warp_search_strings=[
            "FFF9004A01C440060119000000000D60",
            ]),
        Warp(debug_name="SM Grunty's Lair (Going Inside)", object_id=0x12D, warps_to=0x1302, warps_from=0x1300, keep_in_same_setup=True, warp_search_strings=[
            "00000798F13C7506012D0000001C1214",
            ]),
        ],
    }

for season in ["Spring", "Summer", "Fall", "Winter"]:
    for warp in Levels[f"Click Clock Wood - {season}"]:
        Levels["Click Clock Wood"].append(warp)

class Within_World_Warps_Class():
    def __init__(self, seed_val, level_warp_dict):
        self._seed_val = seed_val
        self._increment = 0
        self._level_warp_dict = level_warp_dict
        self._randomized_warp_cheat_sheet_dict = {}
    
    def _choose_from_list(self, original_list):
        '''Selects an option from a list based on the current address and the number of increments, if applicable'''
        seed(a=(self._seed_val + self._increment))
        self._increment += 1
        random_choice = choice(original_list)
        return random_choice

    def _shuffle_warps_within_list(self, warps, shuffle_type):
        self._randomized_warp_dict = {}
        warps_to_main = []
        warps_from_main = []
        for warp in warps:
            self._randomized_warp_dict[warp] = warp.old_warp_search_strings
            if(warp.warps_to % 0x10) == 0:
#                 print(f"To Main: {warp.name}")
                warps_to_main.append(warp)
            else:
#                 print(f"From Main: {warp.name}")
                warps_from_main.append(warp)
        while(warps_to_main):
            randomized_warp = self._choose_from_list(warps_to_main)
            selectable_temp_warps = []
            randomized_warp.keep_in_same_setup
            for warp in warps_to_main:
                if(((randomized_warp.can_enter_warp_zone & warp.can_exit_from_room) > 0) and 
                   (((randomized_warp.can_enter_warp_zone >= 32) and (warp.can_enter_warp_zone >= 32)) or (randomized_warp.can_enter_warp_zone == warp.can_enter_warp_zone)) and
                   (warp.warps_from != randomized_warp.warps_to) and (warp.warps_to != randomized_warp.warps_from)):
                    if(randomized_warp.keep_in_same_setup or warp.keep_in_same_setup):
                        if(randomized_warp.warps_from == warp.warps_from):
                            selectable_temp_warps.append(warp)
                    elif((shuffle_type == "Global") and (randomized_warp.keep_in_same_world or warp.keep_in_same_world)):
                        if((randomized_warp.warps_from // 0x100) == (warp.warps_from // 0x100)):
                            selectable_temp_warps.append(warp)
                    else:
                        selectable_temp_warps.append(warp)
            if(selectable_temp_warps):
                temp_warp = self._choose_from_list(selectable_temp_warps)
                randomized_warp.SwapWarps(temp_warp)
                selectable_from_warps = []
                for warp in reversed(warps_from_main):
                    if(((randomized_warp.can_enter_warp_zone & warp.can_enter_warp_zone) > 0) and 
                       ((randomized_warp.can_exit_from_room & warp.can_exit_from_room) > 0)):# and (randomized_warp.warps_from == warp.warps_to)):
                        selectable_from_warps.append(warp)
                if(selectable_from_warps):
                    warp = self._choose_from_list(selectable_from_warps)
                    warps_from_main.remove(warp)
                    warps_to_main.append(warp)
            warps_to_main.remove(randomized_warp)
            print(f"{randomized_warp.name}   -->   {randomized_warp.warps_name}")
            self._randomized_warp_dict[randomized_warp] = randomized_warp.old_warp_search_strings
            self._randomized_warp_cheat_sheet_dict[randomized_warp.name] = randomized_warp.warps_name

    def _randomize_by_world(self, level_name):
        self._shuffle_warps_within_list(self._level_warp_dict[level_name], shuffle_type="Within World")
    
    def _randomize_by_game(self, level_list):
        level_warp_list = []
        for level_name in level_list:
            for warp in self._level_warp_dict[level_name]:
                level_warp_list.append(warp)
        self._shuffle_warps_within_list(level_warp_list, shuffle_type="Global")

############
### MAIN ###
############

if __name__ == '__main__':
    from random import randint
    seed_val = randint(0, 999)
    print(f"Seed Val: {seed_val}")
    within_world_warps_obj = Within_World_Warps_Class(seed_val, Levels)
#     within_world_warps_obj = Within_World_Warps_Class(18368129, Levels)
#     shuffle_by = "World"
    shuffle_by = "Game"
    if(shuffle_by == "World"):
        print("\nMumbo's Mountain")
        within_world_warps_obj._randomize_by_world("Mumbo's Mountain")
        print("\nTreasure Trove Cove")
        within_world_warps_obj._randomize_by_world("Treasure Trove Cove")
        print("\nClanker's Cavern")
        within_world_warps_obj._randomize_by_world("Clanker's Cavern")
        print("\nBubblegloop Swamp")
        within_world_warps_obj._randomize_by_world("Bubblegloop Swamp")
        print("\nFreezeezy Peak")
        within_world_warps_obj._randomize_by_world("Freezeezy Peak")
        print("\nGobi's Valley")
        within_world_warps_obj._randomize_by_world("Gobi's Valley")
        print("\nMad Monster Mansion")
        within_world_warps_obj._randomize_by_world("Mad Monster Mansion")
        print("\nRusty Bucket Bay")
        within_world_warps_obj._randomize_by_world("Rusty Bucket Bay")
        print("\nClick Clock Wood - Spring")
        within_world_warps_obj._randomize_by_world("Click Clock Wood - Spring")
        print("\nClick Clock Wood - Summer")
        within_world_warps_obj._randomize_by_world("Click Clock Wood - Summer")
        print("\nClick Clock Wood - Fall")
        within_world_warps_obj._randomize_by_world("Click Clock Wood - Fall")
        print("\nClick Clock Wood - Winter")
        within_world_warps_obj._randomize_by_world("Click Clock Wood - Winter")
        print("\nClick Clock Wood")
        within_world_warps_obj._randomize_by_world("Click Clock Wood")
#         for warp_obj in within_world_warps_obj._randomized_warp_dict:
#             print(f"{warp_obj.old_object_id} -> {warp_obj.new_object_id}")
    else:
        within_world_warps_obj._randomize_by_game(["Mumbo's Mountain", "Treasure Trove Cove", "Clanker's Cavern",
                                                   "Bubblegloop Swamp", "Freezeezy Peak", "Gobi's Valley",
                                                   "Mad Monster Mansion", "Rusty Bucket Bay", "Click Clock Wood"])