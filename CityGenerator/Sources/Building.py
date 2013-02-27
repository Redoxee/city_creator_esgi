
from Plot import Plot
class Building(Plot):


    def __init__(self,listCorners,height):
        '''
        Constructor
        '''
        super(Building, self).__init__(listCorners)
        self.height = height
        return
