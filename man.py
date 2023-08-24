import random
def get_choices():
     player_choice = input(" Enter a choice (rock ,paper, scissors) :  ")
     options = ["rock", "paper", "scissors"]
     computer_choice = random.choice(options)
     choices = {"player": player_choice, "computer": computer_choice}

     return choices

def check_win(player, computer):
    print (f"You choose:  ${player} , computer choose:  ${computer}" )
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! you won"
        else:
            return "paper covers rock! You lose"

    elif player == "scissors":
        if computer == "rock":
            return "scissors smashes rock ! you won"
        else:
            return "paper covers rock! You lose"

    elif player == "paper":
        if computer == "rock":
            return "paper smashes rock! you won"
        else:
            return " scissors cuts paper! You lose"

    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! you won"
        else:
            return " rock smashes scissors ! You lose"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

# choosen = get_choices()

# print(choosen)


# food = ["pizza", "cheese",  "carrots", "eggs"]
# diner = random.choice(food)
