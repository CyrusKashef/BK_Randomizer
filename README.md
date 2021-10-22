# Intro

## What Is A Randomizer?
A randomizer takes a game and randomly generates all sorts of aspects, such as what enemy spawns, the location of an item, and what order certain tasks must be accomplished. To learn what the Banjo-Kazooie Randomizer does, look at Feature Overview and Feature Details.

## Who Made The Banjo-Kazooie Randomizer And Why?
I, GiantJigglypuff3, coded the entirety of the Banjo-Kazooie Randomizer. However, I had a lot of help in terms of information and how ROM hacking works from the Banjo-Kazooie modding community (known as Banjo's Backpack). Banjo-Kazooie is my favorite game, and when I saw both Ocarina of Time and Super Mario 64 had randomizers, I felt the need to attempt to create one for Banjo-Kazooie. It may not be as good as the other randomizers, but I'm proud of how far it has gone.

# How To Use

## Requirements
1) Emulator or Everdrive+Console
2) A v1.0 NTSC ROM File of Banjo-Kazooie
Note: I am not providing anyone the ROM file, nor does the script create the ROM file for them. It takes the users software and creates a copy, then modifies that copy. It is up to the user to obtain a copy of the software legally and to not distrubute copies of the software illegally.

## Setting Up
1. Go to https://github.com/CyrusKashef/BK_Randomizer/releases.
2. Locate the latest version of the Banjo-Kazooie Randomizer at the top of the screen (as of this README, the latest version is 1.0.1).
3. Download the zip file called "BK_Randomizer". If your computer is giving you issues about the zip file being a virus, go to the "Common Problems" section of this README for a work around.
4. Extract the contents of the zip file to a directory without spaces or special characters. Underscores and dashes are allowed.
> Bad Example: C:/User/Path/To/Folder/This Has Spaces/BK_Randomizer/
> Bad Example: C:/User/Path/To/Folder/This@Has<>Weird()Characters/BK_Randomizer/
> Good Example: C:/User/Path/To/Folder/This-Is_Okay/BK_Randomizer/
5. Place your software copy of the Banjo-Kazooie v1.0 ROM file into the extracted folder.

## Running

# Feature Overview
* Shuffle/Randomize Items: Challenges the player to search the whole map for collectables.
* Special Modes: Uses extremes of a parameter to create a harder experience.
* World Specific Features: Changes unique things about each world.
* Aesthetic Features: Changes how he game looks and sounds.
* Miscellaneous Features: None of these affect gameplay, but may be useful.

# Feature Details
* ROM DIR: Displays the directory path of the ROM file the user has selected.
* SELECT ROM: Opens a file browser to select the BK ROM file.
* SEED: Allows the player to pick a seed to match other people's randomized ROM.

* LOAD CONFIG: Reads a JSON file to configure the settings automatically.
* SAVE CONFIG: Writes a JSON file for future use. See LOAD CONFIG.
* READ_ME: Opens the README.txt file.
* SUBMIT: Runs the randomizer with the current features, barring everything is set correctly.

Item Options:
* NONE: Skips the setting.
* SHUFFLE: Takes all items of that set and swaps the Object IDs within the world (with the exception of Click Clock Wood).
* RANDOMIZE: For every item in the world, randomly assign a new Object ID.
* ALL TOUGHIES: All ground enemies become Bigbutts. All flying enemies become Bees. All wall enemies become Flotsams (or vents if included).
* ALL NOTES: All eggs and feathers become notes. Brentildas are replaced with egg and feather refills. The refill at that Brentilda location is random.

World Order Warp Options:
* NONE: Skips the setting.
* SIMPLE SHUFFLE: Simplified shuffling to guarantee a solution. Mumbo's Mountain is always the first level, with the moves Talon Trot, Shock Jump Pad, and Beak Buster. All other world and moves are random.
* TRUE SHUFFLE: More complicated shuffle. Worlds are placed in a logical order so that the previous worlds will give the needed moves to progress the game. Logic might not work if worlds are skipped.
* MOVE BOTTLES LOCATIONS: Bottles mounds are shuffled with 1-Up locations to promote more exploration.

