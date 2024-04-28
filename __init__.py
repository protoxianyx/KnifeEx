import bpy
from bpy.props import IntProperty, FloatProperty  # type: ignore
import bmesh

bl_info = {
    "name": "Knife EX",
    "author": "Xianyx",
    "version": (0, 1),
    "blender": (4, 1, 0),
    "location": "View3D > Add Mesh",
    "description": "Extends the Knife Tool functionality",
    "category": "Mesh Editing",
}



class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_Test_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Test Panel Tab"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Sample Text", icon="cube")


def register():
    print("Hello World")
    bpy.utils.register_class(TestPanel)


def unregister():
    print("Goodbye World")
    bpy.utils.unregister_class(TestPanel)


if __name__ == "__main__":
    register()
