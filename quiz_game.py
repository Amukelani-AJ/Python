print("Welcome to the Quiz Game")

playing = input("Do you want to play the game (y/n)?")

if playing.lower() != "y":
    print("Please come again")
    quit()

q_answer = input ("Whats 1+1 = ")
score = 0
if q_answer == '2':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f'Your score is: {score}')