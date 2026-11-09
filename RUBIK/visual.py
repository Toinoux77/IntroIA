def display_node(cube):
    # Dictionnaire de correspondance entre les chiffres et les codes couleur ANSI
    COULEURS = {
        0: "\033[97m",  # Blanc (Bright White)
        1: "\033[31m",  # Rouge
        2: "\033[32m",  # Vert
        3: "\033[34m",  # Bleu
        4: "\033[33m",  # Jaune
        5: "\033[36m",  # Cyan
    }
    RESET = "\033[0m"  # Réinitialise la couleur après l'affichage

    # Fonction interne pour colorer une ligne (liste de chiffres)
    def colorer_ligne(ligne):
        # Convertit chaque chiffre en sa version colorée sous forme de chaîne
        elements_colores = [f"{COULEURS.get(num, '')}{num}{RESET}" for num in ligne]
        # Aligne proprement avec des espaces (ici, gestion des listes ou tuples)
        return " ".join(elements_colores)

    print()
    # Face supérieure (cube[1])
    for i in range(3):
        print("        " + colorer_ligne(cube[1][i]))
    print()
    
    # Faces intermédiaires (Gauche: cube[3], Milieu: cube[0], Droite: cube[2])
    for j in range(3):
        gauche = colorer_ligne(cube[3][j])
        milieu = colorer_ligne(cube[0][j])
        droite = colorer_ligne(cube[2][j])
        print(f"{gauche}   {milieu}   {droite}")
    print()
    
    # Face inférieure (cube[4])
    for k in range(3):
        print("        " + colorer_ligne(cube[4][k]))
    print()
    
    # Face arrière (cube[5])
    for l in range(3):
        print("        " + colorer_ligne(cube[5][l]))
    print()

