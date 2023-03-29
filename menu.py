#Prasannakumar T Bhat
#This is the main menu.py file to load into nuke

#Let me confirm loading of this file in nuke terminal
nuke.tprint('Loading Custom Tools by Prasannakumar T Bhat')

#importing important modules
import os
import nuke

import W_hotbox
import W_hotboxManager
import KnobScripter


#my knobdefaults & snippets
import pbKnobDefaults


#Import all nodes from another script
#nuke.loadToolset("/home/user/Templates/script.nk")

nuke.menu("Nodes").addCommand('Other/Comma','import comma ; comma.makeComma()',',',icon='Comma.png',index=6)

from pbSnippets import *
nuke.menu('Nuke').addCommand('-{ pb }-/GUI Disable','disableGUI()','shift+d')
nuke.menu('Nodes').addCommand('Other/StickyNote','pasteNote()','alt+n')
nuke.menu("Nuke").addCommand("Edit/Node/Label", "nLabel()","n")

#framehold to current frame as default
nuke.menu('Nodes').addCommand( "Time/FrameHold", "nuke.createNode('FrameHold')['first_frame'].setValue( nuke.frame() )", icon='FrameHold.png')




#confirm full file loaded properly
nuke.tprint('pb tools Loaded!')
