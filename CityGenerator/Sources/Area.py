
from Plot import Plot

class Area(Plot):
    '''
    classdocs
    '''

    def __init__(self, listCorners):
        '''
        Constructor
        '''
        Plot.__init__(self, listCorners)

    def asXml(self, doc):
        return super(Area, self).asXml(doc)
    
    def getXmlName(self):
        return "area"
    
    def getListCorners(self):
        return super().getListCorners()