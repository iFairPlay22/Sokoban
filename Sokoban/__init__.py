# -*- coding: utf-8 -*-
import upemtk as tk
import doctest
from dessiner import *
from deplacement import *
from file import *
from fonctions import *

def affichage(largeurFenetre, hauteurFenetre, largeurInventaire, inventaire, carte):
    """ affichage de la fenêtre, la fonction affiche tout les éléments possibles """
    tk.efface_tout()

    #On met à jour la fenêtre et on affiche chaque élément
    largeurCase = largeurDeCase(largeurFenetre, hauteurFenetre, carte)
    #On parcourt la liste 2D (des sous listes dans une liste)
    dessinerQuadrillage(largeurFenetre, hauteurFenetre,largeurCase, carte) # on peut retirer cette ligne pour que ça soit plus jolie
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
            elif carte[i][j] == "TJ":#Joueur On a target
                dessinerCible(j * largeurCase, i * largeurCase, largeurCase)
                dessinerJoueur(j * largeurCase, i * largeurCase, largeurCase)
            elif carte[i][j] == "J":#Joueur
                dessinerJoueur(j * largeurCase, i * largeurCase, largeurCase)
            elif carte[i][j] == "KB":#Box On a key
                dessinerBoite(j * largeurCase, i * largeurCase, largeurCase, "green")

    n = largeurFenetre - largeurInventaire
    dessinerInventaire(n, 0, largeurInventaire, hauteurFenetre)
    dessinerClef(n, 0, largeurCase * 2)

    #largeurCase/1.5 ou largeurCase/15 est là pour centrer le texte 
    tk.texte(n + largeurCase / 1.5, largeurCase * 2, inventaire["nbClefs"], "white")
    tk.texte(n + largeurCase / 1.5, largeurCase * 4, inventaire["nbCoups"], "white")

    n = largeurFenetre - largeurInventaire + largeurCase / 15
    tk.texte(n, largeurCase * 6.5,"Echap: Quitter", "white", "nw","Purisa", 9)#bouton quitter
    tk.texte(n, largeurCase * 7,"E: Tirer", "white", "nw","Purisa", 9)#bouton pour tirer
    tk.texte(n, largeurCase * 7.5,"R: Recharger", "white", "nw","Purisa", 9)#bouton reset
    tk.texte(n, largeurCase * 8,"S: Sauvegarde", "white", "nw","Purisa", 9)#bouton save
    tk.texte(n, largeurCase * 8.5,"B: Recommencer", "white", "nw","Purisa", 9)#bouton save
    tk.mise_a_jour()

def main():
    """ Fonction principale du programme """   

    #---------- Initialisation ----------
    numeroDeMap = "Edited" # le numéro de la map à lire (changeable)
    carte, inventaire = initialisationMap(numeroDeMap)
    carte_debut = [list(l) for l in carte]
    largeurFenetre, hauteurFenetre, largeurInventaire = generationFenetre(carte)
    infoMap = [largeurFenetre, hauteurFenetre, largeurInventaire] #Stockage des infos dans une liste pour limiter le nombre de paramètres envoyés aux fonctions
    tk.cree_fenetre(largeurFenetre, hauteurFenetre)
    #-------- Fin initialisation --------

    # -- boucle de jeu
    while True:
        affichage(largeurFenetre, hauteurFenetre, largeurInventaire,inventaire, carte)
        
        # conditions de sortie
        if partieGagnee(carte):
            dessinerVictoire(largeurFenetre,hauteurFenetre)
            tk.attente_clic()
            break


        #Gestion des touches
        typeEvent = attenteMouvement(carte, infoMap)
        if typeEvent == "r":#commande pour revenir à la précédante sauvegarde
            carte, inventaire = recharger()
            continue
        elif typeEvent == "s":#commande de sauvegarde
            ecritureFichierSauvegarde(carte, inventaire)
            continue
        elif typeEvent == "b":#commande de reset
            carte = [list(l) for l in carte_debut]
            inventaire["nbClefs"], inventaire["nbCoups"] = 0, 0
            continue
        #Touches pour quitter le jeu
        elif typeEvent == "Quitte" or typeEvent =="Escape":
            break
        carte = typeMouvement(typeEvent, carte, infoMap, inventaire) #Modifications de la carte par rapport à la touche

    tk.ferme_fenetre()


if __name__ == '__main__':
    """Ce programme est le jeu principale """
    main()
    #print(doctest.testmod())