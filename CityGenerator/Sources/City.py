from xml.dom.minidom import Document, parse

from Field import Field
import os

class City:

    def __init__(self, name="", field=None):
        self.field = field
        self.name = name
    
        
    def serialize(self):
        """ serialize the city in the "name".xml file"""
        if (self.field == None):
            print("impossible serialization")
            return
        
        if not os.path.exists("./CityGen"):
            os.makedirs("./CityGen")
        
        filename = "CityGen/" + self.name + ".cgxml"
        f = open(filename, "+w")
        f.write(self.asXml(Document()).toxml())
        
    def getName(self):
        return self.name
    
    def asXml(self, doc):
        sCity = doc.createElement(self.getXmlName())
        sCity.setAttribute("name", self.name)
        sCity.appendChild(self.field.asXml(doc))
        return sCity
    
    @staticmethod
    def parseXml(node):
        city = City()
        city.name = node.getAttribute("name")
        city.field = Field.parseXml(node.firstChild)
        return city
    
    @staticmethod 
    def getXmlName():
        return "city"
       
    def getField(self):
        return self.field
    
    def setField(self, field):
        self.field = field
        
    @staticmethod
    def deserialize(fileName):
        """ Function which creates and return a city from an xml file"""
        doc = parse("./CityGen/" + fileName)
        return City.parseXml(doc.firstChild)
    
    def __str__(self):
        return "City name = " + self.name
