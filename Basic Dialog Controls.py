################################################################################
# SampleEtoDialog.py
# MIT License - Copyright (c) 2017 Robert McNeel & Associates.
# See License.md in the root of this repository for details.
################################################################################
import clr
clr.AddReference("Eto")
clr.AddReference("Rhino.UI")

import rhinoscriptsyntax as rs
import sys

from Rhino.UI import *
from Eto.Forms import *
from Eto.Drawing import *

def get_room_number():
    dia = Dialog[bool]()
    dia.Title = "Sample Eto Dialog"
    dia.Padding = Padding(5)
    dia.Resizable = False
    
    cancelButton = Button(Text = "Cancel")
    def cancelButton_Click (sender, e):
	    try:
		    dia.Close(False)
	    except:
		    print "Unexpected error:", sys.exc_info()[0]
		    pass # so we don't bring down rhino if there's a bug in the script
    cancelButton.Click += cancelButton_Click;
    
    okButton = Button(Text = "OK")
    def okButton_Click (sender, e):
	    try:
		    dia.Close(True)
	    except:
		    print "Unexpected error:", sys.exc_info()[0]
		    pass # so we don't bring down rhino if there's a bug in the script
    okButton.Click += okButton_Click
    
    # set default buttons when user presses enter or escape anywhere on the form
    dia.DefaultButton = okButton
    dia.AbortButton = cancelButton

    label = Label()
    label.Text = "Enter your text here:"

    textbox = TextBox();

    layout = DynamicLayout()
    #layout.DefaultPadding = Padding(5)
    layout.DefaultSpacing = Size(5,2)
    layout.AddRow(label, textbox)
    layout.AddRow(None, okButton, cancelButton)

    dia.Content = layout

    dia.ShowModal(RhinoEtoApp.MainWindow)


def room_number():
    number_point = rs.GetPoint("Pick a point for Room Number:")
    room_number_result = get_room_number()
    if room_number_result:
        rs.AddTextDot(textbox.text, number_point)

##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    room_number()