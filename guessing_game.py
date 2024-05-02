"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""
# Import the random and statistics modules.
import random
import statistics


def start_game():
    # 2. Store a random number as the answer/solution.
    # because the user is inputting data, this needs to be an int
    correct_number = random.randint(int(low_num), int(high_num))

    # 3. Continuously prompt the player for a guess. a. If the guess is greater than the solution, display to the
    # player "It's lower". b. If the guess is less than the solution, display to the player "It's higher". 4. Once
    # the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a
    # list.
    game_guesses = 0
    while True:
        try:
            guess = int(input(f"Guess a number between {low_num} and {high_num}: "))
            # limit the user input
            if guess < int(low_num) or guess > int(high_num):
                raise ValueError(f"Please enter a number between {low_num} and {high_num}.")
            game_guesses += 1
            if guess > correct_number:
                print("It's lower")
            elif guess < correct_number:
                print("It's higher")
            else:
                print("Got it!")
                break
        except ValueError:
            print(input_error)

    # 5. Display the following data to the player
    #  a. How many attempts it took them to get the correct number in this game
    tries = game_guesses

    print(f"Tries: {tries}")

    guesses.append(game_guesses)
    # b. The mean of the saved attempts list
    # Added: I don't like seeing long repeating numbers. So I am going to round this to two decimal places
    mean_tries = round(statistics.mean(guesses), 2)
    # c. The median of the saved attempts list
    median_tries = statistics.median(guesses)
    # d. The mode of the saved attempts list
    mode_tries = statistics.mode(guesses)
    best_score = min(guesses)
    worst_score = max(guesses)
    print(f"The best score is: {best_score}")
    print(f"The worst score is: {worst_score}")
    print(f"Average Score: {mean_tries}")
    print(f"Middle Score: {median_tries}")
    print(f"Most Common Score: {mode_tries}")

    #   6. Prompt the player to play again
    play_again = input("Do you want to play again? (yes/no): ")
    #     a. If they decide to play again, start the game loop over.
    if play_again.lower() == "yes" or play_again.lower() == "y":

        start_game()
    #     b. If they decide to quit, show them a goodbye message.
    else:
        print("Thank you for playing. Goodbye.")


# guesses is the total list of guesses for all rounds of the game
guesses = []

input_error = "You did not enter a valid whole number. Please enter a whole number."
wrong_number_order = "The high number is less than the low number. Please enter a higher number."

while True:
    low_num = input("What number would you like to start the range from?\n ")
    if low_num.isnumeric():
        break
    else:
        print(input_error)

while True:
    high_num = input("What number would you like to start the range from?\n ")
    if high_num < low_num:
        print(wrong_number_order)
    elif high_num.isnumeric():
        break
    else:
        print(input_error)

start_game()
