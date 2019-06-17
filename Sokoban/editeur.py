# -*- coding: utf-8 -*-
import upemtk as tk
from dessiner import *
from fonctions import *
from file import *
from deplacement import *

largeurCase = 70
largeurEditeur = 200

def generationFenetreEditeur(carte):
    """ Fonction qui calcule la taille de la fenêtre à partir d'une carte
    la fonction retourne les dimensions de la fenêtre crée (largeur et hauteur)
    """
    return(len(carte[0]) * largeurCase + largeurEditeur, len(carte) * largeurCase)


def transformeChaineVersCaractere(chaine):
    """ Le fonction prend en paramètre une chaine correspondante à un 'objet' de l'éditeur
    et renvoie son symbole
    """
    if chaine == "mur":
        return "W"
    elif chaine == "cible":
        return "T"
    elif chaine == "joueur":
        return "S" #pour mettre un futur point de départ sur la map
    elif chaine == "porte":
        return "D"
    elif chaine == "clef":
        return "K"
    elif chaine == "boite":
        return "B"
    else:
        return "."

def toucher(x, y, objet_x, objet_y, pos):
    """ la fonction retourne vrai si le pointeur x,y est dans le rectangle qui va de x jusqu'à y
    pos est un coefficient qui est le même que celui de l'affichage des objets et qui permet de les choisir facilement
    """
    if objet_x < x and x < objet_x + objet_y and objet_y * pos < y and y < objet_y + objet_y * pos:
        return True
    return False



def gestionClicGauche(clic):
    #Utilise l'objet évènement qui contient un clic, retourne l'objet de la barre d'édition séléctionné ou les coordonnées d'une case ou None
    x = tk.clic_x(clic)
    y = tk.clic_y(clic)

    if x < largeurFenetre-largeurEditeur: # le clic est sur la carte
        return y // largeurCase, x // largeurCase

    else:# le clic est sur la fenêtre d'édition
        # la position par défaut des objets avant d'appliqué le coefficient
        objet_x = largeurFenetre - largeurEditeur + largeurCase // 2
        objet_y = largeurCase * 1.5

        # détection de quel objet est touché par le clic
        if toucher(x, y, objet_x, objet_y, 0):
            return "mur"
        elif toucher(x, y, objet_x, objet_y, 1):
            return "cible"
        elif toucher(x, y, objet_x, objet_y, 2):
            return "joueur"
        elif toucher(x, y, objet_x, objet_y, 3):
            return "porte"
        elif toucher(x, y, objet_x, objet_y, 4):
            return "clef"
        elif toucher(x, y, objet_x, objet_y, 5):
            return "boite"
        else:
            return "vide"


