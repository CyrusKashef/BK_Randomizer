# Intro

## What Is A Randomizer?
A randomizer takes a game and randomly generates all sorts of aspects, such as what enemy spawns, the location of an item, and what order certain tasks must be accomplished. To learn what the Banjo-Kazooie Randomizer does, look at Feature Overview and Feature Details.

## Who Made The Banjo-Kazooie Randomizer?
In terms of coding the randomizer, almost all of it was coded by myself, GiantJigglypuff3. I will mention others who have contributed in the Special Thanks section. As far as hacking, I did almost nothing. I had a lot of help in terms of information and how ROM hacking works from the Banjo-Kazooie modding community (known as Banjo's Backpack). I hope the Banjo-Kazooie Randomizer serves as a small demonstration of what the Banjo-Kazooie modding community is capable of. Please go visit their discord server and try out some of their hacks (Here's an invite to the server: https://discord.gg/KSkN3yf4dt).

## Why Make The Banjo-Kazooie Randomizer?
Banjo-Kazooie is my favorite game, and I'm sure others love the game as well. When I saw both Ocarina of Time and Super Mario 64 had randomizers, I felt the need to attempt to create one for Banjo-Kazooie. It may not be as good as the other randomizers, but I'm proud of how far it has gone.

# How To Use

## Requirements
1) Emulator or Everdrive+Console
2) A v1.0 NTSC ROM File of Banjo-Kazooie
Note: I am not providing anyone the ROM file, nor does the script create the ROM file for them. It takes the user's software and creates a copy, then modifies that copy. It is up to the user to obtain a copy of the software legally.

## Setting Up
1. Go to https://github.com/CyrusKashef/BK_Randomizer/releases.
2. Locate the latest version of the Banjo-Kazooie Randomizer at the top of the screen (as of this README, the latest version is 2.0.Open_Beta).
3. Download the zip file called "BK_Randomizer". If your computer is giving you issues about the zip file being a virus, go to the "Common Problems" section of this README for a work around.
4. Extract the contents of the zip file to a folder.
5. Place your software copy of the Banjo-Kazooie v1.0 ROM file into the extracted folder.

## Running

# Feature Overview
* Shuffle/Randomize Collectables: Challenges the player to search the levels for collectable locations.
* Shuffle Warps: Challenges the player to remember what leads where and what moves are needed for specific locations.
* Shuffle/Randomize Enemies: Allows players to face against selected enemies.
* Aesthetic Features: Changes how he game looks and sounds.
* Customizable Features: Neither competitive nor merely asthetic features with modifiable JSON files for modders to explore with.
* World Specific Features: Changes unique things about each world.
* Miscellaneous Features: None of these affect gameplay, but may prove useful.

