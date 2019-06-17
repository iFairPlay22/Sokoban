Vincent BUISSET / Ewen BOUQUET - DUT Informatique 1 - UPEM
------------- Avancement --------------
La partie 1 est finie.
La partie 2 est finie.
La partie 3 est finie.
Les extensions implémentées sont:
- Tirer une caisse (via la touche E)
- Editer une carte graphiquement (via le script editeur.py)


---------- Organisation --------------
Notre programme est organisé en plusieurs fichiers, __init__.py contient le programme principal et l'affichage principal du jeu. Le fichier dessiner.py contient toutes les fonctions de dessinage du contenu, deplacement.py celles de déplacements et actions, fonctions.py la globalité des fonctions auxiliaires et un file.py pour la lecture de la carte. De plus, editeur.py permet d'éditer une carte. Il faut l'éxécuter pour l'éditer puis éxécuter __init__.py pour jouer

---------- Choix techniques ------------
Pour la structure de la carte, nous avons choisi de mettre les lettres contenant l'objet de la case dans une matrice. A chaque déplacement, on modifie la carte et on appelle la fonction affichage qui mets à jour l'affichage par rapport aux lettres stockées dans la carte.

Pour le stockage des clefs et des déplacements dans la partie 2, nous avons créé un inventaire sous forme de dictionnaire qui contient ces 2 éléments sous forme de nombre (nombre de clefs et le nombre de déplacement)

La boucle principale du projet est organisé comme ceci:
Tant que le joueur n'a pas gagné, on attends un évènement puis on effectue l'action correspondante (ex: modification de la carte, rechargement de la partie, etc.) puis on mets à jour l'affichage à l'écran. La fonction debug est un cas particulier, fonctionnant de manière indépendante des fonctions principales de mouvement (sauf activation).

Les sauvegardes effectuées par le jeu sont enregistrées dans le dossier "map". Pour éviter tout disfoncionnement, il ne faut ne pas supprimer les fichiers du répertoire.

Les modules utilisés sont: upemtk, doctest, random et nos propres modules décrits précédemment.

Par choix d'organisation et de praticité, nous avons utilisé un git.

-------- Problèmes rencontrés ----------
Notre problème principal a été des erreurs d'importation de nos autres fichiers, les fichiers s'importaient les uns les autres et certaines fonctions devenaient inutilisables car "non définies". Nous avons donc rassemblé certaines fonctions et créé un fichier fonction.py pour éviter d'avoir plus de problèmes.

Un second problème que j'ai lors de la création d'une sauvegarde en jeu a été de prendre en compte que notre codage des cases contient des caractères et des chaînes de longueur 2.
Pour ne pas, lors de la lecture, confondre une chaine de longueur 2 (ex: TB) pour 2 caracères (une cible et une boite à la place d'une boite sur une cible), j'ai créé un caractère de délimitation (j'ai choisi "][") que je reconnais lors de la lecture du fichier.

--------- Touches spéciales ----------
I. Jeu

S: Touche de sauvegarde
R: Touche qui permet de relancer la partie précedemment enregistrée
D: Touche qui active le mode debug
E: Touche de sélection de caisse pour la tirer
B: Recommencer la partie
Flèches: déplacer le joueur
Echap: Touche pour quitter

II. Editeur
S: Sauvegarder l'édition 
R: Recommencer l'édition / tout supprimer
Echap: Touche pour quitter

------- Utilisation de la souris --------
La souris est utilisée pour fermer la fenêtre du jeu ou encore pour éditer une carte (sélection du bloc, clic sur la carte pour l'implémenter).

-------- Lancement des scripts ---------
 Jeu principale: __init__.py
 Editeur graphique: editeur.py
 Debug graphique: dessiner.py (pour tester nos fonctions de dessins)

------ Codage des cases en fonction de leur contenu ------
Nous avons rajouté des "types" de case pour pouvoir gérer les éléments par dessus les autres.
".": Case vide
"W": Wall - Mur
"T": Target - Cible
"S": Start - Départ
"D": Door - Porte
"K": Key - Clef
"B": Box - Boite
"TB": Box On a target - Boite sur une cible
"TJ": Player On a target - Joueur sur une cible
"SJ": Player On start - Joueur sur une case de départ
"J": Player - Joueur

Merci de votre attention