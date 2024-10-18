class Grid:
    def __init__(self, size):
        """
        Constructeur de la classe Grid.

        Paramètres:
        -----------
            size (int): la taille de la grille.

        Retourne:
        --------
            None
        """
        self.size = size
        self.data = [[0 for _ in range(self.size)] for _ in range(self.size)]  # Initialisation de la grille dans le constructeur
        self.ship_sizes = {'porte-avions': 5, 'croiseur': 4, 'contre-torpilleur': 3, 'sous-marin': 3, 'torpilleur': 2} # Dictionnaire pour associer chaque type de bateau à sa taille
        self.placed_ships = []
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.data_used = [[0 for _ in range(self.size)] for _ in range(self.size)]
    
    def display_grid(self, data):
        """
        Affiche la grille à l'écran.

        Paramètres:
        -----------
            None

        Retourne:
        ---------
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

    def convert_alphabet_to_int(self, col_alpha):
        """
        Permet de convertir les lettres de l'axe des colonnes en int.

        Paramètres:
        -----------
            col_aplha (string): la lettre correspondant à la colonne.

        Retourne:
        ---------
            int: retourne le nombre de la colonne.
        """
        self.alphabet = self.alphabet.upper()
        col:int
        isContain = False
        for i in range(0, len(self.alphabet)):
             if col_alpha == self.alphabet[i]:
                 col = i
                 return col
             else:
                 continue
        if isContain == False:
            return False
        

    def set_ship_size(self, ship_type):
        """
        Retire un bateau de la liste des bateaux disponibles et met à jour la liste des bateaux placés.

        Paramètres:
        -----------
            ship_type (sting): Le type de bateau à placer.

        Retourne:
        ---------
            bool: True si le bateau a été placé, False sinon.
        """

        if ship_type in self.ship_sizes:
            if ship_type not in self.placed_ships:
                self.placed_ships.append(ship_type)
                return True
            else:
                print("Ce bateau a déjà été placé.")
        else:
            print("Type de bateau inconnu.")
        return False

    def place_ship(self, ship_type, row, col_alpha, orientation):
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
        if type(row) == int and row <= self.size and row > 0:  
            if type(col_alpha) == str:
                
                isContainLetter = False
                for i in self.alphabet:
                    if isContainLetter == False:
                        if col_alpha == i:
                            isContainLetter = True
                
                if isContainLetter == False:
                    print(f"Vous devez mettre une seule lettre parmi ces lettres : {self.alphabet[0:self.size:1]}")
                    return False
                row-=1

                col:int
                isContain = False
                for i in range(0, len(self.alphabet)):
                    if col_alpha == self.alphabet[i]:
                        col = i
                        isContain = True
                    else:
                        continue
                if isContain == False:
                    return False

                # Récupérer la taille du bateau
                ship_size = self.ship_sizes[ship_type]

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
                    self.set_ship_size(ship_type)
                    for i in range(ship_size):
                        self.data[row][col + i] = 1  # 1 représente une case occupée par un bateau
                else:
                    self.set_ship_size(ship_type)
                    for i in range(ship_size):
                        self.data[row + i][col] = 1

                return True
            else: #vérification col
                print(f"Vous devez mettre une seule lettre parmi ces lettres : {self.alphabet[0:self.size:1]}")
                return False
        else: #vérification row
            print(f"Vous devez mettre un nombre entre 1 et {self.size}")
            return False

        
    
    def get_ships(self):
        """
        Cette fonction retourne la liste des bateaux

        Paramètre:
        ----------
            None

        Retourne:
        ---------
            Hashmap: la liste des bateaux
        """
        return self.ship_sizes
    
    