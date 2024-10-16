from grid import Grid;

class Player:
    def __init__(self, name):
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
        self.name = name



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
            string: "Touché" si un bateau a été touché, "coulé" si l'eau est touché et "AGAIN" si le tir est invalid.
        """
        row = int(input("Entrez la ligne (numéro) : "))
        col_alpha = input("Entrez la colonne (lettre) : ")

        
        if type(row) == int and row <= self.g.size and row > 0:  
            if type(col_alpha) == str:
                col_alpha = col_alpha.upper()
                isContainLetter = False
                for i in self.g.alphabet[0:self.g.size:1][::self.g.size]:
                    if isContainLetter == False:
                        if col_alpha == i:
                            isContainLetter = True
                
                if isContainLetter == False:
                    print(f"Vous devez mettre une seule lettre parmi ces lettres : {self.g.alphabet[0:self.g.size:1]}")
                    return "ERROR"
        
                col = self.g.convert_alphabet_to_int(col_alpha)
                
                if self.g.data_used[row-1][col] > 0:
                        return "AGAIN"
                else:
                    self.g.data_used[row-1][col] = enemy_grid.data[row-1][col]

                if enemy_grid.data[row-1][col] == 1:
                    self.g.data_used[row-1][col] = self.g.data_used[row-1][col]
                    return "Touché"
                else:
                    self.g.data_used[row-1][col] = self.g.data_used[row-1][col] + 2
                    return "ERROR"
            else: #vérification colonne (str)
                print(f"Vous devez mettre une seule lettre parmi ces lettres : {self.g.alphabet[0:self.g.size:1]}")
                return False
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
                if j == 1:
                    return False
        return True


