bl_info = {
    "name" : "Overlay Un/Lock Camera",
    "author" : "Claromes",
    "description" : "Fast access to lock/unlock the Camera to View",
    "blender" : (3, 2, 2),
    "version" : (0, 0, 2),
    "location" : "View3D",
    "category" : "3D View",
    "doc_url": "https://github.com/claromes/space_view3d_un_lock_camera",
    "tracker_url": "https://github.com/claromes/space_view3d_un_lock_camera/issues"
}

import bpy
from . lock_op import LOCK_OT_Camera_View_On_Op, LOCK_OT_Camera_View_Off_Op, LOCK_OT_Dialog
from . lock_pnl import LOCK_PT_Panel

classes = (
    LOCK_OT_Camera_View_On_Op,
    LOCK_OT_Camera_View_Off_Op,
    LOCK_OT_Dialog,
    LOCK_PT_Panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)