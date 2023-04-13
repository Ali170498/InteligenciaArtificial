import random
import copy

class Puzzle:
    def __init__(self):
        self.size = 3
        self.board = self._create_board()

    def _create_board(self):
        numbers = list(range(1, self.size * self.size))
        numbers.append(None)
        random.shuffle(numbers)
        board = []
        for i in range(0, self.size * self.size, self.size):
            row = numbers[i:i + self.size]
            board.append(row)
        return board

    def display(self):
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

    def find_blank(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] is None:
                    return row, col

    def is_solved(self):
        flattened = [item for row in self.board for item in row]
        return flattened == list(range(1, self.size * self.size)) + [None]

if __name__ == "__main__":
    puzzle = Puzzle()  # Crear un rompecabezas de 3x3
    print("Rompecabezas inicial:")
    puzzle.display()

    # Lógica para jugar el rompecabezas, mover piezas y verificar si está resuelto
    while not puzzle.is_solved():
        direction = input("Ingresa la dirección para mover (up/down/left/right): ")
        puzzle.move(direction)
        print("Rompecabezas después del movimiento:")
        puzzle.display()

    print("¡Rompecabezas resuelto!")