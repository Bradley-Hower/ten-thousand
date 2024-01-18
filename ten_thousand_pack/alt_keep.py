while True:
      # The input roll of dice as a string
      roll_of_dice = roll1

      # Request the user for a sequence of dice or "q" to quit
      user_input = input("Enter a sequence of dice (e.g., 4452) or 'q' to quit: ")

      if user_input.lower() == 'q':
          print("Thanks for playing.")
          quit()  # Quit the game if the user enters 'q'

      # Initialize an empty list to store the selected dice
      selected_dice = []

      # Iterate through each character in the user_input
      for char in user_input:
          # Convert the character to an integer and subtract 1 to account for 0-based indexing
          index = int(char) - 1
          
          # Check if the index is valid (between 0 and 5) to avoid errors
          if 0 <= index < len(roll_of_dice):
              selected_dice.append(int(roll_of_dice[index]))
          else:
              print("Invalid input. Please enter a valid sequence of dice or 'q' to quit.")
              break  # Break the loop if input is invalid

      if len(selected_dice) == len(user_input):
          print("Selected dice:", selected_dice)