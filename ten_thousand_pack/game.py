from ten_thousand_pack.game_logic import GameLogic


scoring = GameLogic.calculate_score

# score = 0
# roundnum = 0

##new globals
round_set = 1
dice_held = []
score = 0
unbanked = 0
totalrounds = 2
zilchmark = False
setroller = None

def play(roller=None, num_rounds=20):
  global setroller

  setroller = roller
  invite_to_play(num_rounds)


def invite_to_play(num_rounds):
  print("Welcome to Ten Thousand")
  print("(y)es to play or (n)o to decline")
  
  response = ""
  
  while response != "y" or response != "n":
    response = input("> ")
    
    if response == "y":
      start_game(num_rounds)
    
    elif response == "n":
      print("OK. Maybe another time")
      quit()

def start_game(num_rounds):
  global round_set

  while round_set <= totalrounds:
    print(f"Starting round {round_set}")
    for i in range(num_rounds):
      do_round()

def do_round():
  global dice_held
  global round_set
  global zilchmark

  # Caculate number of dice to roll
  remaining_dice = 6 - len(dice_held) 

  # Roll
  roll1 = do_roll(remaining_dice) 
  print(f"Rolling {remaining_dice} dice...")
  format_roll(roll1)

  # Select dice or quit
  
  confirm_keepers(roll1)
  endround_test()

  return

def confirm_keepers(roll):
  global dice_held
  global zilchmark

  points = GameLogic.calculate_score(roll)
  if points == 0:
    zilch()
    zilchmark = True
    return
  
  while True:
    print("Enter dice to keep, or (q)uit:")
    user_input = input("> ")

    if user_input == "q":
      decline_game()
    try:


      if GameLogic.validate_keepers(roll, user_input):
        for x in user_input:
          dice_held.append(int(x))
  
        # Confrim Hotdice
        number_scoring = GameLogic.get_scorers(dice_held)
        print(len(number_scoring))  
        remaining_dice = 6 - len(dice_held) 
        print(remaining_dice)
        if remaining_dice == 0 and len(number_scoring) == 6:
          return False
        else:
          print("Faking it")
          return True
    except:
      return True    
    print("Cheater!!! Or possibly made a typo...")
    dice_held = []
    format_roll(roll)

def do_roll(num_dice):
  
  if setroller:
    return setroller(num_dice)
  else:
    roll = GameLogic.roll_dice(num_dice)
    return roll

def format_roll(roll):
  # Prints out current roll
  print('*** ' + ' '.join(map(str, roll)) + ' ***')

def endround_test():
  global zilchmark

  if zilchmark == False:  
    tally()
    if round_set > totalrounds:
      decline_game()
  zilchmark = False

def tally():
  global dice_held
  global unbanked
  global score
  global round_set

  remaining_dice_to_roll = 6 - len(dice_held)
  points = GameLogic.calculate_score(dice_held)
  unbanked += points

  print(f"You have {unbanked} unbanked points and {remaining_dice_to_roll} dice remaining")
  print("(r)oll again, (b)ank your points or (q)uit:")

  select_input = ''

  while True:
    while select_input != "r" or select_input != "b" or select_input != "q":
      select_input = input("> ")

      if select_input == "r":
        return    
      
      elif select_input == "b":
        print(f"You banked {unbanked} points in round {round_set}")
        score += unbanked
        print(f"Total score is {score} points")
        unbanked = 0
        round_set += 1
        dice_held = []

        if round_set <= totalrounds:
          print(f"Starting round {round_set}")
        return
      
      elif select_input == "q":
        decline_game()
    False

def zilch():
  global dice_held
  global unbanked
  global round_set

  unbanked = 0
  dice_held = []
  
  print(
    """****************************************
**        Zilch!!! Round over         **
****************************************"""
    )
  print(f"You banked {unbanked} points in round {round_set}")
  print(f"Total score is {score} points")
  
  round_set += 1

  if round_set <= totalrounds:
    print(f"Starting round {round_set}")
  return

def decline_game():
  global score

  print(f'Thanks for playing. You earned {score} points')
  quit()
  
if __name__ == "__main__":
  rolls = [
    (1, 3, 4, 2, 3, 6),
    (4, 4, 4, 4, 4, 4),
    (1, 1, 2, 5, 1, 6)
  ]
  def mock_roller(num_dice):
    return rolls.pop(0)
  
  # play(roller=mock_roller)
  play()
