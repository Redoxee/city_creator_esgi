
from xml.dom.minidom import Document, parse

class City:

    def __init__(self, field=None):
        self.field = field
    
        
    def serialize(self, name="defaultCity"):
        """ serialize the city in the "name".xml file"""
        if (self.field == None):
            print("impossible serialization")
            return
        
        filename = "CityGen/" + name + ".xml"
        f = open(filename, "+w")
        f.write(self.asXml(Document()).toprettyxml())
    
    def asXml(self, doc, cityName="MyCity"):
        sCity = doc.createElement(self.getXmlName())
        sCity.setAttribute("name", cityName)
        sCity.appendChild(self.field.asXml(doc))
        return sCity
    
    def parseXml(self, doc):
        return
    
    def getXmlName(self):
        return "city"
       
    def getField(self):
        return self.field
    
    def setField(self, field):
        self.field = field
        
        
def deserialize(fileName):
    """ Function which creates and return a city from an xml file"""
    doc = parse(fileName)
    city = City()
    city.parseXml(doc)
    return city
