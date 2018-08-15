# Link: http://wiki.theprovingground.org/revit-api-py-setup
# import libraries and reference the RevitAPI and RevitAPIUI
import clr
import math
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *

# set the active Revit application and document
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document

#define a transaction variable and describe the transaction
t= Transaction(doc,'This is my new transaction')

#start a transaction in the Revit database
t.Start()

#perform some action here...

#commit the transaction to the Revit database
t.Commit()

#close the script window
__window__.Close()
