# -*- coding: utf-8 -*-

import upemtk as tk
from fonctions import *

def dessinerQuadrillage(largeurFenetre, hauteurFenetre, largeurCase, carte):
    #Dessine le quadrillage
    for i in range(len(carte)): #i les lignes
        for j in range(len(carte[i])): #j les colonnes
            if j != 0 and i != 0:#Condition pour qu'il n'y ai pas de quadrillage sur les côtés
                tk.ligne(j*largeurCase,0,j*largeurCase,hauteurFenetre)
                tk.ligne(0,i*largeurCase,largeurFenetre, i*largeurCase)
                
def dessinerCroix(x, y, largeur, couleur = 'black', epaisseur = 1):
    #Dessine une croix
    tk.ligne(x, y, x+largeur, y+largeur, couleur, epaisseur)
    tk.ligne(x, y+largeur, x+largeur, y, couleur, epaisseur)
    
def dessinerBoite(x, y, largeurCase, couleurCroix = "brown"):
    #Dessine un petit carré
    distanceAuBord = largeurCase/4
    tk.rectangle(x+ distanceAuBord, y+ distanceAuBord, x+largeurCase-distanceAuBord, y+largeurCase-distanceAuBord, "brown", "#ffa724",2, tag = "Carre-Boite")
    dessinerCroix(x+distanceAuBord, y+ distanceAuBord, largeurCase-distanceAuBord*2, couleurCroix, 2)

def dessinerMur(x, y,largeurCase):
    #Dessine le mur    
    largeurBrique = largeurCase / 2
    hauteurBrique = largeurCase / 4
    X,Y = 0,0
    for i in range(4):
        for j in range(2):
            if i % 2 == 0:
                tk.rectangle(x + X,y + Y,x + largeurBrique + X,y + hauteurBrique + Y,"white","brown")
            else:
                tk.rectangle(x + X + largeurBrique / 2,y + Y,x + largeurBrique * 1.5 + X,y + hauteurBrique + Y,"white","brown")
                tk.rectangle(x + X,y + Y,x + X + largeurBrique / 2,y + hauteurBrique + Y,"white","brown")
                tk.rectangle(x + largeurBrique * 1.5 + X,y + Y,x + 2 * largeurBrique,y + hauteurBrique + Y,"white","brown")
                break
            X += largeurBrique
        X = 0
        Y += hauteurBrique
    tk.rectangle(x, y, x+largeurCase, y+largeurCase, 'black', '')# Le contour de la case
     
def dessinerJoueur(x, y,largeurCase):
    #Dessine le joueur
    #Dessine un emplacement pour une caisse/ une cible
    rayon = largeurCase / 2.5
    cstCentrage = largeurCase / 2
    tk.cercle(x + cstCentrage,y + cstCentrage,rayon,"blue","blue", 2, tag = "Joueur")

def dessinerClef(x, y, largeurCase):
    #Dessine une clef
    rayon = largeurCase / 4
    espacementX = largeurCase / 3 - rayon
    espacementY = largeurCase / 2 - rayon
    #Cercle:
    positionX_cercle = x + espacementX + rayon
    positionY_cercle = y + espacementY + rayon
    tk.cercle(positionX_cercle,positionY_cercle,rayon, "#339933", "#339933")
    #Rectangle principal
    hauteurRectangle = rayon / 2.8
    tk.rectangle(positionX_cercle,positionY_cercle - hauteurRectangle,x + largeurCase - espacementX,positionY_cercle + hauteurRectangle, "#339933", "#339933")
    #Rectangles secondaires:
    PositionBDX_Rectangle2 = x + largeurCase - espacementX
    PositionBDY_Rectangle2 = y + largeurCase - espacementY - hauteurRectangle
    PositionHGX_Rectangle2 = PositionBDX_Rectangle2 - hauteurRectangle
    PositionHGY_Rectangle2 = y + espacementY + rayon + hauteurRectangle
    tk.rectangle(PositionHGX_Rectangle2, PositionHGY_Rectangle2,PositionBDX_Rectangle2,PositionBDY_Rectangle2, "#339933", "#339933")
    tk.rectangle(PositionHGX_Rectangle2 - 1.5*espacementX, PositionHGY_Rectangle2,PositionBDX_Rectangle2 - 1.5*espacementX,PositionBDY_Rectangle2, "#339933", "#339933")

def dessinerPorte(x, y,largeurCase):
    #Dessine une porte
    centreDuCercleX = x + largeurCase/2
    centreDuCercleY = y + largeurCase/2.5
    rayon = (largeurCase/3)//2
    tk.rectangle(x, y, x+largeurCase, y+largeurCase, 'black', '#339933')# Le reste de la case
    tk.cercle(centreDuCercleX, centreDuCercleY, rayon, 'black','black', 2)#Le rond de la serrure
    largeurRectangle1 = rayon/3
    #la serrure
    tk.rectangle(centreDuCercleX - largeurRectangle1, centreDuCercleY -10 + rayon, centreDuCercleX + largeurRectangle1, centreDuCercleY -10 + rayon+ largeurCase//3, 'black', 'black')

def dessinerInventaire(x, y, largeur, hauteur):
    tk.rectangle(x, y, x+largeur, y+hauteur, 'black', 'black')

def dessinerCible(x, y,largeurCase):
    #Dessine un emplacement pour une caisse/ une cible
    rayon = largeurCase/3
    cstCentrage = largeurCase / 2
    tk.cercle(x + cstCentrage,y + cstCentrage,rayon,"red","#ff5050", 2)
    tk.cercle(x + cstCentrage,y + cstCentrage,rayon/1.2,"red","#ff5050", 2)

def dessinerVictoire(largeurFenetre,hauteurFenetre):
    tk.texte(largeurFenetre // 4, hauteurFenetre // 3, "Victory !", 'black', police = "Times New Roman", taille = 60)


if __name__ == '__main__':
    """ Ce programme sert à tester les différentes fonctions de dessin """
    tk.cree_fenetre(300, 300)
    dessinerQuadrillage(300, 300, 100, [['.', '.','.'], 
                                ['.','.','.'],
                                ['.','.','.']])
    dessinerMur(0,0,100)
    dessinerClef(100,0,100)

    dessinerCible(0, 100, 100)
    dessinerBoite(100, 100, 100)

    dessinerJoueur(0, 200, 100)
    dessinerPorte(100, 200, 100)

    tk.attente_clic()
    tk.ferme_fenetre()
    
