# pythoncad

* [viewstl]([http://example.com](https://www.viewstl.com/))
* [tinkercad](https://www.tinkercad.com/things/l1mNvxmSD0k-super-krunk-sango/edit)

To create a 3D CAD representation of a cylinder using Python, you can utilize the pyvista library. This library provides a simple interface to generate and visualize 3D geometries. Install the pyvista library by running pip install pyvista before running the following script:
```import pyvista as pv

# Define cylinder parameters
radius = 1.0  # Radius of the cylinder
height = 2.0  # Height of the cylinder
resolution = 100  # Number of points around the circumference of the cylinder

# Create a cylinder
cylinder = pv.Cylinder(radius=radius, height=height, resolution=resolution)

# Save the cylinder as a CAD file
output_file = 'cylinder.stl'
cylinder.save(output_file)

# Display the cylinder in a 3D plot
plotter = pv.Plotter()
plotter.add_mesh(cylinder, color='blue')
plotter.show()
```