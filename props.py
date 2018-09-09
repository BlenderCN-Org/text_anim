import bpy

from .update_functions import update_fct_main

class TextAnimFontPropsColl(bpy.types.PropertyGroup):
    '''name = StringProperty() '''
    
    controller = bpy.props.StringProperty(default="")
    index = bpy.props.IntProperty()
    original_location = bpy.props.FloatVectorProperty(name="Original Location")
    original_spacing = bpy.props.FloatProperty(name="Original Spacing", default=0.0)
    
class TextAnimEmptyPropsColl(bpy.types.PropertyGroup):
    '''name = StringProperty() '''
    
    body = bpy.props.StringProperty()
    
    ### animation ###
    
    #range
    start_pct = bpy.props.IntProperty(name="Start", default=0, min=0, max=100, update=update_fct_main)
    end_pct = bpy.props.IntProperty(name="End", default=100, min=0, max=100, update=update_fct_main)
    
    #location
    location = bpy.props.FloatVectorProperty(name="Location", update=update_fct_main)
    
    #spacing
    spacing = bpy.props.FloatProperty(name="Spacing", default=0, update=update_fct_main)
    spacing_offset = bpy.props.BoolProperty(name="Offset", default=False, update=update_fct_main)
    spacing_type = bpy.props.EnumProperty(items= (('LEFT', 'Left', 'From left'),    
                                                 ('RIGHT', 'Right', 'From Right')),
                                                 name = "Type", default='LEFT', update=update_fct_main)
                                                 
    #node data
    custom_node_data_start = bpy.props.FloatProperty(name="Node Data Start", default=0, update=update_fct_main)
    custom_node_data_end = bpy.props.FloatProperty(name="Node Data End", default=1, update=update_fct_main)