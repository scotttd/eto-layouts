# Imports
import Rhino
import scriptcontext
import rhinoscriptsyntax as rs
import System
import Rhino.UI
import Eto.Drawing as drawing
import Eto.Forms as forms
import Eto
import webbrowser

# SampleEtoViewCaptureDialog dialog class
class SampleEtoViewCaptureDialog(forms.Dialog[bool]):
    
    
    # Dialogbox Class initializer
    def __init__(self):
        # Initialize dialog box
        self.Title = 'Sample Eto: Room Number'
        self.Padding = drawing.Padding(10)
        self.Resizable = True
        self.m_progress = 1
        
        # Create Label for the dailog
        self.m_label = forms.Label(Text = 'Enter the Room Number:')
        self.m_textbox = forms.TextBox(Text = None) 
        
        #Create a Calendar
        self.m_calendar = forms.Calendar()
        self.m_calendar.Mode = forms.CalendarMode.Single
        self.m_calendar.MaxDate = System.DateTime(2017,7,30)
        self.m_calendar.MinDate = System.DateTime(2017,7,1)
        self.m_calendar.SelectedDate = System.DateTime(2017,7,15)
        
        #Create a Checkbox
        self.m_checkbox = forms.CheckBox(Text = 'My Checkbox')
        self.m_checkbox.Checked = False
        
        #Create a ColorPicker Control
        self.m_colorpicker = forms.ColorPicker()
        defaultcolor = Eto.Drawing.Color.FromArgb(255, 0,0)
        self.m_colorpicker.Value = defaultcolor
        
        #Create Combobox
        self.m_combobox = forms.ComboBox()
        self.m_combobox.DataStore = ['first pick', 'second pick', 'third pick']
        self.m_combobox.SelectedIndex = 1

#Create DateTime Picker in Date mode
        self.m_datetimedate = forms.DateTimePicker()
        self.m_datetimedate.Mode = forms.DateTimePickerMode.Date
        self.m_datetimedate.MaxDate = System.DateTime(2017,7,30)
        self.m_datetimedate.MinDate = System.DateTime(2017,7,1)
        self.m_datetimedate.Value = System.DateTime(2017,7,15)

        #Create DateTime Picker in Time mode
        self.m_datetimetime = forms.DateTimePicker()
        self.m_datetimetime.Mode = forms.DateTimePickerMode.Time
        self.m_datetimetime.Value = System.DateTime.Now
        self.m_datetimetime.Value = System.DateTime(2017, 1, 1, 23, 43, 49, 500)

#Create Dropdown List
        self.m_dropdownlist = forms.DropDown()
        self.m_dropdownlist.DataStore = ['first pick', 'second pick', 'third pick']
        self.m_dropdownlist.SelectedIndex = 1
        
#Create Gridview sometimes called a ListView
        self.m_gridview = forms.GridView()
#        self.m_gridview.Size = drawing.Size(400, 400)
        self.m_gridview.ShowHeader = True
        self.m_gridview.DataStore = (['first pick', 'second pick', 'third pick', True],['second','fourth','last', False])

        column1 = forms.GridColumn()
        column1.HeaderText = 'Column 1'
        column1.Editable = True
        column1.DataCell = forms.TextBoxCell(0)
        self.m_gridview.Columns.Add(column1)

        column2 = forms.GridColumn()
        column2.HeaderText = 'Column 2'
        column2.Editable = True
        column2.DataCell = forms.TextBoxCell(1)
        self.m_gridview.Columns.Add(column2)

        column3 = forms.GridColumn()
        column3.HeaderText = 'Column 3'
        column3.Editable = True
        column3.DataCell = forms.TextBoxCell(2)
        self.m_gridview.Columns.Add(column3)
        
        column4 = forms.GridColumn()
        column4.HeaderText = 'Column 4'
        column4.Editable = True
        column4.DataCell = forms.CheckBoxCell(3)
        self.m_gridview.Columns.Add(column4)
        
# Create a group box
        self.m_groupbox = forms.GroupBox(Text = 'Groupbox')
        
        grouplayout = forms.DynamicLayout()
        
        label1 = forms.Label(Text = 'Enter Text:')
        textbox1 = forms.TextBox()

        checkbox1 = forms.CheckBox(Text = 'Start a new row')

        grouplayout.AddRow(label1, textbox1)
        grouplayout.AddRow(checkbox1)
        
        self.m_groupbox.Content = grouplayout
        
