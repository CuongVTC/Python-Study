# IronPython Pad. Write code snippets here and F5 to run.
import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application
 
t = Transaction(doc, 'Create extrusion.')
 
t.Start()
#Define XYZ to define plane corners
try:

    p1 = XYZ(0,0,0)
    p2 = XYZ(1,0,0)
    p3 = XYZ(0,1,1)
    print "created points"
    #Define plane with curves
    #old code:  pline1 = app.Create.NewLine(p1, p2, True)
    #new code:  app.Create.NewLIne has been replaced with:
    pline1 = Line.CreateBound(p1, p2)
   
    #old code:  pline2 = app.Create.NewLine(p2, p3, True)
    #new code:  app.Create.NewLIne has been replaced with:
    pline2 = Line.CreateBound(p2, p3)
    print "created lines"
 
    #create and append a new CurveArray() with plane curves
    parray = CurveArray()
    parray.Append(pline1)
    parray.Append(pline2)
    print "created curvearray"
 
    #create a plane using NewPlane()
    plane = app.Create.NewPlane(parray)
    print "created plane"
 
    #create a sketch plane using NewSketchPlane()
    #old code:  skplane = doc.FamilyCreate.NewSketchPlane(plane)
    #new code:  doc.FamilyCreate.NewSKetchPlane has been replaced with:
    skplane = SketchPlane.Create(doc, plane)
    print "created sketchplane"
except:
    print "sorry error"
t.Commit()
 
#__window__.Close()