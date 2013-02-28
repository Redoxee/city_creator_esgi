
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


    
        
    def drawField(self, field):
        print("drawField")
        nameField = 'Name'
        if(len(field.getBoundaries()) > 2):
            me = bpy.data.meshes.new(nameField + 'Mesh')
            ob = bpy.data.objects.new(nameField, me)
            ob.show_name = False
            # Link object to scene
            bpy.context.scene.objects.link(ob)
            arrayBounds = []
            for bound in  field.getBoundaries():
                arrayBounds.append((bound.x, bound.y, bound.z))
            listFaces = [range(len(field.getBoundaries()))]
            listFaces.append((()))
            
            listVertice = [arrayBounds]
            listVertice.append([])
            me.from_pydata(arrayBounds, [],listFaces)
#            me.from_pydata(((0,0,0),(1,0,0),(1,1,0),(0,1,0)), (), ((0,1,2,3),()))
            
    def drawNetwork(self, network):
        print("drawNetwork")
    def drawBlock(self, block):
        print("drawBlock")
    def drawPlot(self, plot):
        print("drawPlot")
