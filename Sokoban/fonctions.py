# -*- coding: utf-8 -*-

from random import randint
from file import *

#.................................................................................#
#fonctions génériques
def recharger():
    """ Fonction qui lit le fichier de sauvegarde et qui renvoie la carte et l'inventaire
    """
    carte, inventaire = lectureFichierSauvegarde()
    return carte, inventaire

def generationFenetre(carte):
    """ Cette fonction calcul la taille de la fenêtre à ouvrir en fonction de son nombre de case
    Elle renvoie les dimensions de la fenêrte et la largeur de l'inventaire 
    """
    nbrDeLigne = len(carte)
    nbrDeColonne = len(carte[0])
    largeurCase = 50
    largeurInventaire = 100 #La barre à droite
    fenetre_largeur = nbrDeColonne * largeurCase +largeurInventaire
    fenetre_hauteur = nbrDeLigne * largeurCase
    return(fenetre_largeur, fenetre_hauteur, largeurInventaire)

def initialisationMap(numeroDeMap):
    """ La fonction initialise la map et l'inventaire et les renvoie """
    inventaire = dict()
    inventaire["nbClefs"] = 0
    inventaire["nbCoups"] = 0
    carte = lectureFichier("map/map"+str(numeroDeMap))
    return carte, inventaire

def nombreDe(carte, symbole):
    """ La fonction compte le nombre de fois qu'un objet précis est dans la carte
    symbole est le caractère ou la chaine qui est utilisé dans la map
    """
    compteur = 0
    for i in range(len(carte)):
        for j in range(len(carte[i])):
            if carte[i][j] == symbole:
                compteur += 1
    return compteur

def partieGagnee(carte):
    """
    >>> partieGagnee([['W','W','W','W'],['W','W','.','W']])
    True
    >>> partieGagnee([['T','W','W','W'],['W','W','.','W']])
    False
    >>> partieGagnee([['.','W','W','W'],['W','T','.','W']])
    False
    """
    """ Renvoie vrai si la partie est gagnée """
    for i in range(len(carte)): #i les lignes
        for j in range(len(carte[i])): #j les colonnes
            if carte[i][j] in {"T", "TJ", "KB"}: #Si on ne trouve pas de target de ce type dans la carte, c'est gagné.
                return False
    return True
    
def estVide(i, j, carte):
    """ Renvoie vrai si la case carte[i][] est vide """
    """
    >>> estVide(1,0, [['W','W','W','W'],['.','W','W','W'],['W','W','W','W']])
    True
    >>> estVide(1,2, [['W','W','W','W'],['W','W','.','W']])
    True
    >>> estVide(1,1, [['W','W','W','W'],['W','W','.','W']])
    False
    """
    if estQuoi(i, j, carte) == '.':
        return(True)
    return(False)

def estQuoi(i, j, carte):#i ligne et j colonne
    """
    >>> estQuoi(1,0, [[0,1,2,3],[4,5,6,7],[8,9,10,11]])
    4
    >>> estQuoi(2,1, [[0,1,2,3],[4,5,6,7],[8,9,10,11]])
    9
    """
    #Renvoie en caractère le nom de l'objet dans la case
    return(carte[i][j])

def indexJoueur(carte):
    """ Renvoie la poristion du premier joueur trouvé dans la carte """
    """
    >>> indexJoueur([['W','S','W','W'],['W','W','.','W']])
    (0, 1)
    >>> indexJoueur([['W','T','J','W'],['W','W','.','W']])
    (0, 2)
    >>> indexJoueur([['W','T','.','W'],['W','W','.','W']])
    Traceback (most recent call last):
    AssertionError
    """
    for i in range(len(carte)): #i les lignes
        for j in range(len(carte[i])): #j les colonnes
            if carte[i][j] in {"J","S","TJ"}: #Si le joueur est sur la case de départ
                return(i, j)
    assert() #Erreur: il n'y a plus de joueur

def largeurDeCase(largeurFenetre, hauteurFenetre, carte):
    """
    >>> largeurDeCase(300,300,[[0,1,2],[3,4,5],[6,7,8]])
    100
    """
    #Fonction qui renvoie la largeur d'une case
    nbrDeCase = len(carte[0])
    largeurInventaire = 100
    return((largeurFenetre-largeurInventaire)//nbrDeCase)