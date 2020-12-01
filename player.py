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
        direct = False

        if direction == 'W':
            if direct := self.map_update((self.__x - 1, self.__y), self.position) == 1:
                self.__x -= 1

        if direction == 'S':
            if direct := self.map_update((self.__x + 1, self.__y), self.position) == 1:
                self.__x += 1

        if direction == 'A':
            if direct := self.map_update((self.__x, self.__y - 1), self.position) == 1:
                self.__y -= 1

        if direction == 'D':
            if direct := self.map_update((self.__x, self.__y + 1), self.position) == 1:
                self.__y += 1

        self.draw(direct)

    def print_map(self) -> None:
        for i in self.map:
            print(i)
