import random

# Function to start the number guessing game
def guess_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    while True:
        # Ask the user to guess a number
        user_guess = input("Enter your guess: ")
        
        # Ensure the input is a valid integer
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        user_guess = int(user_guess)
        attempts += 1
        
        # Check the guess
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
            break

# Run the game
guess_number()
