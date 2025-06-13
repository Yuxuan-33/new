import os
import random


def number_guess_game():
    seed = os.environ.get("SEED")
    if seed is not None:
        try:
            random.seed(int(seed))
        except ValueError:
            pass
    number = random.randint(1, 100)
    tries = 0
    print("Guess a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        tries += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {tries} tries.")
            break


if __name__ == "__main__":
    number_guess_game()
