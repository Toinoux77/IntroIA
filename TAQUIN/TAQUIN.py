#TAQUIN

def set_board(size):
    board = initialize_board(size)
    board = shuffle_board(board)
    return board

def initialize_board(size):
    board = [[0 for _ in range(size)] for _ in range(size)]
    num = 1
    for i in range(size):
        for j in range(size):
            if num < size * size:
                board[i][j] = num
                num += 1
            else:
                board[i][j] = 0  # Empty space
    return board

def shuffle_board(board):
    import random
    nums = list(range(1, len(board) * len(board))) + [0]
    random.shuffle(nums)
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = nums[i * len(board) + j]
    return board

def print_board(board):
    for row in board:
        print(' '.join(str(x) if x != 0 else ' ' for x in row))
    print()

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    return None

def move_tile(direction, board):
    empty_i, empty_j = find_empty(board)
    if direction == 'up':
        return swap_tiles((empty_i, empty_j), (empty_i - 1, empty_j), board)
    elif direction == 'down':
        return swap_tiles((empty_i, empty_j), (empty_i + 1, empty_j), board)
    elif direction == 'left':
        return swap_tiles((empty_i, empty_j), (empty_i, empty_j - 1), board)
    elif direction == 'right':
        return swap_tiles((empty_i, empty_j), (empty_i, empty_j + 1), board)
    return board  # No move made if direction is invalid

def is_valid_move(board, direction):
    empty_i, empty_j = find_empty(board)
    if direction == 'down':
        return empty_i < len(board) - 1
    elif direction == 'up':
        return empty_i > 0
    elif direction == 'right':
        return empty_j < len(board) - 1
    elif direction == 'left':
        return empty_j > 0
    return False

def swap_tiles(pos1, pos2, board):
    # CRUCIAL : Créer une copie indépendante du plateau
    new_board = [row[:] for row in board]
    
    # Faire l'échange sur la copie
    r1, c1 = pos1
    r2, c2 = pos2
    
    new_board[r1][c1], new_board[r2][c2] = new_board[r2][c2], new_board[r1][c1]
    
    return new_board

def is_solved(board):
    num = 1
    for i in range(len(board)):
        for j in range(len(board)):
            if i == len(board) - 1 and j == len(board) - 1:
                return board[i][j] == 0
            if board[i][j] != num:
                return False
            num += 1
    return True

def is_solvable(board):
    size = len(board)
    flat_board = [num for row in board for num in row if num != 0]
    
    # Calcul des inversions
    inversions = 0
    for i in range(len(flat_board)):
        for j in range(i + 1, len(flat_board)):
            if flat_board[i] > flat_board[j]:
                inversions += 1
                
    # Si la taille est impaire (N=3, N=5), seule la parité des inversions compte
    if size % 2 == 1:
        return inversions % 2 == 0
    
    # Si la taille est paire (N=2, N=4)
    else:
        empty_row_index, _ = find_empty(board)
        # On calcule la ligne de la case vide EN PARTANT DU BAS (1 = dernière ligne, 2 = avant-dernière, etc.)
        empty_row_from_bottom = size - empty_row_index
        
        if empty_row_from_bottom % 2 == 1:
            return inversions % 2 == 0  # Ligne impaire depuis le bas -> inversions doivent être paires
        else:
            return inversions % 2 == 1  # Ligne paire depuis le bas -> inversions doivent être impaires

def new_board(size):
    board = initialize_board(size)
    while True:
        board = shuffle_board(board)
        if is_solvable(board) and not is_solved(board):
            break
    return board

def new_false_board(size):
    board = initialize_board(size)
    while True:
        board = shuffle_board(board)
        if not is_solvable(board):
            break
    return board

def is_partialy_solved(board):
    size = len(board)
    misplaced_count = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] != (i * size + j + 1):
                misplaced_count += 1
    if misplaced_count < 3:
        return True
    return False