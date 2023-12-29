

""" Imprime un tablero de ajedrez y sus piezas """

EMPTY = "-"
PAWN = "PEON"
ROOK = "TORRE"
KNIGHT = "CABALLO"
ALFIL = "ALFIL"
KING = "REY"
QUEEN = "REINA"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

# TORRES
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
# CABALLOS
board[0][1] = KNIGHT
board[0][6] = KNIGHT
board[7][1] = KNIGHT
board[7][6] = KNIGHT
# ALFIL
board[0][2] = ALFIL
board[0][5] = ALFIL
board[7][2] = ALFIL
board[7][5] = ALFIL
# REY
board[0][3] = KING
board[7][3] = KING
# REINA
board[0][4] = QUEEN
board[7][4] = QUEEN
# PEONES
board[1][0] = PAWN
board[1][1] = PAWN
board[1][2] = PAWN
board[1][3] = PAWN
board[1][4] = PAWN
board[1][5] = PAWN
board[1][6] = PAWN
board[1][7] = PAWN
board[6][0] = PAWN
board[6][1] = PAWN
board[6][2] = PAWN
board[6][3] = PAWN
board[6][4] = PAWN
board[6][5] = PAWN
board[6][6] = PAWN
board[6][7] = PAWN

# imprime cada fila en una linea separada
for row in board:
    print(row)
