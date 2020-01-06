from random import choice

print("Wlecom to rock paper scissors VS the machine!")
choices = ["rock","paper","scissors"]
player_choice = input("Plase enter your choice: ")
machine_choice = choice(["rock","paper","scissors"])


if player_choice == machine_choice:
    print("DRAW!")

if player_choice not in choices:
      print("something went wrong")

if machine_choice == "scissors":
  if player_choice == "rock":
    print("YOU WIN!")
  elif player_choice == "paper":
    print("YOU LOST!")
 

if machine_choice == "rock":
  if player_choice == "paper":
    print("YOU WON!")
  elif player_choice == "scissors":
    print("YOU LOST!")

if machine_choice == "paper":
  if player_choice == "rock":
    print("YOU LOST!")
  elif player_choice == "scissors":
    print("YOU WON!")