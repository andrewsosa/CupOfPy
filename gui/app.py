import wx
import logging


"""
This class was adopted from code found here:
     http://wiki.wxpython.org/WorkingWithMenus
"""


class App(wx.App):

    def BringWindowToFront(self):
        logging.info('App.BringWindowToFront() called.')
        try:  # it's possible for this event to come when the frame is closed
            self.GetTopWindow().Raise()
        except:
            pass

    def OnActivate(self, event):
        logging.info('App.OnActivate() called.')
        # if this is an activate event, rather than something else, like
        # iconize.
        if event.GetActive():
            self.BringWindowToFront()
        event.Skip()

    def OpenFileMessage(self, filename):
        logging.info('App.OpenFIleMessage() called.')
        dlg = wx.MessageDialog(None,
                               "This app was just asked to open:\n%s\n" % filename,
                               "File Dropped",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def MacOpenFile(self, filename):
        logging.info('App.MacOpenFile() called.')
        """
        Called for files droped on dock icon, or opened via finders
        context menu
        """
        print filename
        # code to load filename goes here.
        print "%s dropped on app" % (filename)
        self.OpenFileMessage(filename)

    def MacReopenApp(self):
        logging.info('App.MacReopenApp() called.')
        """
        Called when the doc icon is clicked, and ???
        """
        self.BringWindowToFront()

    def MacNewFile(self):
        logging.info('App.MacNewFile() called.')
        pass

    def MacPrintFile(self, file_path):
        logging.info('App.MacPrintFile() called.')
        pass

    def __init__(self, *args, **kwargs):
        logging.info('App.__init__() called.')
        wx.App.__init__(self, *args, **kwargs)

        # This catches events when the app is asked to activate by some other
        # process
        self.Bind(wx.EVT_ACTIVATE_APP, self.OnActivate)

    def OnInit(self):
        logging.info('App.OnInit() called.')
        import sys
        for f in sys.argv[1:]:
            self.OpenFileMessage(f)

        """
        frame = MainFrame(None, wx.ID_ANY)
        frame.Show()
        self.SetTopWindow(frame)
        """

        return True
