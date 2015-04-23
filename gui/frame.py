import wx
import logging

"""
This class was adopted from code found here:
     http://wiki.wxpython.org/WorkingWithMenus
"""


class Frame(wx.Frame):

    # TODO: Add functionaility to pass an ID as an argument
    #       or choose one if not specified
    def BuildSubmenu(self, subMenu):
        logging.info('Frame.BuildSubMenu() called.')
        subMenuObject = wx.Menu()
        for item in subMenu:

            if not item:  # allow now to add separators
                subMenuObject.AppendSeparator()
                continue

            statustext = ''
            uihandler = None

            if len(item) == 2:
                title, action = item
            elif len(item) == 3:
                if type(item[2]) is str:
                    title, action, statustext = item
                else:
                    title, action, statustext = item
            elif len(item) == 4:
                title, action, statustext, uihandler = item
            else:
                # TODO: Change error type to a custom one?
                raise AssertionError, \
                    'Item %s should have either 2 to 4 parts' % (item,)

            if type(action) is list:
                _id = wx.NewId()
                subMenuObject.AppendMenu(_id, title, self.BuildSubmenu(action))
            else:
                _id = wx.NewId()
                tempAppend = subMenuObject.Append(_id, title, statustext)
                self.Bind(wx.EVT_MENU, action, tempAppend)
                #wx.EVT_MENU(self, _id, action)

            if uihandler:
                wx.EVT_UPDATE_UI(self, _id, uihandler)

        return subMenuObject

    def BuildMenu(self, menu):
        logging.info('Frame.BuildMenu() called.')
        mainMenu = wx.MenuBar()

        for title, subMenu in menu:
            mainMenu.Append(self.BuildSubmenu(subMenu), title)

        return mainMenu

    def CreateMainMenu(self):
        # TODO: Figure out how to get logging message to print for derived
        #       class as well
        logging.info('Frame.CreateMainMenu() called.')
        raise NotImplementedError(
            "Subclass should implement CreateMainMenu()!")
        """
        Example Menu to be created for the frame:
        menu = [
            ('&File', [
                ('&Open', self.FileOpen),
            ]),
            ('&Edit', [
                ('&Copy', self.EditCopy),
                ('&Paste', self.EditPaste),
            ]),
            ('&View', [
                ('&One item', curry(self.DataBox, 1)),
                ('&Second item', curry(self.DataBox, 2)),
                ('Sub&menu', [
                    ('&Three', curry(self.DataBox, 3)),
                    ('&Four', curry(self.DataBox, 4)),
                ]),
            ]),
        ]
        self.SetMenuBar(self.BuildMenu(menu))
        """

    def __init__(self, *args, **kwargs):
        logging.info('Frame.__init__() called.')
        wx.Frame.__init__(self, *args, **kwargs)
        self.CreateStatusBar()
        #self.SetStatusText('Welcome to a better menu system!')
        self.CreateMainMenu()
