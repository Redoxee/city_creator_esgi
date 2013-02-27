'''
Created on 27 févr. 2013

@author: Dylan
'''
import Coordinates
from math import acos
PI = 3.14159

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



def intersection(self,A,B,C,D):
    
    inter = Coordinates()
    # soit le segment [AB] d'équation yS = aS*xS + bS
    aS = None #coefficient directeur du segment [AB]
    bS = None # ordonée à l'origine du segment [AB]
    
    # soit le segment [CD] d'équation yF = aF*xF + bF
    aF = None #coefficient directeur du segment [CD]
    bF = None # ordonée à l'origine du segment [CD]

    # si aucun des deux segments n'est vertical
    if ((A.x!=B.x)and(C.x!=D.x)) :
        
        aS = (B.y-A.y)/(B.x-A.x)
        bS = (A.y*B.x - B.y*A.x)/(B.x-A.x)
        aF = (D.y-C.y)/(D.x-C.x)
        bF = (C.y*D.x - D.y*C.x)/(D.x-C.x)

        # le point d'intersection a alors pour coordonnées le couple solution du système   y = aS*x+bS
        #                                                                                  y = aF*x+bF
        det = aF-aS

        # on a donc l'inverse de la matrice  | aS  -1 |  égale à : __1__  t| -1 -aF |
        #                                    | aF  -1 |            aF-aS   |  1  aS |
        # qui nous permet de trouver x et y

        
        inter.x = (1/det)*(bS-bF)
        inter.y = (1/det)*(aF*bS-aS*bF)
    

    # si un des 2 segments est vertical
    else :
    
        if (A.x==B.x):
        
            aF = (D.y-C.y)/(D.x-C.x)
            bF = (C.y*D.x - D.y*C.x)/(D.x-C.x)

            inter.x = A.x
            inter.y = aF*inter.x + bF
        

        elif (C.x==D.x):
        
            aS = (B.y-A.y)/(B.x-A.x)
            bS = (A.y*B.x - B.y*A.x)/(B.x-A.x)

            inter.x = C.x
            inter.y = aS*inter.x + bS
        
    
    return inter


def appartient(M,A,B):
    # mauvaise précision pour le calcul des angles donc utilisation de valeurs approchées
    if (((angle(M,A,B)>179.9) and (angle(M,A,B)<180.1)) or ((angle(M,A,B)<-179.9) and (angle(M,A,B)>-180.1))):
        return True
    else :
        return False


def angle (P0,P1,P2) : #donne l'angle aglébrique (en degré) entre les vecteurs POP1 et P0P2

    angle = 0.0
    x1 = P1.x-P0.x  #coordonnées de P0P1
    y1 = P1.y-P0.y
    x2 = P2.x-P0.x  # coordonnées de POP2
    y2 = P2.y-P0.y

    nor1= pow(pow(x1,2)+pow(y1,2),1/2) # norme de POP1
    nor2= pow(pow(x2,2)+pow(y2,2),1/2) # norme de POP1
    scal = x1*x2+y1*y2

    if (scal==0) : angle=90
    else :
        cosA = scal/(nor1*nor2) # cosinus de l'angle (P0P1,P0P2)
        det =  x1*y2-y1*x2  # déterminant de la matrice | x1 x2 |
                            #                           | y1 y2 |
        if (det>0) : angle = acos(cosA)
        if (det<0) : angle = -acos(cosA)
    
    return angle*180/PI


def estInterieur(S,tabPoint,nombreDePoints):

    interieur = None  # variable résultat
    angleSum = 0   # somme des angles du point aux couples de sommets consécutifs

    for i in range(len(tabPoint)) :
        angleSum += angle(S,tabPoint[i],tabPoint[i+1])
    
    # Si le point est à l'intérieur du polygone
    if (((angleSum>359.9)and(angleSum<360.1))
       or ((angleSum<-359.9)and(angleSum>-360.1))) : # si l'angle est à peu près égal à + ou - 360°
        interieur=True  
    # S'il est en dehors
    else :
        interieur=False

    return interieur



def comparePoint(p1,p2):
    if( ( p1.x == p2.x ) and ( p1.y == p2.y ) ) :
        return True
    else :
        return False


def compareSegment(A,B):
    if ( comparePoint(A.P1,B.P1) and comparePoint(A.P2,B.P2)
         or comparePoint(A.P1,B.P2) and comparePoint(A.P2,B.P1)) :
        return True
    else :
        return False

