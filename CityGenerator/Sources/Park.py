
from Area import Area

class Park(Area):

    def __init__(self, corners):
        super().__init__(corners)

    def asXml(self, doc):
        return super().asXml(doc)
    
    @staticmethod 
    def getXmlName():
        return "park"
    
    def getListCorners(self):
        return super().getListCorners()