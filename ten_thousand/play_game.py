from game_logic import GameLogic


def welcome():
    """
    Prints welcome screen and asks for if the player wants to play the game.
    :return: (str) "y" or "n"
    """
    choice = ""
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    while choice != "n" and choice != "y":
        choice = input("> ")
    if choice == "n":
        return "n"
    return "y"


def print_dice(roll):
    print("***", *roll, "***")  # Thanks, Anthony


def process_kept_dice(roll):
    kept_dice = input("Enter dice to keep, or (q)uit:\n> ")
    if kept_dice == "q":
        return "q"
    kept_rolled_dice = [int(d) for d in kept_dice]
    while not GameLogic.verify_kept_dice(kept_rolled_dice, roll):
        print_dice(roll)
        kept_dice = input("Enter dice to keep, or (q)uit:\n> ")
        kept_rolled_dice = [int(d) for d in kept_dice]
    return tuple([int(digit) for digit in kept_dice])


def roll_bank_quit(unbanked_points, dice_to_roll):
    print(f"You have {unbanked_points} points and {dice_to_roll} dice remaining")
    print(f"(r)oll again, (b)ank your points, or (q)uit:")
    return input("> ")


def play_round(round_number):
    """
    Rolls dice, asks the player to roll again, bank, or quit, keeps track of unbanked points.
    :return: (int) Banked points for the round
    """
    print(f"Starting round {round_number}")
    dice_to_roll = 6
    unbanked_points = 0
    while dice_to_roll:
        curr_dice_roll = GameLogic.roll_dice(dice_to_roll)
        print_dice(curr_dice_roll)
        keep_dice = process_kept_dice(curr_dice_roll)
        if keep_dice == "q":
            return "q"
        unbanked_points += GameLogic.calculate_score(keep_dice)
        dice_to_roll -= len(keep_dice)
        # deal with hot dice
        rbq = roll_bank_quit(unbanked_points, dice_to_roll)
        if rbq == "b":
            return unbanked_points
        if rbq == "q":
            return "q"


def play_game():
    round_number = 0
    banked_points = 0
    if welcome() == "n":
        print("OK. Maybe another time")
        return
    while round_number < 20:
        round_number += 1
        round_points = play_round(round_number)
        if round_points == "q":
            break
        banked_points += round_points
        print(f"You banked {round_points} points in round {round_number}")
        print(f"Total score is {banked_points} points")
    print(f"Thanks for playing. You earned {banked_points} points")


if __name__ == "__main__":
    play_game()
