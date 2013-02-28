
class District:

<<<<<<< HEAD
    def __init__(self,districtType):
=======
    def __init__(self):
>>>>>>> branch 'master' of https://github.com/Redoxee/city_creator_esgi.git
        '''
        Constructor
        '''
        self.boundaries = []
        self.networks = []
        self.blocks = []
        self.districtType = districtType
        
    def getBoundaries(self):
        return self.boundaries
        
    def setBoundaries(self, boundaries):
        self.boundaries = boundaries
    
    def getNetworks(self):
        return self.networks
    
    def addNetwork(self, network):
        self.networks.append(network)
    
    def setNetworks(self, networks):
        self.networks = networks
    
    def clearNetwork(self):
        self.networks = []
    
    def getblocks(self):
        return self.blocks
    
    def setblocks(self, blocks):
        self.blocks = blocks
