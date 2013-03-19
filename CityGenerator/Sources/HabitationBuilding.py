
from Building import Building

class HabitationBuilding(Building):


    def __init__(self, corners=[], height=[]):
        super().__init__(corners, height)

    def asXml(self, doc):
        sHabitationBuilding = doc.createElement(HabitationBuilding.getXmlName())
        self.cornersAsXml(doc, sHabitationBuilding)
        return super().asXml(doc, sHabitationBuilding)
    
    @staticmethod 
    def getXmlName():
        return "habitationBuilding"
    
    def getListCorners(self):
        return super().getListCorners()
    
    @staticmethod
    def parseXml(node):
        habitation = HabitationBuilding()
        return habitation