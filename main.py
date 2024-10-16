from grid import Grid
import time
import os
from player import Player

def main():
    
    #g.place_ship('contre-torpilleur', 9, 2, 'V')
    player1 = Player()
    player2 = Player()

    
    while player1.types_bateaux:
        os.system('cls||clear')
        print("Joueur 1 \n")
        player1.g.place_ship('contre-torpilleur', 1, 'A', 'V')
        player1.g.place_ship('croiseur', 1, 'B', 'V')
        player1.g.place_ship('porte-avions', 1, 'C', 'V')
        player1.g.place_ship('torpilleur', 1, 'D', 'V')
        player1.g.place_ship('sous-marin', 1, 'E', 'V')
        player1.g.display_grid()
        break
        #player1.set_ship()

    while player2.types_bateaux:
        os.system('cls||clear')
        print("Joueur 2 \n")
        player2.g.place_ship('contre-torpilleur', 1, 'A', 'V')
        player2.g.place_ship('croiseur', 1, 'B', 'V')
        player2.g.place_ship('porte-avions', 1, 'C', 'V')
        player2.g.place_ship('torpilleur', 1, 'D', 'V')
        player2.g.place_ship('sous-marin', 1, 'E', 'V')
        player2.g.display_grid()
        break
        #player2.set_ship()   

    player2.attack_enemie(player1.g)
    #SSos.system('cls||clear')
    print("Joueur 2 \n")
    player1.g.display_grid()

    # Affichage du jeu

main()

