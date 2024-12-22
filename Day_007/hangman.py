import random
import hangman_words
import hangman_art

stages = hangman_art.art
word_list = hangman_words.words 
no_of_lives_left = 6

print(hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"********** {no_of_lives_left} LIVES LEFT **********")
    guess = input("Guess the letter: ").lower()
    if guess in correct_letters:
        print(f"You 've already guessed {guess}")
    # print(guess)
    
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
            # if letter not in correct_letters:
            #     correct_letters.append(letter)
            # else:
            #     print(f"You have already guessed {letter} try another one!")
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
            print(f"you guessed {guess}, that is not in the word. You lose a life!")
            no_of_lives_left -= 1
            # print(f"********** {no_of_lives_left} LIVES LEFT **********")
            if no_of_lives_left == 0:
                game_over = True
                print("********** YOU LOSE **********")
    if "_" not in display:
        game_over = True
        print("********** YOU WIN **********")
    print(stages[no_of_lives_left])
    
