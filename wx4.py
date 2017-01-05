import wx
import wx.lib.inspection
import wx.lib.mixins.inspection


class Aplicativo(wx.App, wx.lib.mixins.inspection.InspectionMixin):
    def __init__(self):
        self.frame = None
        super(Aplicativo, self).__init__()

    def OnInit(self):
        wx.Log_SetActiveTarget(wx.LogStderr())

        self.SetAssertMode(wx.PYAPP_ASSERT_DIALOG)
        self.InitInspection()  # for the InspectionMixin base class

        menu_bar = wx.MenuBar()
        menu = wx.Menu()
        item = menu.Append(-1, "&Widget Inspector\tF6", "Show the wxPython Widget Inspection Tool")
        self.Bind(wx.EVT_MENU, self.OnWidgetInspector, item)
        item = menu.Append(-1, "E&xit\tCtrl-Q", "Exit demo")
        self.Bind(wx.EVT_MENU, self.OnExitApp, item)
        menu_bar.Append(menu, "&File")
        self.frame = wx.Frame(None)
        self.frame.CreateStatusBar()
        self.frame.SetMenuBar(menu_bar)
        self.frame.Show(True)
        self.frame.Bind(wx.EVT_CLOSE, self.OnCloseFrame)
        self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyEvent)
        return True

    def OnExitApp(self, _):
        self.frame.Close(True)

    def OnCloseFrame(self, evt):
        if hasattr(self, "window") and hasattr(self.window, "ShutdownDemo"):
            self.window.ShutdownDemo()
        evt.Skip()

    def OnWidgetInspector(self, _):
        wx.lib.inspection.InspectionTool().Show()

    def OnKeyEvent(self, event):
        if event.GetKeyCode() == wx.WXK_CONTROL_Q:
            self.OnExitApp(event)
        elif event.GetKeyCode() == wx.WXK_F6:
            self.OnWidgetInspector(event)
        else:
            event.Skip()


def main():
    app = Aplicativo()
    app.MainLoop()


if __name__ == '__main__':
    main()
