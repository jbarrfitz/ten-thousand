'''python
def process_kept_dice(roll):
    kept_dice = input("Enter dice to keep, or (q)uit:\n> ")
    if kept_dice == "q":
        return "q"
    kept_rolled_dice = [int(d) for d in kept_dice]
    while True:
        try:
            if GameLogic.verify_kept_dice(kept_rolled_dice, roll):
                return tuple(kept_rolled_dice)
            print_dice(roll)
            kept_dice = input("Enter dice to keep, or (q)uit:\n> ")
            if kept_dice == "q":
                return "q"
            kept_rolled_dice = [int(d) for d in kept_dice]
        except ValueError:
            print("Invalid input. Please enter digits only.")
'''