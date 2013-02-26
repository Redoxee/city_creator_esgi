'''
Created on 26 févr. 2013

@author: Antoine
'''

class Field:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.boundaries = []
        self.networks = []
        self.blocks = []
        
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
    
    def getBlocks(self):
        return self.blocks
    
    def setBlocks(self, blocks):
        self.blocks = blocks
        