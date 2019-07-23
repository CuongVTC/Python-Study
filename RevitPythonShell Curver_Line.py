import clr
import math
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *

doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application

t = Transaction(doc, 'Create Line')
t.Start()
#Creat a sketch plane
origin = XYZ.Zero
normal = XYZ.BasisZ

#plane = app.Create.NewPlane(normal,origin)
#skplane = doc.FamilyCreate.NewSketchPlane(plane)

# Create line vertices
lnStart = XYZ(0,0,0)
lnEnd = XYZ(20,20,0)

# Create NewLine()
#line = app.Create.NewLine(lnStart, lnEnd, True)
line = Line.CreateBound(lnStart,lnEnd)

# Create NewModelCurve()
#crv = doc.FamilyCreate.NewModelCurve(line, skplane)

t.Commit()

__window__.Close()
