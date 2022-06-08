from operator import le
import random
import wordList


random_word = wordList.words[random.randint(1,len(wordList.words)-1)]

lives = 7
correct_guesses = 0

hangman_list = ['''
--------------

   +-----+
   |     |
         |
         |
         |
         |
         |

------------
------------
''',
'''
--------------

   +-----+
   |     |
   O     |
         |
         |
         |
         |

------------
------------
''',
'''
--------------

   +-----+
   |     |
   O     |
   |     |
         |
         |
         |

------------
------------
''',
'''
--------------

   +-----+
   |     |
   O     |
   |     |
   |     |
         |
         |

------------
------------
''',
'''
--------------

   +-----+
   |     |
   O     |
  \|     |
   |     |
         |
         |

------------
------------
''',
'''
--------------

   +-----+
   |     |
   O     |
  \|/    |
   |     |
         |
         |

------------
------------
''',
'''
--------------

   +-----+
   |     |
   O     |
  \|/    |
   |     |
  /      |
         |

------------
------------
''',
'''
--------------

   +-----+
   |     |
   O     |
  \|/    |
   |     |
  / \    |
         |

------------
------------
''']

print("Welcome to Hangman Game!!")
print(hangman_list[0])

guess_list = []

guess_list += "_"*len(random_word)

while lives>0 and correct_guesses!=len(random_word):
    correct_choice = 0
    guess_letter = input("\nGuess a letter in word : ").lower()
    if(guess_letter in guess_list):
        print("Already guessed correct letter")
        print(guess_list)
        print("lives remaining : "+str(lives))
        continue

    for i in range(0,len(random_word)):
        current_pos_letter = random_word[i]
        if guess_letter==current_pos_letter:
            guess_list[i] = guess_letter
            correct_choice = 1
            correct_guesses += 1

    if(correct_choice == 1):
        print("Yay!! you are on the way")
        print(guess_list)
        print("lives remaining : "+str(lives))
        print(hangman_list[7-lives])
    else:
        print('naah,its not right')
        print(guess_list)
        lives -= 1
        print("lives remaining : "+str(lives))
        print(hangman_list[7-lives])

                    
if correct_guesses == len(random_word):
    print('WOW!! YOU WIN')
    print("The word was "+random_word)
else:
    print('you lose, better luck next time!!')
    print("The word was "+random_word)
