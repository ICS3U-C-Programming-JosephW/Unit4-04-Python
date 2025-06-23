#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 1, 2025
# This program is a guessing game loop
# that generates a correct number from
# 0 to 9 and breaks the loop once the
# user guesses the number correctly.

# Import the constants module
# for useful constants.
import constants

# Import the random module to
# generate random integers.
import random


# Define the main function.
def main():
    # Generate a correct number from 0 to 9.
    correct_num = random.randint(constants.MIN_NUM, constants.MAX_NUM)

    # Construct an infinite loop.
    while True:
        # Get the number guess from the user as a string.
        user_num_guess_str = input("\nGuess a number between 0 and 9: ")

        # Try to check the validity of the user input.
        try:
            # Attempt to convert the entered string into an integer.
            user_num_guess_int = int(user_num_guess_str)

            # Check if the entered guess is between 0 and 9.
            if (user_num_guess_int >= constants.MIN_NUM) and (
                user_num_guess_int <= constants.MAX_NUM
            ):
                # Check if the entered guess is correct.
                if user_num_guess_int == correct_num:
                    # Break the infinite loop.
                    break
                # Otherwise, the guess was incorrect.
                else:
                    # Display to the user that they made an incorrect guess.
                    print(
                        f"\n{user_num_guess_int} is an incorrect guess. "
                        "Please try again."
                    )
            # Otherwise, the entered whole number is not between 0 and 9.
            else:
                # Display to the user that they made an incorrect guess
                # since the entered number was not between 0 and 9.
                print(
                    f"\n{user_num_guess_int} is an incorrect guess. "
                    "Please try again."
                )

        # Runs if int() could not convert the
        # user's string input into an integer.
        except ValueError:
            # Display to the user that they
            # did not enter a whole number.
            print(f"\n{user_num_guess_str} is not a whole number. Please try again.")

    # After the loop eventually breaks,
    # display that the user guessed
    # correctly, along with a thanks.
    print("\nYou guessed correctly! Thanks for playing!")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
