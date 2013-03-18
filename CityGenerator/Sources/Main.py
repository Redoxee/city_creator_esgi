from Block import Block
from City import City
from Coordinates import Coordinates
from District import District
from Field import Field
from Road import Road
from HabitationBuilding import HabitationBuilding
from FunctionBuilding import FunctionBuilding
from Area import Area


from imp import reload
import TraductorModule
reload(TraductorModule)
from TraductorModule import Traductor 

boundaries = [Coordinates(0, 0, 0), Coordinates(100, 0, 0), Coordinates(100, 100, 0), Coordinates(0, 100, 0)]
field = Field(boundaries)
city = City("Paris", field)
road = Road([Coordinates(50, 0, 5), Coordinates(50, 50, 5)])
field.addNetwork(road)

districtBoundaries = [Coordinates(10, 10, 0), Coordinates(40, 10, 0), Coordinates(40, 90, 0), Coordinates(10, 90, 0)]
district = District()
district.setBoundaries(districtBoundaries)
field.setDistricts([district])

habitation = HabitationBuilding(districtBoundaries, 50)
function = FunctionBuilding(districtBoundaries, 20)
area = Area(districtBoundaries)

blocks=[]
for i in range(10):
    block = Block()
    block.canBuild = True
    block.setPlots([habitation, function, area])
    blocks.append(block)

district.setblocks(blocks)


traductor = Traductor();
traductor.draw(city)


city.serialize()

deserializedCity = City.deserialize("CityGen/" + city.getName() + ".cgxml")


