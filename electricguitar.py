import pyvista as pv

# Define guitar body parameters
body_length = 40.0
body_width = 14.0
body_thickness = 4.0
neck_length = 30.0
neck_width = 3.0
neck_thickness = 1.0

# Create guitar body as a combination of multiple geometries
body_mesh = pv.Cylinder(radius=body_width / 2, height=body_thickness, resolution=100)
body_mesh.translate([(body_length - body_thickness) / 2, 0, body_thickness / 2])
body_mesh.rotate_z(90)

# Create guitar neck as a cylinder
neck_mesh = pv.Cylinder(radius=neck_width / 2, height=neck_length, resolution=100)
neck_mesh.translate([neck_length / 2, 0, neck_thickness / 2])

# Combine body and neck meshes
guitar_mesh = body_mesh + neck_mesh

# Save the guitar body as a CAD file
output_file = 'electric_guitar.stl'
guitar_mesh.save(output_file)

# Display the guitar body in a 3D plot
plotter = pv.Plotter()
plotter.add_mesh(guitar_mesh, color='brown')
plotter.show()
