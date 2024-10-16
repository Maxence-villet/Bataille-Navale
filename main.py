from grid import Grid
import time
import os
from player import Player

def main():
    
    #g.place_ship('contre-torpilleur', 9, 2, 'V')
    player1 = Player()
    i = 0

    
    while player1.types_bateaux:
        os.system('cls||clear')
        player1.g.display_grid()
        player1.set_ship()

    # Affichage du jeu

main()

