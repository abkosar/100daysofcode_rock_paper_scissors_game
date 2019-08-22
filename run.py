import random

from player import Player
from roll import Roll


def print_header():
    print('-------------------------------------------------')
    print('            ROCK, PAPER, SCISSORS GAME')
    print('-------------------------------------------------')


def get_players_name():
    player_name = input("Please type your name: ")
    return player_name


def build_the_three_rolls():
    rock = Roll('rock')
    paper = Roll('paper')
    scissors = Roll('scissors')

    return [rock, paper, scissors]


def game_loop(player1, player2, rolls):
    count = 1
    player_score = 0
    computer_score = 0
    while count <= 3:
        p2_roll = random.choice(rolls)
        p1_roll = input("Please select a roll: [R]ock / [P]aper / [S]cissors ")

        if p1_roll == 'R':
            p1_roll = rolls[0]
        if p1_roll == 'P':
            p1_roll = rolls[1]
        if p1_roll == 'S':
            p1_roll = rolls[2]

        while p1_roll.name == p2_roll.name:
            p2_roll = random.choice(rolls)
            p1_roll = input("Same roll selected, please select ahain: [R]ock / [P]aper / [S]cissors ")
            if p1_roll == 'R':
                p1_roll = rolls[0]
            if p1_roll == 'P':
                p1_roll = rolls[1]
            if p1_roll == 'S':
                p1_roll = rolls[2]

        outcome = p1_roll.can_defeat(p2_roll.name)

        # display throws
        print(f"{player1.name}'s roll: {p1_roll.name}")
        print(f"Computers's roll: {p2_roll.name}")

        # display winner for this round
        if outcome:
            print(f"{player1.name} wins this round!")
            player_score += 1
            print(f"{player1.name}: {player_score} - Computer: {computer_score}")
        if not outcome:
            print("Computer wins this round!")
            computer_score += 1
            print(f"{player1.name}: {player_score} - Computer: {computer_score}")

        count += 1

    # Compute who won

    if player_score > computer_score:
        print(f"{player1.name} wins!")
    else:
        print("Computer wins!")


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


if __name__ == "__main__":
    main()
