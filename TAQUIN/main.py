import TAQUIN as taquin
import heuristique as heuristique
import plusCourtChemin as pcc

def play_taquin():
    """
    Function to play the Taquin game.
    This function initializes the game board and handles user input to move tiles.
    """
    # Initialize the game board
    SIZE = get_board_size()
    board = taquin.new_board(SIZE)

    compare_algorithms(board)

    while not taquin.is_solved(board):
        taquin.print_board(board)
        print(f"Hamming: {heuristique.h1(board)}, Manhattan: {heuristique.h2(board)}, Linear Conflict: {heuristique.h3(board)}")
        move = get_user_move()
        if taquin.is_valid_move(board, move):
            board = taquin.move_tile(move, board)
        else:
            print("Invalid move. Please try again.")
    
    print("Congratulations! You've solved the Taquin puzzle!")
    taquin.print_board(board)

def solve_taquin_with_algorithm(board, algorithm, heuristic_func=None):
    if not taquin.is_solvable(board):
        if heuristic_func is None:
            raise ValueError("Heuristic function is required for A* algorithm")
        return pcc.find_shortest_partial_path_with_A_star_fast(board, heuristic_func, False)
    if algorithm == "BFS":
        return pcc.find_shortest_path(board,False)
    elif algorithm == "Dijkstra":
        return pcc.find_shortest_path_with_Dijkstra(board,False)
    elif algorithm == "A*":
        if heuristic_func is None:
            raise ValueError("Heuristic function is required for A* algorithm")
        return pcc.find_shortest_path_with_A_star_fast(board, heuristic_func, False)

def show_solution(board, path):
    """
    Function to display the solution path on the board.
    This function takes the initial board and the solution path, and displays each step of the solution.
    """
    print("Displaying the solution path:")
    current_board = [row[:] for row in board]  # Create a copy of the board
    taquin.print_board(current_board)
    
    for move in path:
        current_board = taquin.move_tile(move, current_board)
        print(f"Move: {move}")
        taquin.print_board(current_board)

def A_star_with_optimal_heuristic(board):

    print("Running A* with combined heuristic (1.4 * Manhattan + 2.8 * Linear Conflict + 2.8 * Corner Conflict...")
    a_star_hOptimal_path = solve_taquin_with_algorithm(board, "A*", heuristique.hOptimal)
    print(f"A* (Combined) path length: {len(a_star_hOptimal_path) if a_star_hOptimal_path else 'No solution found'}")
    print(a_star_hOptimal_path)
    show_solution(board,a_star_hOptimal_path)

def A_star_manhattan(board):

    print("Running A* with Manhattan heuristic")
    a_star_manhattan_path = solve_taquin_with_algorithm(board, "A*", heuristique.h2)
    print(f"A* Manhattan path length: {len(a_star_manhattan_path) if a_star_manhattan_path else 'No solution found'}")
    print(a_star_manhattan_path)

def compare_algorithms():
    """
    Function to compare the performance of different algorithms on the given board.
    This function runs BFS, Dijkstra, and A* algorithms and prints their results.
    """
    print("Here you can compare the performance of different algorithms on the Taquin puzzle.")

    while True:
        print("\nGenerating a new board... enter size for the board (e.g., 3 for a 3x3 board):")
        SIZE = get_board_size()
        board = taquin.new_board(SIZE)
        print("New board generated:")
        taquin.print_board(board)

        # BFS
        if SIZE > 2:
            print("BFS, Dijkstra and A* will take a long time for boards larger than 4x4. Skipping these algorithms for this size.")
        else:
            print("Running BFS...")
            bfs_path = solve_taquin_with_algorithm(board, "BFS")
            print(f"BFS path length: {len(bfs_path) if bfs_path else 'No solution found'}")
            print(bfs_path)
        
            # Dijkstra
            print("Running Dijkstra...")
            dijkstra_path = solve_taquin_with_algorithm(board, "Dijkstra")
            print(f"Dijkstra path length: {len(dijkstra_path) if dijkstra_path else 'No solution found'}")
            print(dijkstra_path)
            
            # A* with Hamming heuristic
            print("Running A* with Hamming heuristic...")
            a_star_h1_path = solve_taquin_with_algorithm(board, "A*", heuristique.h1)
            print(f"A* (Hamming) path length: {len(a_star_h1_path) if a_star_h1_path else 'No solution found'}")
            print(a_star_h1_path)
        
            # A* with Manhattan heuristic
            print("Running A* with Manhattan heuristic...")
            a_star_h2_path = solve_taquin_with_algorithm(board, "A*", heuristique.h2)
            print(f"A* (Manhattan) path length: {len(a_star_h2_path) if a_star_h2_path else 'No solution found'}")
            print(a_star_h2_path)

        # A* with combined heuristic (Manhattan + Linear Conflict)
        print("Running A* with combined heuristic (Manhattan + Linear Conflict + Corner Conflict...")
        a_star_h5_path = solve_taquin_with_algorithm(board, "A*", heuristique.h5)
        print(f"A* (Combined) path length: {len(a_star_h5_path) if a_star_h5_path else 'No solution found'}")
        print(a_star_h5_path)
        show_solution(board, a_star_h5_path)

def get_board_size():
    """
    Function to get the size of the board from the user.
    Returns an integer representing the size of the board.
    """
    while True:
        try:
            size = int(input("Enter the size of the board (e.g., 3 for a 3x3 board): "))
            if size < 2:
                print("Size must be at least 2. Please try again.")
            else:
                return size
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_user_move():
    """
    Function to get the user's move input.
    Returns a string representing the direction of the move.
    """
    while True:
        move = input("Enter your move (up, down, left, right): ").strip().lower()
        if move in ['up', 'down', 'left', 'right']:
            return move
        else:
            print("Invalid move. Please enter 'up', 'down', 'left', or 'right'.")

easy_board = [[2,6,10,5],[7,9,1,0],[8,3,15,4],[11,13,12,14]]
hard_board = [[5,13,8,9],[4,12,7,3],[10,11,1,15],[6,14,2,0]]

SIZE = get_board_size()
new_board = taquin.new_board(SIZE)
A_star_with_optimal_heuristic(new_board)
