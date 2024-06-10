# Tic tac toe input
# Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:

# 1:  X | O | X
#    -----------
# 2:    |   |  
#    -----------
# 3:  O |   |

#     A   B  C
# The board is represented as a 2D list:

# board = [
#     ["X", "O", "X"],
#     [" ", " ", " "],
#     ["O", " ", " "],
# ]
# Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].

# Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

# For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.

# Traducido:
# Ta te ti: entrada de datos
# Aquí está la historia de fondo para este desafío: imagina que estás escribiendo un juego de tres en raya, donde el tablero se ve así:

# yaml
# Copiar código
# 1:  X | O | X
#    -----------
# 2:    |   |  
#    -----------
# 3:  O |   |

#     A   B  C
# El tablero está representado como una lista 2D:

# python
# Copiar código
# board = [
#     ["X", "O", "X"],
#     [" ", " ", " "],
#     ["O", " ", " "],
# ]
# Imagina que tu usuario ingresa "C1" y necesitas ver si hay una X o una O en esa celda del tablero. Para hacerlo, necesitas traducir la cadena "C1" a la fila 0 y la columna 2 para que puedas verificar board[row][column].

# Tu tarea es escribir una función que pueda traducir de cadenas de longitud 2 a una tupla (fila, columna). Nombra tu función get_row_col; debe tomar un único parámetro que es una cadena de longitud 2 que consiste en una letra mayúscula y un dígito.

# Por ejemplo, llamar a get_row_col("A3") debe devolver la tupla (2, 0) porque A3 corresponde a la fila en el índice 2 y la columna en el índice 0 en el tablero.

def get_row_col(cell, board):
    # crear un diccionario para mapear las letras a índices de columna
    column_map = {'A' : 0, 'B' : 1, 'C' : 2}
    
    # extraer la letra y eñ dígito de la casdena usando indexación
    letter = cell[0]
    digit = cell[1]
    
    # vamos a convertir el dígito a un índice de fila restando ya que la numeración en Pythpn emipieza en 0
    row = int(digit) - 1
    
    # convertimos la letra a un índioce de la columna usando el diccionario contrastando contra sus valores clave : valor
    column = column_map[letter]
    
    # devilvemos la tupla (fila, columna) con la posición
    return (row, column)

# Pasamos un Board con la lista que representa el tablero de juego:

board = [
    ['X', 'O', 'X'],
    [' ', ' ', 'X'],
    ['O', ' ', ' '],
]

# probamos la función pasando la celda a verificar y el tablero con el juego

print(get_row_col('A3', board))
print(get_row_col('B1', board))
print(get_row_col('C2', board))

# uso la técnica lamada desestructración de objeto, en este caso una tupla para asignar varios elementos a la vez
row, column = get_row_col('A3', board)

# con la tupla de valores obtenidos impirmo el valor correspondiente en esa posición dentro del tablero
print(board[row][column])

row, column = get_row_col('B1', board)
print(board[row][column])

row, column = get_row_col('C2', board)
print(board[row][column])
