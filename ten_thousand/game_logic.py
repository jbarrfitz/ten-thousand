import random
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(n):
        """
            Roll n number of dice
            :param n: number of dice to be rolled
            :return: tuple containing the six results
        """
        """
        random.randint(1, 6) generates a random integer between 1 and 6,
        representing the result of a die roll. This is repeated n times,
        represented by for _ in range(n). The result of those n die rolls
        is used to create a tuple through tuple comprehension. That tuple
        is then returned by the function. This is what Chat GPT produced,
        except that they assigned the tuple to a variable name and returned
        that variable, where I just returned the tuple itself and saved a
        line.
        """
        print(f"Rolling {n} dice...")
        return tuple(random.randint(1, 6) for _ in range(n))

    @staticmethod
    def calculate_score(dice_roll):
        """
            Calculates the score of a roll of dice in the game of 10,000
            :param dice_roll: tuple representing a number of dice being rolled
            :return: integer representing the total score
        """
        """
        I tried not to use Chat GPT for this part of the exercise, as figuring
        out the logic was by far the most interesting part to me. I did ask
        it to help me figure out the dice_counter.most_common(1)[0][1] notation
        as it took me a minute to realize I wasn't nesting deep enough to get
        the frequency of the most-rolled number.
        """
        # invalid number of dice for the game
        if not len(dice_roll) or len(dice_roll) > 6:
            return 0
        dice_counter = Counter(dice_roll)
        distinct_dice = len(dice_counter)
        most_common_roll_count = dice_counter.most_common(1)[0][1]
        # 6 distinct dice means that you've rolled some combo of 1, 2, 3, 4, 5, 6
        if distinct_dice == 6:
            return 1500
        # 3 distinct dice, with the frequency of the most common of 2 = 3 pairs
        if distinct_dice == 3 and most_common_roll_count == 2:
            return 1500
        roll_score = 0
        # base scores are the value awarded for a triple of any given number
        base_scores = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
        for number_on_dice, frequency in dice_counter.items():
            if frequency >= 3:
                roll_score += base_scores[number_on_dice] * (frequency - 2)
            # the only numbers scoring in occurrences of less than 3 are 1 and 5
            # except for a straight or three pairs, both of which have already
            # been handled and returned a score before reaching here.
            elif number_on_dice == 1:
                roll_score += 100 * frequency
            elif number_on_dice == 5:
                roll_score += 50 * frequency
        return roll_score

    @staticmethod
    def verify_kept_dice(held_dice, dice_roll):
        """
        Checks that the dice that the user selects are all in the roll to prevent cheating/typos
        :param held_dice: tuple of dice that the user has selected to hold
        :param dice_roll: tuple of dice from the original roll
        :return: boolean (true if the dice being held are OK)
        """
        held_dice_counter = Counter(held_dice)
        dice_roll_counter = Counter(dice_roll)
        for die, frequency in held_dice_counter.items():
            if not dice_roll_counter[die] or dice_roll_counter[die] < held_dice_counter[die]:
                print("Cheater!!! Or possibly made a typo...")
                return False
        return True

    @staticmethod
    def get_scorers(dice):
        # version_3

        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scorers = []

        # for i in range(len(dice)):

        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i + 1:]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(val)

        return tuple(scorers)

