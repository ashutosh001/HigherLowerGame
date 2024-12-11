from art import logo,versus
from questions import question
print(logo)

score = 0
game_over = False

while not game_over:
    question1 = "question1"
    question2 = "question2"
    correct_ans = 'A'
    print(question1)
    print(versus)
    print(question2)
    answer = input("Type 'A' or 'B': ")
    if answer == correct_ans:
        score +=1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_over = True