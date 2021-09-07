import random

def get_file_bytes(file_dir, read_file):
    """Reads the contents of a hex file without using mmap"""
    logger.info("Get File Bytes")
    with open(file_dir + read_file, "rb") as file:
        file_bytes = file.read()
    return file_bytes

def leading_zeros(num_string, num_of_digits):
    '''Adds leading zeros to a string that's supposed to be a certain number of digits in length'''
    if(num_of_digits <= len(num_string)):
        return num_string
    for add_zero in range(num_of_digits - len(num_string)):
        num_string = "0" + num_string
    return num_string

def run_crc_tool(seed_val, file_dir):
    '''Runs the CRC Tool that allows a modified game to run'''
    logger.info("Running CRC Tool")
    cmd = file_dir + "rn64crc2/rn64crc.exe -u " + file_dir + tmp_folder + "Banjo-Kazooie_Randomized_Seed_" + str(seed_val) + ".z64"
    subprocess.Popen(cmd.split(),shell=True).communicate()

# def negative_hex_value(pos_dec_value):
#     '''Returns the decimal value of a hexidecimal number with an inversed sign'''
#     neg_dec_value = pos_dec_value - 65536
#     return neg_dec_value