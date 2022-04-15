# Treasure Island
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print('Welcome to Treasure Island!! \n')

print('Your mission is to find the treasure \n')
direction = input('You \'re at a crossroad, where do you want to go?? "Left-L/l" OR "Right-R/r"?? \n')

if direction=='L' or direction=='l':
    print('You fell off the cliff, Game Over!! \n');
else:
    lakeDecision = input('Now you have arrived over a lake and there you see an island in the middle.Type "s/S" to swim OR "w/W" to wait for a boat or raft \n')
    if lakeDecision == 's' or lakeDecision == 'S':
        print("Sharks ate you....Game Over!! \n");
    else:
        door = input('Which door would you choose ? "Red - R/r" | "Blue - B/b" | "Yellow - Y/y" \n')
        if door == 'R' or door == 'r':
            print("The room is on FIRE!!....Game Over!!! \n")
        elif door == 'B' or door == 'b':
            print('It doesn\'t seems like the treasure.....Oh NO ,its a trap....Game Over!!! \n')
        else:
            print('Yayy!! you found the treasure...!!!We are rich now!!✨😆 \n')

