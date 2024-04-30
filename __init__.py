
import bpy
# from bpy.props import IntProperty # type: ignore



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
        row.label(text="Sample Text", icon="MESH_CUBE")
        row = layout.row()
        row.operator("mesh.primitive_cube_add")
        row.operator("transform.rotate")
        row = layout.row()
        row.operator("mesh.primitive_torus_add")


class TestPanelB(bpy.types.Panel):
    bl_label = 'Test Panel B'
    bl_idname = 'PT_Test_Panel_B'
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Test Panel Tab'
    bl_parent_id = 'PT_Test_Panel'
    bl_options={
        'DEFAULT_CLOSED'
    }

    def draw(self, context):
        layout = self.layout        

        row = layout.row()
        row.label(text="Sample Text", icon="MESH_CUBE")

class GizmoTest(bpy.types.Gizmo):
    bl_idname="PT_Test_Gizmo"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        pass
    
class WM_OT_myop(bpy.types.Operator):
    bl_idname="wm.myop"
    bl_label="Add a Cube Dialog Box"
    
    text = bpy.props.StringProperty(name= "Enter Text", default= "")  # noqa: F811
    number_scale = bpy.props.FloatProperty(name= "scale Z Axis", default= 1)
    
    
    def execute(self, context):
        
        
        t = self.text
        
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.object
        obj.name = t
        
        return {'FINISHED'}
    
    def invoke(self, context, event):
        
        return context.window_manager.invoke_props_dialog(self)


def register():
    print("Hello World")
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(TestPanelB)
    bpy.utils.register_class(GizmoTest)
    bpy.utils.register_class(WM_OT_myop)


def unregister():
    print("Goodbye World")
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(TestPanelB)
    bpy.utils.unregister_class(GizmoTest)
    bpy.utils.unregister_class(WM_OT_myop)


if __name__ == "__main__":
    register()
    
    bpy.ops.wm.myop('INVOKE_DEFAULT')
