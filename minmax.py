import math

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return row[0]
    # Check columns
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col]) and board[0][col] != ' ':
            return board[0][col]
    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != ' ':
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != ' ':
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_score = -math.inf
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if board[row][col] != ' ':
            print("Cell already taken. Try again.")
            continue
        board[row][col] = 'O'
        print_board(board)
        if check_winner(board) == 'O':
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = 'X'
        print("AI's move:")
        print_board(board)
        if check_winner(board) == 'X':
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

while(True):
    main()
    choice=int(input('do you wish to continue (1 or 0)?'))
    if choice == 1:
        break