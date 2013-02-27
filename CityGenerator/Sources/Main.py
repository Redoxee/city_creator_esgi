from Field import Field
from City import City
from Coordinates import Coordinates

def main():
    c1 = Coordinates(1.0, 0.0, 2.0)
    c2 = Coordinates(0.0, 0.0, 0.0)
    c3 = Coordinates(2.0, 0.0, 2.0)
    field = Field([c1, c2, c3])
    city = City(field)
    city.serialize()
    return

main()