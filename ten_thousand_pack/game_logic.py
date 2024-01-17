from collections import Counter
import random

class GameLogic:
    @staticmethod
    def calculate_score(dice):
        "Here the code is confirming an actual roll has occurred so as to avoid a exeption error"
        if len(dice) == 0:
            return 0
        
        "Checking for a straight and returning the points associated with such"
        # Check for a straight
        if set(dice) == {1, 2, 3, 4, 5, 6}:
            return 1500

        "Checks for three pairs and returns associated points. Counter is a a container that keeps track of the number of repeating values, thus, here confirms three pairs are present. The code following 'and' confirms that each time there is a repeat that it is indeed as a two, according to the values in the dictionary."
        # Check for three pairs
        if len(dice) == 6 and len(Counter(dice)) == 3 and all(count == 2 for count in Counter(dice).values()):
            return 1500

        score = 0

        "Instance of Counter, provides full dictionary of all occurances of each die number"
        counts = Counter(dice)

        "This if-else tree,  tabulates occording to the frequency of die numbers, according to the preset algorithm."
        for num, count in counts.items():
            if count >= 3:
                if num == 1:
                    score += 1000 * (count - 2)
                else:
                    score += num * 100 * (count - 2)
            elif num == 1:
                score += count * 100
            elif num == 5:
                score += count * 50

        return score

    "Dice roll generator which rolls the input number of dice."
    @staticmethod
    def roll_dice(n):
        return tuple(random.randint(1, 6) for _ in range(n))

