import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *

app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document

t = Transaction(doc, 'create a single reference point')

t.Start()

for i in range(0,30):
    for j in range(0,30):
        x = i*10
        y = j*10
        #change z position acording to consine and sine formula
        z = (10*math.cos(i)) + (10*math.sin(j))
        
        myXYZ = XYZ(x,y,z)
        # use ZYZ to define a refernence point
        refPoint = doc.FamilyCreate.NewReferncePoint(myXYZ)

t.Commit()

__window__.Close()
