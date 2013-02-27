
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
    def drawNetwork(self, network):
        print("drawNetwork")
    def drawBlock(self, block):
        print("drawBlock")
    def drawPlot(self, plot):
        print("drawPlot")