# Feature Details
## Overall Buttons
* Load Config: Reads a JSON file to configure the settings automatically.
* Save Config: Writes a JSON file for future use. See LOAD CONFIG.
* Open README: Opens the README.txt file (If you're reading this, bless your heart).
* Submit: Runs the randomizer with the current features, barring everything is set correctly. If not, a window should appear telling you what is incorrect/missing.

## General
* ROM File: Displays the directory path of the ROM file the user has selected.
* Select ROM Button (Folder): Click on the folder button to open a file browser and select the BK ROM file.
* Seed: Allows the player to pick a seed to match other people's randomized ROM.
* Random Seed Button (Acorn): Randomly generates a seed value.

## Collectables
### All Items
* None: Skips the setting.
* Shuffle (World): Takes all items of that set and swaps the Object IDs within the world (can be overriden for Click Clock Wood; see World Specific Features).
* Shuffle (Game): Takes all items of that set and swaps the Object IDs within all worlds/lair. This will override the World Specific Feature for Click Clock Wood.
* Randomize: For every item in the world, randomly assign a new Object ID.
### Jiggy, Empty Honeycomb, & Mumbo Token Specific
* Include Abnormalities: Some items have special properties that won't softlock the game, but create weird effects in game.
* Include Potential Softlocks: Some items create scenarios that prevent the player from 100%-ing or sometimes finishing the game.
* Door Of Grunty Only: All worlds will automatically open, and the value for the Door Of Grunty can be set on the side (from 0 to 99).
* Free Transformations: All Mumbo transformations won't cost you a single Mumbo Token.
### Notes, Blue Eggs, Red Feathers, & Gold Feathers
* Scaling Note Doors:
* All Notes: All eggs and feathers become notes. Brentildas are replaced with egg and feather refills. The refill at that Brentilda location is random.
* Scaling Note Doors: Depending on how many notes you set the 810 Note Door Value to, the number of notes needed per proceeding door will be increased/decreased accordingly.
* Final Note Door Only: Removes all note doors proceeding the 810 Note Door, and sets the value of the 810 Note Door to the desired value.
* Item Carrying Capacity: Sets the number of each item the player can carry before and after visiting Cheato between 0 and 255, inclusively.
#### WARNINGS:
* Before opening any Note Door, the player must talk to Bottles at the 50 Note door. In order to add to the Quality of Life, a bottles is added to the 810 Note Door Location for Final Note Door Only mode.
* Item Carrying Capacity: I'm not sure if the game will break if you set the After Cheato value to a value smaller than the Before Cheato value. Please be weary.
### Jinjos, Extra Lives, & Misc Objects
* Include Abnormalities: Some blue eggs, red feathers, and gold feathers are structured differently in the ROM than normal eggs and feathers, and turning on this feature will shuffle them in with these instead.

## Warps
### World Order Warps
* None: Skips the setting.
* Simple Shuffle: Simplified shuffling to guarantee a solution. Mumbo's Mountain is always the first level, with the moves Talon Trot, Shock Jump Pad, and Beak Buster. All other world and moves are random.
* Bottles Shuffle: More complicated shuffle. Worlds are placed in a logical order so that the previous worlds will give the needed moves to progress the game. Logic might not work if worlds are skipped. Bottles mounds are shuffled with Jinjos, Extra Lives, and Miscellaneous Object locations to promote more exploration.
### Within World Warps
* None: Skips the setting
* Shuffle By World: All warps going into a room are linked with warps until there's an eventual exit. Includes transformation warps if possible.
* Shuffle By Game: LMAO this is ambitious and is not currently implemented.
### Starting Area
* New Game Start Area: Starting a new game will start you here. Loading a game may start you here depending on what flags you hit, but I'm not entirely sure.
* Skip Intro Cutscene: Skips the cutscene when starting a new game, but not the one where the player enters the lair for the first time.

## Enemies
* None: Skips the setting.
* Shuffle: Shuffles the enemies by category (Ground, Flying, Wall).
* Randomize: Randomizes the enemies by category (Ground, Flying, Wall). Some enemies only appear in specific worlds.
* Checkboxes: Select the enemies you want to appear when using the Randomize option. Must select at least 1 generic Ground, Wall, and Flying enemy each. Enemies with an asterisks may softlock/crash the game.

## Aesthetics

### Banjo-Kazooie Model Color
Stuff Here
### Short Sounds, Fanfare/Jingles, & Looped Music
Stuff Here
### Sprites & Textures
Stuff Here

## Customizable

### Models
Stuff Here
### Animations
Stuff Here
### Properties
Stuff Here

## World Specific

### Gruntilda's Lair
* Skip Furnace: Places a warp on the first square of Furnace Fun that leads to the next area. Also changes Brentilda's text to potentially give useful hints.
* No Detransformations: Removes all transformation barriers in the lair.
* Final Battle Difficulty:
* Monster House:
* What Floor?:

### Mumbo's Mountain
* Include Flowers: If the notes/eggs/feathers feature is not set to 'none', the flowers in the level will be included.

### Treasure Trove Cove
* Scattered Notes/Eggs/Feathers: Notes, eggs, and feathers are scattered across the level, both in the water and in the air, based on the location they would normally appear.

### Clanker's Cavern
* Shuffle Clanker Ring Order: Clanker's ring order is shuffled.

### Bubblegloop Swamp
* Shuffle Croctus Order: Croctus spawn order is shuffled.
* Mr. Vile Bigger, Badder Crocodile: Makes Mr. Vile appear larger. He still moves at the same speed and eats at the same distance, but it's harder to see where the Yumblies and Grumblies spawn.
* Tiptup Choir: The turtles are scattered across the room, with their heads barely appearing above the floor.

### Freezeezy Peak
* Boggy Races Moved Flags: Flag poles for the Boggy race are either tighter left, tighter right, lowered to the floor to make harder to see, or rotated.

### Gobi's Valley
* Shuffle Ancient Ones Order: Ancient Ones order is shuffled.
* Shuffle Maze Jinxy Heads Order: Jinxy heads to raise King Sandybutt's Tomb order is shuffled.
* Randomize Matching Puzzle: The matching puzzle changes the colors of the tiles that the player has to match, rather than the icons themselves.

### Mad Monster Mansion
* Pots Are Lit:

### Rusty Bucket Bay
* Randomized Button Combo: Generates a random 6-digit combination of 1s, 2s, and 3s for the whistle buttons and places the code over the original code spot.

### Click Clock Wood
* By Season: All shuffling happens within each seasons/lobby area. This makes it easier for players to track what they are missing.
* Within World: All shuffling happens throughout the level.

## Miscellaneous
* Create Cheat Sheet(s): Writes helpful into to files that gives hints item locations, warps, and some misc info.
* Remove Extra Files: Removes the compressed and decompressed files extrated from the ROM. Useful for BK modders or debugging an issue.
* Show Tool Tips: With the feature on, hovering over a Brentilda icon will inform the user what the feature does.

# Common Problems

## Computer Says Randomizer Is A Virus
If you go to virustotal.com and upload the BK Randomizer, it will tell you that about 10% (this value changes) of Anti-Virus softwares will claim this is a virus. This is a common issue when using pyinstaller to turn the python code into an exectuable file. I will have my code in a GitHub repository if anyone would like to check to see that the BK Randomizer is not doing anything malicious. If you trust me that the randomizer is not a virus, there is a work around to the Windows Defender Anti-Virus, demonstrated in the following YouTube video: https://www.youtube.com/watch?v=_5gbWPEcHZs

## GUI Errors/Warnings
* ROM directory cannot include spaces. This is because GZIP.EXE uses the command prompt and treats spaces as new inputs. Avoid using special characters as well.
* ROM file must be a Banjo-Kazooie ROM v1.0 NTSC (.z64). Other formats are currently not supported. Randomizer may work on top of other BK mods, but not guaranteed.
* Seed, upper bounds, and lower bounds must be positive integers.
* Python Files, Folders, and GZIP.EXE must be in their original locations with the BK ROM in the main folder.

## Potential Softlocks
* When turning on the 'Potential Softlock' features, the game may be put into a state where a collectable cannot be reached or the game cannot be progressed without resetting.
* If performing RBA (Reverse Bee Adventure, where you avoid the detransformation areas to roam the rest of the game as the bee), the bee can get stuck in a lot of places.

## Known Bugs/Crashes
* In Clanker's Cavern, if the move in the gold feather room gets randomized, there's a possible chance the game will crash due to the lack of cameras in that room. The work around is to start the dialog, end the dialog using L+R+B, then reactivating the dialog.
* In specific areas, such as Treasure Trove Cove and Furnace Fun, the game may crash. The reason is unknown, and there are currently no work arounds.
* In Mad Monster Mansion, Napper may be indefinetly awake and guarding a Jiggy. The reason is unknown, but only occurs with potential softlocks.
* In Click Clock Wood, there is an occasional glitch where the player can collect 11/10 Jiggies when items are only shuffled within the world. The reason is unknown.

# FAQ

## Where Could I Find A Banjo-Kazooie v1.0 NTSC ROM File?
I am not providing anyone the ROM file for Banjo-Kazooie, nor does the script create the ROM file for them. It takes the users software and creates a copy, then modifies that copy. It is up to the user to obtain a copy of the software legally.

## Could ___ Feature Be Added?
Not-Planned Features:
* Non-Collectable Objects, such as trees, crates, etc
* Bosses, such as Conga, Nipper, etc
If you have any suggestions for new features, feel free to let me know. I honestly didn't think people would care about shuffling music, but that turned out to be a really funny feature. If you don't like a feature, don't use it, but if you have an idea of how it can be changed, let me know. Even if your feedback is "This part of the game is too easy", I could try to figure out some way to make it harder.

# Special Thanks
* The RARE staff, for making such an impactful game. Big shoutouts to Grant Kirkhope for an amazing soundtrack and being an amazing person in general.
* The Developers Of Banjo-Kazooie Modding/Viewing Tools, such as Banjo's Backpack, GEDecompressor, CRC Tool, and BK2BT. Also thank you to anyone who posted information on Hack64. I cannot name everyone by name, but your work is very appreciated and on behalf of the Banjo-Kazooie modding community, we cannot thank you enough. Discord link is listed in Contributing.
* People Who Played The Randomizer, whether it was playtesting, casually experiencing, or racing others. All feedback was taken seriously. All features that could reasonable be added were attempted at the very least. All issues brought up were either fixed or a work around was needed. Big shoutout to g0go, BlackDragonMax, HatWearingGamer, Wizzard, and Brittanykins for beta testing and feedback.
* Wizzard for providing the general basis for the Within World Warps code logic.
* Trynan for providing a more adaptable GUI interface.
* Mittenz for providing the checksum calculating code in C/C++, which was translated to Python for this project.
* Banjo's Backpack Discord, for everything ranging from technical support to emotional support. Big shoutouts to Jombo for most of the technical support. Other shoutouts go to BanjoFreak64, ThatCowGuy, PaleKing, Atezian, TheSourOG, Wedarobi, RetroNuva, and SapChap99.
* OoT And SM64 Randomizers, for inspiring me to find the Banjo's Backpack discord.

# Contributing
* If you'd like to take the source code to use for your own purposes, feel free. If you plan on making your own randomizer from the one I've made, consider the next bullet point or at least giving me credit somewhere.
* I currently wrote this code in Python, which is simple to pick up if anyone would like to learn. If you'd like to continue working on the Python version or need help creating a randomizer in a different coding language or something, I'll try to provide comments and answer questions as to what I personally did to randomize the ROM. Keep in mind that I'm learning how to randomize Banjo-Kazooie as I go, and might not have all of the answers to your questions.
* There's a community dedicated to Banjo-Kazooie modding called "Banjo's Backpack". There's a lot of smart people there, though most of us are still trying to learn as we go. Here is an invite: https://discord.gg/KSkN3yf4dt

# Contacting Me
I'm really bad at looking at social media messages, but here are different ways to try to reach me:
Twitter: https://twitter.com/GiantJigglypuff
YouTube: https://www.youtube.com/channel/UCipn0cYaHIAOtnEAc6NOw8g
Twitch: https://www.twitch.tv/giantjigglypuff3
My Discord Server: https://discord.gg/SrFxshj4fF

If you read all of this, bless your heart.