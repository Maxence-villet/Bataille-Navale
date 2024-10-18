from grid import Grid
import time
import os
from player import Player
from ai import AI

def main():
    
    #g.place_ship('contre-torpilleur', 9, 2, 'V')
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    bot = AI("Bot")
    #verification_enemie_type_bot = 0
    #verification_enemie_type_player = 0
    enemie_type = 0 # 0 -> Bot & 1 -> Player

    heure = 0.1
    bot.set_ship_ai()
 

    
    while player1.types_bateaux:
        
        os.system('cls||clear')
        #print("Joueur 1 \n\n   Grille du Joueur 1 \n-----------------------")
        #player1.g.place_ship('contre-torpilleur', 1, 'A', 'V')
        #player1.g.place_ship('croiseur', 1, 'B', 'V')
        #player1.g.place_ship('porte-avions', 1, 'C', 'V')
        #player1.g.place_ship('torpilleur', 1, 'D', 'V')
        #player1.g.place_ship('sous-marin', 1, 'E', 'V')
        #player1.g.display_grid(player1.g.data)
        
        player1.set_ship_ai()
        break
        
        #player1.set_ship()
        #time.sleep(heure)

    if enemie_type ==1:
        while player2.types_bateaux:
            #os.system('cls||clear')
            #print("Joueur 2 \n\n   Grille du Joueur 2 \n-----------------------")
            #player2.g.place_ship('contre-torpilleur', 1, 'A', 'V')
            #player2.g.place_ship('croiseur', 2, 'A', 'V')
            #player2.g.place_ship('porte-avions', 3, 'A', 'V')
            #player2.g.place_ship('torpilleur', 4, 'A', 'V')
            #player2.g.place_ship('sous-marin', 5, 'A', 'V')
            #player2.g.display_grid(player2.g.data)
            
            #player2.set_ship_ai()
            #break
            
            player2.set_ship() 
            time.sleep(heure)  

    
    player_placement = 1 # nombre du tour

    while True:
        
        if enemie_type == 0: # Bot
            if(player_placement == 1):
                time.sleep(heure)
                os.system('cls||clear')

                print("Joueur 1 \n\n   Grille du Joueur 2 \n-----------------------")

                win = player1.win_check(bot.g)
                if win:
                    print(f"{player1.name} a gagné")
                    break
                else:
                    print("Tour suivant")
                    player_placement = 2
                
                #player1.g.display_grid(player1.g.data)
                player1.g.display_grid(bot.g.data_used)
                print("-----------------------")
                status = bot.attack_enemie(player1.g, enemie_type)

                if(status == "AGAIN"):
                    continue
                elif(status == "coulé"):
                    #enemie_type = verification_enemie_type_player
                    print("Le missile est tombé dans l'eau...")
                elif(status == "Touché"):
                    #enemie_type = verification_enemie_type_player
                    print("Le missile a touché un bateau !")
                elif(status == "ERROR"):
                    #enemie_type = verification_enemie_type_player
                    print("veuillez vérifier la bonne combinaison")
                    time.sleep(heure)
                    continue
                else:
                    print("code error 404: status not found")
                    time.sleep(heure)
                    continue
                
                
            
            elif(player_placement == 2):
                time.sleep(heure)
                os.system('cls||clear')
                print("Joueur 2 \n\n   Grille du Joueur 1 \n-----------------------")

                win = bot.win_check(player1.g)
                if win:
                    print(f"{bot.name} a gagné")
                    break
                else:
                    print("Tour suivant")
                    player_placement = 1

                #player1.g.display_grid(player2.g.data)
                bot.g.display_grid(player1.g.data_used)
                print("-----------------------")
                status = player1.attack_enemie(bot.g, enemie_type)
                if(status == "AGAIN"):
                    print("Vous avez déjà séléctionné cette case")
                    continue
                elif(status == "coulé"):
                    #enemie_type = verification_enemie_type_player
                    print("Le missile est tombé dans l'eau...")
                elif(status == "Touché"):
                    #enemie_type = verification_enemie_type_player
                    print("Le missile a touché un bateau !")
                elif(status == "ERROR"):
                    #enemie_type = verification_enemie_type_player
                    print("veuillez vérifier la bonne combinaison")
                    time.sleep(heure)
                    continue
                else:
                    print("code error 404: status not found")
                    time.sleep(heure)
                    continue

                
            else:
                print("Code error 404: player_placement not found")
        
        elif enemie_type == 1: # Player
            if(player_placement == 1):
                time.sleep(heure)
                os.system('cls||clear')
                print("Joueur 1 \n\n   Grille du Joueur 2 \n-----------------------")


                win = player1.win_check(player2.g)
                if win:
                    print(f"{player1.name} a gagné")
                    break
                else:
                    print("Tour suivant")
                    player_placement = 2
                
                #player1.g.display_grid(player1.g.data)
                player1.g.display_grid(player2.g.data_used)
                print("-----------------------")
                status = player2.attack_enemie(player1.g, enemie_type)
                if(status == "AGAIN"):
                    continue
                elif(status == "coulé"):
                    #enemie_type = verification_enemie_type_bot
                    print("Le missile est tombé dans l'eau...")
                elif(status == "Touché"):
                    #enemie_type = verification_enemie_type_bot
                    print("Le missile a touché un bateau !")
                elif(status == "ERROR"):
                    #enemie_type = verification_enemie_type_bot
                    print("veuillez vérifier la bonne combinaison")
                    time.sleep(heure)
                    continue
                else:
                    print("code error 404: status not found")
                    time.sleep(heure)
                    continue
                
                
            
            elif(player_placement == 2):
                time.sleep(heure)
                os.system('cls||clear')
                print("Joueur 2 \n\n   Grille du Joueur 1 \n-----------------------")

                win = player2.win_check(player1.g)
                if win:
                    print(f"{player2.name} a gagné")
                    break
                else:
                    print("Tour suivant")
                    player_placement = 1
                
                #player1.g.display_grid(player2.g.data)
                player2.g.display_grid(player1.g.data_used)
                print("-----------------------")
                status = player1.attack_enemie(player2.g, enemie_type)
                if(status == "AGAIN"):
                    print("Vous avez déjà séléctionné cette case")
                    continue
                elif(status == "coulé"):
                    #enemie_type = verification_enemie_type_bot
                    print("Le missile est tombé dans l'eau...")
                elif(status == "Touché"):
                    #enemie_type = verification_enemie_type_bot
                    print("Le missile a touché un bateau !")
                elif(status == "ERROR"):
                    #enemie_type = verification_enemie_type_bot
                    print("veuillez vérifier la bonne combinaison")
                    time.sleep(heure)
                    continue
                else:
                    print("code error 404: status not found")
                    time.sleep(heure)
                    continue

               
            else:
                print("Code error 404: player_placement not found")
        else:
            print("error 404: Not Found")
            break
        

        
        

main()

