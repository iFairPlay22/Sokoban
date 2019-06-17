# -*- coding: utf-8 -*-
import string

def lectureFichier(nomFichier):
    # On lit la carte au format .txt et la renvoie sous forme de liste 2D (Matrice)
    carte, ligne_actuelle, l1 = [], [], True #Initialisation
    with open(nomFichier,'r') as fichier:
        for ligne in fichier:
            for caractere in ligne:           
                if caractere != "\n":
                    ligne_actuelle.append(caractere)
            carte.append(ligne_actuelle)#On ajoute la ligne à la carte
            ligne_actuelle = []#reset
    resultat = carte[1:]
    verifierCarte(resultat)
    return resultat

def verifierCarte(carte):
    #Verifie si la carte est valable et l'ajuste dans certains cas
    if carte:
        hauteurCarte, longueurCarte, nbJoueur = len(carte), max({len(lst) for lst in carte}), 0
        for i in range(hauteurCarte):
            for j in range(len(carte[i])):
                nbJoueur = modifierEnPlace(carte, i, j, nbJoueur)
            #Gestion des matrices non carrées
            if len(carte[i]) != longueurCarte:
                diffTaille = longueurCarte - len(carte[i])
                print("Erreur de taille de carte:", diffTaille,"murs seront ajoutés en ligne", i, "\b.")
                for k in range(diffTaille):
                    carte[i].append("W")
        #Gestion de l'absence de joueurs
        if nbJoueur == 0:
            print("Erreur: étant donné qu'il n'y a pas d'emplacement réservé pour le joueur, celui-ci a été ajouté en position 0 0.")
            carte[0][0] = "S"
        #Gestion de la taille maximale de la matrice
        if 6 <= hauteurCarte and hauteurCarte < 35 and 3 <= longueurCarte and longueurCarte <= 25:
            return carte
        print("Erreur: format de carte invalide\nTaille minimum: 6 x 3\nTaille maximum: 25 x 35\nTaille actuelle:", hauteurCarte, "x", longueurCarte)
        assert()
    print("Erreur: La carte est vide.")
    assert()

def modifierEnPlace(carte, i, j, nbJoueur):
    #Fonction qui modifie la carte pour palier à certaines erreurs de carte
    #Gestion des caractères indésirables
    if not(carte[i][j] in {".", "W", "T", "S", "D", "K", "B", "TB", "KB"}):
        print("Erreur dans la carte: le caractère", carte[i][j], "située à la ligne", i,"sera remplacé par un mur.")
        carte[i][j] = "W"
    #Gestion du nombre trop important de joueurs
    if carte[i][j] == "S":
        nbJoueur += 1
    if nbJoueur > 1:
        print("Erreur concernant le nombre de joueurs: celui-ci sera remplacé par une case vide en position", i, j,"\b.")
        carte[i][j] = "."
    return nbJoueur

def lectureFichierSauvegarde():
    carte, inventaire = [], dict()
    with open("map/mapSaved",'r') as fichier:
        texte = fichier.read()
    texte = texte.split("\n")
    inventaire = {"nbClefs": int(texte[1]),"nbCoups": int(texte[2])}
    texte = texte[3:-1]#pour retirer les infos du dico au début et retirer le "" vide à la fin
    for i in range(len(texte)):
        texte[i] = texte[i].split("][")# caractère délimiteur
        texte[i].pop()
    for chaine in texte:
        sousListe = []
        for caractere in chaine:
            sousListe.append(caractere)
        carte.append(sousListe)
    return carte, inventaire

def ecritureCarte(carte):
    #Pour créer une carte à partir de l'éditeur
    texte = 'Titre : "mapEdited"\n'
    for ligne in carte:
        for element in ligne:
            texte += element
        texte += "\n"
    with open("map/mapEdited" ,"w") as f:
        f.write(texte)


def ecritureFichierSauvegarde(liste, inventaire):
    #Pour créer une carte/sauvegarder une partie en cours
    texte = 'Titre : "mapSaved"\n' + str(inventaire["nbClefs"])+ "\n" + str(inventaire["nbCoups"])+"\n"
    for sousListe in liste:
        for element in sousListe:
            texte += element+"]["#caractère pour split
        texte += "\n"
    with open("map/mapSaved" ,"w") as f:
        f.write(texte)


