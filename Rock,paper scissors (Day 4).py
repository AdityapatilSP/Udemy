import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______w
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]
user_input = int(input("What would you like to choose ? type 0 for rock ,1 for paper and 2 for scissors"))
print("you choose")
print(game_images[user_input])

computer_choice = random.randint(0,2)
print("Computer choose:")
print(game_images[computer_choice])

if user_input >= 3 or user_input < 0:
    print("Invalid entry , You lose")
elif user_input == 0 and computer_choice == 2 :
    print("You win!")
elif user_input == 2 and computer_choice == 0 :
    print("you lose")
elif computer_choice > user_input:
    print("you lost")
elif user_input > computer_choice:
    print("you win!")
elif user_input == computer_choice:
    print("its a draw")