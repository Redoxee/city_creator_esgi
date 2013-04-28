'''
Created on 28 avr. 2013

@author: Antoine
'''
from Coordinates import Coordinates

class LineSegment:
    '''
    classdocs
    '''

    def __init__(self, c1, c2):
        '''
        Constructor
        '''
        if not isinstance((c1, c2), (Coordinates, Coordinates)):
            raise TypeError("c1 and c2 should be 2 Coordinates")
        
        self.c1 = c1
        self.c2 = c2
        
    def __eq__(self, segment):
        return (self.c1 == segment.c1 and self.c2 == segment.c2) or (self.c1 == segment.c2 and self.c2 == segment.c1)
    