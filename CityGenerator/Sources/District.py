from Coordinates import Coordinates
from Network import Network
from Block import Block

class District:

    def __init__(self,districtType=0):
        '''
        Constructor
        '''
        self.boundaries = []
        self.networks = []
        self.blocks = []
        self.districtType = districtType
        
    def addBoundary(self, boundary):
        self.boundaries.append(boundary)
        
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
        
    def addBlock(self, block):
        self.blocks.append(block)
    
    def getblocks(self):
        return self.blocks
    
    def setblocks(self, blocks):
        self.blocks = blocks
        
    def asXml(self, doc):
        sDistrict = doc.createElement(self.getXmlName())
        sDistrict.setAttribute("type", str(self.districtType))
        for bound in self.boundaries:
            sDistrict.appendChild(bound.asXml(doc))
        for network in self.networks:
            sDistrict.appendChild(network.asXml(doc))
        for block in self.blocks:
            sDistrict.appendChild(block.asXml(doc))
        return sDistrict
    
    @staticmethod 
    def getXmlName():
        return "district"
    
    @staticmethod
    def parseXml(node):
        district = District()
        district.districtType = int(node.getAttribute("type"))
        for child in node.childNodes:
            if child.tagName == Coordinates.getXmlName():
                district.addBoundary(Coordinates.parseXml(child))
            if child.tagName == Network.getXmlName():
                district.addNetwork(Network.parseXml(child))
            if child.tagName == Block.getXmlName():
                district.addBlock(Block.parseXml(child))
        return district
    