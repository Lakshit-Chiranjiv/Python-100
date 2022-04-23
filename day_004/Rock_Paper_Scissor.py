import random

print("ROCK-PAPER-SCISSORS")
print("Whoever get 5 points first, wins this game!!\n")

user_points = 0
computer_points = 0

choices = ['r','p','s']

#while loop hasn't been taught in course till day 4 yet I am using it to make the game more fun
while user_points<5 and computer_points<5:
    user_choice = input("Enter \nr/R for ROCK\np/P for PAPER\ns/S for SCISSOR\nEnter your choice : ")
    computer_choice = choices[random.randint(0,2)]
    if user_choice=='r' and computer_choice=='p':
        computer_points += 1
        print("You chose ROCK - Computer chose PAPER --> Computer wins this round")
    elif user_choice=='p' and computer_choice=='s':
        computer_points += 1
        print("You chose PAPER - Computer chose SCISSOR --> Computer wins this round")
    elif user_choice=='s' and computer_choice=='r':
        computer_points += 1
        print("You chose SCISSOR - Computer chose ROCK --> Computer wins this round")
    elif user_choice=='r' and computer_choice=='s':
        user_points += 1
        print("You chose ROCK - Computer chose SCISSOR --> You win this round")
    elif user_choice=='p' and computer_choice=='r':
        user_points += 1
        print("You chose PAPER - Computer chose ROCK --> You win this round")
    elif user_choice=='s' and computer_choice=='p':
        user_points += 1
        print("You chose SCISSOR - Computer chose PAPER --> You win this round")
    else:
        print("Round TIED")
    print(f"Computer = {computer_points} | You = {user_points}\n")

if(computer_points>user_points):
    print("Computer won the game, Good luck next time!!")
else:
    print("You won the game, Congratss!!!")

print(f"Computer = {computer_points} | You = {user_points}\n")
print("GAME OVER!!")