'''
Created on Jun 1, 2021

@author: Cyrus
'''

###################
### FILE IMPORT ###
###################

from Randomization_Processes.Misc_Manipulation.Model_Data import Generic_Models

#########################
### JINJO MODEL CLASS ###
#########################

class Jinjo_Model_Class(Generic_Models.Model):
    def _jinjo_model_vertices(self, original_color):
        model_vertex_dict = {
            "Blue": {
                "Main_Vertex": ["274F89FF", "179BF7FF", "173C75FF", "0C3A75FF", "2F69B9FF", "3D5A98FF", "0D2153FF"],
                "Belly": ["A03000FF", "873000FF", "EC4A00FF", "FF7A00FF"]
            },
            "Green": {
                "Main_Vertex": ["087400FF", "0CD500FF", "054900FF", "155B04FF", "0D9325FF", "077F02FF", "1A3900FF"],
                "Belly": []#"5B5B5BFF", "595959FF", "B5B5B5FF", "FFFFFFFF"]
            },
            "Orange": {
                "Main_Vertex": ["B33000FF", "FF7301FF", "CB2C00FF", "A01C01FF", "FF4D00FF", "EA6807FF", "A51100FF"],
                "Belly": ["B34002FF", "943000FF", "FF8D00FF", "FFDC00FF"]
            },
            "Pink": {
                "Main_Vertex": ["B02B8DFF", "FA61FFFF", "891275FF", "7D0060FF", "D65BBCFF", "D23498FF", "600047FF"],
                "Belly": []#"757575FF", "625F5FFF", "C9C0C4FF", "FFFFFFFF"]
            },
            "Yellow": {
                "Main_Vertex": ["D68008FF", "FFFF33FF", "CB5800FF", "AD6A00FF", "FF9F0AFF", "EAA60EFF", "A54D14FF"],
                "Belly": ["5E2800FF", "501900FF", "DD6702FF", "FFA21FFF"]
            },
        }
        self.model_vertex_dict = model_vertex_dict[original_color]
    
    def _jinjo_textures(self):
        self.model_texture_dict = {
            "Main_Texture": [0x80, 0x124, 0x1C0, 0x260]
        }

    def _jinjonator_model_textures(self):
        self.model_texture_dict = {
            # "Dark_Texture": [0x52, 0x56, 0x5C, 0x60, 0x68],
            # "Regular_Texture": [0x50, 0x54, 0x58, 0x5E, 0x62, 0x66, 0x6A, 0x6E],
            # "Light_Texture": [0x5A, 0x64, 0x6C],
            "Main_Texture": [num for num in range(0x50, 0x70, 0x2)]
        }

    # def _progressively_darker(self, color_one_str):
    #     darkest_color = int(color_one_str[:-2], 16) // 5
    #     color_two = darkest_color * 4
    #     color_two_str = f"{color_two}FF"
    #     color_three = darkest_color * 3
    #     color_three_str = f"{color_three}FF"
    #     return color_two_str, color_three_str

    def _main(self, original_color="", primary_color="", secondary_color=""):
        # DEFINE MODEL
        if(original_color == "Jinjonator"):
            self._jinjonator_model_textures()
            # darker_color, dark_color = self._progressively_darker(primary_color)
            # print(f"Light Color: {primary_color}")
            # print(f"Regular Color: {darker_color}")
            # print(f"Dark Color: {dark_color}")
            # self._texture_change_color("Dark_Texture", dark_color)
            # self._texture_change_color("Regular_Texture", darker_color)
            # self._texture_change_color("Light_Texture", primary_color)
            self._texture_change_color("Main_Texture", primary_color)
        else:
            self._jinjo_model_vertices(original_color)
            self._jinjo_textures()
            # MAIN COLOR
            self._vertex_change_color("Main_Vertex", primary_color)
            self._texture_change_color("Main_Texture", primary_color)
            # BELLY COLOR
            self._vertex_change_color("Belly", secondary_color)
        # CLOSE MM
        self._close_mm()