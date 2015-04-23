import wx
import wx.dataview as dv
from gui import cupofpyGUI
import logging

"""
This class was adopted from code found here:
     http://wiki.wxpython.org/WorkingWithMenus
"""


class MainFrame(cupofpyGUI.pyFrame):

    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)

        self.InitToolbar()

        self.InitUI()

        self.Show()

    def InitToolbar(self):
        toolbar = self.CreateToolBar()

        qtool = toolbar.AddLabelTool(
            wx.ID_ANY, 'Quit', wx.Bitmap('images/statusbar/close-tab.png'))
        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

        toolbar.Realize()

    def InitUI(self):
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &" + str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        # Example followed from here:
        # https://github.com/wxWidgets/wxPython/blob/master/demo/DVC_IndexListModel.py
        self.treeData = dv.DataViewCtrl(self,
                                        style=wx.BORDER_THEME
                                        # nice alternating bg colors
                                        | dv.DV_ROW_LINES
                                        #| dv.DV_HORIZ_RULES
                                        | dv.DV_VERT_RULES
                                        | dv.DV_MULTIPLE
                                        )

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.side_by_side_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.side_by_side_sizer.Add(self.treeData, 1, wx.EXPAND)
        self.side_by_side_sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.side_by_side_sizer, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        # Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.sizer.Fit(self)

    def OnQuit(self, e):
        self.Close()


class MainApp(cupofpyGUI.pyApp):

    def OnInit(self):
        frame = MainFrame(None, wx.ID_ANY)
        frame.Show()
        self.SetTopWindow(frame)

        cupofpyGUI.pyApp.OnInit(self)

        return True


if __name__ == '__main__':
    # TODO: Moar logging support
    #       https://docs.python.org/2/howto/logging.html
    #       utlize config file?
    logging.basicConfig(level=logging.DEBUG)
    app = MainApp(0)
    app.MainLoop()
