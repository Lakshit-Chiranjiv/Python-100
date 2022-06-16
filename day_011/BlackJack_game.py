import random
print("Welcome to Black-Jack Game")

card_numbers = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards = [random.choice(card_numbers),random.choice(card_numbers)]
computer_cards = [random.choice(card_numbers),random.choice(card_numbers)]

user_cards_sum = sum(user_cards)
print("Your cards are : "+str(user_cards)+" and card sum is : "+str(user_cards_sum))

computer_cards_sum = sum(computer_cards)
print("1st Computer card is : "+str(computer_cards[0]))

if user_cards_sum == 21 and computer_cards_sum < 21:
    print("User Won")
elif user_cards_sum < 21 and computer_cards_sum == 21:
    print("Computer Won")
elif user_cards_sum == 21 and computer_cards_sum == 21:
    print("Match Tied")
else:
    user_choice = input("Do you want to Hit or Stand : H/S")