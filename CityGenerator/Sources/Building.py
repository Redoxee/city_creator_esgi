
from Plot import Plot
class Building(Plot):

    def __init__(self,listCorners,height):
        '''
        Constructor
        '''
        Plot.__init__(self, listCorners)
        self.height = height
        return
