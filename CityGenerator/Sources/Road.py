
from Network import Network

class Road(Network):
    
    def __init__(self, wayPoints=[]):
        super().__init__(wayPoints)

    def asXml(self, doc):
        sRoad = doc.createElement(Road.getXmlName())
        sNetwork = super().asXml(doc, sRoad)
        self.wayPointsAsXml(doc, sRoad)
        return sNetwork
    
    @staticmethod 
    def getXmlName():
        return "road"
    
    def getWayPoints(self):
        return super().getWayPoints()
    
    @staticmethod
    def parseXml(node):
        road = Road()
        return road