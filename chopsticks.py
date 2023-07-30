def print_status(p1r, p1l, p2r, p2l):
    print(f'P1 has {p1r} sticks on their right hand and {p1l} sticks on their left.')
    print(f'P2 has {p2r} sticks on their right hand and {p2l} sticks on their left.')


def clap(player_r, player_l):
    total = player_r + player_l
    while True:
        try:
            rhc = int(input(f'You have {total} sticks, how many would you like to add to the right hand?: '))
            if 0 < rhc < total:
                return rhc
            else:
                print('Invalid input, try again.')
        except ValueError:
            print('Invalid input, try again.')


def player_turn(player_name, player_r, player_l, opponent_r, opponent_l):
    print_status(player_r, player_l, opponent_r, opponent_l)
    while True:
        hand = input(f'{player_name}, Which hand (l / r): ')
        action = input(f'{player_name}, What action (a / c): ')

        if action == 'a':
            target_hand = input(f'{player_name}, Which hand of the opponent (l / r): ')
            if target_hand == 'l':
                opponent_l += player_r if hand == 'r' else player_l
            elif target_hand == 'r':
                opponent_r += player_r if hand == 'r' else player_l
            else:
                print('Invalid input, try again.')
                continue
        elif action == 'c':
            if player_r == 1 or player_l == 1:
                print('Denied, one hand has only 1 stick.')
                continue
            else:
                rhc = clap(player_r, player_l)
                player_r, player_l = rhc, total - rhc

        return player_r, player_l, opponent_r, opponent_l


def main():
    p1r, p1l, p2r, p2l = 1, 1, 1, 1
    print('Legend: "a" means to add sticks. E.g: ap1r means add to player 1s right hand.')
    print('"l" means left and "r" means right')
    print('"c" means to clap and split the total amount of sticks')

    while True:
        if p1r == 0 and p1l == 0:
            print('Player 2 wins!')
            break
        elif p2r == 0 and p2l == 0:
            print('Player 1 wins!')
            break

        p1r, p1l, p2r, p2l = player_turn('Player 1', p1r, p1l, p2r, p2l)
        if p1r == 0 and p1l == 0:
            print('Player 2 wins!')
            break
        elif p2r == 0 and p2l == 0:
            print('Player 1 wins!')
            break

        p2r, p2l, p1r, p1l = player_turn('Player 2', p2r, p2l, p1r, p1l)


if __name__ == "__main__":
    main()