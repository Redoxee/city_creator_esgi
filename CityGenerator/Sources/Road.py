
from Network import Network

class Road(Network):
    
    def __init__(self, wayPoints):
        super().__init__(wayPoints)

    def asXml(self, doc):
        return super().asXml(doc)
    
    def getXmlName(self):
        return "road"
    
    def getWayPoints(self):
        return super().getWayPoints()