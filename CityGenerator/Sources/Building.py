
from Plot import Plot
class Building(Plot):

    def __init__(self,listCorners,height):
        '''
        Constructor
        '''
        super().__init__(listCorners)
        self.height = height
        return
    
    def asXml(self, doc):
        sPlot = super().asXml(doc)
        sPlot.setAttribute("height", str(self.height))
        return sPlot
    
    def getListCorners(self):
        return super().getListCorners()
        
    def getXmlName(self):
        return "building"