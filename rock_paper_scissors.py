import random

user_score = 0
computer_score = 0
options = ["rock", "paper", "scissor"]

while True:
    user_pick = input("Enter Rock/Paper/Scissor,(press Q to quit) :").lower()
    if user_pick == 'q':
        break

    if user_pick not in options:
        print("Please either rock,paper,scissor")
        continue

    random_val = random.randint(0,2)
    computer_pick = options[random_val]

    #Choice
    print(f'You chose {user_pick} and Computer picked {computer_pick}')


    if user_pick == "rock" and computer_pick == "scissor":
        user_score += 1
        print("You Won!!")
    elif user_pick == "paper" and computer_pick == "rock":
        user_score += 1
        print("You Won!!")
    elif user_pick == "scissor" and computer_pick == "paper":
        user_score += 1
        print("You Won!!")
    elif user_pick == computer_pick:
        print("Draw!!")
    else:
        computer_score += 1
        print("Computer Won!!")

print(f'You Won x{user_score}')
print(f'Computer Won x{computer_score}')



