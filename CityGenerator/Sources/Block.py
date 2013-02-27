
class Block:
    '''
    classdocs
    '''


    def __init__(self,districtType,canBuild=True):
        '''
        Constructor
        '''
        self.districtType = districtType
        self.canBuild = canBuild
        
    def getCanBuild(self):
        return self.canBuild
    
    def getPlots(self):
        return
    
    def setPlots(self,VerticesList):
        return