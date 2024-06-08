import bpy

modifier_stack_data = bpy.context.active_object.modifiers.keys()

print(modifier_stack_data)


def smooth_toogle():
    for i in range(len(modifier_stack_data)):
        if(bpy.context.active_object.modifiers[modifier_stack_data[i]].type == 'SUBSURF'):
            bpy.context.active_object.modifiers[modifier_stack_data[i]].show_in_editmode = False
            bpy.ops.mesh.faces_shade_flat()


