from Building import Building

class FunctionBuilding(Building):
    def __init__(self, corners=[], height=[]):
        super().__init__(corners, height)

    def asXml(self, doc):
        sFunctionBuilding = doc.createElement(FunctionBuilding.getXmlName())
        self.cornersAsXml(doc, sFunctionBuilding)
        return super().asXml(doc, sFunctionBuilding)
    
    @staticmethod
    def getXmlName():
        return "functionBuilding"
    
    def getListCorners(self):
        return super().getListCorners()
    
    @staticmethod
    def parseXml(node):
        function = FunctionBuilding()
        return function
    