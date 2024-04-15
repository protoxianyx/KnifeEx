import bpy
import bpy.ops as bop
from bpy.props import IntProperty, FloatProperty # type: ignore
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


class ModalOperator(bpy.types.Operator):
    """Move an object with the mouse, example"""

    bl_idname = "object.modal_operator"
    bl_label = "Simple Modal Operator"

    first_mouse_x: IntProperty() # type: ignore
    first_value: FloatProperty() # type: ignore

    def modal(self, context, event):
        if event.type == "MOUSEMOVE":
            delta = self.first_mouse_x - event.mouse_x
            context.object.location.x = self.first_value + delta * 0.01

        elif event.type == "LEFTMOUSE":
            return {"FINISHED"}

        elif event.type in {"RIGHTMOUSE", "ESC"}:
            context.object.location.x = self.first_value
            return {"CANCELLED"}

        return {"RUNNING_MODAL"}

    def invoke(self, context, event):
        if context.object:
            self.first_mouse_x = event.mouse_x
            self.first_value = context.object.location.x

            context.window_manager.modal_handler_add(self)
            return {"RUNNING_MODAL"}
        else:
            self.report({"WARNING"}, "No active object, could not finish")
            return {"CANCELLED"}


def menu_func(self, context):
    self.layout.operator(ModalOperator.bl_idname, text=ModalOperator.bl_label)


def register():
    bpy.utils.register_class(ModalOperator)
    print("Hello World")


key_config = bpy.context.window_manager.keyconfigs.addon
if key_config:
    key_map = key_config.keymaps.new(name="3D View", space_type="VIEW_3D")
    key_entry = key_map.keymap_items.new(
        "object.modal_operator",
        type="Q",
        value="PRESS",
        shift=True,
    )
    mode_keymap = (key_map, key_entry)


def unregister():
    print("Goodbye World")


if __name__ == "__main__":
    register()
