
class Field:

    def __init__(self, boundaries):
        self.boundaries = boundaries
        self.networks = []
        self.districts = []
        
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
    
    def getDistricts(self):
        return self.districts
    
    def setDistricts(self, districts):
        self.districts = districts
        
