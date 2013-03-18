
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
    
    @staticmethod 
    def getXmlName():
        return "coordinate"
    
    @staticmethod
    def parseXml(node):
        coordinates = Coordinates()
        coordinates.x = float(node.getAttribute("x"))
        coordinates.y = float(node.getAttribute("y"))
        coordinates.z = float(node.getAttribute("z"))
        return coordinates
    
    def __str__(self):
        return "(" + self.x + ", " + self.y + ", " + self.z + ")"
