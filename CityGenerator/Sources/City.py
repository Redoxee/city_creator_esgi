'''
Created on 26 févr. 2013

@author: Antoine
'''

class City:
    '''
    classdocs
    '''


    def __init__(self, field):
        '''
        Constructor
        '''
        self.field = field
        
    def serialize(self):
        return
    
    def deserialize(self):
        return
    
    def getField(self):
        return self.field
    
    def setField(self, field):
        self.field = field
        