#!/usr/bin/env python
import wx


class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

app = wx.App()  # Create a new app, don't redirect stdout/stderr to a window.
frame = MyFrame(None, "Hello World")  # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()
