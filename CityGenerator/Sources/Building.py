'''
Created on 26 f�vr. 2013

@author: Antoine
'''

import Plot

class Building(Plot):
    '''
    classdocs
    '''


    def __init__(self, listCorner, height):
        '''
        Constructor
        '''
        super.__init__(listCorner)
        self.height = height;
