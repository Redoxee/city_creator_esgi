
from xml.dom.minidom import parse

class City:

    def __init__(self, field):
        self.field = field
        
    def serialize(self, name="defaultCity"):
        """ serialize the city in the "name".xml file"""
        if (self.field == None):
            print("impossible serialization")
            return
        parser = parse(name + ".xml")
        if (parser.hasChildNodes()):
            print("impossible serialization : file already exists")
            return
        
        """xml creation"""
        sField = parser.createElement("field")
        fieldBounds = self.field.getBoundaries()
        for bound in fieldBounds:
            sBound = parser.createElement("bound");
            sBound.setAttribute("x", bound.x)
            sBound.setAttribute("y", bound.y)
            sBound.setAttribute("z", bound.z)
            sField.appendChild(sBound)
            parser.appendChild(sField)
        return
    
    def deserialize(self):
        return
    
    def getField(self):
        return self.field
    
    def setField(self, field):
        self.field = field
        
