# BK_Randomizer

Which ROM extentions work with the randomizer?
 * I've only tested for .z64 roms. I don't know if it works for others.

Which emulators did you test on?
 * I did most of my testing on Mupen64Py, but it should work on others.

Does this work with ROM hacks?
 * I can't guarantee it, but because the script makes a copy of your game, it won't ruin the original and you can test it without worry.

Some Terms You Should Know:
>Flagged vs Non-Flagged Objects
 * A flagged object is an object where when you collect it and exit the level, the object will not return back to the level, such as Jiggies, Mumbo Tokens, and Empty Honeycombs. A non-flagged object is an object you collect, but will respawn when you re-enter the level. This includes, but isn't limited to, Jinjos, 1-Ups, and temporary collectibles for various NPCs, like an orange, acorns, and worms.
>Structs
 * A struct is a collectible that adds to your values, such as notes, blue eggs, red feathers, and gold feathers.
>Enemies
 * This includes all small enemies, but not bosses.

What isn't randomized?
 * Flagged objects
 * Some enemies with weird properties
 * Bottles Mounds
 * Warps from Gruntilda's Lair to worlds
 * Warps within worlds
 * Non-Collectible Objects (trees, crates, etc)
 * Bosses (Conga, Napper, etc)

Do I plan on expanding on the randomizer?
 * If the community wants some new feature and I have the time and energy to do it, sure lol.
 * Here are the features I'm planning on making in the future:
   a) Randomize flagged objects that won't cause errors
   b) Randomizing all of the other worlds
   c) Specific enemy modes, where all of the enemies are the same, such as bulls, skeletons, mummies, ghosts
   d) Randomize the warps within the world that won't cause errors
   e) Randomizing the warps from Grunty's Lair to worlds that are progressable
   f) Randomizing the warps from Grunty's Lair to worlds and adding Bottle's Mounds to them to make them progressable

GUI Explained:
>Rom Select
 * Opens a browser to select the rom file (default to .z64)
>Seed
 * Can optionally set a seed
Randomization Options:
>None
 * Nothing changes in that category
>Within World
 * All of the items in a world rearrange the order with each other
>Completely
 * All of the items in a world change into an item that can take its place

Script Errors:
 * Providing a rom file that doesn't end in .z64 will cause an error that will show up in the log.
 * Providing a seed that isn't comprised of just numbers will cause an error that will show up in the log.
 * Rom file formatted differently than the tested roms may cause an error and show up in the log.

Known ROM Errors:
 * Location where enemy normally was will be blank. This is because some enemies can't appear in that world, so they end up disappearing.
 * When randomizing objects with flags (Jiggies, Mumbo Tokens, Empty Honeycombs), you might encounter one of two errors:
   1) The Empty Honeycomb does not add to your total when collected.
   2) When entering the world/demo screen, the screen is black with no music.
 During either of these cases, that's a sign that something in the randomization has messed up. My only suggestion is to try a different seed.

What To Do If Rom Errors:
 * If it's the base game with the .z64 extension, send me (GiantJigglpuff3/Cyrus Kashef) a message with the log file and briefly explain what the error is.
 * If it's the practice rom mod, do the above, but also let me know that it's the practice rom mod and what extension you're using. For this one, I won't be able to fix the issues alone since I didn't make the practice rom, but I know there might be a few people wanting to test it out.
 * If it's any other modded version of the game, please be patient with me, as I'm still trying to get the randomizer to work for the base game.

Instructions
1) Place the original rom file, the Banjo Kazooie Randomizer executable file, and GZIP in the same folder.
2) Run the Banjo Kazooie Randomizer executable file.
3) Input the rom file, seed, and prefered customizations.
4) Click submit.
5) In that same folder, a new folder should have been created called EPIIISA. In that folder should be the new randomized rom file, with it's name being "Banjo-Kazooie_Randomized_Seed_#.z64". That # is the seed value.

Is This A Virus?
If you go to virustotal.com and upload the BK Randomizer, it will tell you that about 10% (this value changes) of Anti-Virus softwares will claim this is a virus. This is a common issue when using pyinstaller to turn the python code into an exectuable file. I will have my code in a GitHub repository if anyone would like to check to see that the BK Randomizer is not doing anything malicious.

Taking Source Code:
>If you'd like to take the source code to use for your own purposes, feel free. If you plan on making your own randomizer from the one I've made, consider the next section of this README or at least giving me credit somewhere.

Contributing
>I coded entire project on my own, but that doesn't mean I wouldn't mind a team to work with. I currently wrote this code in Python. If you'd like to continue working on the Python version or need help creating a randomizer in a different coding language, I'll try to provide comments and answer questions as to what I personally did to randomize the rom. Keep in mind that I'm learning how to randomize this rom as I go, and might not have all of the answers to your questions.

Special Thanks
>Although I coded the randomizer myself, I could not have gotten this far without:
 1) The technical knowledge of SapChap99 and Jombo.
 2) The entire Banjo's Backpack community for their support, most notably BanjoFreak64, ThatCowGuy, and PaleKing.
 3) The Banjo Kazooie speedrun community, whose excitement for the randomizer kept me going.
 4) The Ocarina of Time and Super Mario 64 randomizers for serving as inspirations for this randomizer.
>And a special shoutout to RARE for making such an impactful game to me and so many others.
