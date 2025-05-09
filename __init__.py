import bpy


# from bpy.props import IntProperty # type: ignore

bpycon = bpy.context

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
    bl_label = "Test Panel B"
    bl_idname = "PT_Test_Panel_B"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Test Panel Tab"
    bl_parent_id = "PT_Test_Panel"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Sample Text", icon="MESH_CUBE")


class GizmoTest(bpy.types.Gizmo):
    bl_idname = "PT_Test_Gizmo"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        pass


class WM_OT_myop(bpy.types.Operator):
    bl_idname = "wm.myop"
    bl_label = "Add a Cube Dialog Box"

    text: bpy.props.StringProperty(name="Enter Text", default="")  # type: ignore # noqa: F811
    scale: bpy.props.FloatVectorProperty(name="scale Axis", default=(1, 1, 1))  # type: ignore

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.object
        obj.name = self.text # type: ignore
        obj.scale[0] = self.scale[0] # type: ignore
        obj.scale[1] = self.scale[1] # type: ignore
        obj.scale[2] = self.scale[2] # type: ignore

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class WM_OT_Bounds_Toggle(bpy.types.Operator):
    bl_idname = "wm.bound_toggle"
    bl_label = "Toogle Bound View of the Active Object"

    mode_options = ("EDIT", "OBJECT")

    boundbool: bpy.props.BoolProperty(name="Boundry Toogle", default=False)  # type: ignore

    def execute(self, context):
        bpy.context.active_object.show_bounds = self.boundbool
        bpy.ops.object.mode_set(mode="EDIT", toggle=True)

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class WM_BMesh_Test(bpy.types.Operator):
    bl_idname = "wm.bmesh_test"
    bl_label = "Trying out the bmesh module"

    def subdiv_edit_toogle(self, context):
        bpy.context.active_object.modifiers["Subdivision"]

    def execute(self, context):
        bpy.ops.object.shade_flat()


class WM_Smooth_Toogle(bpy.types.Operator):
    bl_idname = "wm.smooth_toogle"
    bl_label = "Not really intrested"

    def smooth_toogle(): # type: ignore
        modifier_stack_data = bpy.context.active_object.modifiers.keys()

        # print(modifier_stack_data)

        for i in range(len(modifier_stack_data)):
            if (
                bpy.context.active_object.modifiers[modifier_stack_data[i]].type
                == "SUBSURF"
            ):
                bpy.context.active_object.modifiers[
                    modifier_stack_data[i]
                ].show_in_editmode = False
                bpy.ops.object.shade_flat()

    def execute(self, context):
        self.smooth_toogle() # type: ignore

        return {"FINISHED"}


def menu_fucn(self, context):
    self.layout.operator(WM_OT_myop.bl_idname)


def new_bound_func(self, context):
    self.layout.operator(WM_OT_Bounds_Toggle.bl_idname)


def register():
    print("Hello World")
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(TestPanelB)
    bpy.utils.register_class(GizmoTest)
    bpy.utils.register_class(WM_OT_myop)
    bpy.utils.register_class(WM_OT_Bounds_Toggle)
    bpy.utils.register_class(WM_Smooth_Toogle)
    bpy.types.VIEW3D_MT_object.append(menu_fucn)
    bpy.types.VIEW3D_MT_view.append(new_bound_func)


def unregister():
    print("Goodbye World")
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(TestPanelB)
    bpy.utils.unregister_class(GizmoTest)
    bpy.utils.unregister_class(WM_OT_myop)
    bpy.utils.unregister_class(WM_OT_Bounds_Toggle)
    bpy.utils.unregister_class(WM_Smooth_Toogle)
    bpy.types.VIEW3D_MT_object.remove(menu_fucn)
    bpy.types.VIEW3D_MT_view.remove(new_bound_func)


if __name__ == "__main__":
    register()

    bpy.ops.wm.myop("INVOKE_DEFAULT") # type: ignore
