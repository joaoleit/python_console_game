from player import Player

if __name__ == '__main__':
    ash = Player(10, 'ash', 'pokemon')
    ash.start_player(init_row=2, init_col=2)
    ash.draw()

    control = None
    while control != "EXIT":
        control = input("Type the directions: ").upper()

        if control != "EXIT":
            ash.move(control)

