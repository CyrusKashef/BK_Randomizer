# BK_Randomizer

Basic Instructions
1) Place the original rom file, the Banjo Kazooie Randomizer executable file, GZIP, and the CRC Tool (unzipped) in the same folder.
2) Run the Banjo Kazooie Randomizer executable file.
3) Input the rom file, seed, and prefered customizations.
4) Click submit.
5) In that same folder, a new folder should have been created called EPIIISA. In that folder should be the new randomized rom file, with it's name being "Banjo-Kazooie_Randomized_Seed_#.z64". That # is the seed value.

Which ROM extentions work with the randomizer?
 * I've only tested for .z64 roms. I don't know if it works for others (probably not).

Which emulator(s) did you test on?
 * I did most of my testing on Mupen64Py and Project 64 (versions 1.6 and 2.3), but it should work on others.

Does this work with ROM hacks?
 * I can't guarantee it, but because the script makes a copy of your game, it won't ruin the original and you can test it without worry.

Some Terms You Should Know:
>Flagged vs Non-Flagged Objects
 * A flagged object is an object where when you collect it and exit the level, the object will not return back to the level, such as Jiggies, Mumbo Tokens, and Empty Honeycombs. A non-flagged object is an object you collect, but will respawn when you re-enter the level. This includes, but isn't limited to, Jinjos, 1-Ups, and temporary collectibles for various NPCs, like an orange, acorns, and worms.
>Structs
 * A struct is a collectible that adds to your values, such as notes, blue eggs, red feathers, and gold feathers.
>Enemies
 * This includes all small enemies, but not bosses.
>Final Note Door
 * This is typically the 810 note door before reaching the Gruntilda battle. With this feature on, you can either set or randomize the note door's value, with every other door having a value of zero. Bottles's unskippable text at the start of the game will inform you the value if randomized.
>Final Puzzle
 * This is typically the 25 puzzle before reaching the Gruntilda battle. With this feature on, you can either set or randomize the puzzle's value, with every other puzzle having a value of zero, making the worlds open by default. Bottles's unskippable text at the start of the game will inform you the value if randomized.

What isn't randomized?
 * Some enemies with weird properties
 * Bottles Mounds
 * Warps from Gruntilda's Lair to worlds
 * Warps within worlds
 * Non-Collectible Objects (trees, crates, etc)
 * Bosses (Conga, Napper, etc)

Do I plan on expanding on the randomizer?
 * If the community wants some new feature and I have the time and energy to do it, sure lol.
 * Here are the features I'm planning on making in the future:
   a) Randomize the warps within the world that won't cause errors
   b) Randomizing the warps from Grunty's Lair to worlds that are progressable
   c) Randomizing the warps from Grunty's Lair to worlds and adding Bottle's Mounds to them to make them progressable

GUI Explained:
>Rom Select
 * Opens a browser to select the rom file (default to .z64)
>Seed
 * Can optionally set a seed
Randomization Options:
>None
 * Nothing changes in that category
>Shuffle
 * All of the items in a world rearrange their xyz locations with each other
>Completely
 * All of the items in a world change into an item that can take its place

Script Errors:
 * Providing a rom file that doesn't end in .z64 will cause an error that will show up in the log.
 * Providing a seed that isn't comprised of just numbers will cause an error that will show up in the log.
 * Rom file formatted differently than the tested roms may cause an error and show up in the log.
 * Having a space in the directory path will cause a pop up.
 * Not having GZIP or the CRC Tool in the folder with the ROM file will cause a pop up.
 * Giving a non-integer value to the note door and puzzle options.

Known ROM Errors:
 * Location where enemy normally was will be blank. This is because some enemies can't appear in that world, so they end up disappearing. In Grunty's Lair, this happens because you have to enter the world first for that enemy to appear. Example, entering Gobi's Valley will allow Mummies to roam the lair.
 * When randomizing objects with flags (Jiggies, Mumbo Tokens, Empty Honeycombs), you might encounter an Empty Honeycomb that does not add to your total when collected.
 During either of these cases, that's a sign that something in the randomization has messed up. My only suggestion is to inform me of the error with the seed number and try a different seed.

What To Do If Rom Errors:
 * If it's the base game with the .z64 extension, send me (GiantJigglpuff3/Cyrus Kashef) a message with the log file and briefly explain what the error is.
 * If it's the practice rom mod, do the above, but also let me know that it's the practice rom mod and what extension you're using. For this one, I won't be able to fix the issues alone since I didn't make the practice rom, but I know there might be a few people wanting to test it out.
 * If it's any other modded version of the game, please be patient with me, as I'm still trying to get the randomizer to work for the base game.

Is This A Virus?
>If you go to virustotal.com and upload the BK Randomizer, it will tell you that about 10% (this value changes) of Anti-Virus softwares will claim this is a virus. This is a common issue when using pyinstaller to turn the python code into an exectuable file. I will have my code in a GitHub repository if anyone would like to check to see that the BK Randomizer is not doing anything malicious.

Legality
>I am not providing anyone the ROM file for Banjo-Kazooie, nor does the script create the ROM file for them. It takes the users software and creates a copy, then modifies that copy. It is up to the user to obtain a copy of the software legally and to not distrubute copies of the software illegally.

Taking Source Code
>If you'd like to take the source code to use for your own purposes, feel free. If you plan on making your own randomizer from the one I've made, consider the next section of this README or at least giving me credit somewhere.

Contributing
>I coded entire project on my own, but that doesn't mean I wouldn't mind a team to work with. I currently wrote this code in Python. If you'd like to continue working on the Python version or need help creating a randomizer in a different coding language, I'll try to provide comments and answer questions as to what I personally did to randomize the rom. Keep in mind that I'm learning how to randomize this rom as I go, and might not have all of the answers to your questions.
>There's a community dedicated to Banjo-Kazooie modding called "Banjo's Backpack". There's a lot of smart people there, though most of us are still trying to learn as we go, since there was no documentation for us to work with.

Special Thanks
>Although I coded the randomizer myself, I could not have gotten this far without:
 1) The technical knowledge of SapChap99 to help me get started.
 2) The expertise of Jombo, who not only taught me how to compress/decompress, what tools I could use (GZIP and CRC), and guided me through pointers, but also put up with my snarky behavior and for running the Banjo's Backpack discord, along with the moderators.
 3) The entire Banjo's Backpack community for their support, most notably BanjoFreak64, ThatCowGuy, PaleKing, Atezian, and TheSourOG
 4) The Banjo Kazooie speedrun community, whose excitement for the randomizer kept me going, most notably Gogo, who helped me test the randomizer.
 5) The Ocarina of Time and Super Mario 64 randomizers for serving as inspirations for this randomizer.
>And a special shoutout to RARE for making such an impactful game to me and so many others.