Within World Warp Options:
* NONE: Skips the setting
* SIMPLE SHUFFLE: All warps going into a room are shuffled with each other. All warps going out of a room are shuffled with each other. Some warps are excluded to prevent softlock. Transformation warps are excluded.
* TRUE SHUFFLE: All warps going into a room are linked with warps until there's an eventual exit. Includes transformation warps if possible.

* CREATE CHEAT SHEET: Writes a JSON file that gives a hint for the location of each Jiggy, the location of empty honeycombs, and how many notes are in each room.
* REMOVE EXTRA FILES: Removes the compressed and decompressed files extrated from the ROM. Useful for BK modders or debugging an issue.

Gruntilda's Lair:
* FINAL NOTE DOOR: The 810 note door's note requirement can be altered to any value within the lower and upper bounds, inclusively. The lower bound's minimum is 0; the upper bound's maximum is 900 unless the feature 'ALL NOTES' is selected, which will extend the maximum to 2000. All other note doors are removed.
* FINAL PUZZLE: The door leading to the final boss fight's Jiggy requirement can be altered to any value within the lower and upper bounds, inclusively. The lower bound's minimum is 0; the upper bound's maximum is 99. The number of Jiggies required for red honeycombs is 100 - Jiggies Needed, minimum being 1, maximum being 4. All world puzzles are complete by default, meaning worlds are automatically opened.
* SKIP FURNACE FUN: Places a warp on the first square of Furnace Fun that leads to the next area.
* REMOVE MAGIC BARRIERS: Removes all transformation barriers in the lair.

Mumbo's Mountain
* INCLUDE FLOWERS: If the notes/eggs/feathers feature is not set to 'none', the flowers in the level will be included.

Treasure Trove Cove
* SCATTERED NOTES: Notes are scattered across the level, both in the water and in the air.

Clanker's Cavern
* HARDER SWIMMING: Gloop is removed. Chumps are added to the water.
* HARD RINGS: Clanker's ring order is shuffled.

Bubblegloop Swamp
* CROCTUS: Croctus spawn order is shuffled.
* MR. VILE: Not sure as of typing this. Maybe move yumblies/grumblies around. Maybe remove running shoes. Maybe make Mr. Vile larger.
* TIPTUP CHOIR: Not sure as of typing this. Maybe move/rotate choir students.

Freezeezy Peak
* HARD RACES: Flag poles for the Boggy race are either tighter left, tighter right, lowered to the floor to make harder to see, or rotated.

Gobi's Valley
* ANCIENT ONES: Ancient Ones order is shuffled.
* MAZE JINXY HEADS: Jinxy heads to raise King Sandybutt's Tomb order is shuffled.
* MATCHING PUZZLE: Shuffles the tiles around.

Mad Monster Mansion
* TRICKY ENEMIES: Painting objects turn into Portrait Chompas. RIP Tombstones turn into Rippers. Maybe more?
* TRICKY OBJECTS: Jiggies without flags are placed around the map. The fire sprites in Mumbo's skull are shuffled, but the fire hurtboxes aren't moved.

Rusty Bucket Bay
* RANDOM BUTTON COMBO: Generates a random 6-digit combination of 1s, 2s, and 3s for the whistle buttons and places the code over the original code spot.

Click Clock Wood
* BY SEASON: All shuffling happens within each seasons/lobby area. This makes it easier for players to track what they are missing.
* WITHIN WORLD: All shuffling happens throughout the level.
* SHUFFLE SEASON ORDER: Shuffles the locations of 'Season Open' buttons and Witch Switch.

# Common Problems

## Computer Says Randomizer Is A Virus
If you go to virustotal.com and upload the BK Randomizer, it will tell you that about 10% (this value changes) of Anti-Virus softwares will claim this is a virus. This is a common issue when using pyinstaller to turn the python code into an exectuable file. I will have my code in a GitHub repository if anyone would like to check to see that the BK Randomizer is not doing anything malicious. If you trust me that the randomizer is not a virus, there is a work around to the Windows Defender Anti-Virus, demonstrated in the following YouTube video: https://www.youtube.com/watch?v=_5gbWPEcHZs

## GUI Errors/Warnings
* ROM directory cannot include spaces. This is because GZIP.EXE uses the command prompt and treats spaces as new inputs. Avoid using special characters as well.
* ROM file must be a Banjo-Kazooie ROM v1.0 NTSC (.z64). Other formats are currently not supported. Randomizer may work on top of other BK mods, but not guaranteed.
* Seed, upper bounds, and lower bounds must be positive integers.
* Python Files, Folders, GZIP.EXE, and CRC Tool must be in their original locations with the BK ROM in the main folder.

