import random
import csv

def main():
    print_header()

    #rolls = build_the_three_rolls()
    rolls_15 = build_the_fifteen_rolls()
    name = get_players_name()

    player1 = Player(name, 0)
    player2 = Player("Computer", 0)

    game_loop(player1, player2, rolls_15)

class Rolls:
    def __init__(self, name, can_defeat):
        self.name = name
        self.can_defeat = can_defeat

class Player:
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins

def print_header():
    print('-------------------------------------------------')
    print('       ROCK PAPER SCISSORS and many others')
    print('-------------------------------------------------')
    print('')


def build_the_fifteen_rolls():
    rolls = []
    with open('data/battle-table.csv') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            rolls.append(Rolls(read_roll(row)[0], read_roll(row)[1]))
    return rolls       


def read_roll(row: dict):
    name = row['Attacker']
    can_defeat = []
    for k in row.keys():
        if row[k].strip().lower() == 'win':
            can_defeat.append(k)
    return (name, can_defeat)


def get_players_name():
    name = input("What are you called?: ")
    return name


def choose_roll(rolls, count):
    if count == 0:
        print("Here are your choices: ")
    for roll in rolls:
        print("*[{}]{}".format(roll.name[:2], roll.name[2:]))
    roll = input("What do you want to roll?: ")
    for i in rolls:
        if roll.lower() == i.name[:2].lower():
            return i


def game_loop(player1, player2, rolls_15):
    count = 0
    rounds = 3
    while count < rounds:
        p2_roll = random.choice(rolls_15)
        p1_roll = choose_roll(rolls_15, count)
        print("")
        print("{} rolls {}".format(player2.name, p2_roll.name))
        print("{} rolls {}".format(player1.name, p1_roll.name))
        print("")
        if p2_roll.name in p1_roll.can_defeat and p1_roll.name not in p2_roll.can_defeat:
            print("{} beats {}!".format(p1_roll.name, p2_roll.name))
            count += 1
            player1.wins += 1
        elif p1_roll.name in p2_roll.can_defeat and p2_roll.name not in p1_roll.can_defeat:
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
