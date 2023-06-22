#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: inf Fix
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('expr0').setValue('isinf (r) ? 0:r')
    i.knob('expr1').setValue('isinf (r) ? 0:g')
    i.knob('expr2').setValue('isinf (r) ? 0:b')
    i.knob('expr3').setValue('isinf (b) ? 0:a')
    i.knob('label').setValue('inf fixed')