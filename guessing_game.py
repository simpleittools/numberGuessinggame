"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""
# Import the random and statistics modules.
import random
import statistics


# Create the start_game function.
# Write your code inside this function.
def start_game():
    #   1. Display an intro/welcome message to the player.
    print("Welcome to the Number Guessing Game by Simple IT Tools!")

    # user can set the range of numbers
    low_num = input("What number would you like to start the range from?\n ")
    high_num = input("What number would you like to end the range from?\n ")

    #   2. Store a random number as the answer/solution.
    #  because the user is inputting data, this needs to be an int
    correct_number = random.randint(int(low_num), int(high_num))

    # 3. Continuously prompt the player for a guess. a. If the guess is greater than the solution, display to the
    # player "It's lower". b. If the guess is less than the solution, display to the player "It's higher". 4. Once
    # the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a
    # list.
    guesses = []
    while True:
        try:
            guess = int(input(f"Guess a number between {low_num} and {high_num}: "))
            # limit the user input
            if guess < int(low_num) or guess > int(high_num):
                raise ValueError(f"Please enter a number between {low_num} and {high_num}.")
            guesses.append(guess)
            if guess > correct_number:
                print("It's lower")
            elif guess < correct_number:
                print("It's higher")
            else:
                print("Got it!")
                break
        except ValueError as err:
            print(err)

    #   5. Display the following data to the player
    #     a. How many attempts it took them to get the correct number in this game
    tries = len(guesses)
    #     b. The mean of the saved attempts list
    mean_tries = statistics.mean(guesses)
    #     c. The median of the saved attempts list
    median_tries = statistics.median(guesses)
    #     d. The mode of the saved attempts list
    mode_tries = statistics.mode(guesses)
    print(f"Tries: {tries}")
    print(f"Mean: {mean_tries}")
    print(f"Median: {median_tries}")
    print(f"Mode: {mode_tries}")

    #   6. Prompt the player to play again
    play_again = input("Do you want to play again? (yes/no): ")
    #     a. If they decide to play again, start the game loop over.
    if play_again.lower() == "yes" or play_again.lower() == "y":
        start_game()
    #     b. If they decide to quit, show them a goodbye message.
    else:
        print("Goodbye!")


# Kick off the program by calling the start_game function.
start_game()
