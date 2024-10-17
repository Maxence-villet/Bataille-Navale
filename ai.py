import random
from grid import Grid

class AI:
    def __init__(self, name):
        """
        Constructeur de la classe AI.

        Paramètres:
        -----------
            None

        Retourne:
        --------
            None
        """
        self.g = Grid(10)
        self.name = name
        self.ships_type = self.g.get_ships()
        self.types_bateaux = list(self.g.ship_sizes.keys())
        self.placed_ships = []
    
    def display_grid(self, data):
        """
        Affiche la grille à l'écran.

        Paramètres:
        -----------
            None

        Retourne:
        --------
            None
        """
        i = 1 # Incrémentation des colonnes
        

        print("   ", end="")
        for letter in range(0,self.size):
            print(self.alphabet[letter], end=" ")
        print()

        # Affichage de la grille
        for row in data:
            if i <10:
                print(i, end="  ")
            else:
                print(i, end=" ")
            for cell in row:
                print(cell, end=" ")
            print()
            i+=1 # Incrémentation des colonnes


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

    def attack_enemie(self, enemy_grid:Grid, enemie_type):
        """
        Permet à l'AI d'attaquer la grille adverse.

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
        point_ship = 0
        for i in enemy_grid.data_used:
            for j in i:
                if j == 1: # 1 signifie le ship
                    point_ship += 1
        if point_ship > 16:
            return True # Gagné
        else:
            return False