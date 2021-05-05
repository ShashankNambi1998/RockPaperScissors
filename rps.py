import random

user_action = input("Please Enter Rock, Paper or Scissors: ")
possible_responses = ['Rock', 'Paper', 'Scissors']

computer_response = random.choice(possible_responses)

print(f"You chose {user_action}, the computer chose {computer_response}")



