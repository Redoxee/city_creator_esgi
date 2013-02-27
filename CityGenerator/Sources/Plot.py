from Coordinates import Coordinates
class Plot:
    def __init__(self, listCorners):
        self.setListCorners(listCorners);
    def setListCorners(self, listCorners):
        self.corners = listCorners;
        if(len(listCorners) > 0):
            self.centerPlot = Coordinates(0,0,0)
            for i in range(len(listCorners)):
                self.centerPlot.x += listCorners[i].x
                self.centerPlot.y += listCorners[i].y
                self.centerPlot.z += listCorners[i].z
            self.centerPlot.x /= len(listCorners)
            self.centerPlot.y /= len(listCorners)
            self.centerPlot.z /= len(listCorners)
