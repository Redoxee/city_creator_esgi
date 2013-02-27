
class Block:


    def __init__(self):
        self.canBuild = True
        self.plots = []
        
    def getCanBuild(self):
        return self.canBuild
    
    def getPlots(self):
        return self.plots
    
    def setPlots(self, plots):
        self.plots = plots