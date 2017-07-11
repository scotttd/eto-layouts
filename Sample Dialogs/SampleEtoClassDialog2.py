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
    
    # Class initializer
    def __init__(self):
        # Initialize dialog box
        self.Title = 'SampleEtoViewCaptureDialog'
        self.Padding = Padding(10)
        
        cancelButton = Button(Text = "Cancel")
        def cancelButton_Click (sender, e):
	        try:
	    	    self.Close(False)
	        except:
	    	    print "Unexpected error:", sys.exc_info()[0]
	    	    pass # so we don't bring down rhino if there's a bug in the script
        cancelButton.Click += cancelButton_Click;
    
        okButton = Button(Text = "OK")
        def okButton_Click (sender, e):
	        try:
		        self.Close(True)
	        except:
		        print "Unexpected error:", sys.exc_info()[0]
		        pass # so we don't bring down rhino if there's a bug in the script
        okButton.Click += okButton_Click
    
        # set default buttons when user presses enter or escape anywhere on the form
        self.DefaultButton = okButton
        self.AbortButton = cancelButton
        
        m_room_number = TextBox() 


        # Create a table layout and add all the controls
        layout = DynamicLayout()
        layout.Spacing = Size(5, 5)
        layout.AddRow(Label(Text="Enter Room Number"), m_room_number)
        layout.Rows.Add(None) # spacer
        layout.Rows.Add(self.CreateButtons())

        # Set the dialog content
        self.Content = layout


    # Close button click handler
    def OnCloseButtonClick(self, sender, e):
        rc = self.m_image_view.Image is not None
        if rc:
            self.Close(True)
        else:
            self.Close(False)

    # Create the dialog buttons
    def CreateButtons(self):

        # Create the abort button
        self.AbortButton = Button(Text = 'Close')
        self.AbortButton.Click += self.OnCloseButtonClick
        # Create button layout
        button_layout = TableLayout()
        button_layout.Spacing = Size(5, 5)
        if Rhino.Runtime.HostUtils.RunningOnWindows:
            button_layout.Rows.Add(TableRow(None, self.DefaultButton, self.AbortButton))
        else:
            button_layout.Rows.Add(TableRow(None, self.AbortButton, self.DefaultButton))
        return button_layout
        
    # Returns the captured image
    def Image(self):
        return self.m_image_view.Image

def TestSampleEtoViewCaptureDialog():
    dialog = SampleEtoViewCaptureDialog();
    rc = dialog.ShowModal(RhinoEtoApp.MainWindow)
    if (rc):
        print 'have image'
            
if __name__ == "__main__":
    TestSampleEtoViewCaptureDialog()