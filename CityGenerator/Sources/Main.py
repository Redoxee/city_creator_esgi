'''
Created on 26 f�vr. 2013

@author: Anton
'''
from City import City
from Field import Field
from Coordinates import Coordinates

city = City()
boundaries = [Coordinates(0,0,0),Coordinates(100,0,0),Coordinates(100,100,0),Coordinates(0,100,0)]
field =  Field(boundaries)