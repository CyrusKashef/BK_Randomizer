'''
Created on Sep 4, 2021

@author: Cyrus
'''

###################
### FILE IMPORT ###
###################

from .Generic_Models import Model

######################
### BK MODEL CLASS ###
######################

class BK_Model(Model):
    '''Banjo-Kazooie model class based on the generic model class'''
    def _bk_model1(self, banjo_color, kazooie_color):
        '''Runs the process of editing the low poly Banjo-Kazooie model'''
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