import bpy

activeobj = bpy.context.active_object

active_modifier_stack = activeobj.modifiers.keys()

for i in range(len(active_modifier_stack)):
    activeobj.modifiers.remove(activeobj.modifiers[active_modifier_stack[i]])

modifierstack = ("BEVEL", "SUBSURF", "ARRAY")

for i in range(len(modifierstack)):
     bpy.context.active_object.modifiers.new(modifierstack[i], modifierstack[i])