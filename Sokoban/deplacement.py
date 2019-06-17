# -*- coding: utf-8 -*-

import upemtk as tk
from fonctions import *
from __init__ import recharger, affichage
from random import randint

def attenteMouvement(carte, infoMap):
    """ Cette fonction s'éxécute sans fin dans l'attente d'une action du joueur (clic, clavier,quitter) 
    Elle retourne le type de la touche
    """
    while True:
        event = tk.donne_evenement() # objet event de tk
        typeEvent = tk.type_evenement(event) # type de l'event

        # Lorsque l'évènement est une touche, on regarde laquelle et on la renvoie
        if typeEvent == 'Touche': 
            typeEvent = tk.touche(event) 
            if typeEvent in {"Left", "Right", "Up", "Down", "d", "e", "r", "s", "b", "Escape"}:
                break
        # Lorsque l'évènement est un autre dans cette liste, pareil
        elif typeEvent in {"Quitte","ClicGauche"}:
            break
        tk.mise_a_jour() #Mettre à jour les évènements
    return typeEvent 

def debugDeplacement(carte, infoMap, inventaire):
    #Fonction qui nous permet d'effectuer le déplacement aléatoire du joueur de manière automatique
    largeurFenetre, hauteurFenetre, largeurInventaire = infoMap[0], infoMap[1], infoMap[2] #Affectations pour plus de clarté
    while True:
        nb = randint(1,4) #Génération d'un entier entre 1 et 4 qui va engendrer un mouvement aléatoire du joueur
        if nb == 1:
            carte = mouvement(0,-1,carte, inventaire) #Gauche
        elif nb == 2:
            carte = mouvement(0,1,carte, inventaire) #Droite
        elif nb == 3:
            carte = mouvement(-1,0,carte, inventaire) #Haut
        elif nb == 4:
            carte = mouvement(1,0,carte, inventaire) #Bas
        affichage(largeurFenetre, hauteurFenetre, largeurInventaire, inventaire, carte) #Afficher la carte à l'écran
        
        event = tk.donne_evenement() #Récupérer un évènement
        typeEvent = tk.type_evenement(event) #Récupérer son type
        if typeEvent == 'Touche':
            typeEvent = tk.touche(event) #Récupérer la touche
            if typeEvent == "d": #Si la touche est 0, fin de boucle
                break
        if partieGagnee(carte):
            break
        tk.mise_a_jour() #Mise à jour de l'évènement
    return carte

def typeMouvement(typeEvent, carte, infoMap, inventaire):
    #Faire bouger le joueur selon la touche qu'il a utilisé ou encore ouvre le mode débug
    if typeEvent == "Left": #Gauche
        carte = mouvement(0,- 1, carte, inventaire)
    elif typeEvent == "Right": #Droite
        carte = mouvement(0, 1, carte, inventaire)
    elif typeEvent == "Up": #Haut
        carte = mouvement(-1, 0, carte, inventaire)
    elif typeEvent == "Down": #Bas
        carte = mouvement(1, 0, carte, inventaire)
    elif typeEvent == "d": #Débug
        carte = debugDeplacement(carte, infoMap, inventaire)
    else: #Sélection d'une case pour la tirer
        carte = typeTirerCaisse(carte, infoMap, inventaire)
    return carte

def tirerCaisse(carte, cst_i, cst_j, i, j, inventaire):
    #Modifie la carte par rapport au tirage d'une box vers un joueur
    #Les constantes cst_i (ligne) et cst_j (colonne) dépendent de la touche utilisée par le joueur (voir typeTirerCaisse)
    if 0 <= i + cst_i and i + cst_i < len(carte) and 0 <= j + cst_j and j + cst_j < len(carte[0]): #Si l'index de la box existe
        if 0 <= i - cst_i and i - cst_i < len(carte) and 0 <= j - cst_j and j - cst_j < len(carte[0]): #Si l'index où le joueur va se diriger existe
            if "B" in estQuoi(i + cst_i,j + cst_j,carte) and (estDeplacable(i - cst_i,j - cst_j,carte) or (carte[i - cst_i][j - cst_j] == "D" and inventaire["nbClefs"] > 0)): #Si la case à bouger est de type "boite" et quelle est déplaçable, c'est coorect. Sinon, sinon, la case à bouger est de type "boite" et que la case vers lequel se dirige le joueur est une door et qu'il a au moins une clef (cas particulier), c'est correct aussi.
                #Gestion de l'endroit ou était située la box
                case = carte[i + cst_i][j + cst_j]
                if case == "TB": #Si target on a box,...
                    carte[i + cst_i][j + cst_j] = "T" #Target
                elif case == "KB": #Si key on a box ...
                    carte[i + cst_i][j + cst_j] = "K" #Clef
                else: #Si c'est une box basique
                    carte[i + cst_i][j + cst_j] = "." #Vide
                #Gestion de l'endroit ou le joueur va se déplacer
                case = carte[i - cst_i][j - cst_j]
                if case == "T": #Si c'est un target
                    carte[i - cst_i][j - cst_j] = "TJ" #Player on a target
                elif case == "K": #Si c'est une clef
                    inventaire["nbClefs"] += 1 #Gagne la clé (inventaire)
                    carte[i - cst_i][j - cst_j] = "J" #Player
                elif case == "D":
                    inventaire["nbClefs"] -= 1 #Décrémmentation du nombre de clefs
                    carte[i - cst_i][j - cst_j] = "J" #Player
                    inventaire["nbCoups"] += 1 #Condition pour ne pas comptabiliser le déplacement
                else: #Si c'est un "."
                    carte[i - cst_i][j - cst_j] = "J" #Player
                #Gestion de l'endroit ou était situé le joueur
                if carte[i][j] == "TJ": #Target
                    carte[i][j] = "TB" #Box on a target
                else: #Si case normale
                    carte[i][j] = "B" #Box classique
                inventaire["nbCoups"] += 1 #Comptabiliser un déplacement
    return carte

