import math
import bpy
from Coordinates import Coordinates

def vecNormal(vx, vy, vz):
    return Coordinates(-vy, vx, 0)
def vecNormalized(vx, vy, vz):
    length = math.sqrt(vx * vx + vy * vy + vz * vz)
    if length == 0 : return 0
    return Coordinates(vx / length, vy / length, vz / length)

class Traductor:
    '''
    classdocs
    '''
    def draw(self, city):
        self.drawField(city.getField())
        self.drawNetwork(city.getField().getNetworks())
        if len(city.getField().getDistricts()) > 0 :
            for district in city.getField().getDistricts():
                self.drawNetwork(district.getNetworks())
                if len(district.getblocks()) > 0 :
                    for bloc in district.getblocks():
                        if len(bloc.getPlots()) > 0 :
                            for plot in bloc.getPlots():
                                self.drawPlot(plot)
        return


    def drawPolygone(self, boundaries, namePoly):
        if(len(boundaries) > 2):
            me = bpy.data.meshes.new(namePoly + 'Mesh')
            ob = bpy.data.objects.new(namePoly, me)
            ob.show_name = False
            # Link object to scene
            bpy.context.scene.objects.link(ob)
            arrayBounds = []
            for bound in  boundaries:
                arrayBounds.append((bound.x, bound.y, bound.z))
            listFaces = [range(len(boundaries))]
            listFaces.append((()))
            
            listVertice = [arrayBounds]
            listVertice.append([])
            me.from_pydata(arrayBounds, [], listFaces)
            
    def drawField(self, field):
        print("drawField")
        nameField = 'Name'
        self.drawPolygone(field.getBoundaries(), nameField)

            
    def drawNetwork(self, network):
        print("drawNetwork")
        wayPoint1 = None
        wayPoint2 = None
        if len(network) > 0:
            for road in network:
                if len(road.getwayPoints()) > 1:
                    print("draw a road")
                    for way in road.getwayPoints():
                        wayPoint1 = wayPoint2
                        wayPoint2 = way
                        if not wayPoint1 == None:
                            normal = vecNormal(wayPoint1.x + wayPoint2.x, wayPoint1.y + wayPoint2.y, wayPoint1.z + wayPoint2.z)
                            normal = vecNormalized(normal.x, normal.y, normal.z)
                            print ("normal(" + str(normal.x) + "," + str(normal.y) + "," + str(normal.z) + ")")
                            point1 = Coordinates(wayPoint1.x - normal.x / 2 , wayPoint1.y - normal.y / 2, wayPoint1.z)
                            point2 = Coordinates(wayPoint2.x - normal.x / 2 , wayPoint2.y - normal.y / 2, wayPoint2.z)
                            point3 = Coordinates(wayPoint2.x + normal.x / 2 , wayPoint2.y + normal.y / 2, wayPoint2.z)
                            point4 = Coordinates(wayPoint1.x + normal.x / 2 , wayPoint1.y + normal.y / 2, wayPoint1.z)
                            self.drawPolygone([point1, point2, point3, point4], "road")
    def drawBlock(self, block):
        print("drawBlock")
    def drawPlot(self, plot):
        print("drawPlot")
