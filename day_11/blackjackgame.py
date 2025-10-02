# Complete Blackjack Game with ASCII Art
import random
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    # In blackjack: Ace=11/1, Jack/Queen/King=10, Numbers=face value
    # We have 4 cards worth 10 points (Jack, Queen, King, 10)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    
    # Check for blackjack (Ace + 10-value card = 21 with only 2 cards)

    if sum(cards) == 21 and len(cards) == 2:
        return 0  # We use 0 to represent blackjack
    
    # Check for Ace and adjust if score goes over 21
    # If we have an Ace (11) and score > 21, change Ace from 11 to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    """Compare user and computer scores and return the result"""

    if user_score > 21 and computer_score > 21:
        return "You went over. You lose "

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    """Main function to play one round of blackjack"""
    
    # Display the logo when game starts
    print(logo)
    
    # Initialize empty lists for cards
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal 2 cards to each player at the start
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn - they can choose to draw more cards
    while not is_game_over:
        # Calculate current scores
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        # Show user's cards and score, but only show computer's first card
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        # Check for game ending conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn - computer draws cards until score is 17 or higher
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show final hands and scores
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    
    # Determine and print the winner
    print(compare(user_score, computer_score))

# Main game loop - allows playing multiple rounds
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    # Clear screen for new game (optional - works on most terminals)
    print("\n" * 20)
    play_game()
