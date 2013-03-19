from Coordinates import Coordinates
from Network import Network
from District import District
class Field:

    def __init__(self, boundaries = []):
        self.boundaries = boundaries
        self.networks = []
        self.districts = []
        
    def getBoundaries(self):
        return self.boundaries
        
    def setBoundaries(self, boundaries):
        self.boundaries = boundaries
    
    def addBoundary(self, boundary):
        self.boundaries.append(boundary)
    
    def getNetworks(self):
        return self.networks
    
    def addNetwork(self, network):
        self.networks.append(network)
    
    def setNetworks(self, networks):
        self.networks = networks
    
    def clearNetwork(self):
        self.networks = []
        
    def addDistrict(self, district):
        self.districts.append(district)
    
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
    
    @staticmethod
    def parseXml(node):
        field = Field()
        for child in node.childNodes:
            if child.tagName == Coordinates.getXmlName():
                field.addBoundary(Coordinates.parseXml(child))
            if child.tagName == Network.getXmlName():
                field.addNetwork(Network.parseXml(child))
            if child.tagName == District.getXmlName():
                field.addDistrict(District.parseXml(child))
        return field
    
    @staticmethod 
    def getXmlName():
        return "field"
    
