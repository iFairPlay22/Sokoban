Vincent BUISSET / Ewen BOUQUET - DUT Informatique 1 - UPEM
------------- Avancement --------------
La partie 1 est finie.
La partie 2 est finie.
La partie 3 est finie.
Les extensions impl�ment�es sont:
- Tirer une caisse (via la touche E)
- Editer une carte graphiquement (via le script editeur.py)


---------- Organisation --------------
Notre programme est organis� en plusieurs fichiers, __init__.py contient le programme principal et l'affichage principal du jeu. Le fichier dessiner.py contient toutes les fonctions de dessinage du contenu, deplacement.py celles de d�placements et actions, fonctions.py la globalit� des fonctions auxiliaires et un file.py pour la lecture de la carte. De plus, editeur.py permet d'�diter une carte. Il faut l'�x�cuter pour l'�diter puis �x�cuter __init__.py pour jouer

---------- Choix techniques ------------
Pour la structure de la carte, nous avons choisi de mettre les lettres contenant l'objet de la case dans une matrice. A chaque d�placement, on modifie la carte et on appelle la fonction affichage qui mets � jour l'affichage par rapport aux lettres stock�es dans la carte.

Pour le stockage des clefs et des d�placements dans la partie 2, nous avons cr�� un inventaire sous forme de dictionnaire qui contient ces 2 �l�ments sous forme de nombre (nombre de clefs et le nombre de d�placement)

La boucle principale du projet est organis� comme ceci:
Tant que le joueur n'a pas gagn�, on attends un �v�nement puis on effectue l'action correspondante (ex: modification de la carte, rechargement de la partie, etc.) puis on mets � jour l'affichage � l'�cran. La fonction debug est un cas particulier, fonctionnant de mani�re ind�pendante des fonctions principales de mouvement (sauf activation).

Les sauvegardes effectu�es par le jeu sont enregistr�es dans le dossier "map". Pour �viter tout disfoncionnement, il ne faut ne pas supprimer les fichiers du r�pertoire.

Les modules utilis�s sont: upemtk, doctest, random et nos propres modules d�crits pr�c�demment.

Par choix d'organisation et de praticit�, nous avons utilis� un git.

-------- Probl�mes rencontr�s ----------
Notre probl�me principal a �t� des erreurs d'importation de nos autres fichiers, les fichiers s'importaient les uns les autres et certaines fonctions devenaient inutilisables car "non d�finies". Nous avons donc rassembl� certaines fonctions et cr�� un fichier fonction.py pour �viter d'avoir plus de probl�mes.

Un second probl�me que j'ai lors de la cr�ation d'une sauvegarde en jeu a �t� de prendre en compte que notre codage des cases contient des caract�res et des cha�nes de longueur 2.
Pour ne pas, lors de la lecture, confondre une chaine de longueur 2 (ex: TB) pour 2 carac�res (une cible et une boite � la place d'une boite sur une cible), j'ai cr�� un caract�re de d�limitation (j'ai choisi "][") que je reconnais lors de la lecture du fichier.

--------- Touches sp�ciales ----------
I. Jeu

S: Touche de sauvegarde
R: Touche qui permet de relancer la partie pr�cedemment enregistr�e
D: Touche qui active le mode debug
E: Touche de s�lection de caisse pour la tirer
B: Recommencer la partie
Fl�ches: d�placer le joueur
Echap: Touche pour quitter

II. Editeur
S: Sauvegarder l'�dition 
R: Recommencer l'�dition / tout supprimer
Echap: Touche pour quitter

------- Utilisation de la souris --------
La souris est utilis�e pour fermer la fen�tre du jeu ou encore pour �diter une carte (s�lection du bloc, clic sur la carte pour l'impl�menter).

-------- Lancement des scripts ---------
 Jeu principale: __init__.py
 Editeur graphique: editeur.py
 Debug graphique: dessiner.py (pour tester nos fonctions de dessins)

------ Codage des cases en fonction de leur contenu ------
Nous avons rajout� des "types" de case pour pouvoir g�rer les �l�ments par dessus les autres.
".": Case vide
"W": Wall - Mur
"T": Target - Cible
"S": Start - D�part
"D": Door - Porte
"K": Key - Clef
"B": Box - Boite
"TB": Box On a target - Boite sur une cible
"TJ": Player On a target - Joueur sur une cible
"SJ": Player On start - Joueur sur une case de d�part
"J": Player - Joueur

Merci de votre attention