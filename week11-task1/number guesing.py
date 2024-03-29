import random

def number_guessing_game():

    secret_number = random.randint(1, 100)

    
    attempts = 0

    while True:
        
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    number_guessing_game()












