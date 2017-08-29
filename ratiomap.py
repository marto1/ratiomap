import wx, sys, os, logging, operator
from squaremap.squaremap import SquareMap

class TestApp(wx.App):
    """Application to view ratios as a SquareMap"""
    def OnInit(self):
        """Initialise the application"""
        wx.InitAllImageHandlers()
        self.frame = frame = wx.Frame(None)
        model = self.get_model(sys.argv[1:])
        self.sq = SquareMap(frame, model=model)
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

    def get_model(self, values):
        """ args - LABEL:VALUE LABEL:VALUE..."""
        nodes = []
        for pair in values:
            label, value = pair.split(":")
            nodes.append(Node(label, float(value), []))
        return Node("Total" , sum([x.size for x in nodes]), nodes )


class Node(object):
    def __init__(self, path, size, children):
        self.path = path
        self.size = size
        self.children = children
    def __repr__(self):
        return '%s( %r, %r, %r )'%( self.__class__.__name__, self.path, self.size, self.children )

def main():
    app = TestApp(0)
    app.MainLoop()
    

if __name__ == '__main__':
    main()
