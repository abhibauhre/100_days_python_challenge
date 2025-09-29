#while loop is a control flow statement that allows code to execute repeatedly based on a given boolean condition.

print("="*50)
print("WHILE LOOP EXAMPLES WITH STEP-BY-STEP EXPLANATION")
print("="*50)

# ============ EXAMPLE 1: COUNTING FROM 1 TO 5 ============
print("\nExample 1: Counting from 1 to 5")
print("-" * 30)

# Step 1: Initialize the counter variable
counter = 1  # This is our starting point

# Step 2: While loop with condition
# The loop will continue as long as counter <= 5
while counter <= 5:
    # Step 3: Code inside the loop (executed repeatedly)
    print(f"Count: {counter}")
    
    # Step 4: IMPORTANT - Update the counter (increment by 1)
    # Without this, the loop will run forever (infinite loop)
    counter += 1  # Same as: counter = counter + 1

# Step 5: Code after the loop (executes when condition becomes False)
print("Loop finished! Counter is now:", counter)

print("\n" + "="*50)

# ============ EXAMPLE 2: USER INPUT GUESSING GAME ============
print("\nExample 2: Number Guessing Game")
print("-" * 35)

# Step 1: Set up the game variables
secret_number = 7  # The number user needs to guess
user_guess = 0     # Initialize user's guess
attempts = 0       # Count how many attempts user makes

# Step 2: While loop with condition
# Loop continues while user's guess is NOT equal to secret number
while user_guess != secret_number:
    
    # Step 3: Get input from user (inside the loop)
    user_guess = int(input("Guess the secret number (between 1-10): "))
    attempts += 1  # Count each attempt
    
    # Step 4: Check the guess and give feedback
    if user_guess < secret_number:
        print("📈 Too low! Try a higher number.")
    elif user_guess > secret_number:
        print("📉 Too high! Try a lower number.")
    else:
        # This runs when user_guess == secret_number
        print("🎉 Congratulations! You guessed it!")
        print(f"✅ You found the number {secret_number} in {attempts} attempts!")

# Step 5: Loop ends when condition becomes False
print("Thanks for playing!")

print("\n" + "="*50)

# ============ BONUS: WHILE LOOP STRUCTURE EXPLANATION ============
print("\nWHILE LOOP STRUCTURE:")
print("-" * 20)
print("""
while condition:
    # Code to execute repeatedly
    # MUST have something that changes the condition
    # Otherwise = infinite loop!

Key Points:
✅ condition: Must be True/False (boolean)
✅ Indentation: Code inside loop must be indented
✅ Update: Always update variables to avoid infinite loops
✅ Use cases: When you don't know exact number of iterations
""")

print("\n" + "="*50)
print("🎯 WHILE vs FOR LOOP:")
print("• WHILE: Use when you don't know how many times to loop")
print("• FOR: Use when you know exact number of iterations")
print("="*50)

