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
* Generate Settings Code: Generates a string of your settings, not including seed, aesthetic changes, and misc options.
* Apply Settings Code: Applies a predetermined configuration to your settings, not including seed, aesthetic changes, and misc options.
* Randomly Select Configurations: Selects a saved configuration in the "Configurations" folder and applies the settings.
* Randomly Select EVERY Setting: Randomly generates every setting.

## Collectables
### All Items
* None: Skips the setting.
* Shuffle (World): Takes all items of that set and swaps the Object IDs within the world (can be overriden for Click Clock Wood; see World Specific Features).
* Shuffle (Game): Takes all items of that set and swaps the Object IDs within all worlds/lair. This will override the World Specific Feature for Click Clock Wood.
* Randomize: For every item in the world, randomly assign a new Object ID.
### Jiggy, Empty Honeycomb, & Mumbo Token Specific
* Include Abnormalities: Some items have special properties that won't softlock the game, but create weird effects.
* Include Potential Softlocks: Some items create scenarios that may prevent the player from 100%-ing or finishing the game.
* Door Of Grunty Only: All worlds will automatically open, and the value for the Door Of Grunty can be set on the side (from 0 to 99).
* Free Transformations: All Mumbo transformations won't cost you a single Mumbo Token.
* One Health Only: You will only have one health the entire game, no matter how many Empty Honeycombs you pick up. Good luck not getting hit or falling!
### Notes, Blue Eggs, Red Feathers, & Gold Feathers
* Randomize: Based on the number of notes needed to complete the game, the odds of a note appearing will be adjusted.
* All Notes: All eggs and feathers become notes. Brentildas are replaced with egg and feather refills. The refill at that Brentilda location is random.
* Scaling Note Doors: Depending on how many notes you set the 810 Note Door Value to, the number of notes needed per proceeding door will be increased/decreased accordingly.
* Final Note Door Only: Removes all note doors proceeding the 810 Note Door, and sets the value of the 810 Note Door to the desired value.
* Item Carrying Capacity: Sets the number of each item the player can carry before and after visiting Cheato between 0 and 255, inclusively.
* Note Door Warning: Before opening any Note Door, the player must talk to Bottles at the 50 Note door. In order to add to the Quality of Life, a bottles is added to the 810 Note Door Location for Final Note Door Only mode.
* Item Capacity Warning: I'm not sure if the game will break if you set the After Cheato value to a value smaller than the Before Cheato value. Please be weary.
### Jinjos, 1-Ups, & Misc Objects
* Include Abnormalities: Some areas have Eggs and Feathers that aren't formatted like regular Eggs and Feathers, so they can be swapped with this category if checked.
* Starting Life Count: Can be set anywhere from 0 to "technically 255", but I'm not sure what happens if you overflow the value, so please just make it max of 100.

