import wx

last = None
for key in dir(wx):
    if isinstance(getattr(wx, key), type):
        item = getattr(wx, key)
        info = 'wx.' + key + '()'

        try:
            if last not in ["wx.CommandLinkButton()", "wx.FSFile()", "wx.FileConfig()", "wx.PixelDataBase()"]:
                item()
        except Exception as e:
            print '# ' + info + ' Exception: ' + e.message
        else:
            print info

        last = info
