'''
Created on 26 févr. 2013

@author: Antoine
'''

import FieldClipper
import Coordinates

class ManhattanClipper(FieldClipper):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super.__init__();
        
        
    def coupe(self,A,B,C,D):
        detACAD = (C.x-A.x)*(D.y-A.y)-(C.y-A.y)*(D.x-A.x)
        detBCBD = (C.x-B.x)*(D.y-B.y)-(C.y-B.y)*(D.x-B.x)
        detCACB = (A.x-C.x)*(B.y-C.y)-(A.y-C.y)*(B.x-C.x)
        detDADB = (A.x-D.x)*(B.y-D.y)-(A.y-D.y)*(B.x-D.x)
    
        # si les déterminants sont de signes opposés 2 à 2, alors alors les 2 segments se croisent
        if (((detACAD >= 0 and detBCBD <= 0) or (detACAD <= 0 and detBCBD >= 0)) and
            ((detCACB >= 0 and detDADB <= 0) or (detCACB <= 0 and detDADB >= 0))) :
            return True
        else :
            return False
        
        
    def subdivide(self,polygon,minLength,minWidth):
        """"prend en paramètre un polygone de n côtés et n+1 sommets (avec le premier sommet égal au dernier),
        ainsi que la longueur et la largeur minimales attendues des parties que l'on souhaite découper"""
        
        # on récupère le plus grand côté du polygone pour en faire la base de la figure
        maxLength = 0
        supportEdge = 0
        supportLength = pow(pow(polygon[supportEdge+1].x-polygon[supportEdge].x,2)
                                   + pow(polygon[supportEdge+1].y-polygon[supportEdge].y,2),1/2)
        for i in range(len(polygon)) :
            length = pow(pow(polygon[i+1].x-polygon[i].x,2)+pow(polygon[i+1].y-polygon[i].y,2),1/2)
            if length>maxLength : supportEdge=i
        # on cherche la hauteur du polygone (par rapport à cette base): pour chaque sommet autre que les
        # deux qui composent la base, on calcule la distance qui le sépare de son projeté sur la droite
        # support du segment de base
        maxHeight = 0
        for n in range(len(polygon)) :
            if (n!=supportEdge) and (n!=supportEdge+1) : 
                ScalProd = (polygon[supportEdge+1].x-polygon[supportEdge].x) * (polygon[n].y-polygon[i].y) \
                           - (polygon[supportEdge+1].y-polygon[supportEdge].y) * (polygon[n].x-polygon[i].x)
                H=Coordinates(polygon[i].x + ScalProd*(polygon[supportEdge+1].x - polygon[supportEdge+1].x)/supportLength,
                              polygon[i].y + ScalProd*(polygon[supportEdge+1].y - polygon[supportEdge+1].y)/supportLength)
            height = pow(pow(polygon[n].x-H.x,2) + pow(polygon[n].y-H.y,2),1/2)
            if height > maxHeight:
                maxHeight = height
        # on va ensuite diviser cette hauteur par le plus grand nombre entier tel que la longueur obtenue soit
        # supérieure à la longueur minimale passée en paramètre
        cellLength = maxHeight
        newCellLength = maxHeight
        numberOfCells = 1
        while (cellLength>minLength) :
            cellLength = newCellLength
            numberOfCells = numberOfCells + 1
            newCellLength = maxHeight/(numberOfCells)
            
        # on va ensuite diviser la longueur du segment de base par le plus grand nombre entier tel que la largeur
        # obtenue soit supérieure à la largeur minimale passée en paramètre
        cellWidth = supportLength
        newCellWidth = supportLength
        numberOfCells = 1
        while (cellWidth>minWidth) :
            cellWidth = newCellWidth
            numberOfCells = numberOfCells + 1
            newCellWidth = supportLength/(numberOfCells)
            
        # on définit ensuite la liste des routes qui sépareront la zone à découper : On part du premier sommet du
        # segment de base du polygone, et cherche lequel des autres côtés du polygone croise la perpendiculaire à la base
        # on fait effectue ensuite la même opération en avançant sur le segment de base, d'une distance égale à la largeur
        # des blocs souhaités
        
        for j in range(len(polygon)) :
            if (j!=supportEdge) and (j!=supportEdge+1) : 
                ScalProd = (polygon[supportEdge+1].x-polygon[supportEdge].x) * (polygon[n].y-polygon[i].y) \
                           - (polygon[supportEdge+1].y-polygon[supportEdge].y) * (polygon[n].x-polygon[i].x)
                H=Coordinates(polygon[i].x + ScalProd*(polygon[supportEdge+1].x - polygon[supportEdge+1].x)/supportLength,
                              polygon[i].y + ScalProd*(polygon[supportEdge+1].y - polygon[supportEdge+1].y)/supportLength)
            height = pow(pow(polygon[n].x-H.x,2) + pow(polygon[n].y-H.y,2),1/2)
            if height > maxHeight:
                maxHeight = height
                
                
                
                
                
                
