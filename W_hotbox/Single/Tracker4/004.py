#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Set Ref
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('reference_frame').setValue(nuke.frame())
