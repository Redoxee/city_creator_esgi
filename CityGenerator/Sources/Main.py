from Block import Block
from Building import Building
from City import City
from Coordinates import Coordinates
from District import District
from Field import Field
from Network import Network
from imp import reload
import TraductorModule
reload(TraductorModule)
from TraductorModule import Traductor 
boundaries = [Coordinates(0, 0, 0), Coordinates(100, 0, 0), Coordinates(100, 100, 0), Coordinates(0, 100, 0)]
field = Field(boundaries)
city = City(field)
road = Network([Coordinates(50, 0, 5), Coordinates(50, 50, 5)])
field.setNetworks([road])

districtBoundaries = [Coordinates(10, 10, 0), Coordinates(40, 10, 0), Coordinates(40, 90, 0), Coordinates(10, 90, 0)]
district = District(0)
district.setBoundaries(districtBoundaries)
field.setDistricts([district])

building = Building(districtBoundaries, 50)
block = Block(0)

district.setblocks([block])
block.canBuild = True
block.setPlots([building])

traductor = Traductor();
traductor.draw(city)

city.serialize("firstExempleCity")