## Potential Softlocks
* When turning on the 'Potential Softlock' features, the game may be put into a state where a collectable cannot be reached or the game cannot be progressed without resetting.
* If performing RBA (Reverse Bee Adventure, where you avoid the detransformation areas to roam the rest of the game as the bee), the bee can get stuck in a lot of places.

## Known Bugs/Crashes
* In Clanker's Cavern, if the move in the gold feather room gets randomized, there's a possible chance the game will crash due to the lack of cameras in that room. The work around is to start the dialog, end the dialog using L+R+B, then reactivating the dialog.
* In specific areas, such as Treasure Trove Cove and Furnace Fun, the game may crash. The reason is unknown, and there are currently no work arounds.
* In Mad Monster Mansion, Napper may be indefinetly awake and guarding a Jiggy. The reason is unknown.
* In Click Clock Wood, there is an occasional glitch where the player can collect 11/10 Jiggies. The reason is unknown.

# FAQ

## Where Could I Find A Banjo-Kazooie v1.0 NTSC ROM File?
I am not providing anyone the ROM file for Banjo-Kazooie, nor does the script create the ROM file for them. It takes the users software and creates a copy, then modifies that copy. It is up to the user to obtain a copy of the software legally and to not distrubute copies of the software illegally.

## Could ___ Feature Be Added?
Not-Planned Features:
* Non-Collectable Objects, such as trees, crates, etc
* Bosses, such as Conga, Nipper, etc
Features I Attempted But Couldn't Get Working:
* Starting the game with all of the moves
* Free Mumbo transformations
If you have any suggestions for new features, feel free to let me know. I honestly didn't think people would care about shuffling music, but that turned out to be a really funny feature. Even if your feedback is "This part of the game is too easy", I could try to figure out some way to make it harder.

# Special Thanks
* The RARE staff, for making such an impactful game. Big shoutouts to Grant Kirkhope for an amazing soundtrack and being an amazing person in general.
* The Developers Of Banjo-Kazooie Modding/Viewing Tools, such as Banjo's Backpack, GEDecompressor, CRC Tool, and BK2BT. Also thank you to anyone who posted information on Hack64. I cannot name everyone by name, but your work is very appreciated and on behalf of the Banjo-Kazooie modding community, we cannot thank you enough. Discord link is listed in Contributing.
* Banjo's Backpack Discord, for everything ranging from technical support to emotional support. Big shoutouts to Jombo for most of the technical support. Other shoutouts go to BanjoFreak64, ThatCowGuy, PaleKing, Atezian, TheSourOG, Wedarobi, Retro, and SapChap99.
* People Who Played The Randomizer, whether it was playtesting, casually experiencing, or racing others. All feedback was taken seriously. All features that could reasonable be added were attempted at the very least. All issues brought up were either fixed or a work around was needed. Big shoutout to g0go for beta testing and feedback.
* OoT And SM64 Randomizers, for inspiring me to find the Banjo's Backpack discord and 

# Contributing
* If you'd like to take the source code to use for your own purposes, feel free. If you plan on making your own randomizer from the one I've made, consider the next bullet point or at least giving me credit somewhere.
* I coded entire project on my own, but that doesn't mean I wouldn't mind a team to work with. I currently wrote this code in Python. If you'd like to continue working on the Python version or need help creating a randomizer in a different coding language or something, I'll try to provide comments and answer questions as to what I personally did to randomize the rom. Keep in mind that I'm learning how to randomize this rom as I go, and might not have all of the answers to your questions.
* There's a community dedicated to Banjo-Kazooie modding called "Banjo's Backpack". There's a lot of smart people there, though most of us are still trying to learn as we go. Here is an invite: https://discord.gg/KSkN3yf4dt

# Contacting Me
I'm really bad at looking at social media messages, but here are different ways to try to reach me:
Twitter: https://twitter.com/GiantJigglypuff
YouTube: https://www.youtube.com/channel/UCipn0cYaHIAOtnEAc6NOw8g
Twitch: https://www.twitch.tv/giantjigglypuff3
My Discord Server: https://discord.gg/SrFxshj4fF