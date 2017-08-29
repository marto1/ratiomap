import wx, sys
from squaremap.squaremap import SquareMap, DefaultAdapter
from random import randint as rand

class RatioMapAdapter(DefaultAdapter):
    def background_color(self, node, depth):
        return node.bgcolor #only 1 layer deep

class TestApp(wx.App):
    """Application to view ratios as a SquareMap"""
    def OnInit(self):
        """Initialise the application"""
        wx.InitAllImageHandlers()
        self.frame = frame = wx.Frame(None)
        model = self.get_model(sys.argv[1:])
        self.sq = SquareMap(
            frame,
            model=model,
            square_style = True,
            adapter = RatioMapAdapter(),
        )
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

    def get_model(self, values):
        """ args - LABEL:VALUE LABEL:VALUE..."""
        nodes = []
        for pair in values:
            label, value = pair.split(":")
            label = "{}\n{}".format(label, value)
            bgcol  = (100+rand(0, 150),100+rand(0, 150),100+rand(0, 150))
            nodes.append(Node(label, float(value), [], bgcol))
        return Node("Total" , sum([x.size for x in nodes]), nodes, (0, 240, 0))

class Node(object):
    def __init__(self, path, size, children, bgcolor):
        self.path = path
        self.size = size
        self.children = children
        self.bgcolor = bgcolor

    def __repr__(self):
        return '%s( %r, %r, %r )'%( self.__class__.__name__, self.path, self.size, self.children )

def main():
    app = TestApp(0)
    app.MainLoop()
    

if __name__ == '__main__':
    main()
