from grid import Grid;
import time
import os


def main():
    g = Grid(10)
    #g.place_ship('contre-torpilleur', 9, 2, 'V')

    i = 0
    
    types_bateaux = list(g.ship_sizes.keys())
    print(types_bateaux)

    # Boucle pour placer tous les bateaux
    while types_bateaux:
        os.system('cls||clear')
        g.display_grid()
        # Afficher les types de bateaux restants à placer
        print("Bateaux restants à placer :", types_bateaux)

        # Demander au joueur de choisir un type de bateau
        type_bateau = input("Choisissez un type de bateau à placer : ")

        # Vérifier si le type de bateau est valide
        if type_bateau not in types_bateaux:
            print("Type de bateau invalide. Veuillez réessayer.")
            continue

        # Demander les coordonnées et l'orientation du bateau
        ligne = int(input("Entrez la ligne (numéro) : "))
        colonne = input("Entrez la colonne (lettre) : ")
        orientation = input("Entrez l'orientation (horizontale ou verticale) : ")

        # Appeler la fonction place_ship() pour placer le bateau
        if g.place_ship(type_bateau, ligne, colonne, orientation):
            # Si le placement est réussi, retirer le type de bateau de la liste
            types_bateaux.remove(type_bateau)
        else:
            print("Placement impossible. Veuillez réessayer.")

    print("Tous les bateaux ont été placés !")


    # Affichage du jeu
    while i < 20:
        
        i+=2
main()

