import pyvista as pv

# Define guitar body parameters
body_length = 40.0
body_width = 14.0
body_thickness = 4.0

# Define bounds for the guitar body
x_min, x_max = 0, body_length
y_min, y_max = -body_width/2, body_width/2
z_min, z_max = 0, body_thickness

# Create a guitar body mesh
body_mesh = pv.Box(bounds=(x_min, x_max, y_min, y_max, z_min, z_max))

# Save the guitar body as a CAD file
output_file = 'electric_guitar.stl'
body_mesh.save(output_file)

# Display the guitar body in a 3D plot
plotter = pv.Plotter()
plotter.add_mesh(body_mesh, color='brown')
plotter.show()
