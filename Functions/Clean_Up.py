def remove_bin_files(file_dir):
    """Removes compressed and decompressed bin files created during the randomization"""
    logger.info("Remove Bin Files")
    for filename in os.listdir(file_dir + tmp_folder):
        file_path = os.path.join(file_dir + tmp_folder, filename)
        try:
            if((os.path.isfile(file_path) or os.path.islink(file_path)) and file_path.endswith(".bin")):
                os.unlink(file_path)
            elif(os.path.isdir(file_path)):
                shutil.rmtree(file_path)
        except Exception as e:
            logger.warning('Failed to delete %s. Reason: %s' % (file_path, e))