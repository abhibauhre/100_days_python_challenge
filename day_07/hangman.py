import random

# ASCII Art for Hangman stages (6 wrong guesses = game over)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Hangman logo
logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __    
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \   
| | | | (_| | | | | (_| | | | | | | (_| | | | |  
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  
                    __/ |                      
                   |___/    
'''

print(logo)
print(" Welcome to Hangman Game")
print("Guess the animal name letter by letter")
print("You have 6 wrong guesses before the man is hanged")

some_names = ["lion", "camel", "deer", "elephant", "wolf"]
lives = 6

chosen_words = random.choice(some_names)
print(f"\n🎯 Word chosen! It has {len(chosen_words)} letters.")
print("🔤 Hint: It's an animal name!")

alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Create placeholder with blanks
place_holder = ""
word_length = len(chosen_words)
for position in range(word_length):
    place_holder += "_"

print(f"\n📝 Word to guess: {place_holder}")
print(stages[lives])

game_over = False 
correct_letters = []
wrong_letters = []

while not game_over:
    print(f"\n💖 Lives remaining: {lives}")
    print(f"✅ Correct letters: {correct_letters}")
    print(f"❌ Wrong letters: {wrong_letters}")
    
    guess = input("\n🔤 Guess a letter: ").lower()
    
    # Check if letter was already guessed
    if guess in correct_letters or guess in wrong_letters:
        print(f"⚠️  You already guessed '{guess}'. Try a different letter!")
        continue
    
    # Check if guess is valid
    if guess not in alphabets:
        print("⚠️  Please enter a valid letter (a-z)!")
        continue
    
    display = ""
    
    # Build display string
    for letter in chosen_words:
        if letter == guess:
            display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(f"\n📝 Word: {display}")
    
    # Check if guess was wrong
    if guess not in chosen_words:
        lives -= 1
        wrong_letters.append(guess)
        print(f"❌ Wrong! '{guess}' is not in the word.")
        
        if lives == 0:
            game_over = True
            print(f"\n💀 YOU LOSE! 💀")
            print(f"🎯 The word was: '{chosen_words}'")
            print("Better luck next time!")
    else:
        print(f"✅ Great! '{guess}' is in the word!")
    
    # Check for win condition
    if "_" not in display:
        game_over = True
        print(f"\n CONGRATULATIONS! YOU WIN ")
        print(f" You guessed '{chosen_words}' correctly!")
        print(f" You had {lives} lives remaining!")
    
    # Show hangman stage
    print(stages[lives])

print("\n Thanks for playing Hangman")        