def split_dir_rom(rom_dir):
    '''Separates the directory to the rom with the name of the rom'''
    logger.info("Split Dir Rom")
    if("\\" in rom_dir):
        rom_file = rom_dir.split("\\")[-1]
    elif("/" in rom_dir):
        rom_file = rom_dir.split("/")[-1]
    else:
        logger.info("File Directory Unfamiliar Format?")
        logger.warning("File Directory Unfamiliar Format?")
    file_dir = rom_dir.replace(rom_file, "")
    return (file_dir, rom_file)

def setup_tmp_folder(file_dir):
    """Creates temporary folder that'll be used to store bin files and the randomized ROM."""
    logger.info("Set Up Temporary Folder")
    if(not os.path.isdir(file_dir + tmp_folder)):
        os.mkdir(file_dir + tmp_folder)
    else:
        for filename in os.listdir(file_dir + tmp_folder):
            file_path = os.path.join(file_dir + tmp_folder, filename)
            try:
                if(os.path.isfile(file_path) or os.path.islink(file_path)):
                    os.unlink(file_path)
                elif(os.path.isdir(file_path)):
                    shutil.rmtree(file_path)
            except Exception as e:
                logger.error('Failed to delete %s. Reason: %s' % (file_path, e))

def seed(seed_val=None):
    """If seed was not provided, generates a seed value."""
    logger.info("Generate Seed")
    if((seed_val == None) or (seed_val == "")):
        seed_val = random.randint(10000000, 19940303)
        seed_generated = True
    else:
        seed_generated = False
    logger.debug("Seed: " + str(seed_val))
    return (seed_val, seed_generated)

def make_copy_of_rom(seed_val, file_dir, rom_file):
    """Creates a copy of the rom that will be used for randomization"""
    logger.info("Make Copy Of Rom")
    randomized_rom_file = file_dir + tmp_folder + "Banjo-Kazooie_Randomized_Seed_" + str(seed_val) + ".z64"
    shutil.copyfile(file_dir + rom_file, randomized_rom_file)