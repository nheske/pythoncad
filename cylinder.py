import pyvista as pv

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
