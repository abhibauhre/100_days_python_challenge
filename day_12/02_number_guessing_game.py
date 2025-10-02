# Number Guessing Game with ASCII Art
import random
from art import logo

# Display the logo when game starts
print(logo)

def play_game():
    
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    
    # Choose difficulty level
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
        
    # Generate random number
    number = random.randint(1, 100)
    
    print(f"You have {attempts} attempts remaining to guess the number.")
    
    # Game loop
    game_over = False
    while not game_over and attempts > 0:
        guess = int(input("Make a guess: "))
        
        if guess == number:
            print(f"You got it! The answer was {number}.")
            game_over = True
        elif guess > number:
            print("Too high.")
            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print("Too low.")
            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts remaining to guess the number.")
    
    if attempts == 0 and not game_over:
        print(f"You've run out of guesses, you lose. The number was {number}.")

# Main game loop
while input("Do you want to play the Number Guessing Game? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)  # Clear screen
    print(logo)  # Show logo again
    play_game()
