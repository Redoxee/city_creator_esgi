
class Coordinates:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def asXml(self, doc):
        sCoordinate = doc.createElement(self.getXmlName())
        sCoordinate.setAttribute("x", str(self.x))
        sCoordinate.setAttribute("y", str(self.y))
        sCoordinate.setAttribute("z", str(self.z))
        return sCoordinate
    
    def getXmlName(self):
        return "coordinate"