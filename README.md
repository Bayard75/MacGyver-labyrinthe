# Aider MacGyver à s'échapper !

Un jeu de labyrinthe dont le but est d'aider MacGyver à s'echapper en reunissant 3 objet : une aiguille, un tube en plastique et de l'ether pour pouvoir fabriquer une seringue et endormir le gardien !
Ce jeux a été realisé grâce à pygame.

Les principales fonctionnalités de ce programme sont les suivantes :
-Il n'y a qu'un seul niveau. La structure (départ, emplacement des murs, arrivée), devra être enregistrée dans un fichier pour la modifier facilement au besoin.

-MacGyver sera contrôlé par les touches directionnelles du clavier.

-Les objets seront répartis aléatoirement dans le labyrinthe et changeront d’emplacement si l'utilisateur ferme le jeu et le relance.

-La fenêtre du jeu sera un carré pouvant afficher 15 sprites sur la longueur.

-MacGyver devra donc se déplacer de case en case, avec 15 cases sur la longueur de la fenêtre !

-Il récupèrera un objet simplement en se déplaçant dessus.

-Le programme s'arrête uniquement si MacGyver a bien récupéré tous les objets et trouvé la sortie du labyrinthe. S'il n'a pas tous les
objets et qu'il se présente devant le garde, il meurt (la vie est cruelle pour les héros).

-Le programme sera standalone, c'est-à-dire qu'il pourra être exécuté sur n'importe quel ordinateur.

# Instalation local
Tout d'abord assurer vous que vous avez télécharger python 3.0 ou supérieur.
Téléchargez ou clonez ce répo.
Dans votre terminal :
```
cd dossier_du_repo
pip install virtualenv
virtualenv nom_environnment
env/scripts/activate.ps1
pip install -r requirements.txt
python labyrithn.py
```
**Enjoy !**

Programme réalisé par Bayard Maniraho dans le cadre de la formation développeur d'applications - python d'OpenclassRooms.
