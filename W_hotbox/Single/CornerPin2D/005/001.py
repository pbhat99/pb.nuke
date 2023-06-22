#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Delete Key
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('to1').removeKey()
    i.knob('to2').removeKey()
    i.knob('to3').removeKey()
    i.knob('to4').removeKey()