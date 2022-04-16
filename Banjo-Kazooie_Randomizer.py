'''
Created on Nov 5, 2021

@author: Cyrus
'''

####################
### FILE IMPORTS ###
####################

from User_GUI import User_GUI_Class

#################
### VARIABLES ###
#################

BK_RANDO_VERSION = "2.0.20220416"

############
### MAIN ###
############

if __name__ == '__main__':
    user_app = User_GUI_Class(BK_RANDO_VERSION)
    user_app._main()
