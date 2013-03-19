import ast
from Plot import Plot

class Block:

    def __init__(self, blockType=0,canBuild=True, plots=[]):
        '''
        Constructor
        '''
        self.blockType = blockType
        self.canBuild = canBuild
        self.plots = plots
        
    def getCanBuild(self):
        return self.canBuild
    
    def addPlot(self, plot):
        self.plots.append(plot)
    
    def getPlots(self):
        return self.plots
    
    def setPlots(self, plots):
        self.plots = plots

    def asXml(self, doc):
        sBlock = doc.createElement(Block.getXmlName())
        sBlock.setAttribute("canBuild", str(self.canBuild))
        sBlock.setAttribute("type", str(self.blockType))
        for plot in self.plots:
            sBlock.appendChild(plot.asXml(doc))
        return sBlock
    
    @staticmethod 
    def getXmlName():
        return "block"
    
    @staticmethod
    def parseXml(node):
        block = Block()
        block.canBuild = ast.literal_eval(node.getAttribute("canBuild"))
        block.blockType = int(node.getAttribute("type"))
        for child in node.childNodes:
            block.addPlot(Plot.parseXml(child))
        return block
    
    