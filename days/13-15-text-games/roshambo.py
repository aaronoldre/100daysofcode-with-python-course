import random

def main():
    print_header()

    rolls = build_the_three_rolls()
    name = get_players_name()

    player1 = Player(name, 0)
    player2 = Player("Computer", 0)

    game_loop(player1, player2, rolls)
    


class Rolls:
    def __init__(self, name, can_defeat):
        self.name = name
        self.can_defeat = can_defeat

class Player:
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins

def print_header():
    print('---------------------------------')
    print('       ROCK PAPER SCISSORS')
    print('---------------------------------')
    print('')


def build_the_three_rolls():
    rolls = [
        Rolls("Rock", "Scissors"),
        Rolls("Paper", "Rock"),
        Rolls("Scissors", "Paper")
    ]
    return rolls


def get_players_name():
    name = input("What are you called?: ")
    return name


def choose_roll(rolls, count):
    if count == 0:
        print("Here are your choices: ")
    print("[R]ock [P]aper or [S]cissors")
    roll = input("What do you want to roll?: ")
    for i in rolls:
        if roll.lower() == i.name[0].lower():
            return i


def game_loop(player1, player2, rolls):
    count = 0
    while count < 3:
        p2_roll = random.choice(rolls)
        p1_roll = choose_roll(rolls, count)

        print("{} rolls {}".format(player2.name, p2_roll.name))
        print("{} rolls {}".format(player1.name, p1_roll.name))
        
        if p1_roll.can_defeat == p2_roll.name:
            print("{} beats {}!".format(p1_roll.name, p2_roll.name))
            count += 1
            player1.wins += 1
        elif p2_roll.can_defeat == p1_roll.name:
            print("{} beats {}!".format(p2_roll.name, p1_roll.name))       
            count += 1
            player2.wins += 1
        else:
            print("Tie")
        print ('')

    if player1.wins > player2.wins:
        print("{} wins!".format(player1.name))
    else:
        print("{} was destroyed by {}".format(player1.name, player2.name))

if __name__ == '__main__':
    main()
