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
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

rps = [rock, paper, scissors]
inp_str = input(
    "What do you choose? Type 0 for rock, Type 1 for paper, Type 2 for scissors: \n"
)
inp = int(inp_str)
if (inp > 2 or inp < 0):
    print("Invalid input!")
else:
    print(rps[inp])
    rand_num = random.randint(0, len(rps) - 1)
    print("Computer Chose: ")
    print(rps[rand_num])
    rps = ["rock", "paper", "scissors"]

    if (rps[inp] == "rock" and rps[rand_num] == "paper"):
        print("You lose!")
    elif (rps[inp] == "rock" and rps[rand_num] == "scissors"):
        print("You win!")
    elif (rps[inp] == "paper" and rps[rand_num] == "rock"):
        print("You win!")
    elif (rps[inp] == "paper" and rps[rand_num] == "scissors"):
        print("You lose!")
    elif (rps[inp] == "scissors" and rps[rand_num] == "rock"):
        print("You lose!")
    elif (rps[inp] == "scissors" and rps[rand_num] == "paper"):
        print("You win!")
    else:
        print("You draw!")
