from Coordinates import Coordinates
import bpy
import math

def vecNormal(vx, vy, vz):
    return Coordinates(-vy, vx, 0)
def vecNormalized(vx, vy, vz):
    length = math.sqrt(vx * vx + vy * vy + vz * vz)
    if length == 0 : return 0
    return Coordinates(vx / length, vy / length, vz / length)
DEFAULT_HEIGHT_BLOC = 5
class Traductor:
    '''
    classdocs
    '''
    def draw(self, city):
        self.drawField(city.getField())
        self.drawNetwork(city.getField().getNetworks())
        nbPlot = 0
        if len(city.getField().getDistricts()) > 0 :
            for district in city.getField().getDistricts():
                self.drawNetwork(district.getNetworks())
                if len(district.getblocks()) > 0 :
                    for bloc in district.getblocks():
                        self.drawBlock(bloc)
                        if len(bloc.getPlots()) > 0 :
                            for plot in bloc.getPlots():
                                nbPlot += 1
                                self.drawPlot(plot, nbPlot)
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
        index = 0
        index2 = 0
        if len(network) > 0:
            for road in network:
                index += 1
                index2 = 0
                if len(road.getWayPoints()) > 1:
                    print("draw a road")
                    for way in road.getWayPoints():
                        index2 += 1
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
                            self.drawPolygone([point1, point2, point3, point4], "road" + str(index) + str(index2))
                            
    def drawBlock(self, block):
        print("drawBlock")
    def drawPlot(self, plot, nbPlots):
        print("drawPlot")
        nomPlot = "plot"
        height = 0
        try:
            height = plot.height
        except AttributeError:
            height = DEFAULT_HEIGHT_BLOC

        corners = plot.corners
        if len(plot.corners) > 2:
            self.drawPolygone(corners, nomPlot + str(nbPlots))
            obj = bpy.context.scene.objects[nomPlot + str(nbPlots)]
            bpy.context.scene.objects.active = obj
            obj.select = True
            bpy.ops.object.mode_set(mode='EDIT') 
            bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, height), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "release_confirm":False})
            bpy.ops.object.mode_set(mode='OBJECT')  
            obj.select = False           