## Warps
### World Order Warps
* None: Skips the setting.
* Basic Shuffle: Simplified shuffling to guarantee a solution. Mumbo's Mountain is always the first level, with the moves Talon Trot, Shock Jump Pad, and Beak Buster. All other world and moves are random.
* Bottles Shuffle: More complicated shuffle. Worlds are placed in a logical order so that the previous worlds will give the needed moves to progress the game. Logic might not work if worlds are skipped. Bottles mounds are shuffled with Jinjos, Extra Lives, and Miscellaneous Object locations to promote more exploration.
* Start Game With All Moves: You start the game with all of the moves, though you won't be given Eggs and Feathers to start with.
### Within World Warps
* None: Skips the setting
* Shuffle By World: All warps within a level are shuffled, barring some constraints. Excludes transformation warps.
* Shuffle By Game: All warps within the levels (not including Gruntilda's Lair) are shuffled, barring some constraints. Excludes transformation warps.
### Starting Area
* New Game Start Area: Starting a new game will start you here. Loading a game may start you here depending on what flags you hit, but I'm not entirely sure.
* Skip Intro Cutscene: Skips the cutscene when starting a new game, but not the one where the player enters the lair for the first time.

## Enemies
* None: Skips the setting.
* Shuffle: Shuffles the enemies by category (Ground, Flying, Wall).
* Randomize: Randomizes the enemies by category (Ground, Flying, Wall). Some enemies only appear in specific worlds.
* Select All Non-Softlock Enemies: Checks all of the non-softlock enemy boxes.
* Remove All Enemies: Unchecks all of the enemy boxes.
* Checkboxes: Select the enemies you want to appear when using the Randomize option. Must select at least 1 generic Ground, Wall, and Flying enemy each. Enemies with an asterisks may softlock/crash the game. If no enemy is checked for a category, no enemy will appear.

## Aesthetics

### Banjo-Kazooie Model Color
* Dropbox: Select from presets of color combinations.
* Random Preset: Randomly sets a preset for colors.
* Random Colors: Randomly sets colors.
* Note: When setting your own colors, longer entries are made for 32-bit and shorter entries are made for 16-bit. If you're using a 16-bit color, the last value must be odd in order to be visible. You can use the following link to convert the colors: https://trolsoft.ru/en/articles/rgb565-color-picker
### Short Sounds, Fanfare/Jingles, & Looped Music
* Shuffle Sounds: Sounds last about a second long. This includes things like Eggs, Feathers, Honeycombs, Mumbo Tokens, etc.
* Shuffle Jingles: Jingles last a few seconds. This includes the Jiggy Jig, successfully finishing a task, etc.
* Shuffle Music: Music is typically long and potentially loops. This includes level background music, mini games music, and ambient noises.
* Include Beta Sounds: Some songs not used in the final game but are present in the data are including in shuffling for all checked categories.
### Sprites & Textures
* Shuffle Skyboxes: Shuffles the skies and the clouds of the levels.
* Shuffle Talking Sprites: Shuffles the head sprites used in conversations.

## Customizable

### Models, Animations, & Properties
* Model Manipulation: Can swap or replace models.
* Animation Manipulation: Can swap or replace animations.
* Properties Manipulation: Can replace properties.
* Buttons: Opens up the JSON files to allow custom editing.

### How To Edit The JSON Files
* Next to each option, there's a button that will open a JSON file.
* The JSON is broken into sections. The names of the sections don't matter, but they must be distinct from the other sections.
* Each section may have different subsection types:
  - Original/Replacements: Each original will be randomly replaced with a replacement. For models and animations, replacements must be the same size or smaller than the original and each replacement will only be used once. For properties, any number of original/replacement files are allowed and each property can be used more than once.
  - Swap: Swap1 will swap into Swap2, Swap2=>Swap3... Last Swap#=>Swap1.
  - Shuffle: All items in the subcategory will be shuffled within each other.
* For more address values, check out Hack64.net under ROM Map.

## World Specific

### Gruntilda's Lair
* Skip Furnace: Going past the 765 Note Door will skip the Furnace Fun pad area and lead straight to the 810 Note Door room. Also changes Brentilda's text to potentially give useful hints.
* No Detransformations: Removes all transformation barriers in the lair. Warning: Some areas may softlock the transformations.
* Final Battle Difficulty: On a scale of 1 to 3, it adds effects to the grunty fight. Zero turns off the feature.
* Monster House: Replaces some items with enemies.
* What Floor?: Removes collision with the floor. Shock Jump Pads are placed on the field to help move around, and the pillars will still have collision.
* Mini Me: Gruntilda shrinks in size, making her harder to hit.

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
* Pots Are Lit: The flower pots located in the graveyard switch places with the fire pain objects, which are shown with sparkles and steam. Look at torches and other fire places for sparkles. If you don't see it, shoot/poop an egg in.
* Randomize Motzand's Song: Randomly selects new keys to press. Follow Motzand to find the pattern.

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
* There's a possible chance the game will crash due to the lack of cameras in a room with a move that's not normally there. The work around is to start the dialog, end the dialog using L+R+B, then reactivate the dialog to read what the move does.
* In specific areas, such as Treasure Trove Cove and Furnace Fun, the game may crash. The reason is unknown, and there are currently no work arounds. This shouldn't prevent the player from restarting the console and replaying the level. If it does, please contact me.
* In Mad Monster Mansion, Napper may be indefinetly awake and guarding a Jiggy. The reason is unknown, but should only occur with potential softlocks checked on.
* In Click Clock Wood, there is an occasional glitch where the player can collect 11/10 Jiggies when items are only shuffled within the world. The reason is unknown, but may only occur with abnormal or potential softlock Jiggies/Tokens/Honeycombs.

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
* Banjo's Backpack Discord, for everything ranging from technical support to emotional support. Big shoutouts to Jombo for most of the technical support. Other shoutouts go to BanjoFreak64, ThatCowGuy, PaleKing, Atezian, TheSourOG, Bynine, Wedarobi, RetroNuva, and SapChap99.
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