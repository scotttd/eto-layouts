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
        self.m_groupbox.Padding = drawing.Padding(5)

        
        grouplayout = forms.DynamicLayout()
        grouplayout.Spacing = drawing.Size(3, 3)
        
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
        self.m_image_view.Image = Rhino.UI.EtoExtensions.ToEto(view.CaptureToBitmap())

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
        self.m_slider.Orientation = forms.Orientation.Vertical
        
# Create Spinner
        self.m_spinner = forms.Spinner()
        self.m_spinner.Enabled = True
        
# Create Text Area Box
        self.m_textarea = forms.TextArea()
        self.m_textarea.Size = drawing.Size(200, 200)

# Create TreeGridView
        self.m_treegridview = forms.TreeGridView()
        self.m_treegridview.Size = drawing.Size(200, 200)

        column1 = forms.GridColumn()
        column1.HeaderText = 'Tree'
        column1.Editable = True
        column1.DataCell = forms.TextBoxCell(0)
        self.m_treegridview.Columns.Add(column1)
        
        column2 = forms.GridColumn()
        column2.HeaderText = 'Prop 2'
        column2.Editable = True
        column2.DataCell = forms.TextBoxCell(1)
        self.m_treegridview.Columns.Add(column2)

        column3 = forms.GridColumn()
        column3.HeaderText = 'Prop 3'
        column3.Editable = True
        column3.DataCell = forms.TextBoxCell(2)
        self.m_treegridview.Columns.Add(column3)
        
        treecollection = forms.TreeGridItemCollection()
        item1 = forms.TreeGridItem(Values=('node1', 'node1b', 'node1c'))
        item1.Expanded = True
        item1.Children.Add(forms.TreeGridItem(Values=('node2', 'node2b', 'node2c')))
        item1.Children.Add(forms.TreeGridItem(Values=('node3', 'node3b', 'node3c')))
        treecollection.Add(item1)
        item2 = forms.TreeGridItem(Values=('node11', 'node11b', 'node11c'))
        treecollection.Add(item2)
        self.m_treegridview.DataStore = treecollection

# Create a WebView
        self.m_webview = forms.WebView()
        self.m_webview.Size = drawing.Size(300, 400)
        self.m_webview.Url = System.Uri('http://developer.rhino3d.com/guides/rhinopython/')

        # Create the default button
        self.DefaultButton = forms.Button(Text = 'OK')
        self.DefaultButton.Click += self.OnOKButtonClick

        # Create the abort button
        self.AbortButton = forms.Button(Text = 'Cancel')
        self.AbortButton.Click += self.OnCloseButtonClick
        

##############################################################################
# The Dynamic Layout Example
##############################################################################
        # Create a layout of ok and cancel buttons
        buttonslayout = forms.DynamicLayout()
        buttonslayout.Spacing = drawing.Size(5,5)
        buttonslayout.AddRow(None,self.m_gobutton, self.DefaultButton, self.AbortButton)

        # Create a table layout and add all the controls
        controllayout = forms.DynamicLayout()
        controllayout.Spacing = drawing.Size(5, 5)
        controllayout.AddRow(self.m_treegridview)
        
        # Create stacklayout for control and buttons layouts.
        layout1 = forms.DynamicLayout()
        layout1.Spacing = drawing.Size(5, 5)
        layout1.AddRow(controllayout)
        layout1.AddRow(None)
        layout1.AddRow(buttonslayout)
        
##############################################################################
# The Dynamic Layout controls using Rows
##############################################################################
        layout = forms.DynamicLayout(DefaultSpacing = drawing.Size(2,2))
#        layout.AddAutoSized(self.m_progressbar)
#        layout.AddRow(self.m_gobutton)
  
        layout.AddRow(None, forms.Label(Text = 'Label1'), forms.Label(Text = 'Button1'), None)
        layout.AddRow(None, forms.Label(Text = 'Label2'), forms.Label(Text = 'Button2'), None)
#        layout.AddCentered(self.collapsePanel) # we need this auto-sized so we can get its width to adjust form height
#        layout.Add(None); # expanding space, in case you want the form re-sizable
        layout.AddRow(None,self.DefaultButton, self.AbortButton, None);

##############################################################################
# The Dynamic Layout controls using Columns
##############################################################################
        layout3 = forms.DynamicLayout(DefaultSpacing = drawing.Size(2,2))
#        layout3.AddAutoSized(self.m_progressbar)
#        layout3.AddRow(self.m_gobutton)
        layout3.AddRow(None)
        layout3.AddSeparateColumn(None, forms.Label(Text = 'Label1'), forms.Label(Text = 'Button1'), None)
        layout3.AddSeparateColumn(None, forms.Label(Text = 'Label2'), forms.Label(Text = 'Button2'), None)
#        layout3.AddCentered(self.collapsePanel) # we need this auto-sized so we can get its width to adjust form height
#        layout3.Add(None); # expanding space, in case you want the form re-sizable
        layout3.AddRow(None,self.DefaultButton, self.AbortButton, None);

        
##############################################################################
# The Dynamic Layout using Horizontal and Vertical
##############################################################################
        layout2 = forms.DynamicLayout(DefaultSpacing = drawing.Size(2,2))
# This example uses the verbose methods creating sections in separate statements

        layout2.BeginHorizontal()
        layout2.Add(self.m_gobutton)
        layout2.Add(self.m_progressbar)
        layout2.EndHorizontal()

        layout2.BeginHorizontal()
        layout2.Add(self.m_slider)

        layout2.BeginVertical(padding = drawing.Padding(10))
        layout2.Add(forms.TextBox())
        layout2.Add(self.m_searchbox)
        layout2.EndVertical()
        layout2.EndHorizontal()
        
        layout2.BeginHorizontal()
        layout2.Add(None)
        layout2.Add(self.DefaultButton)
        layout2.Add(self.AbortButton)
        layout2.Add(None)
        layout2.EndHorizontal()

##############################################################################
# The Dynamic Layout using Horizontal and Vertical with row
##############################################################################
        layout4 = forms.DynamicLayout(DefaultSpacing = drawing.Size(2,2))
# This example uses the verbose methods creating sections in separate statements

        layout4.AddRow('Camera:') 

        layout4.BeginCentered(padding = drawing.Padding(10, 5, 10, 10))
        layout4.AddRow('Name:', forms.TextBox(Text = 'Persp1')) 
        layout4.AddRow('Lens:', forms.TextBox(Text = '50mm')) 
        layout4.AddRow('Projection:  ', forms.TextBox(Text = '2-point')) 
        layout4.EndCentered()

        layout4.AddSeparateRow(None, self.DefaultButton, self.AbortButton, None)



##############################################################################
# The Dynamic Layout using Horizontal and Vertical with row
##############################################################################
        layout5 = forms.DynamicLayout(DefaultSpacing = drawing.Size(2,2))
# This example uses the verbose methods creating sections in separate statements

        layout5.AddRow('Camera:') 


        layout5.BeginVertical(padding = drawing.Padding(10, 5, 10, 10))
        layout5.AddRow('Name:', forms.TextBox(Text = 'Persp1')) 
        layout5.AddRow('Lens:', forms.TextBox(Text = '50mm')) 
        layout5.AddRow('Projection:  ', forms.TextBox(Text = '2-point'))
        layout5.EndVertical()

        layout5.BeginVertical()
        layout5.AddRow(None, self.DefaultButton, self.AbortButton, None)
        layout5.EndVertical()

        self.Content = layout4

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