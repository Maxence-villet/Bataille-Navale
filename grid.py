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
        self.size = 10
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
        alphabet = "ABCDEFGHIJ"
        print("   ", end="")
        for letter in range(0,10):
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
