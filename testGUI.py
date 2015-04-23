import wx


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)

        self.CreateStatusBar()

        filemenu = wx.Menu()
        menuItem_About = filemenu.Append(
            wx.ID_ABOUT, "&About", " Information about this program")

        filemenu.AppendSeparator()

        menuItem_Exit = filemenu.Append(
            wx.ID_EXIT, "&Exit", " Terminate the program")

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, 'About', "Information about this program")

        menuBar = wx.MenuBar()
        # Adding the "filemenu" to the MenuBar
        menuBar.Append(filemenu, "&File")
        menuBar.Append(help_menu, "&Help")
        self.SetMenuBar(menuBar)

        self.SetSize((220, 180))
        self.SetTitle("Standard ids")
        self.Centre()
        self.Show(True)

    def onAbout(self, e):

        # A message dialog box with an OK button. wx.OK is a standard ID in
        # wxWidgets.
        dlg = wx.MessageDialog(
            self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished.

    def onExit(self, event):
        self.Close(True)  # Close the frame.


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
