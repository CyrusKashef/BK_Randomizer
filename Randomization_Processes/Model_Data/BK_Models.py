'''
Created on Sep 4, 2021

@author: Cyrus
'''

from Generic_Models import Model

class BK_Model(Model):
    def _bk_model1(self, banjo_color, kazooie_color):
        model_dict1 = {}
        model_dict1["Banjo"] = {}
        model_dict1["Banjo"]["Model_List"] = [(0x10B90,0x13050),(0x14A40,0x161F0),(0x194C0,0x1AE90),(0x1C6B0,0x1D540),(0x1FF90,0x226B0)]
        model_dict1["Banjo"]["Color_Check"] = lambda red, green, blue, alpha: (red > 0x25) and (red > (2.2*green)) and (red < (3*green)) and (red > (10*blue)) and (alpha == 0xFF)
        model_dict1["Kazooie"] = {}
        model_dict1["Kazooie"]["Model_List"] = [(0x16760,0x16CB0),(0x16CE0,0x16D00),(0x16D70,0x16DB0),(0x16DE0,0x179F0),(0x19050,0x19480),(0x1D560,0x1E180),(0x22E10,0x22E70)]
        model_dict1["Kazooie"]["Color_Check"] = lambda red, green, blue, alpha: (red > 0x50) and (red > (2.6*green)) and (blue < 0x5) and (alpha == 0xFF)
        model_dict1["Kazooie"]["Texture"] = {}
        model_dict1["Kazooie"]["Texture"]["Wing"] = {}
        model_dict1["Kazooie"]["Texture"]["Wing"]["Map"] = [0x17A0,0x17AA,0x17AC,0x17B0,0x17B4,0x17B6,0x17B8,0x17BA,0x17BC,0x17BE]
        model_dict1["Banjo"]["New_Color"] = banjo_color
        model_dict1["Kazooie"]["New_Color"] = kazooie_color
        self._main(model_dict1, custom_name=f"Banjo_{model_dict1['Banjo']['New_Color']}_Kazooie_{model_dict1['Kazooie']['New_Color']}")

    def _bk_model2(self, banjo_color, kazooie_color):
        model_dict2 = {}
        model_dict2["Banjo"] = {}
        model_dict2["Banjo"]["Model_List"] = [(0xB410,0xC9F0),(0xE210,0xF0B0),(0x11A90,0x11EA0),(0x13500,0x13F70),(0x14120,0x142B0)]
        model_dict2["Banjo"]["Color_Check"] = lambda red, green, blue, alpha: (red > 0x25) and (red > (2.2*green)) and (red < (3*green)) and (red > (10*blue)) and (alpha == 0xFF)
        model_dict2["Kazooie"] = {}
        model_dict2["Kazooie"]["Model_List"] = [(0xF0C0, 0xF270),(0xF570,0xF6C0),(0xF840,0xF8E0),(0x11490,0x118C0)]
        model_dict2["Kazooie"]["Color_Check"] = lambda red, green, blue, alpha: (red > 0x50) and (red > (2.6*green)) and (blue < 0x5) and (alpha == 0xFF)
        model_dict2["Kazooie"]["Texture"] = {}
        model_dict2["Kazooie"]["Texture"]["Wing"] = {}
        model_dict2["Kazooie"]["Texture"]["Wing"]["Map"] = [0x1570,0x157C,0x1582,0x1586,0x1588,0x158A]
        model_dict2["Banjo"]["New_Color"] = banjo_color
        model_dict2["Kazooie"]["New_Color"] = kazooie_color
        self._main(model_dict2, custom_name=f"Banjo_{model_dict2['Banjo']['New_Color']}_Kazooie_{model_dict2['Kazooie']['New_Color']}")

if __name__ == '__main__':
    # file_dir = r"C:\\Users\\Cyrus\\Desktop\\N64\\ROMs\\GEDecompressor_Files\\test\\19D530\\"
    # address = "19D530"
    # color_list = ["Black", "Navy", "Blue", "Swamp", "Avery", "Cosmos",
    #               "Green", "Emerald", "Teal", "Rust", "Purple", "Violet",
    #               "Shit", "Gray", "Lavendar", "Lime2", "Lime", "Turquiose",
    #               "Red", "Pink", "Magenta", "Brown", "Amber", "Magenta2",
    #               "Yellow", "Gold", "White"]
    # len_color_list = len(color_list)
    # for color_index in range(len_color_list):
    #     bk_model1 = Model(file_dir, address)
    #     bk_model1._bk_model1(color_list[color_index], color_list[-1-color_index])
    
    file_dir = r"C:\\Users\\Cyrus\\Desktop\\N64\\ROMs\\GEDecompressor_Files\\test\\19D530\\"
    address = "19D530"
    bk_model1 = BK_Model(file_dir, address)
    bk_model1._bk_model1("Black", "White")
    
    file_dir = r"C:\\Users\\Cyrus\\Desktop\\N64\\ROMs\\GEDecompressor_Files\\test\\197E38\\"
    address = "197E38"
    bk_model2 = BK_Model(file_dir, address)
    bk_model2._bk_model2("Black", "White")