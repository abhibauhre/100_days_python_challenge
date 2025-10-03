
import random
from art import logo, vs
from data import data

print(logo)

def format_data(account):
    '''takes the account data and returns the printable format'''
    account_name = account["name"]
    account_descr = account["description"]
    account_work = account["work"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"  

def check_answer(user_guess, account_a ,account_b):
    '''checks the user guess against the follower counts and returns True if they got it right. Or False if they got it wrong.'''
    if account_a > account_b:
        return user_guess == "a"
    else:
        return user_guess == "b"
score = 0
game_should_continue = True    
    
while game_should_continue:
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data) 

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    if is_correct :
        score +=1
        print(f"correct your score is {score}")
    else :
        print(f"sorry this is wrong final score {score}")
        game_should_continue = False