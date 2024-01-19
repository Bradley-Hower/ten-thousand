from ten_thousand_pack.game_logic import GameLogic

class Game:
  scoring = GameLogic.calculate_score
  dice_held = []
  score = 0
  new_score = 0
  bank = 0
  roundnum = 0

  def play():
    print(
    """
    Welcome to Ten Thousand
    (y)es to play or (n)o to decline
    """
    )

    response = ""

    while response != "y" or response != "n":
      response = input("> ")
      if response == "y":
        print(
        """
        Starting round 1
        Rolling 6 dice...
        """
        )
        return
      elif response == "n":
        print("OK. Maybe another time")
        quit()
    
  @classmethod
  def round(cls):
  
    cls.dice_held = []
    while cls.roundnum <= 1: 

      while True:
        # Score keeping. Two scorings to compare after roll to see if bust.
        cls.score = cls.new_score
        remaining_dice = 6 - len(cls.dice_held)
        roll1 = list(GameLogic.roll_dice(remaining_dice))
        cls.new_score = GameLogic.calculate_score(roll1)
        cls.new_score += cls.score

        # Prints out current roll
        print('*** ', end="")
        for i in roll1:
          print(f'{i} ', end="")
        print(' ***')

        if cls.score > 0:
          if cls.roundnum > 1:
            print(f"Nice Game. Your total score was {cls.new_score} pints.")
            quit()
          elif cls.new_score <= cls.score:
            print(
              """
              You busted!
              """
            )
            quit()

        cls.new_score += cls.score


        selected_dice = []
        roll_of_dice = []

        # Saves roll for modification
        for x in roll1:
          roll_of_dice.append(x)
        user_input = input("Enter a sequence of dice (e.g., 4452) or 'q' to quit: ")

        if user_input == "q":
          print(f'Thanks for playing. You earned {cls.new_score} points')
          quit()

        # Iterate through each character in the user_input, if valid, reserves dice, if invalid, requests again.
        
        try:
          for char in user_input:
            x = roll_of_dice.index(int(char))
            to_pop = roll_of_dice.pop(x)
            selected_dice.append(to_pop)
          for x in selected_dice:
            cls.dice_held.append(x)

          print("Reserved dice:", cls.dice_held)

          # Calculates score of held thus far
          dice_held_score = GameLogic.calculate_score(cls.dice_held)
          remaining_dice = 6 - len(cls.dice_held)

          print(
            f"""
            You have {dice_held_score} unbanked points and {remaining_dice} dice remaining. 
            (r)oll again, (b)ank your points or (q)uit:
            """
            )
          
          roll_sub = input("> ")

          # If rolling
          if roll_sub == "r":     
            True

          # If banked
          elif roll_sub == "b":
            cls.score = cls.new_score
            cls.bank += cls.score

            print(
              f"""
              You banked {cls.bank} points in round 1
              Total score is {cls.score} points
              """)
            
            # Sets up for round two
            cls.roundnum += 1
            if cls.roundnum == 1:
            
              print(
                """
                Starting round 2
                Rolling 6 dice...
                """
                )
            False

          elif roll_sub == "q":

            print(f"You quit. Your total score was {cls.new_score} pints.")
            quit()

        except:
          print("Not a vald entry.")
    
if __name__ == "__main__":
  game = Game
  game.play()
  game.round()