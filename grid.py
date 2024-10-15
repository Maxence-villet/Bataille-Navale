class Grid:
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
        self.size = 4
        self.data = [[0 for _ in range(self.size)] for _ in range(self.size)]  # Initialisation de la grille dans le constructeur

    def display_grid(self):
        """
        Affiche la grille à l'écran.

        Paramètres:
        -----------
            None

        Retourne:
        --------
            None
        """
        i = 1
        
        # Affichage Alphabet
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print("   ", end="")
        for letter in range(0,self.size):
            print(alphabet[letter], end=" ")
        print()

        for row in self.data:
            if i <10:
                print(i, end="  ")
            else:
                print(i, end=" ")
            for cell in row:
                print(cell, end=" ")
            print()
            i+=1

    def place_ship(self, ship_type, row, col, orientation):
        """
        Place un bateau sur la grille.

        Paramètres:
        -----------
            ship_type (string): Le type de bateau .
            row (int): La ligne de départ du bateau.
            col (int): La colonne de départ du bateau.
            orientation (char): L'orientation du bateau ('H' pour horizontal, 'V' pour vertical).
        
        Retourne:
        ---------
            True si le placement est valide, False sinon.
        """

        # Dictionnaire pour associer chaque type de bateau à sa taille
        ship_sizes = {'porte-avions': 5, 'croiseur': 4, 'contre-torpilleur': 3, 'sous-marin': 3, 'torpilleur': 2}

        # Récupérer la taille du bateau
        ship_size = ship_sizes[ship_type]

        # Vérifier si le placement est valide
        if orientation == 'H':
            if col + ship_size > self.size:
                return False  # Le bateau dépasse de la grille
            for i in range(ship_size):
                if self.data[row][col + i] != 0:
                    return False  # Il y a déjà un bateau à cet endroit
        else:
            if row + ship_size > self.size:
                return False  # Le bateau dépasse de la grille
            for i in range(ship_size):
                if self.data[row + i][col] != 0:
                    return False  # Il y a déjà un bateau à cet endroit

        # Si le placement est valide, mettre à jour la grille
        if orientation == 'H':
            for i in range(ship_size):
                self.data[row][col + i] = 1  # 1 représente une case occupée par un bateau
        else:
            for i in range(ship_size):
                self.data[row + i][col] = 1

        return True