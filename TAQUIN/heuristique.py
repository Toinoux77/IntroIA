def h1(board):
    """
    Heuristic 1: Count the number of misplaced tiles.
    This function counts how many tiles are not in their goal position.
    """
    size = len(board)
    misplaced_count = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] != 0 and board[i][j] != (i * size + j + 1):
                misplaced_count += 1
    return misplaced_count

def h2(board):
    """
    Heuristic 2: Calculate the sum of Manhattan distances of tiles from their goal positions.
    This function computes the total distance each tile is from its target position.
    """
    size = len(board)
    manhattan_distance = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] != 0:
                target_i = (board[i][j] - 1) // size
                target_j = (board[i][j] - 1) % size
                manhattan_distance += abs(i - target_i) + abs(j - target_j)
    return manhattan_distance

def h3(board):
    size = len(board)
    linear_conflict = 0

    # 1. Vérification des lignes
    for i in range(size):
        # Liste des conflits pour chaque case de la ligne i
        conflicts = [0] * size
        for j in range(size):
            if board[i][j] != 0 and (board[i][j] - 1) // size == i:
                for k in range(j + 1, size):
                    if board[i][k] != 0 and (board[i][k] - 1) // size == i and board[i][j] > board[i][k]:
                        conflicts[j] += 1
                        conflicts[k] += 1
        
        # Résolution gloutonne des conflits multiples
        while max(conflicts) > 0:
            # On cherche la tuile qui pose le plus de problèmes
            max_idx = conflicts.index(max(conflicts))
            # On élimine ses conflits de la ligne
            conflicts[max_idx] = 0
            for j in range(size):
                if board[i][j] != 0 and (board[i][j] - 1) // size == i:
                    # Si cette tuile était en conflit avec max_idx, on réduit son compteur
                    # (Pour simplifier, on applique une logique similaire sur les indices)
                    pass 
            # Version simplifiée robuste : on ajoute un conflit réel
            linear_conflict += 1
            # On remet à zéro les conflits liés à cette tuile
            # (Pour un code 100% exact, on reconstruit le graphe de conflit épuré)

    # Pour éviter une usine à gaz, voici la méthode standard approuvée :
    return count_true_conflicts(board, size)

def count_true_conflicts(board, size):
    total_conflicts = 0
    
    # Analyse des lignes
    for r in range(size):
        in_place_tiles = []
        for c in range(size):
            val = board[r][c]
            if val != 0 and (val - 1) // size == r:
                in_place_tiles.append((c, val))
        total_conflicts += _resolve_line_conflicts(in_place_tiles)
        
    # Analyse des colonnes
    for c in range(size):
        in_place_tiles = []
        for r in range(size):
            val = board[r][c]
            if val != 0 and (val - 1) % size == c:
                in_place_tiles.append((r, val))
        total_conflicts += _resolve_line_conflicts(in_place_tiles)
        
    return total_conflicts

def _resolve_line_conflicts(tiles):
    # tiles est une liste de tuples (position_actuelle, valeur_tuile)
    conflicts = 0
    counts = [0] * len(tiles)
    
    # Établir le nombre de conflits par tuile
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i][1] > tiles[j][1]:
                counts[i] += 1
                counts[j] += 1
                
    # Éliminer la tuile ayant le plus de conflits jusqu'à ce qu'il n'y en ait plus
    while any(c > 0 for c in counts):
        max_idx = counts.index(max(counts))
        # Vider les conflits de cette tuile et réduire ceux des autres avec qui elle était liée
        for j in range(len(tiles)):
            if j != max_idx and tiles[max_idx][1] > tiles[j][1] if max_idx < j else tiles[j][1] > tiles[max_idx][1]:
                if counts[j] > 0:
                    counts[j] -= 1
        counts[max_idx] = 0
        conflicts += 1
        
    return conflicts

def h4(board):
    size = len(board)
    penalty = 0

    # --- 1. COIN HAUT-GAUCHE ---
    # Cible du coin: 1 | Voisin Droite: 2 | Voisin Bas: size + 1
    if board[0][0] != 1:
        if board[0][1] == 2 and board[1][0] == size + 1:
            penalty += 2

    # --- 2. COIN HAUT-DROITE ---
    # Cible du coin: size | Voisin Gauche: size - 1 | Voisin Bas: size * 2
    if board[0][size-1] != size:
        if board[0][size-2] == size - 1 and board[1][size-1] == size * 2:
            penalty += 2

    # --- 3. COIN BAS-GAUCHE ---
    # Cible du coin: size*(size-1) + 1 | Voisin Droite: +1 | Voisin Haut: cible - size
    target_bg = size * (size - 1) + 1
    if board[size-1][0] != target_bg:
        if board[size-1][1] == target_bg + 1 and board[size-2][0] == target_bg - size:
            penalty += 2

    # --- 4. COIN BAS-DROITE ---
    # Cible du coin: 0 | Voisin Gauche: (size*size) - 1 | Voisin Haut: (size*size) - size
    # Le conflit n'existe que si la tuile dans le coin n'est PAS le 0 cible, mais une vraie tuile bloquée
    if board[size-1][size-1] != 0:
        if board[size-1][size-2] == (size * size) - 1 and board[size-2][size-1] == (size * size) - size:
            penalty += 2

    return penalty

def h5(board):
    """
    Heuristic 5: Combine Manhattan distance, linear conflict, and corner conflict.
    This function adds the Manhattan distance, twice the number of linear conflicts, and the corner conflict penalty to provide a more informed heuristic.
    """
    return h2(board) + 2*h3(board) + h4(board)  # Combining Manhattan distance, linear conflict, and corner conflict

def hOptimal(board):
    return 1.4*(h2(board) + 2*h3(board) + 2*h4(board))