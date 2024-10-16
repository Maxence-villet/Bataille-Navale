from grid import Grid
import time
import os
from player import Player

def main():
    
    #g.place_ship('contre-torpilleur', 9, 2, 'V')
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    player3 = Player("Player 3")

    player3.set_ship_ai()
    print(player3.g.data)

    
    while player1.types_bateaux:
        
        os.system('cls||clear')
        print("Joueur 1 \n\n   Grille du Joueur 1 \n-----------------------")
        player1.g.place_ship('contre-torpilleur', 1, 'A', 'V')
        player1.g.place_ship('croiseur', 1, 'B', 'V')
        player1.g.place_ship('porte-avions', 1, 'C', 'V')
        player1.g.place_ship('torpilleur', 1, 'D', 'V')
        player1.g.place_ship('sous-marin', 1, 'E', 'V')
        #player1.g.display_grid(player1.g.data)
        break
        #player1.set_ship()
        #time.sleep(2)

    while player2.types_bateaux:
        os.system('cls||clear')
        print("Joueur 2 \n\n   Grille du Joueur 2 \n-----------------------")
        player2.g.place_ship('contre-torpilleur', 1, 'A', 'V')
        player2.g.place_ship('croiseur', 2, 'A', 'V')
        player2.g.place_ship('porte-avions', 3, 'A', 'V')
        player2.g.place_ship('torpilleur', 4, 'A', 'V')
        player2.g.place_ship('sous-marin', 5, 'A', 'V')
        player2.g.display_grid(player2.g.data)
        break
        #player2.set_ship() 
        #time.sleep(2)  

    player_placement = 1
    while True:
        
        if(player_placement == 1):
            time.sleep(2)
            os.system('cls||clear')
            print("Joueur 1 \n\n   Grille du Joueur 2 \n-----------------------")
            
            #player1.g.display_grid(player1.g.data)
            player1.g.display_grid(player2.g.data_used)
            print("-----------------------")
            status = player2.attack_enemie(player1.g)
            print(status)
            if(status == "AGAIN"):
                continue
            elif(status == "coulé"):
                print("Le missile est tombé dans l'eau...")
            elif(status == "Touché"):
                print("Le missile a touché un bateau !")
            elif(status == "ERROR"):
                print("veuillez vérifier la bonne combinaison")
                time.sleep(3)
                continue
            else:
                print("code error 404: status not found")
                time.sleep(3)
                continue
            
            win = player1.win_check(player2.g)
            if win:
                print(f"{player1.name} a gagné")
                break
            else:
                print("Tour suivant")
                player_placement = 2
        
        elif(player_placement == 2):
            time.sleep(2)
            os.system('cls||clear')
            print("Joueur 2 \n\n   Grille du Joueur 1 \n-----------------------")
            
            #player1.g.display_grid(player2.g.data)
            player2.g.display_grid(player1.g.data_used)
            print("-----------------------")
            status = player1.attack_enemie(player2.g)
            if(status == "AGAIN"):
                print("Vous avez déjà séléctionné cette case")
                continue
            elif(status == "coulé"):
                print("Le missile est tombé dans l'eau...")
            elif(status == "Touché"):
                print("Le missile a touché un bateau !")
            elif(status == "ERROR"):
                print("veuillez vérifier la bonne combinaison")
                time.sleep(3)
                continue
            else:
                print("code error 404: status not found")
                time.sleep(3)
                continue

            win = player2.win_check(player1.g)
            if win:
                print(f"{player2.name} a gagné")
                break
            else:
                print("Tour suivant")
                player_placement = 1
        else:
            print("Code error 404: player_placement not found")

        
        

main()

