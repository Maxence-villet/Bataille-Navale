from grid import Grid;
import random

class Player:
    def __init__(self, name):
        """
        Constructeur de la classe Grid.

        Paramètres:
        -----------
            None

        Retourne:
        ---------
            None
        """
        self.g = Grid(10)
        self.ships_type = self.g.get_ships
        self.types_bateaux = list(self.g.ship_sizes.keys())
        self.name = name
        self.placed_ships = []



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


    def attack_enemie(self, enemy_grid:Grid, enemie_type):
        """
        Permet au joueur d'attaquer la grille adverse.

        Paramètres:
        -----------
            enemy_grid (Grid): La grille de l'adversaire.

        Retourne:
        ---------
            string: "Touché" si un bateau a été touché, "coulé" si l'eau est touché et "AGAIN" si le tir est invalid.
        """
        if enemie_type == 1:
            row = int(input("Entrez la ligne (numéro) : "))
            col_alpha = input("Entrez la colonne (lettre) : ")
            


            if type(col_alpha) == str: # vérification du type string
                col_alpha = col_alpha.upper()
                isContainLetter = False
                for i in self.g.alphabet[0:self.g.size:1]:
                    if isContainLetter == False:
                        if col_alpha == i:
                            isContainLetter = True
                if isContainLetter == False:
                    print(f"Vous devez mettre une seule lettre parmi ces lettres : {self.g.alphabet[0:self.g.size:1]}")
                    return "ERROR"
                else:
                    col = self.g.convert_alphabet_to_int(col_alpha)
        else:
            row = random.randint(1, self.g.size)
            col = random.randint(1, self.g.size)

            col -= 1
            row -= 2
        
        if type(row) == int and row <= self.g.size:   # vérification nombre compris entre 1 et la size de la grille


            if self.g.data_used[row][col] > 0: # case déjà touchée
                    return "AGAIN"
            else:
                self.g.data_used[row][col] = enemy_grid.data[row][col] # ajouter un point dans la case cachée

            if enemy_grid.data[row][col] == 1: # bateau touchée
                self.g.data_used[row][col] = self.g.data_used[row][col]
                return "Touché"
            else:
                self.g.data_used[row][col] = self.g.data_used[row][col] + 2 # tir dans l'eau
                return "coulé"
        else: #vérification ligne (int)
            print(f"Vous devez mettre un nombre entre 1 et {self.g.size}")
            return "ERROR"
    
    def win_check(self, enemy_grid:Grid):
        """
        Vérification de victoire.

        Paramètres:
        -----------
            enemy_grid (Grid): La grille de l'adversaire.

        Retourne:
            bool: True si la partie est gagné, False si la partie continue.
        ---------
            
        """
        for i in enemy_grid.data:
            for j in i:
                if j == 1: # 1 signifie le ship
                    return False
        return True # Gagné

    def set_ship_ai(self):
        """
        Place aléatoirement les bateaux sur la grille.

        Args:
            self: Instance de la classe contenant la grille.

        Returns:
            bool: True si tous les bateaux ont été placés avec succès.
        """
        self.types_bateaux = list(self.g.ship_sizes.keys())

        # Liste des types de bateaux (à partir des clés du dictionnaire)
        types_bateaux = list(self.g.ship_sizes.keys())

        # Boucle pour placer tous les bateaux
        while types_bateaux:
            # Afficher les types de bateaux restants à placer
            print("Bateaux restants à placer :", types_bateaux)

            # Demander au joueur de choisir un type de bateau
            type_bateau = random.choice(list(self.g.ship_sizes.keys()))

            # Vérifier si le type de bateau est valide
            if type_bateau not in types_bateaux:
                print("Type de bateau invalide. Veuillez réessayer.")
                continue

            # Récupérer la taille du bateau à partir du dictionnaire
            taille_bateau = random.choice(list(self.g.ship_sizes.keys()))

            # Demander les coordonnées et l'orientation du bateau
            ligne = random.randint(1, self.g.size)
            colonne = random.randint(0, self.g.size-1)
            orientation = random.choice(['V', 'H'])

            # Appeler la fonction place_ship() en passant la taille du bateau
            if self.g.place_ship(type_bateau, ligne, self.g.alphabet[colonne], orientation):
                # Si le placement est réussi, retirer le type de bateau de la liste
                types_bateaux.remove(type_bateau)
            else:
                print("Placement impossible. Veuillez réessayer.")

        print("Tous les bateaux ont été placés !")
