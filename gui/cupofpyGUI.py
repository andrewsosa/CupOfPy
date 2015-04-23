import wx
import frame
import app
from functools import partial
from cupofpyHelper import curry


class pyFrame(frame.Frame):
    def CreateMainMenu(self):
        menu = [
            ('&File', [
                ('&Open', self.FileOpen),
            ]),
            ('&Edit', [
                ('&Copy', self.EditCopy),
                ('&Paste', self.EditPaste),
            ]),
            ('&View', [
                ('&One item', partial(self.DataBox, 1)),
                ('&Second item', partial(self.DataBox, 2)),
                None,
                ('Sub&menu', [
                    ('&Three', partial(self.DataBox, 3)),
                    ('&Four', partial(self.DataBox, 4)),
                ]),
            ]),
        ]
        self.SetMenuBar(self.BuildMenu(menu))

    def FileOpen(self, event):
        self.Info(self, 'You chose File->Open')

    def EditCopy(self, event):
        self.Info(self, 'You chose Edit->Copy')

    def EditPaste(self, event):
        self.Info(self, 'You chose Edit->Paste')

    def DataBox(self, num, event):
        self.Info(self, 'You chose item %d' % (num,))

    def Info(self, parent, message, caption='Info'):
        dlg = wx.MessageDialog(parent, message, caption,
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


class pyApp(app.App):
    pass
