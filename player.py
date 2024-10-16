from grid import Grid;

class Player:
    def __init__(self):
        """
        Constructeur de la classe Grid.

        Paramètres:
        -----------
            None

        Retourne:
        --------
            None
        """
        self.g = Grid(10)
        self.ships_type = self.g.get_ships
        self.types_bateaux = list(self.g.ship_sizes.keys())



    def set_ship(self):
        """
        Permet au joueur de placer les bateaux.

        Paramètres:
        -----------
            None

        Retourne:
        ---------
            bool: False si la position est invalide
        """

        # Boucle pour placer tous les bateaux

        # Afficher les types de bateaux restants à placer
        print("Bateaux restants à placer :", self.types_bateaux)

        # Demander au joueur de choisir un type de bateau
        type_bateau = input("Choisissez un type de bateau à placer : ")

        # Vérifier si le type de bateau est valide
        if type_bateau not in self.types_bateaux:
            print("Type de bateau invalide. Veuillez réessayer.")
            return False

        # Demander les coordonnées et l'orientation du bateau
        ligne = int(input("Entrez la ligne (numéro) : "))
        colonne = input("Entrez la colonne (lettre) : ")
        orientation = input("Entrez l'orientation (horizontale ou verticale) : ")

        # Appeler la fonction place_ship() pour placer le bateau
        if self.g.place_ship(type_bateau, ligne, colonne, orientation):
            # Si le placement est réussi, retirer le type de bateau de la liste
            self.types_bateaux.remove(type_bateau)
        else:
            print("Placement impossible. Veuillez réessayer.")

    print("Tous les bateaux ont été placés !")


    def attack_enemie(self, enemy_grid:Grid):
        """
        Permet au joueur d'attaquer la grille adverse.

        Paramètres:
        -----------
            enemy_grid (Grid): La grille de l'adversaire.

        Retourne:
        ---------
            bool: True si un bateau a été touché, False sinon.
        """
        row = int(input("Entrez la ligne (numéro) : "))
        col_alpha = input("Entrez la colonne (lettre) : ")
        
        col = self.g.convert_alphabet_to_int(col_alpha)
        resultat:str

        if enemy_grid.data[row-1][col] == 1:
            print("Touché !")
            print(enemy_grid.data[row-1][col])
            enemy_grid.data[row-1][col] = 2
        else:
            print("Dans l'eau...")
