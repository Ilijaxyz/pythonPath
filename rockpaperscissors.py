from random import choice

def endGame():
  machine_choice = None
  print("Play again? Y/N")
  is_playing = input()
  if is_playing and is_playing.lower().startswith("y"):
    machine_choice = choice(["rock","paper","scissors"])
    playGame(machine_choice)
  else:
    print("Thanks for playing, see you soon")
    return machine_choice

def playGame(machine_choice):
  player_choice = input("Plase enter your choice: ").lower()
  
  if player_choice == machine_choice:
      print(f"\nMachine played {machine_choice.upper()}")
      print("DRAW!")
      machine_choice = endGame()

  if player_choice not in choices:
        print("something went wrong")
        machine_choice = endGame()
       
  if machine_choice == "scissors":
    print(f"\nMachine played {machine_choice.upper()}")
    if player_choice == "rock":
      print("YOU WIN!")
      endGame()
    elif player_choice == "paper":
      print("YOU LOST!")
      endGame()
  

  if machine_choice == "rock":
    print(f"\nMachine played {machine_choice.upper()}")
    if player_choice == "paper":
      print("YOU WON!")
      endGame()
    elif player_choice == "scissors":
      print("YOU LOST!")
      endGame()

  if machine_choice == "paper":
    print(f"\nMachine played {machine_choice.upper()}")
    if player_choice == "rock":
      print("YOU LOST!")
      endGame()
    elif player_choice == "scissors":
      print("YOU WON!")
      endGame()

if __name__ == "__main__":
  choices = ["rock","paper","scissors"]
  machine_choice = choice(["rock","paper","scissors"])
  print("Welcome to ROCK, PAPER, SCISSORS VS the MACHINE!")
  playGame(machine_choice)