def affichageEditeur(carte, selection, message):
    """ affichage de la fenêtre, la fonction affiche tout les éléments possibles """
    tk.efface_tout()

    #On parcourt la liste 2D (des sous listes dans une liste)
    dessinerQuadrillage(largeurEditeur//2+largeurFenetre, hauteurFenetre,largeurCase, carte)
    for i in range(len(carte)): #i les lignes
        for j in range(len(carte[i])): #j les colonnes
            if carte[i][j] == ".":#Case vide
                pass
            elif carte[i][j] == "W":#Wall
                dessinerMur(j * largeurCase, i * largeurCase, largeurCase)
            elif carte[i][j] == "T":#Target
                dessinerCible(j * largeurCase, i * largeurCase, largeurCase)
            elif carte[i][j] == "S":#Start
                dessinerJoueur(j * largeurCase, i * largeurCase, largeurCase)
            elif carte[i][j] == "D":#Door
                dessinerPorte(j * largeurCase, i * largeurCase, largeurCase)
            elif carte[i][j] == "K":#Key
                dessinerClef(j * largeurCase, i * largeurCase, largeurCase)
            elif carte[i][j] == "B":#Box
                dessinerBoite(j * largeurCase, i * largeurCase, largeurCase)
            elif carte[i][j] == "TB":#Box On a target
                dessinerCible(j * largeurCase, i * largeurCase, largeurCase)
                dessinerBoite(j * largeurCase, i * largeurCase, largeurCase)
            elif carte[i][j] == "TJ":#Player On a target
                dessinerCible(j * largeurCase, i * largeurCase, largeurCase)
                dessinerJoueur(j * largeurCase, i * largeurCase, largeurCase)
            elif carte[i][j] == "J":#Player
                dessinerJoueur(j * largeurCase, i * largeurCase, largeurCase)
            elif carte[i][j] == "KB":#Box On a key
                dessinerBoite(j * largeurCase, i * largeurCase, largeurCase, "green")

    #------- la fenêtre d'édition
    tk.rectangle(largeurFenetre-largeurEditeur, 0, largeurFenetre, hauteurFenetre, 'black', 'black')

    # la position de base des objets avant d'appliquer un coefficient
    x = largeurFenetre - largeurEditeur + largeurCase // 2 # la position de base des objets de l'éditeur
    y = largeurCase * 1.5

    # le texte
    tk.texte(0, 0, "Echap pour quitter","black")
    tk.texte(0, 40, "S pour sauvegarder","black")
    tk.texte(0, 80, "R pour tout effacer","black")

    #le message s'il y en a un
    if message[1] > 0:
        taille = 42
        #longueur texte est là pour centrer le  texte
        tk.texte(((largeurFenetre - largeurEditeur) - tk.longueur_texte(message[0]) * (taille / 24)) // 2, hauteurFenetre // 2, message[0],"#e82020", taille=taille)
    
    # Les objets selectionnables
    dessinerMur(x, y * 0, y)
    dessinerCible(x, y * 1, y)
    dessinerJoueur(x, y * 2, y)
    dessinerPorte(x, y * 3, y)
    dessinerClef(x, y * 4, y)
    dessinerBoite(x, y * 5, y)
    dessinerCroix(x, y * 6, y, "white")
    # les cadres verts de sélections
    if selection == "mur":
        tk.rectangle(x, y * 0, x + y, y + y * 0, 'green','', 7)
    elif selection == "cible":
        tk.rectangle(x, y * 1, x + y, y + y * 1, 'green','', 7)
    elif selection == "joueur":
        tk.rectangle(x, y * 2, x + y, y + y * 2, 'green','', 7)
    elif selection == "porte":
        tk.rectangle(x, y * 3, x + y, y + y * 3, 'green','', 7)
    elif selection == "clef":
        tk.rectangle(x, y * 4, x + y, y + y * 4, 'green','', 7)
    elif selection == "clef":
        tk.rectangle(x, y * 4, x + y, y + y * 4, 'green','', 7)
    elif selection == "boite":
        tk.rectangle(x, y * 5, x + y, y + y * 5, 'green','', 7)
    elif selection == "vide":
        tk.rectangle(x, y * 6, x + y, y + y * 6, 'green','', 7)

    tk.mise_a_jour()

def verifierCarte(carte):
    """ La fonction renvoie un tuple de la forme (bool, message)
    bool est un booleen qui confirme si la carte est bonne, et message est un message d'erreur si bool == false
    Les critères d'une bonne carte:
    - un seul joueur
    - moins ou autant de caisse que de cible
    - au moins une cible
    - au moins une caisse
    """
    if nombreDe(carte, "S") > 1:
        return False, ["Il ne peut y avoir qu'un seul joueur.", 1]
    if nombreDe(carte, "S") == 0:
        return False, ["Il n'y a pas de joueur.", 1]
    if nombreDe(carte, "T") == 0:
        return False, ["Il n'y a pas de cible.", 1]
    if nombreDe(carte, "B") == 0:
        return False, ["Il n'y a pas de caisse.", 1]
    if nombreDe(carte, "T") > nombreDe(carte, "B"):
        return False, ["Il y a plus de cible que de caisses.", 1]
    return True, ["", 0]

def initialiseCarte():
    """ Renvoie une carte vide """
    return [["." for i in range(14)] for j in range(11)]

def main():
    """ Fonction principale du programme """   
    global largeurFenetre, hauteurFenetre #Limiter les paramètres des fonctions

    #---------- Initialisation ----------
    carte = initialiseCarte()
    largeurFenetre, hauteurFenetre = generationFenetreEditeur(carte)
    tk.cree_fenetre(largeurFenetre, hauteurFenetre)
    selection = (0, 0) # pour savoir quel objet l'utilisateur a selectionné
    nouvelleSelection = (0, 0)
    message = ["", 0] # Un message à afficher à l'écran [0] contient le message et [1] contient un boolean d'affichage (0 ou 1)
    #-------- Fin initialisation --------

    # ---- Boucle principale du jeu
    quitter = False
    while not(quitter):

        #Affichage
        affichageEditeur(carte, selection, message) #Afficher la carte à l'écran

        #Retirer le message après un clic
        if message[1] > 0:
            message[1] = 0

        ############ Boucle de Gestion des évènements ############
        while True : # Boucle de récupération des évènements

            ev = tk.donne_evenement()
            typeEv = tk.type_evenement(ev)
            if typeEv == "Quitte": # Quand quelqu'un clique sur la croix pour fermer la fenêtre
                quitter = True
                break #Sortir de la boucle d'attente
            elif typeEv == "ClicGauche":
                nouvelleSelection = gestionClicGauche(ev)
                break
            elif typeEv == "ClicDroit":
                break
            elif typeEv == "Touche":
                # ------------ gestion des touches ------------
                touche = tk.touche(ev)
                if touche == "s":
                    # On vérifie la carte, on affiche un message si nécessaire ou on la sauvegarde
                    verification = verifierCarte(carte)
                    if verification[0]:
                        ecritureCarte(carte)
                        message = ["La carte a été sauvegardée !",1]
                    else:
                        message = verification[1]
                elif touche == "r":
                    nouvelleSelection = "vide" # pour éviter qu'un nouveau truc se place
                    carte = initialiseCarte()
                elif touche == "Escape":#touche pour sortir
                    quitter = True
                break
                # -------- fin de gestion des touches -------
                

            tk.mise_a_jour() #mise à jour des évènements
        ############ Fin de gestion des évènements ############

        #------ Changements sur le jeu
        if nouvelleSelection not in {"mur","cible","joueur","porte","clef","boite","vide"}:
            i, j = nouvelleSelection # on place l'objet sélectionné sur la case
            carte[i][j] = transformeChaineVersCaractere(selection)
        else: # si un nouveau truc est sélectionné, on le change
            selection = nouvelleSelection
        #-------
    tk.ferme_fenetre()

if __name__ == '__main__':
    """ Ce programme sert à éditer et sauvegarder une map """
    main()
