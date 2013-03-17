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
       
    def asXml(self, doc):
        sField = doc.createElement(self.getXmlName())
        for bound in self.boundaries:
            sField.appendChild(bound.asXml(doc))
        for network in self.networks:
            sField.appendChild(network.asXml(doc))
        for district in self.districts:
            sField.appendChild(district.asXml(doc))
        return sField
    
    def getXmlName(self):
        return "field"
    
