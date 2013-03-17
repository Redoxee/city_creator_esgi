
from Building import Building

class HabitationBuilding(Building):


    def __init__(self, listCorners, height):
        Building.__init__(self, listCorners, height)

    def asXml(self, doc):
        pass
    
    def getXmlName(self):
        pass
    
    def getListCorners(self):
        return super().getListCorners()