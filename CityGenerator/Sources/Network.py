

class Network:
    def __init__(self, wayPoints=[]):
        self.wayPoints = wayPoints
        
    def getWayPoints(self):
        return self.wayPoints
    
    def addWayPoint(self, wayPoint):
        self.wayPoints.append(wayPoint)
        
    def wayPointsAsXml(self, doc, node):
        for wayPoint in self.getWayPoints():
            node.appendChild(wayPoint.asXml(doc))
    
    def asXml(self, doc, child):
        sNetwork = doc.createElement(Network.getXmlName())
        sNetwork.appendChild(child)
        return sNetwork
            
    @staticmethod 
    def getXmlName():
        return "network"

    @staticmethod
    def parseXml(node):
        from Road import Road
        child = node.firstChild
        road = None
        if (child.tagName == Road.getXmlName()):
            road = Road.parseXml(child)
        return road