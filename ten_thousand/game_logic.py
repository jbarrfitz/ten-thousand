import random


class GameLogic:

    @staticmethod
    def roll_dice(n):
        """
            Roll n number of dice
            :param n: number of dice to be rolled
            :return: tuple containing the six results
        """
        results = tuple(random.randint(1, 6) for _ in range(n))
        return results

    @staticmethod
    def calculate_score(dice_roll):
        """
            Calculates the score of a roll of dice in the game of 10,000
            :param dice_roll: tuple representing a number of dice being rolled
            :return: integer representing the total score
        """
