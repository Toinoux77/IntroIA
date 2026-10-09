import TAQUIN as taquin
from time import time
import heapq

def next_moves(board):
    moves = []
    for direction in ['up', 'down', 'left', 'right']:
        if taquin.is_valid_move(board, direction):
            new_board = taquin.move_tile(direction, board)
            moves.append((direction, new_board))
    return moves

def find_shortest_path(board,show):
    from collections import deque
    nb_of_visited = 0
    visited = set()
    queue = deque([(board, [])])  # Each element is a tuple of (current_board, path_taken)

    while queue:
        current_board, path_taken = queue.popleft()
        if show:
            taquin.print_board(current_board)
        board_tuple = tuple(tuple(row) for row in current_board)

        if board_tuple in visited:
            continue
        visited.add(board_tuple)
        nb_of_visited += 1
        if nb_of_visited > 1000000:
            print("Too many nodes visited(1000000+), stopping the search.")
            return None  # Stop if too many nodes have been visited
        if nb_of_visited % 10000 == 0:
            print(f"Nombre de nœuds visités : {nb_of_visited}")
        if taquin.is_solved(current_board):
            print(f"Nombre de nœuds visités : {nb_of_visited}")
            return path_taken  # Return the path taken to reach the solution

        for direction, new_board in next_moves(current_board):
            new_path = path_taken + [direction]
            queue.append((new_board, new_path))

    print(f"Nombre de nœuds visités : {nb_of_visited}")
    return None  # No solution found

def find_shortest_path_with_Dijkstra(board,show):
    from queue import PriorityQueue
    nb_of_visited = 0
    visited = set()
    pq = PriorityQueue()
    pq.put((0, board, []))  # Each element is a tuple of (cost, current_board, path_taken)

    while not pq.empty():
        cost, current_board, path_taken = pq.get()
        if show:
            taquin.print_board(current_board)
        board_tuple = tuple(tuple(row) for row in current_board)

        if board_tuple in visited:
            continue
        visited.add(board_tuple)
        nb_of_visited += 1
        if nb_of_visited > 1000000:
            print("Too many nodes visited(1000000+), stopping the search.")
            return None  # Stop if too many nodes have been visited
        if nb_of_visited % 10000 == 0:
            print(f"Nombre de nœuds visités : {nb_of_visited}")
        if taquin.is_solved(current_board):
            print(f"Nombre de nœuds visités : {nb_of_visited}")
            return path_taken  # Return the path taken to reach the solution

        for direction, new_board in next_moves(current_board):
            new_path = path_taken + [direction]
            new_cost = cost + 1  # Each move has a cost of 1
            pq.put((new_cost, new_board, new_path))

    print(f"Nombre de nœuds visités : {nb_of_visited}")
    return None  # No solution found

def find_shortest_path_with_A_star_fast(board, heuristic_func, show=False):
    nb_of_visited = 0
    visited = set()
    
    # Dictionnaire pour suivre le coût minimal trouvé pour chaque état
    best_costs = {}
    
    # Utilisation d'une liste Python standard gérée par heapq
    heap = []
    count = 0 
    
    initial_board_tuple = tuple(tuple(row) for row in board)
    best_costs[initial_board_tuple] = 0
    
    # On pousse le premier élément : (priorité, coût, compteur, plateau, chemin)
    heapq.heappush(heap, (heuristic_func(board), 0, count, board, []))
    print(heuristic_func(board)) # Affiche la valeur de l'heuristique pour le plateau initial

    t1 = time()
    while heap:
        priority, cost, _, current_board, path_taken = heapq.heappop(heap)
  
        board_tuple = tuple(tuple(row) for row in current_board)

        # 1. Élimination définitive à la sortie (visite unique)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)
        nb_of_visited += 1
        
        if nb_of_visited % 100000 == 0:
            print(f"Nombre de nœuds visités : {nb_of_visited}")
            
        if taquin.is_solved(current_board):
            print(f"Nombre de nœuds visités : {nb_of_visited}")
            t2 = time()
            print(f"Temps d'exécution : {t2 - t1} secondes")
            return path_taken  

        for direction, new_board in next_moves(current_board):
            new_board_tuple = tuple(tuple(row) for row in new_board)
            new_cost = cost + 1
            
            # OPTIMISATION : On filtre AVANT d'insérer dans la file
            if new_board_tuple in best_costs and new_cost >= best_costs[new_board_tuple]:
                continue
                
            best_costs[new_board_tuple] = new_cost
            new_path = path_taken + [direction]
            new_priority = new_cost + heuristic_func(new_board)
            
            count += 1
            # Insertion ultra-rapide avec heapq
            heapq.heappush(heap, (new_priority, new_cost, count, new_board, new_path))

    print(f"Nombre de nœuds visités : {nb_of_visited}")
    t2 = time()
    print(f"Temps d'exécution : {t2 - t1} secondes")
    return None  

def find_shortest_partial_path_with_A_star_fast(board, heuristic_func, show=False):
    nb_of_visited = 0
    visited = set()
    
    # Dictionnaire pour suivre le coût minimal trouvé pour chaque état
    best_costs = {}
    
    # Utilisation d'une liste Python standard gérée par heapq
    heap = []
    count = 0 
    
    initial_board_tuple = tuple(tuple(row) for row in board)
    best_costs[initial_board_tuple] = 0
    
    # On pousse le premier élément : (priorité, coût, compteur, plateau, chemin)
    heapq.heappush(heap, (heuristic_func(board), 0, count, board, []))
    print(heuristic_func(board)) # Affiche la valeur de l'heuristique pour le plateau initial

    t1 = time()
    while heap:
        priority, cost, _, current_board, path_taken = heapq.heappop(heap)
  
        board_tuple = tuple(tuple(row) for row in current_board)

        # 1. Élimination définitive à la sortie (visite unique)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)
        nb_of_visited += 1
        
        if nb_of_visited % 100000 == 0:
            print(f"Nombre de nœuds visités : {nb_of_visited}")
            
        if taquin.is_partialy_solved(current_board):
            print(f"Nombre de nœuds visités : {nb_of_visited}")
            t2 = time()
            print(f"Temps d'exécution : {t2 - t1} secondes")
            return path_taken  

        for direction, new_board in next_moves(current_board):
            new_board_tuple = tuple(tuple(row) for row in new_board)
            new_cost = cost + 1
            
            # OPTIMISATION : On filtre AVANT d'insérer dans la file
            if new_board_tuple in best_costs and new_cost >= best_costs[new_board_tuple]:
                continue
                
            best_costs[new_board_tuple] = new_cost
            new_path = path_taken + [direction]
            new_priority = new_cost + heuristic_func(new_board)
            
            count += 1
            # Insertion ultra-rapide avec heapq
            heapq.heappush(heap, (new_priority, new_cost, count, new_board, new_path))

    print(f"Nombre de nœuds visités : {nb_of_visited}")
    t2 = time()
    print(f"Temps d'exécution : {t2 - t1} secondes")
    return None