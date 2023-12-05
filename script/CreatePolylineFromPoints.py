output.Points = inputs[0].Points
numPoints = len(output.Points)

pointIds = vtk.vtkIdList()
pointIds.SetNumberOfIds(numPoints)
for i in range(numPoints):
    pointIds.SetId(i, i)

output.Allocate(1, 1)
output.InsertNextCell(vtk.VTK_POLY_LINE, pointIds)