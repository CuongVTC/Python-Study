import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *

doc = __revit__.UIApplication.Document
app = __revit__.Application

t = Transaction(doc, 'Create Line')

t.Start()

# Định nghĩa điểm gốc và vector từ tọa độ XYZ
origin = XYZ.Zero
normal = XYZ.BasisZ

# Định nghĩa mặt phẳng mới bằng điểm gốc và vector
plane = app.Create.NewPlane(normal, origin)

# Định nghĩa một mặt mới từ một mặt phẳng khác
skplane = doc.FamilyCreate.NewSketchPlane(plane)

t.Commit()

__window__.Close()
