from game_logic import GameLogic

round_number = 0
banked_points = 0


def main():
    def welcome():
        choice = ""
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        while choice != "n" and choice != "y":
            choice = input("> ")
        if choice == "n":
            print("OK. Maybe another time")
        else:
            new_round()

    def new_round():
        dice_to_roll = 6
        unbanked_points = 0
        global round_number
        if round_number <= 20:
            round_number += 1
        print(f"Starting round {round_number}")
        print(f"Rolling {dice_to_roll} dice...")
        curr_dice_roll = GameLogic.roll_dice(dice_to_roll)
        dice_roll_msg = "*** "
        for die in curr_dice_roll:
            dice_roll_msg += f"{die} "
        dice_roll_msg += "***"
        print(dice_roll_msg)
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
            bank_choice = input("> ")
            if bank_choice == "q":
                quit_game()
            elif:
                bank_choice == ""
    def quit_game():
        print(f"Thanks for playing. You earned {banked_points} points")

    welcome()


if __name__ == "__main__":
    main()
