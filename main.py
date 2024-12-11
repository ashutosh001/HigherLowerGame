from art import logo,versus
from questions import question
import random
print(logo)

score = 0
game_over = False

def pick_instagram_user(log):
    """Picks a random instagram user and checks the log
        Returns the picked user if it is not already in log"""
    pick = random.choice(question)
    if  pick not in log:
        log.append(pick)
        return pick
    else:
        return pick_instagram_user(log)
    
def compare_followers(q1,q2):
    """Compares the follower count of both the instagram users and returns the one with higher follower count"""
    if q1['follower_count'] > q2['follower_count']:
        return 'A'
    else:
        return 'B'

while not game_over:
    picked = []
    question1 = pick_instagram_user(picked)
    question2 = pick_instagram_user(picked)
    correct_ans = compare_followers(question1,question2)
    print(f"Compare A: {question1['name']}, {question1['description']}, {question1['country']}")
    print(versus)
    print(f"Compare B: {question2['name']}, {question2['description']}, {question2['country']}")
    answer = input("Type 'A' or 'B': ")
    if answer == correct_ans:
        score +=1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_over = True