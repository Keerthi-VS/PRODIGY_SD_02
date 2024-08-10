import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # Loop until the user guesses the number
    while not guessed:
        # Get the user's guess
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        # Check if the guess is too low, too high, or correct
        if user_guess < number_to_guess:
            print("Your guess is too low. Try again!")
        elif user_guess > number_to_guess:
            print("Your guess is too high. Try again!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            guessed = True

# Run the guessing game
if __name__ == "__main__":
    guessing_game()
