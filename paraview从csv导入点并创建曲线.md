cfd-online讨论原帖

https://www.cfd-online.com/Forums/paraview/223851-plot-over-curved-lines.html



1. Create a .csv file of the XYZ points that defines the curve



2. Import .csv file into Paraview



3. Apply Filter "Table to Points" to the .csv file



4. Create a polyline of the points (got this from another post awhile back but I don't have link to it): Apply Filter "Programmable Filter".



Code:

```python
output.Points = inputs[0].Points
numPoints = len(output.Points)

pointIds = vtk.vtkIdList()
pointIds.SetNumberOfIds(numPoints)
for i in range(numPoints):
    pointIds.SetId(i, i)

output.Allocate(1, 1)
output.InsertNextCell(vtk.VTK_POLY_LINE, pointIds)
```

5. Then use Filter "Slice Along Polyline" using the newly created polyline from step 4.

