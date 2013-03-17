
class Block:

    def __init__(self,districtType,canBuild=True):
        '''
        Constructor
        '''
        self.districtType = districtType
        self.canBuild = canBuild
        self.plots = []
        
    def getCanBuild(self):
        return self.canBuild
    
    def getPlots(self):
        return self.plots
    
    def setPlots(self, plots):
        self.plots = plots

    def asXml(self, doc):
        sBlock = doc.createElement(self.getXmlName())
        sBlock.setAttribute("type", str(self.districtType))
        sBlock.setAttribute("canBuild", str(self.canBuild))
        for plot in self.plots:
            sBlock.appendChild(plot.asXml(doc))
        return sBlock
    
    def getXmlName(self):
        return "block"