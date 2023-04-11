from game_logic import GameLogic


def main():
    round_number = 0
    banked_points = 0

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
            print("OK. Maybe another time")
        else:
            return "y"

    def play_round():
        """
        Rolls dice, asks the player to roll again, bank, or quit, keeps track of unbanked points.
        :return: (int) Banked points for the round
        """
        dice_to_roll = 6
        unbanked_points = 0
        choice = "r"
        print(f"Starting round {round_number}")
        while choice == "r":
            curr_dice_roll = GameLogic.roll_dice(dice_to_roll)
            dice_roll_msg = f"*** {' '.join(str(die) for die in curr_dice_roll)} ***"
            print(dice_roll_msg)
            if not GameLogic.calculate_score(curr_dice_roll):
                return 0
            print("Enter dice to keep, or (q)uit:")
            choice = input("> ")
            if choice == "q":
                quit_game()
            else:
                held_dice = tuple([int(digit) for digit in choice])
                unbanked_points += GameLogic.calculate_score(held_dice)
                dice_to_roll -= len(held_dice)
                print(f"You have {unbanked_points} unbanked points and {dice_to_roll} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                while True:
                    choice = input("> ")
                    if choice == "r" or choice == "q" or choice == "b":
                        break
                if choice == "q":
                    quit_game()
                    return
                elif choice == "b":
                    return unbanked_points

    def quit_game():
        print(f"Thanks for playing. You earned {banked_points} points")
        quit()

    if welcome() == "y":
        while round_number < 20:
            round_number += 1
            round_points = play_round()
            banked_points += round_points
            print(f"You banked {round_points} points in round {round_number}")
            print(f"Total score is {banked_points} points")


if __name__ == "__main__":
    main()
