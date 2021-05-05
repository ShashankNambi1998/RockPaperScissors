import random

loop = True

while loop == True:
    user_action = input("Please Enter Rock, Paper or Scissors: ")
    possible_responses = ['Rock', 'Paper', 'Scissors']

    computer_response = random.choice(possible_responses)

    print(f"You chose {user_action}, the computer chose {computer_response}")

    if user_action == computer_response:
        print("Same Response, No Winner")

    if user_action == "Rock":
        if computer_response == "Scissors":
            print("You Win!")
        elif computer_response == "Paper":
            print("You Lose :(")
    if user_action == "Scissors":
        if computer_response == "Paper":
            print("You Win!")
        elif computer_response == "Rock":
            print("You Lose :(")
    if user_action == "Paper":
        if computer_response == "Rock":
            print("You Win!")
        elif computer_response == "Scissors":
            print("you Lose :(")

    loop_condition = input("Would you like to keep playing? Yes/No ")

    if loop_condition != "Yes":
        loop = False




