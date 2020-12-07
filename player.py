from time import sleep
from board import Board


class Player(Board):
    def __init__(self, size: int, name: str, enemy: str) -> None:
        super().__init__(size, name, enemy)
        self.__name = name.title()
        self.__row = 0
        self.__col = 0

    @property
    def position(self) -> tuple:
        return self.__row, self.__col

    def start_player(self, *, random: int = 8, init_row: int = 0, init_col: int = 0) -> None:
        self.__row, self.__col = self.begin_board(random=random, init_row=init_row, init_col=init_col)

    def move(self, directions: str) -> None:
        for direction in directions:
            self.__movement(direction)

    def __movement(self, direction: str) -> None:
        moved = False
        moving_directions = {"W": (self.__row - 1, self.__col), "S": (self.__row + 1, self.__col),
                             "A": (self.__row, self.__col - 1), "D": (self.__row, self.__col + 1)}

        if direction in moving_directions:
            if moved := self.board_update(moving_directions[direction], self.position):
                self.__row = moving_directions[direction][0]
                self.__col = moving_directions[direction][1]

        self.draw()
        self.__moved_to(direction, moved)
        print(self.position)

    def __moved_to(self, direction: str, moved: bool) -> None:
        directions_dict = {"W": "Up", "S": "Down", "A": "Left", "D": "Right"}
        moved_dict = {False: "couldn't move", True: "moved"}

        if direction in directions_dict:
            print(f"{self.__name} {moved_dict[moved]} {directions_dict[direction]}")
        else:
            print(f"{direction} is not an movement")

        for i in range(self.size * 2 - 1):
            print(".", end="")
            sleep(0.10)
        print()
