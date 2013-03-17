
class District:

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
        
    def asXml(self, doc):
        sDistrict = doc.createElement(self.getXmlName())
        sDistrict.setAttribute("type", str(type))
        for bound in self.boundaries:
            sDistrict.appendChild(bound.asXml(doc))
        for network in self.networks:
            sDistrict.appendChild(network.asXml(doc))
        for block in self.blocks:
            sDistrict.appendChild(block.asXml(doc))
        return sDistrict

    def getXmlName(self):
        return "district"