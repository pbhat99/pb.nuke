#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Set IP
#
#----------------------------------------------------------------------------------------------------------

sn = nuke.selectedNode().name()
print (sn)
nuke.toNode('Viewer1').knob("input_process_node").setValue(sn)