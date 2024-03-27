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
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
n = int(input("enter 1 for rock, 2 for paper and 3 for secissors \n"))
if n == 1:
    print(rock)
elif n == 2:
    print(paper)
else:
    print(scissors)
r = random.randrange(0, 4)
if r == 1:
    print(rock)
elif r == 2:
    print(paper)
else:
    print(scissors)

if n == r:
    print("It's a draw")
elif n == 1 & r == 3:
    print("You win")
elif n < r:
    print("You lose")
else:
    print("You Win")
