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
user_choice= int(input("what do you choose ? type 0 for rock ,1 for Paper or 2 for Scissors "))
image=[rock,paper,scissors]
computer_input=random.randint(0,2)
computer_choice=image[computer_input]
if user_choice>=3 or user_choice<0:
    print("invalid number try again ")
else:
    print(image[user_choice])
    print("Computer choice :")
    print(computer_choice)
    if user_choice == computer_input:
        print("It's a tie")
    elif computer_input==0 and  user_choice==1:
        print("you win")
    elif computer_input==1 and  user_choice==0:
        print("you lose")
    elif computer_input==0 and user_choice==2:
        print("you lose")
    elif computer_input==2 and user_choice==0:
        print("you win")
    elif computer_input==1 and user_choice==2:
        print("you win")
    elif computer_input==2 and user_choice==1:
        print(" you lose")










































































































