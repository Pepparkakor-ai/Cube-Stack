import bpy

generate  = bpy.data.texts["generate_cubes.py"].as_module()

generate.clean()
generate.create(50)

cube_list = []
for c in bpy.data.objects:
    if c.type=="MECH":
        cube_list.append(c)

def measure_cube(cube):
    return cube.dimensions.z

cube_list.sort(key=measure_cube)

start= -20.0
for c in cube_list:
    start += c.dimensions.x
    c.location.x = start
