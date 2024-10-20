# Bataille Navale

Implémentation du jeu de la bataille navale 

Rappel des règles:
- Deux joueurs possèdent chacun une grille 10x10 sur laquelle ils placent 5 bateaux.
- Les types de bateaux et leurs tailles :
    - Porte-avions (5 cases)
    - Croiseur (4 cases)
    - Contre torpilleur (3 cases)
    - Sous-marin (3 cases)
    - Torpilleur (2 cases)
- Chaque joueur attaque une case de la grille adverse à tour de rôle.

Objectif : Couler tous les bateaux de l’adversaire en touchant toutes les cases de chaque bateau.

## comment installer le projet

```
git clone https://github.com/Maxence-villet/Bataille-Navale.git
cd Bataille-Navale
python3 main.py
```

## Taille ajustable

La taille de la grille est ajustable, elle s'ajuste parfaitement grace à la variable size:
```
    // grid.py
    self.size = 10
```

![alt text](https://github.com/Maxence-villet/Bataille-Navale/blob/main/images/grid-size-10.png)    ![alt text](https://github.com/Maxence-villet/Bataille-Navale/blob/main/images/grid-size-15.png) ![alt text](https://github.com/Maxence-villet/Bataille-Navale/blob/main/images/grid-size-4.png)


