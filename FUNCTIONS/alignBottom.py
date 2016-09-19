import rhinoscriptsyntax as rs

objs= rs.GetObjects('target',0,True, True)

objs2= rs.GetObjects('conformers',0,True, True)

bbox= rs.BoundingBox(objs)

for obj in objs2:
    bbox2= rs.BoundingBox(obj)
    rs.MoveObject(obj, rs.VectorCreate([0,0,bbox[0][2]],[0,0,bbox2[0][2]]))
