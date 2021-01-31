import random

while True:
    print("Welcome to the Rock Paper Scissors game!")

    while True:
        players_choice = input("Choose Rock, Paper, or Scissors.")

        if players_choice.title() in ["Rock", "Paper", "Scissors"]:
            break
        print("Please enter a valid input.")

    computer_actions = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_actions)

    key = {"Scissors": "Paper",
           "Paper": "Rock",
           "Rock": "Scissors"}

    verb_details = {"Rock": "crushes",
                    "Paper": "covers",
                    "Scissors": "cuts"}

    draw = {"Rock": "bash",
            "Paper": "slap",
            "Scissors": "scratch"}

    def final_result():
        player_choice_t = players_choice.title()

        print(f"You chose {player_choice_t}, The computer chose {computer_choice}")

        if key[player_choice_t] == computer_choice:
            win = f"{player_choice_t} {verb_details[players_choice.title()]} {computer_choice}. You win."
            return win
        elif key[computer_choice] == player_choice_t:
            lose = f"{computer_choice} {verb_details[computer_choice]} {player_choice_t}. You lose."
            return lose
        else:
            result = f"The {player_choice_t}(s) {draw[player_choice_t]} each other, and it's a draw."
            return result

    print(final_result())

    while True:
        cont_choice = input("Would you like to play again? Type (yes/no): ")

        if cont_choice.lower() in ("yes", "no"):
            break
        print("Invalid input.")

    if cont_choice.lower() == "yes":
        continue

    else:
        print("Thanks for playing!")
        break
