from random import randrange


class Board:
    def __init__(self, size: int, symbol: str, enemy: str):
        self.size = size
        self.symbol = symbol[0].upper()
        self.value = 3
        self.enemy = enemy[0].upper()
        self.enemy_value = 1
        self.board = [[0 for _ in range(self.size)]for _ in range(self.size)]

    def begin_board(self, *, random: int, init_row: int = 0, init_col: int = 0) -> tuple:
        self.board[init_row][init_col] = self.value

        while random > 0:
            row = randrange(self.size)
            col = randrange(self.size)
            while self.board[row][col] != 0:
                row = randrange(self.size)
                col = randrange(self.size)

            self.board[row][col] = self.enemy_value
            random -= 1

        return init_row, init_col

    def board_update(self, posicao: tuple, posicao_atual: tuple) -> bool:
        pos_row = posicao[0]
        pos_col = posicao[1]

        if self.board[pos_row][pos_col] != self.enemy_value:
            self.board[posicao_atual[0]][posicao_atual[1]] = 0
            self.board[pos_row][pos_col] = self.value
            return True
        return False

    def draw(self) -> None:
        print('-' * (self.size * 2 - 1))

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == self.value:
                    print(f'{self.symbol} ', end='')
                elif self.board[i][j] == self.enemy_value:
                    print(f'{self.enemy} ', end='')
                else:
                    print('. ', end='')
            print()
