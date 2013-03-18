
from Plot import Plot
class Building(Plot):

    def __init__(self,corners = [],height = 0):
        '''
        Constructor
        '''
        super().__init__(corners)
        self.height = height
        return
    
    def asXml(self, doc, child):
        sBuilding = doc.createElement(Building.getXmlName())
        sBuilding.setAttribute("height", str(self.height))
        sBuilding.appendChild(child)
        return super().asXml(doc, sBuilding)

    def getListCorners(self):
        return super().getListCorners()
        
    @staticmethod 
    def getXmlName():
        return "building"
    
    @staticmethod
    def parseXml(node):
        from HabitationBuilding import HabitationBuilding
        from FunctionBuilding import FunctionBuilding
        child = node.firstChild
        building = None
        if (child.tagName == HabitationBuilding.getXmlName()):
            building = HabitationBuilding.parseXml(child)
        if (child.tagName == FunctionBuilding.getXmlName()):
            building = FunctionBuilding.parseXml(child)
        return building
    
        