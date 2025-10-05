#Class is a blueprint for creating objects. An object has properties and methods(functions) associated with it.

class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0  # Number of people following this user
        self.following = 0  # Number of people this user is following
    
    def follow(self, user):
        """Make this user follow another user"""
        user.followers += 1    # The other user gains a follower
        self.following += 1    # This user is now following one more person

# Create two users
user_1 = User("2400552", "abhibauhre")
user_2 = User("2400442", "arnav khulbe")

print(f"User 1 name: {user_1.name}")

user_1.follow(user_2)


print(f"User 1 followers: {user_1.followers}")   
print(f"User 1 following: {user_1.following}")
print(f"User 2 followers: {user_2.followers}")    
print(user_2.following)
