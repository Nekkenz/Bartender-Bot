from GUI import TKGUI as TK
import json
import os
# For Testing
#from Util import DrinkList as DL
#from Util import WriteToJSON as WJ

#######################################################
# Import new json files containing drink recipes here #
#######################################################

dirname = os.path.dirname(__file__)
FilePath = os.path.join(dirname, "Drinks/Drinks.json")

#######################################################

TK.createApp(FilePath)
