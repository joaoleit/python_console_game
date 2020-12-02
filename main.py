from player import Player

if __name__ == '__main__':
    ash = Player(10, 'ash', 'pokemon')
    ash.draw()

    control = None
    while control != "EXIT":
        control = input("Type the directions: ").upper()

        if control != "EXIT":
            ash.move(control)

