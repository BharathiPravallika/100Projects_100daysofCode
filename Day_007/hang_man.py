import random
stages = ['''
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
''','''
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
''','''
    +---+
    |   |
    o   |
   /|\  |
        |
        |
''','''
    +---+
    |   |
    o   |
   /|   |
        |
        |
''','''
    +---+
    |   |
    o   |
        |
        |
        |
''',''' 
    +---+
    |   |
        |
        |
        |
        |
'''
]
word_list = ["lion", "tiger", "elephant"]
no_of_lives_left = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess the letter: ").lower()
    print(guess)
    
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
            no_of_lives_left -= 1
            if no_of_lives_left == 0:
                game_over = True
                print("you lose")
    if "_" not in display:
        game_over = True
        print("You Win!")
    print(stages[no_of_lives_left])
    
    
