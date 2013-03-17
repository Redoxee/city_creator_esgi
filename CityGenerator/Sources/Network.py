
class Network:
    def __init__(self, wayPoints):
        self.wayPoints = wayPoints
        
    def getWayPoints(self):
        return self.wayPoints
    
    def asXml(self, doc):
        sNetwork = doc.createElement(self.getXmlName())
        for wayPoint in self.getWayPoints():
            sNetwork.appendChild(wayPoint.asXml(doc))
        return sNetwork
            
    def getXmlName(self):
        pass
