from collections import Counter
import random

class GameLogic:
    @staticmethod
    def calculate_score(dice):
        if len(dice) == 0:
            return 0

        # Check for a straight
        if set(dice) == {1, 2, 3, 4, 5, 6}:
            return 1500

        # Check for three pairs
        if len(dice) == 6 and len(Counter(dice)) == 3 and all(count == 2 for count in Counter(dice).values()):
            return 1500

        score = 0
        counts = Counter(dice)

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

    @staticmethod
    def roll_dice(n):
        return tuple(random.randint(1, 6) for _ in range(n))