def typeTirerCaisse(carte, infoMap, inventaire):
    #Appelle la fonction tirerCaisse qui effectue les modifications sur la carte si les conditions de "tirage de boîte" sont remplies
    i,j = indexJoueur(carte) #On stocke les positions du joueur: i pour la ligne et j pour la colonne (NB: on n'aura pas à tester la validité des index du joueur par la suite)
    typeEvent = attenteMouvement(carte, infoMap) #On attend un évènement de type flèche au clavier ou 0 (mode débug) ou 1 (sélection d'une box à tirer) et on la stocke dans la variable typeEvent
    if typeEvent == "Left": #Gauche
        carte = tirerCaisse(carte, 0, 1, i, j, inventaire)
    elif typeEvent == "Right": #Droite
        carte = tirerCaisse(carte, 0, -1, i, j, inventaire)
    elif typeEvent == "Up": #Haut
        carte = tirerCaisse(carte, 1, 0, i, j, inventaire)
    elif typeEvent == "Down": #Bas
        carte = tirerCaisse(carte, -1, 0, i, j, inventaire)
    elif typeEvent == "d": #Lancement du mode débug
        carte = debugDeplacement(carte, infoMap, inventaire)

    return carte #Actualisation de la carte

def mouvement(cst_i, cst_j, carte, inventaire):
    #Si le mouvement "basique" du joueur est possible, alors effectuer les modifications sur la carte
    i,j = indexJoueur(carte) #Stocker l'index du joueur
    if 0 <= i + cst_i and i + cst_i < len(carte) and 0 <= j + cst_j and j + cst_j < len(carte[i]): #Ne pas sortir de la carte
        case = estQuoi(i + cst_i, j + cst_j, carte)
        if case in {'.', 'T', 'S', 'K', 'D', 'TK'}: 
            #Si il est possible d'avancer, gestion de la case où le joueur va
            if case == 'T':
                carte[i + cst_i][j + cst_j] = 'TJ' #Player on a target
            elif case == "D":
                if inventaire["nbClefs"] > 0: #Si c'est une porte et que le joueur possède au moins une clé, ...
                    carte[i + cst_i][j + cst_j] = "J" #Il l'ouvre
                    inventaire["nbClefs"] -= 1
            else:
                if case in {"K","TK"}: #Si la case est de type clé, ...
                    inventaire["nbClefs"] += 1 #Incrémentation du nombre de clefs
                carte[i + cst_i][j + cst_j] = 'J' #Joueur
            #Gestion de case où le joueur était
            if carte[i][j] == 'TJ': #Si c'est une player on a target, ...
                carte[i][j] = 'T' #Target
                inventaire["nbCoups"] += 1 #Incrémentation du nombre de coups
            else:
                if "J" in estQuoi(i + cst_i, j + cst_j, carte): #Sinon, si le joueur a été déplacé, ...
                    carte[i][j] = '.' #Vide
                    inventaire["nbCoups"] += 1 #Incrémentation du nombre de coups
        elif case in {'B','TB','KB'}: #Si c'est une boîte
            if estDeplacable(i + 2 * cst_i,j + 2 * cst_j, carte): #Si la case située derrière la caisse à l'opposé du joueur rends possible un déplacement
                carte = deplacerCaisse(i + cst_i, j + cst_j, i + 2 * cst_i, j + 2 * cst_j, carte, inventaire) #Modifier la carte
                inventaire["nbCoups"] += 1 #Incrémentation du nombre de coups
    return carte

def deplacerCaisse(avant_i, avant_j, apres_i, apres_j, carte, inventaire):
    #Permet de pousser une caisse
    i, j = indexJoueur(carte) #Socker l'index du joueur
    #Gestion de la case où était le joueur
    if carte[i][j] == 'TJ': #Si le joueur est sur un target, ...
        carte[i][j] = 'T' #Target
    else:
        carte[i][j] = '.' #Vide
    #Gestion de la case ou était la box
    case = carte[avant_i][avant_j]
    if case == 'TB': #Si la box était sur un target, ...
        carte[avant_i][avant_j] = 'TJ' #Joueur on a target
    else:
        if case == 'KB': #Si la box est sur une clef, ...
            inventaire["nbClefs"] += 1 #Incrémentation du nombre de clef
        carte[avant_i][avant_j] = "J" #Joueur
    #Gestion de la case ou la boîte va aller
    case = carte[apres_i][apres_j]
    if case == 'T': #Si c'est un target, ...
        carte[apres_i][apres_j] = 'TB' #Box on a target
    elif case == 'K': #Si c'est une clé
        carte[apres_i][apres_j] = 'KB' #Key on a box
    else:
        carte[apres_i][apres_j] = 'B' #Sinon, la case devient une box "classique"
    return carte

def estDeplacable(i, j, carte):
    #Renvoie True s'il n'y a rien derrière la caisse à l'opposé du joueur
    #i et j sont les cordonnées de cette caisse
    if 0 <= i and i < len(carte) and 0 <= j and j < len(carte[i]):
        if estQuoi(i, j, carte) in {'.', 'T', 'S', 'K', 'TK'}: #Si la case où avancer est vide ou il y a un objectif
            return True
    return False

if __name__ == '__main__':
    pass
    #print(doctest.testmod()) #Pour tester toutes les fonctions