
from FieldClipper import FieldClipper
import Coordinates
import Utils


class ManhattanClipper(FieldClipper):

    def __init__(self, field):
        FieldClipper.__init__(self, field);     
        

    def subdivide(self,polygon,minLength,minWidth):
        """"prend en param�tre un polygone de n c�t�s et n+1 sommets (avec le premier sommet �gal au dernier),
        ainsi que la longueur et la largeur minimales attendues des parties que l'on souhaite d�couper"""
        
        if len(polygon) <= 3 : return False
        
        # on r�cup�re le plus grand c�t� du polygone pour en faire la base de la figure
        maxLength = 0
        supportEdge = 0
        for i in range(len(polygon)) :
            length = pow(pow(polygon[i+1].x-polygon[i].x,2)+pow(polygon[i+1].y-polygon[i].y,2),1/2)
            if length>maxLength :
                maxLength = length
                supportEdge=i
        supportLength = maxLength
        # on d�finit alors les deux vecteurs d'un rep�re orthonormal normal local (direct ou indirect selon le sens du polygone)
        I = Coordinates( (polygon[supportEdge+1].x - polygon[supportEdge].x)/supportLength ,
                         (polygon[supportEdge+1].y - polygon[supportEdge].y)/supportLength)
        J = None
        n = 0
        while J==None :
            if Utils.angle(polygon[n],polygon[n+1],polygon[n+2])<0:
                J = Coordinates(I.y,-I.x)
            elif Utils.angle(polygon[n],polygon[n+1],polygon[n+2])>0:
                J = Coordinates(-I.y,I.x)
            else : n+=1
        # on cherche la hauteur du polygone (par rapport � cette base): pour chaque sommet autre que les
        # deux qui composent la base, on calcule la distance qui le s�pare de son projet� sur la droite
        # support du segment de base
        maxHeight = 0
        for n in range(len(polygon)) :
            if (n!=supportEdge) and (n!=supportEdge+1) : 
                ScalProd = (polygon[supportEdge+1].x-polygon[supportEdge].x) * (polygon[n].y-polygon[i].y) \
                           - (polygon[supportEdge+1].y-polygon[supportEdge].y) * (polygon[n].x-polygon[i].x)
                H=Coordinates(polygon[i].x + ScalProd*I.x , polygon[i].y + ScalProd*I.y)
            height = pow(pow(polygon[n].x-H.x,2) + pow(polygon[n].y-H.y,2),1/2)
            if height > maxHeight:
                maxHeight = height
        # on va maintenant diviser cette hauteur par le plus grand nombre entier tel que la longueur obtenue soit
        # sup�rieure � la longueur minimale pass�e en param�tre
        cellLength = maxHeight
        newCellLength = maxHeight
        numberOfRows = 1
        while (newCellLength>minLength) :
            cellLength = newCellLength
            numberOfRows = numberOfRows + 1
            newCellLength = maxHeight/(numberOfRows)
        numberOfRows-=1 
        # on va ensuite diviser la longueur du segment de base par le plus grand nombre entier tel que la largeur
        # obtenue soit sup�rieure � la largeur minimale pass�e en param�tre
        cellWidth = supportLength
        newCellWidth = supportLength
        numberOfColumns = 1
        while (newCellWidth>minWidth) :
            cellWidth = newCellWidth
            numberOfColumns = numberOfColumns + 1
            newCellWidth = supportLength/(numberOfColumns)
        numberOfColumns-=1
            
        # on d�finit ensuite la liste des routes perpendiculaires � la base qui s�pareront la zone � d�couper : on part
        # du premier sommet du segment de base du polygone, et on cherche lequel des autres c�t�s du polygone croise la
        # perpendiculaire � la base, puis on effectue ensuite la m�me op�ration en avan�ant sur le segment de base, d'une
        # distance �gale � la largeur des blocs souhait�s 
        perpendicularRoads = []
        for i in range(numberOfColumns+1) :
            perpendicularRoads[i] = None
            
        for i in range(numberOfColumns+1) :
            perp1 = Coordinates(polygon[supportEdge].x + i*cellWidth*I.x,
                                polygon[supportEdge].y + i*cellWidth*I.y)
            perp2 = Coordinates(perp1.x + maxHeight*J.x , perp1.y + maxHeight*J.y)
            for n in range(len(polygon)) :
                if (n!=supportEdge) :
                    if Utils.cross(perp1,perp2,polygon[n],polygon[n+1]):
                        inter=Utils.intersection(perp1,perp2,polygon[n],polygon[n+1])
                        perpendicularRoads[i] = [perp1,inter]
                        
        # On cherche maintenant la liste des routes parall�les au segment de base, en parcourant la premi�re des perpendiculaires
        # pr�c�demment d�finies par intervalles r�guliers (de longeur �gale � la longueur des cellules). Pour chacun des points
        # parcourus, on trace la perpendiculaire (donc parall�le au segment de base) et on cherche les 2 points d'intersection avec
        # des c�t�s du polygone, soit de part et d'autre de notre segment (si le point est dans le polygone), soit tous deux du m�me
        # c�t� du segment (si le point est en dehors)               
        parallelRoads = []
        for j in range(numberOfRows+1) :
            parallelRoads[j] = None
            
        for j in range(numberOfRows) :
            paral0 = Coordinates(polygon[supportEdge].x + i*cellLength*J.x,
                                polygon[supportEdge].y + i*cellLength*J.y)
            paral1 = None
            paral2 = None
            # Si le point est � l'int�rieur du polygone : on cherche une intersection de chaque c�t� du segment
            if Utils.isInside(paral0,polygon) :
                l = 0
                while paral1==None :
                    l += supportLength
                    paralL = Coordinates(paral0.x+l*I.x , paral0.y+l*I.y)
                    for n in range(len(polygon)) :
                        if Utils.cross(paral0,paralL,polygon[n],polygon[n+1]):
                            paral1=Utils.intersection(paral0,paralL,polygon[n],polygon[n+1])
                l=0            
                while paral2==None :
                    l += supportLength
                    paralL = Coordinates(paral0.x-l*I.x , paral0.y-l*I.y)
                    for n in range(len(polygon)) :
                        if Utils.cross(paral0,paralL,polygon[n],polygon[n+1]):
                            paral2=Utils.intersection(paral0,paralL,polygon[n],polygon[n+1])
            # si le point est en dehors du polygone, on cherche les deux intersections du m�me c�t� du segment
            else :
                l = 0
                while paral2==None :
                    l += supportLength
                    paralL = Coordinates(paral0.x+l*I.x , paral0.y+l*I.y)
                    for n in range(len(polygon)) :
                        if Utils.cross(paral0,paralL,polygon[n],polygon[n+1]):
                            if paral1==None :
                                paral1=Utils.intersection(paral0,paralL,polygon[n],polygon[n+1])
                            elif paral2==None :
                                paral2=Utils.intersection(paral0,paralL,polygon[n],polygon[n+1])                        
        parallelRoads[j] = Coordinates(paral1,paral2)    
        return perpendicularRoads + parallelRoads        