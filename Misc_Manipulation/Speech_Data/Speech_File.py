'''
Created on Nov 12, 2021

@author: Cyrus
'''

import mmap

def leading_zeros(num_string, num_of_digits):
    '''Adds leading zeros to a string that's supposed to be a certain number of digits in length'''
    if(num_of_digits <= len(num_string)):
        return num_string
    for add_zero in range(num_of_digits - len(num_string)):
        num_string = "0" + num_string
    return num_string

class Speech_File_Class():
    def __init__(self, file_dir, pointer):
        self._file_dir = file_dir
        with open(f"{self._file_dir}Randomized_ROM/{pointer}-Decompressed.bin", "r+b") as decomp_file:
#         with open(f"{self._file_dir}{pointer}.bin", "r+b") as decomp_file:
            self.mm_decomp = mmap.mmap(decomp_file.fileno(), 0)
        self.speech_list = []
    
    def _breakdown(self):
        curr_index = 0
        mm_len = len(self.mm_decomp)
        last_sprite = -1
        curr_text = ""
        while(curr_index < mm_len):
            first_index = self.mm_decomp[curr_index]
            second_index = self.mm_decomp[curr_index + 1]
            third_index = self.mm_decomp[curr_index + 2]
            fourth_index = self.mm_decomp[curr_index + 3]
            no_text_added = True
            # This Is The Header
            if((first_index == 1) and (second_index == 3) and (third_index == 0)):
                self.speech_list.append(("Header", "010300"))
            # This Is An Empty String
            elif((third_index == 1) and (fourth_index == 0)):
                self.speech_list.append((last_sprite, curr_text))
                empty_string = (leading_zeros(str(hex(first_index))[2:], 2).upper() +
                                leading_zeros(str(hex(second_index))[2:], 2).upper() +
                                leading_zeros(str(hex(third_index))[2:], 2).upper() +
                                leading_zeros(str(hex(fourth_index))[2:], 2).upper())
                self.speech_list.append(("Empty", empty_string))
                curr_text = ""
                curr_index += 1
            # This Is A Selectable Option (Furnace Fun)
            elif(second_index == 8):
                # Flush Text
                if(len(curr_text) > 0):
                    self.speech_list.append((last_sprite, curr_text))
                    curr_text = ""
                # This is an option for the text; Replaces the ~
                last_sprite = second_index
                for text_index in range(curr_index + 3, curr_index + 2 + third_index):
                    curr_text += leading_zeros(str(hex(self.mm_decomp[text_index]))[2:], 2).upper()
                curr_index += third_index - 1
            # Speech Is Continued By Same Person
            elif(last_sprite == second_index):
                no_text_added = False
                curr_text += "\n"
                # In this case, the third index is the length of the string.
                for text_index in range(curr_index + 3, curr_index + 2 + third_index):
                    curr_text += leading_zeros(str(hex(self.mm_decomp[text_index]))[2:], 2).upper()
                curr_index += third_index - 1
            # Person Talking Changed
            else:
                no_text_added = False
                # Save who talked last
                self.speech_list.append((last_sprite, curr_text))
                curr_text = ""
                # New person talking
                last_sprite = second_index
                for text_index in range(curr_index + 3, curr_index + 2 + third_index):
                    curr_text += leading_zeros(str(hex(self.mm_decomp[text_index]))[2:], 2).upper()
                curr_index += third_index - 1
            # Flush Text
            if(no_text_added and (len(curr_text) > 0)):
                self.speech_list.append((last_sprite, curr_text))
                curr_text = ""
            curr_index += 3
    
    def _print_speech(self, readable=True):
        for (curr_sprite, curr_text) in self.speech_list:
            if(len(curr_text) > 0):
                if(readable and isinstance(curr_sprite, int)):
                    readable_text = ""
                    for char_index in range(0, len(curr_text), 2):
                        readable_text += bytearray.fromhex(curr_text[char_index:char_index+2]).decode()
                    print(f"{curr_sprite}: {readable_text}")
                else:
                    print(f"{curr_sprite}: {curr_text}")
    
    def _replace_line(self, old_text, new_text):
        old_text_index = self.mm_decomp.find(bytes.fromhex(old_text))
        if(old_text_index == -1):
            print("SOMETHING MESSED UP HERE, BROSKI")
            raise SystemError
        old_len = self.mm_decomp[old_text_index - 1] - 1
        self.mm_decomp[old_text_index - 1] = len(new_text) + 1
        ending_size = len(self.mm_decomp) - old_text_index - old_len
        ending = []
        for index in range(old_text_index + old_len, len(self.mm_decomp)):
            ending.append(self.mm_decomp[index])
        self.mm_decomp.resize(old_text_index + len(new_text) + ending_size)
        index_add = 0
        for char in new_text:
            self.mm_decomp[old_text_index + index_add] = ord(char)
            index_add += 1
        ending_index = 0
        for index in range(old_text_index + len(new_text), len(self.mm_decomp)):
            self.mm_decomp[index] = ending[ending_index]
            ending_index += 1
    
    def _furnace_fun_question_format(self, question_part1, question_part2, answer1, answer2, answer3):
        self.mm_decomp.resize(27 + len(question_part1) + len(question_part2) + len(answer1) + len(answer2) + len(answer3))
        # HEADER
        header = [0x01, 0x01, 0x02, 0x05, 0x00, 0x05]
        grunty_sprite = 0x80
        for index, value in enumerate(header):
            self.mm_decomp[index] = value
        curr_index = len(header)
        # QUESTION 1
        self.mm_decomp[curr_index] = grunty_sprite
        self.mm_decomp[curr_index + 1] = len(question_part1) + 1
        for index_add, char in enumerate(question_part1):
            self.mm_decomp[curr_index + 2 + index_add] = ord(char)
        curr_index += 2 + len(question_part1)
        self.mm_decomp[curr_index] = 0x00
        # QUESTION 2
        if(question_part2):
            self.mm_decomp[curr_index + 1] = grunty_sprite
            self.mm_decomp[curr_index + 2] = len(question_part2) + 1
            for index_add, char in enumerate(question_part2):
                self.mm_decomp[curr_index + 3 + index_add] = ord(char)
            curr_index += 3 + len(question_part2)
            self.mm_decomp[curr_index] = 0x00
        # Answer 1
        self.mm_decomp[curr_index + 1] = 0x81
        self.mm_decomp[curr_index + 2] = len(answer1) + 3
        self.mm_decomp[curr_index + 3] = 0xFD
        self.mm_decomp[curr_index + 4] = 0x6C
        for index_add, char in enumerate(answer1):
            self.mm_decomp[curr_index + 4 + index_add] = ord(char)
        curr_index += 5 + len(answer1)
        self.mm_decomp[curr_index] = 0x00
        # Answer 2
        self.mm_decomp[curr_index + 1] = 0x82
        self.mm_decomp[curr_index + 2] = len(answer2) + 3
        self.mm_decomp[curr_index + 3] = 0xFD
        self.mm_decomp[curr_index + 4] = 0x6C
        for index_add, char in enumerate(answer2):
            self.mm_decomp[curr_index + 4 + index_add] = ord(char)
        curr_index += 5 + len(answer2)
        self.mm_decomp[curr_index] = 0x00
        # Answer 3
        self.mm_decomp[curr_index + 1] = 0x83
        self.mm_decomp[curr_index + 2] = len(answer3) + 3
        self.mm_decomp[curr_index + 3] = 0xFD
        self.mm_decomp[curr_index + 4] = 0x6C
        for index_add, char in enumerate(answer3):
            self.mm_decomp[curr_index + 4 + index_add] = ord(char)
        self.mm_decomp[curr_index + 5 + len(answer3)] = 0x00