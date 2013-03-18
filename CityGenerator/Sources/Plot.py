from Coordinates import Coordinates

class Plot:
    
    def __init__(self, corners=[]):
        self.corners = corners;
        self.calculateCenterPlot()
        
    def addCorner(self, corner):
        self.corners.append(corner)
        
    def getListCorners(self):
        return self.corners
        
    def setListCorners(self, listCorners):
        self.corners = listCorners;
        self.calculateCenterPlot()

    def calculateCenterPlot(self):
        if(len(self.corners) > 0):
            self.centerPlot = Coordinates(0,0,0)
            for i in range(len(self.corners)):
                self.centerPlot.x += self.corners[i].x
                self.centerPlot.y += self.corners[i].y
                self.centerPlot.z += self.corners[i].z
            self.centerPlot.x /= len(self.corners)
            self.centerPlot.y /= len(self.corners)
            self.centerPlot.z /= len(self.corners)
            
    def cornersAsXml(self, doc, node):
        for corner in self.getListCorners():
            node.appendChild(corner.asXml(doc))

    def asXml(self, doc, child):
        sPlot = doc.createElement(Plot.getXmlName())
        sPlot.appendChild(child)
        return sPlot
    
    @staticmethod 
    def getXmlName():
        return "plot"
    
    @staticmethod
    def listCornersAsXml():
        return
    
    @staticmethod
    def parseXml(node):
        from Building import Building
        from Area import Area
        child = node.firstChild
        plot = None
        if (child.tagName == Building.getXmlName()):
            plot = Building.parseXml(child)
        if (child.tagName == Area.getXmlName()):
            plot = Area.parseXml(child)
        return plot
    
    