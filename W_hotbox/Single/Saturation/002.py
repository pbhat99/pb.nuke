#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: +0.1
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('saturation').setValue(i.knob('saturation').value()+0.1)