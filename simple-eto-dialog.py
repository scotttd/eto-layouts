################################################################################
# SampleEtoDialog.py
# MIT License - Copyright (c) 2017 Robert McNeel & Associates.
# See License.md in the root of this repository for details.
################################################################################
import clr
clr.AddReference("Eto")
clr.AddReference("Rhino.UI")

from Rhino.UI import *
from Eto.Forms import *
from Eto.Drawing import *

dia = Dialog()
dia.Title = "Sample Eto Dialog"
# dia.ClientSize = Size(200, 200)
dia.Padding = Padding(20,20)

group1label = Label(Text = "Show")
groupbox1 = GroupBox(Text = "Show")

layout = DynamicLayout()
layout.DefaultSpacing = Size(2,2)
layout.AddRow(grouplabel, None)
layout.AddRow(


label = Label()
label.Text = "Hello Rhino.Python!"


dia.Content = layout

dia.ShowModal(RhinoEtoApp.MainWindow)