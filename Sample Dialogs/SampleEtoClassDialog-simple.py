# References
import clr
clr.AddReference("Eto")
clr.AddReference("Rhino.UI")

# Imports from
from Rhino.UI import *
from Eto.Forms import *
from Eto.Drawing import *

# Imports
import Rhino
import scriptcontext
import System

# SampleEtoViewCaptureDialog dialog class
class SampleEtoViewCaptureDialog(Dialog[bool]):
    
    # Dialogbox Class initializer
    def __init__(self):
        # Initialize dialog box
        self.Title = 'Sample Eto: Room Number'
        self.Padding = Padding(10)
        self.Resizable = False
        
        # Create controls for the dailog
        self.m_label = Label(Text = 'Enter the Room Number:')
        self.m_textbox = TextBox(Text = None) 
        
        # Create the default button
        self.DefaultButton = Button(Text = 'OK')
        self.DefaultButton.Click += self.OnOKButtonClick

        # Create the abort button
        self.AbortButton = Button(Text = 'Cancel')
        self.AbortButton.Click += self.OnCloseButtonClick

        # Create a table layout and add all the controls
        layout = DynamicLayout()
        layout.Spacing = Size(5, 5)
        layout.AddRow(self.m_label, self.m_textbox)
        layout.AddRow(None) # spacer
        layout.AddRow(None, self.DefaultButton, self.AbortButton, None)


        # Set the dialog content
        self.Content = layout

    # Start of the class functions

    # Get the value of the textbox
    def GetText(self):
        return self.m_textbox.Text

    # Close button click handler
    def OnCloseButtonClick(self, sender, e):
        self.m_textbox.Text = ""
        self.Close(False)

    # Close button click handler
    def OnOKButtonClick(self, sender, e):
        if self.m_textbox.Text == "":
            self.Close(False)
        else:
            self.Close(True)
            
    ## End of Dialog Class ##

# The script that will be using the dialog.
def SampleEtoRoomNumberDialog():
    dialog = SampleEtoViewCaptureDialog();
    rc = dialog.ShowModal(RhinoEtoApp.MainWindow)
    if (rc):
        print dialog.GetText()



##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if __name__ == "__main__":
    SampleEtoRoomNumberDialog()