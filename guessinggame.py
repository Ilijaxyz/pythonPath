from random import randint

print("Welcome to guessing game")


tries = 0
play_again = True
try:
  number = int(input("Please guess the number between 1 and a 100?\n"))
  computer_number = randint(1,100)

  while play_again:
    tries += 1
    if(number > 100 or number < 1):
      print("Did you see the range? It's between 1 and 100")
      
    elif(number == computer_number):
      print(f"WoW you guessed it it's {computer_number}, it took you {tries} tries")
      user_decison = input("Do you wanna play again? (y/n) ").lower()

      if(user_decison != "" and user_decison.startswith("y")):
        play_again = True
        tries = 0
        computer_number = randint(1,100)
        print("Please guess the number between 1 and a 100?\n")
      else:
        break

    elif(number > computer_number):
      print("A bit lower ")

    else:
      print("A bit higher ")
    number = int(input())

  print("Thanks for playing see you soon")
except:
  print("Something wnet wrong")
