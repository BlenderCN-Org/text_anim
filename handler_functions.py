import bpy

from .update_functions import update_char_position, update_char_spacing, update_data_value
from .misc_functions import get_list_from_controller, change_object_index
from .evaluation_functions import evaluation_linear_pct

#main update for handler
def handler_update_main():
    for ob in bpy.context.scene.objects:
        if len(ob.text_anim)!=0:
            controller=ob
            
            #do something
            
            #get influences
            inf_list=evaluation_linear_pct(controller)
            
            #get object list
            obj_list=get_list_from_controller(controller)
            
            #do things
            loc_list=update_char_position(controller, obj_list, inf_list)
            update_char_spacing(controller, obj_list, loc_list, inf_list)
            update_data_value(controller, obj_list, inf_list)