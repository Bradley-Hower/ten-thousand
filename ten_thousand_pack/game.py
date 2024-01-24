from ten_thousand_pack.game_logic import GameLogic

scoring = GameLogic.calculate_score

# score = 0
# roundnum = 0

##new globals
round_set = 1
dice_held = []
score = 0
hotdicepoints = 0
unbanked = 0
totalrounds = 2
zilchmark = False
setroller = None

def play(roller=None, num_rounds=20):
  """Initializes the game. Sets the roller"""
  global setroller

  setroller = roller
  invite_to_play(num_rounds)


def invite_to_play(num_rounds):
  """Initial promp to start the game or to quit."""
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
  """Starts any given round. Variable 'num_rounds' is the rolls, 'round_set' is the actual round"""
  global round_set

  while round_set < totalrounds:
    print(f"Starting round {round_set}")
    for i in range(num_rounds):
      do_round()

def do_round():
  """Group action, runs rolling of dice (calculates number), confirms dice selection, ends round if bust. Ends game once all rounds are concluded."""
  global dice_held
  global round_set
  global zilchmark

  # Caculate number of dice to roll
  if len(dice_held) == 6:
    dice_held = []
  remaining_dice = 6 - len(dice_held) 

  if round_set <= totalrounds:
    # Roll
    roll1 = do_roll(remaining_dice) 
    print(f"Rolling {remaining_dice} dice...")
    format_roll(roll1)

    # Select dice or quit
    confirm_keepers(roll1)
    endround_test()

  else:
    decline_game()


def confirm_keepers(roll):
  """Confirms if dice selection is valid, resets dice held if hotdice (all dice are scoring)."""
  global dice_held
  global zilchmark
  global unbanked

  points = GameLogic.calculate_score(roll)
  if points == 0:
    zilch()
    zilchmark = True
    return
  
  while True:
    global hotdicepoints

    print("Enter dice to keep, or (q)uit:")
    user_input = input("> ")
    nospaces = user_input.replace(" ", "")

    if user_input == "q":
      decline_game()
    try:

      # Validate selection
      if GameLogic.validate_keepers(roll, nospaces):
        for x in nospaces:
          dice_held.append(int(x))
      # Confrim Hotdice
        remaining_dice = 6 - len(dice_held)
        number_scoring = GameLogic.get_scorers(dice_held)
        if remaining_dice == 0 and len(number_scoring) == 6:
          hotdicepoints += GameLogic.calculate_score(dice_held)
          return False
        elif remaining_dice > 0:
          return False
        else:
          print("Faking it")
    except:
      return True    
    print("Cheater!!! Or possibly made a typo...")
    dice_held = []
    format_roll(roll)

def do_roll(num_dice):
  """Pulls roll numbers from cache. Otherwise, generates roll."""
  if setroller:
    return setroller(num_dice)
  else:
    roll = GameLogic.roll_dice(num_dice)
    return roll

def format_roll(roll):
  """Formats dice for display."""
  # Prints out current roll
  print('*** ' + ' '.join(map(str, roll)) + ' ***')

def endround_test():
  """Resets zilch indicator. Runs round tally and ends game post-tally."""
  global zilchmark

  if zilchmark == False:  
    tally()
    if round_set > totalrounds:
      decline_game()
  zilchmark = False

def tally():
  """Allows user to either roll again, or bank points to move to next round. Round points are added to total score, dice held and unbanked points are reset. Round is increased. """
  global dice_held
  global score
  global round_set
  global hotdicepoints
  global unbanked

  if len(dice_held) == 6:
    dice_held = []
  remaining_dice_to_roll = 6 - len(dice_held)

  unbanked += GameLogic.calculate_score(dice_held)
  unbanked += hotdicepoints
  
  print(f"You have {unbanked} unbanked points and {remaining_dice_to_roll} dice remaining")
  print("(r)oll again, (b)ank your points or (q)uit:")

  select_input = ''

  while True:
    while select_input != "r" or select_input != "b" or select_input != "q":
      select_input = input("> ")

      if select_input == "r":
        unbanked = 0
        return    
      
      elif select_input == "b":
        unbanked = GameLogic.calculate_score(dice_held)
        unbanked += hotdicepoints
        print(f"You banked {unbanked} points in round {round_set}")
        score += unbanked
        print(f"Total score is {score} points")
        unbanked = 0
        round_set += 1
        dice_held = []
        hotdicepoints = 0

        if round_set <= totalrounds:
          print(f"Starting round {round_set}")
        return
      
      elif select_input == "q":
        decline_game()
    False

def zilch():
  """Prints zilch message if roll is zero points. Resets unbanked and dice held. Round is increased."""
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
  """Ends game."""
  global score

  print(f'Thanks for playing. You earned {score} points')
  quit()
  
if __name__ == "__main__":
  rolls = [
    # (2, 3, 1, 3, 1, 2), 
    # (4, 1, 4, 4, 3, 4),
    # (3, 2, 3, 2, 1, 4),
    # (1, 1, 1, 5, 5, 5),
    # (1, 3, 4, 2, 3, 6),
    # (4, 4, 4, 4, 4, 4),
    # (1, 1, 2, 5, 1, 6)

    (2, 3, 1, 3, 4, 2),
    (4, 2, 4, 4, 6),
    (3, 2, 3, 2, 1, 4),
    (2, 3, 1, 3, 1, 2), 
    (4, 1, 4, 4, 3, 4),
    (3, 2, 3, 2, 1, 4),
    (5, 2, 3, 5, 4, 2),
    (1, 2, 5, 1, 2, 1),
    (4, 4, 4, 4, 4,4),
    (1, 1, 2, 5, 1, 6)
  ]
  def mock_roller(num_dice):
    select_roll = rolls.pop(0)
    return select_roll[:num_dice]
  
  play(roller=mock_roller)
  # play()
