
from Area import Area

class Park(Area):

    def __init__(self, listCorners):
        Area.__init__(self, listCorners)

    def asXml(self, doc):
        return super(Park, self).asXml(doc)
    
    def getXmlName(self):
        return "park"
    
    def getListCorners(self):
        return super().getListCorners()