# Create an image view
        self.m_image_view = forms.ImageView()
        self.m_image_view.Size = drawing.Size(300, 200)
        self.m_image_view.Image = None
        
        # Capture the active view to a System.Drawing.Bitmap
        view = scriptcontext.doc.Views.ActiveView
        bitmap = view.CaptureToBitmap()
        
        # Convert the System.Drawing.Bitmap to an Eto.Drawing.Bitmap
        # which is required for an Eto image view control
        stream = System.IO.MemoryStream()
        format = System.Drawing.Imaging.ImageFormat.Png
        System.Drawing.Bitmap.Save(bitmap, stream, format)
        if stream.Length != 0:
          self.m_image_view.Image = drawing.Bitmap(stream)
        stream.Dispose()

        
#Create ListBox
        self.m_listbox = forms.ListBox()
        self.m_listbox.DataStore = ['first pick', 'second pick', 'third pick']
        self.m_listbox.SelectedIndex = 1
        
# Create LinkButton
        self.m_linkbutton = forms.LinkButton(Text = 'For more details...')
        self.m_linkbutton.Click += self.OnLinkButtonClick
        
# Create Numeric Up Down
        self.m_numeric_updown = forms.NumericUpDown()
        self.m_numeric_updown.DecimalPlaces = 2
        self.m_numeric_updown.Increment = 0.01
        self.m_numeric_updown.MaxValue = 10.0
        self.m_numeric_updown.MinValue = 1.0
        self.m_numeric_updown.Value = 5.0
        
# Create Password Box
        self.m_password = forms.PasswordBox()
        self.m_password.MaxLength = 7
        
# Create Progress Bar
        self.m_progressbar = forms.ProgressBar()
        self.m_progressbar.MinValue = 0
        self.m_progressbar.MaxValue = 10
        
        self.m_gobutton = forms.Button(Text = "Click for more progress!")
        self.m_gobutton.Click += self.OnGoButtonClick

# Create Radio Button List Control
        self.m_radiobuttonlist = forms.RadioButtonList()
        self.m_radiobuttonlist.DataStore = ['first pick', 'second pick', 'third pick']
        self.m_radiobuttonlist.Orientation = forms.Orientation.Vertical
        self.m_radiobuttonlist.SelectedIndex = 1
        
# Create Rich Text Edit Box
        self.m_richtextarea = forms.RichTextArea()
        self.m_richtextarea.Size = drawing.Size(200, 200)
        
                
# Create Search Box
        self.m_searchbox = forms.SearchBox()
        
# Create a slider
        self.m_slider = forms.Slider()
        self.m_slider.MaxValue = 10
        self.m_slider.MinValue = 0
        self.m_slider.Value = 3
        
# Create Spinner
        self.m_spinner = forms.Spinner()
        self.m_spinner.Enabled = True
        
# Create Text Area Box
        self.m_textarea = forms.TextArea()
        self.m_textarea.Size = drawing.Size(200, 200)
        

        # Create the default button
        self.DefaultButton = forms.Button(Text = 'OK')
        self.DefaultButton.Click += self.OnOKButtonClick

        # Create the abort button
        self.AbortButton = forms.Button(Text = 'Cancel')
        self.AbortButton.Click += self.OnCloseButtonClick

        # Create a table layout and add all the controls
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(5, 5)
        layout.AddRow(self.m_groupbox)
        layout.AddRow(None) # spacer
        layout.AddRow(self.DefaultButton, self.AbortButton)


        # Set the dialog content
        self.Content = layout

    # Start of the class functions

    # Get the value of the textbox
    def GetText(self):
        return self.m_textbox.Text
        
        
    # Linkbutton click handler
    def OnLinkButtonClick(self, sender, e):
        webbrowser.open("http://rhino3d.com")

    # GoButton button click handler
    def OnGoButtonClick(self, sender, e):
        self.m_progress = self.m_progress + 1
        if self.m_progress > 10:
            self.m_progress = 10
        self.m_progressbar.Value = self.m_progress

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
    rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)
    if (rc):
        print dialog.GetText()



##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if __name__ == "__main__":
    SampleEtoRoomNumberDialog()