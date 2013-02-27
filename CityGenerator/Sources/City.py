
from xml.dom.minidom import Document

class City:

    def __init__(self, field):
        self.field = field
        
    def serialize(self, name="defaultCity"):
        """ serialize the city in the "name".xml file"""
        if (self.field == None):
            print("impossible serialization")
            return
        
        filename = "CityGen" + name + ".xml"
        
        doc = Document()
        
        """xml creation"""
        sField = doc.createElement("field")
        fieldBounds = self.field.getBoundaries()
        for bound in fieldBounds:
            sBound = doc.createElement("bound");
            sBound.setAttribute("x", bound.x)
            sBound.setAttribute("y", bound.y)
            sBound.setAttribute("z", bound.z)
            sField.appendChild(sBound)
            doc.appendChild(sField)
            
        f = open(filename, "+w")
        f.write(doc.toxml())
        return
    
    def deserialize(self):
        return
    
    def getField(self):
        return self.field
    
    def setField(self, field):
        self.field = field
        
