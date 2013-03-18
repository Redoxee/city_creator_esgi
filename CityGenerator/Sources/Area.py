
from Plot import Plot

class Area(Plot):
    '''
    classdocs
    '''

    def __init__(self, corners=[]):
        '''
        Constructor
        '''
        super().__init__(corners)

    def asXml(self, doc):
        sArea = doc.createElement(Area.getXmlName())
        self.cornersAsXml(doc, sArea)
        return super(Area, self).asXml(doc, sArea)
    
    @staticmethod
    def getXmlName():
        return "area"
    
    def getListCorners(self):
        return super().getListCorners()
    
    @staticmethod
    def parseXml(node):
        area = Area()
        return area