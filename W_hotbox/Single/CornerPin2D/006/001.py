#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Delete Key
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('from1').removeKey()
    i.knob('from2').removeKey()
    i.knob('from3').removeKey()
    i.knob('from4').removeKey()