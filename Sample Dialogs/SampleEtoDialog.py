################################################################################
# SampleEtoDialog.py
# MIT License - Copyright (c) 2017 Robert McNeel & Associates.
# See License.md in the root of this repository for details.
################################################################################

import Rhino.UI
import Eto.Forms as forms
import Eto.Drawing as drawing

obj = forms.Dialog()
obj.Title = "Sample Eto Dialog"
obj.ClientSize = drawing.Size(200, 100)
obj.Padding = drawing.Padding(5)
obj.Resizable = False

label = forms.Label()
label.Text = "Hello Rhino.Python!"

obj.Content = label

obj.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)