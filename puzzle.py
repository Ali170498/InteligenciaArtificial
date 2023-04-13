import random
import copy

class Puzzle: #definimos la clase Puzzle
    def __init__(self): #el metodo init se inicializa el rompecabezas creando el tablero utilizando el metodo privado
        self.size = 3
        self.board = self._create_board() #create_board es para mezclar aleatoriamente los numeros

    def _create_board(self):
        numbers = list(range(1, self.size * self.size))
        numbers.append(None) #utilizamos None para representar la casilla en blanco
        random.shuffle(numbers) # el metodo _create_board ultiliza la funcion random,shuffle() para mezclar aleatoriamente (numeros)
        board = []
        for i in range(0, self.size * self.size, self.size):
            row = numbers[i:i + self.size]
            board.append(row)
        return board

    def display(self): #el metood display muestra el tablero en la consola
        for row in self.board:
            print(row)

    def move(self, direction): 
        row, col = self.find_blank()
        if direction == "up" and row > 0:
            self.board[row][col], self.board[row - 1][col] = self.board[row - 1][col], self.board[row][col]
        elif direction == "down" and row < self.size - 1:
            self.board[row][col], self.board[row + 1][col] = self.board[row + 1][col], self.board[row][col]
        elif direction == "left" and col > 0:
            self.board[row][col], self.board[row][col - 1] = self.board[row][col - 1], self.board[row][col]
        elif direction == "right" and col < self.size - 1:
            self.board[row][col], self.board[row][col + 1] = self.board[row][col + 1], self.board[row][col]

    def find_blank(self): # busca la posición de la casilla en blanco en el tablero y devuelve su fila y columna
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] is None:
                    return row, col

    def is_solved(self): #verifica si el rompecabezas está resuelto
        flattened = [item for row in self.board for item in row]
        return flattened == list(range(1, self.size * self.size)) + [None]

if __name__ == "__main__":
    puzzle = Puzzle()  # Crear un rompecabezas de 3x3
    print("Rompecabezas inicial:")
    puzzle.display()

    # Lógica para jugar el rompecabezas, mover piezas y verificar si está resuelto
    while not puzzle.is_solved(): #while repite hasta que este resuelto y salga el mensaje de aviso
        direction = input("Ingresa la dirección para mover (up/down/left/right): ")
        puzzle.move(direction)
        print("Rompecabezas después del movimiento:")
        puzzle.display() #display es un metodo para actualizar el tablero

    print("¡Rompecabezas resuelto!")
