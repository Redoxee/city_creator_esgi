
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
        return
    
    def setPlots(self, plots):
        self.plots = plots
