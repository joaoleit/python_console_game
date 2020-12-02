from time import sleep
from board import Map


class Player(Map):
    def __init__(self, size: int, symbol: str, enemy: str) -> None:
        super().__init__(size, symbol, enemy)
        self.__x = 0
        self.__y = 0
        self.begin_map(number=8)

    @property
    def position(self) -> tuple:
        return self.__x, self.__y

    def move(self, directions: str) -> None:
        for direction in directions:
            self.__movement(direction)

    def __movement(self, direction: str) -> None:
        moved = False
        moving_directions = {"W": (self.__x - 1, self.__y), "S": (self.__x + 1, self.__y),
                             "A": (self.__x, self.__y - 1), "D": (self.__x, self.__y + 1)}

        if direction in moving_directions:
            moved = self.map_update(moving_directions[direction], self.position)
            if moved:
                self.__x = moving_directions[direction][0]
                self.__y = moving_directions[direction][1]

        self.draw()
        self.__moved_to(direction, moved)

    def __moved_to(self, direction: str, moved: bool):
        directions_dict = {"W": "Up", "S": "Down", "A": "Left", "D": "Right"}
        moved_dict = {False: "couldn't move", True: "moved"}

        if direction in directions_dict:
            print(f"The Player {moved_dict[moved]} {directions_dict[direction]}")
        else:
            print(f"{direction} is not an movement")

        for i in range(self.size * 2 - 1):
            print(".", end="")
            sleep(0.15)
        print()
