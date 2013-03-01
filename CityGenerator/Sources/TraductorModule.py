
import bpy
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


    def drawPolygone(self,boundaries,namePoly):
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
            me.from_pydata(arrayBounds, [],listFaces)
            
    def drawField(self, field):
        print("drawField")
        nameField = 'Name'
        self.drawPolygone(field.getBoundaries(), nameField)

            
    def drawNetwork(self, network):
        print("drawNetwork")
        if len(network) > 0:
            for way in network:
                if  not way == None:
                    self.drawWay(way)
    def drawWay(self,road):
        print("drawWays")
        if len(road) > 0:
            for wayPoint in road:
                print ("drawwaypoints")
    def drawBlock(self, block):
        print("drawBlock")
    def drawPlot(self, plot):
        print("drawPlot")
