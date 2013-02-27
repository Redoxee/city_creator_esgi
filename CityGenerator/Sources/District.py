'''
Created on 26 févr. 2013

@author: Dylan
'''
class District:
    '''
    classdocs
    '''


    def __init__(self,districtType):
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