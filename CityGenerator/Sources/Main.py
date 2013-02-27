

from Block import Block
from Building import Building
from City import City
from Coordinates import Coordinates
from District import District
from Field import Field
from Network import Network
from Traductor import Traductor


boundaries = [Coordinates(0, 0, 0), Coordinates(100, 0, 0), Coordinates(100, 100, 0), Coordinates(0, 100, 0)]
field = Field(boundaries)
city = City(field)
road = Network([Coordinates(50, 0, 0), Coordinates(50, 100, 0)])
field.setNetworks([road])

districtBoundaries = [Coordinates(10, 10, 0), Coordinates(40, 10, 0), Coordinates(40, 90, 0), Coordinates(10, 90, 0)]
district = District()
district.setBoundaries(districtBoundaries)
field.setDistricts([district])

block = Block()

district.setblocks([block])
block.canBuild =  True
building = Building()


traductor = Traductor();
traductor.draw(city)
