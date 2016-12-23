#!/usr/bin/env python
import wx


def embaixo(elemento):
    return elemento.GetPosition()[0], elemento.GetPosition()[1] + elemento.GetSize()[1]

app = wx.App()  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, title="Hello World", size=(800, 600))  # A Frame is a top-level window.
panel = wx.Panel(frame)
text_ctrl1 = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos=(0, 0), size=(100, 100))
text_ctrl2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos=(100, 0), size=(100, 100))
button1 = wx.Button(panel, pos=(0, 100), size=(200, 100))
panel.SetSize(panel.GetBestSize())
button2 = wx.Button(frame, pos=embaixo(panel), size=(200, 100))
button3 = wx.Button(frame, pos=embaixo(button2), size=(200, 100))
frame.SetSize(frame.GetBestSize())
frame.Show(True)
app.MainLoop()
