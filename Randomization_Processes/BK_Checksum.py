import mmap

class BK_Checksum_Class():
    def __init__(self, file_dir, seed_val):
        self._file_dir = file_dir
        self._seed_val = seed_val

    def leading_zeros(self, num, num_of_digits):
        '''Adds leading zeros to a string that's supposed to be a certain number of digits in length'''
        if(isinstance(num, int)):
            if(num < 0):
                num += 0x10000
            num = str(hex(num))[2:].upper()
        while (len(num) < num_of_digits):
            num = "0" + num
        return num

    def _calc_checksum(self, address):
        with open(f"{self._file_dir}Randomized_ROM/{address}-Decompressed.bin", "r+b") as f:
            f_bytearray = bytearray(f.read())
        crc1 = 0
        crc2 = 0xFFFFFFFF
        for byte in f_bytearray:
            crc1 = crc1 + byte
            crc2 = crc2 ^ (byte << (crc1 & 0x17))
        return crc1, crc2
    
    def _set_checksum(self, checksum_val, index_start, address=None):
        if(address):
            with open(f"{self._file_dir}Randomized_ROM/{address}-Decompressed.bin", "r+b") as f:
                mm = mmap.mmap(f.fileno(), 0)
        else:
            with open(f"{self._file_dir}Randomized_ROM/Banjo-Kazooie_Randomized_Seed_{self._seed_val}.z64", "r+b") as f:
                mm = mmap.mmap(f.fileno(), 0)
        checksum_str = self.leading_zeros(checksum_val, 8)
        print(checksum_str)
        for index_add in range(4):
            mm[index_start + index_add] = int(checksum_str[index_add * 2: (index_add + 1) * 2], 16)
    
    def _main(self):
        # ASM_ENGINE_CODE ->  0xF37F90
        #     CRC2 -> ASM_ENGINE_VARS @ 0xF260
        crc1, crc2 = self._calc_checksum("F37F90")
        print(f"CRC 1: {self.leading_zeros(crc1, 8)}    CRC 2: {self.leading_zeros(crc2, 8)}")
        self._set_checksum(crc2, 0xF264, "F9CAE0")
        # ASM_ENGINE_VARS ->  0xF9CAE0
        #     CRC2 -> ASM_LIBRARY_VARS @ 0xF64
        crc1, crc2 = self._calc_checksum("F9CAE0")
        print(f"CRC 1: {self.leading_zeros(crc1, 8)}    CRC 2: {self.leading_zeros(crc2, 8)}")
        self._set_checksum(crc2, 0xF64, "F362EB")
        # ASM_LIBRARY_CODE -> 0xF19250
        #     CRC1 -> ROM @ 0x5E78
        #     CRC2 -> ROM @ 0x5E7C
        crc1, crc2 = self._calc_checksum("F19250")
        print(f"CRC 1: {self.leading_zeros(crc1, 8)}    CRC 2: {self.leading_zeros(crc2, 8)}")
        self._set_checksum(crc1, 0x5E78)
        self._set_checksum(crc2, 0x5E7C)
        # ASM_LIBRARY_VARS -> 0xF362EB
        #     CRC1 -> ROM @ 0x5E80
        #     CRC2 -> ROM @ 0x5E84
        crc1, crc2 = self._calc_checksum("F362EB")
        print(f"CRC 1: {self.leading_zeros(crc1, 8)}    CRC 2: {self.leading_zeros(crc2, 8)}")
        self._set_checksum(crc1, 0x5E80)
        self._set_checksum(crc2, 0x5E84)

if __name__ == '__main__':
    bk_checksum_obj = BK_Checksum_Class("C:/Users/Cyrus/eclipse-workspace/BK_Rando_v2.0/", 13526812)
    bk_checksum_obj._main()