from hangman_art import stages,logo
from hangman_words import word_list
import random
print(logo)
chosen_word=random.choice(word_list)
print(chosen_word)
word_length=len(chosen_word)
game_over=False
correct_list=[]
placeholder=""
for i in range(word_length):
    placeholder+="_"
print("Word to guess: " + placeholder)
lives=6
num=0


while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_list:
        print(f"You've already guessed {guess}")
    display=""
    for letter in chosen_word:
        if letter==guess:
            correct_list.append(letter)
            display+=letter
            num+=1
        elif letter  in  correct_list:
            display+=letter
        else:
            display+="_"
    print(display)
    if num == word_length:
        game_over = True
        print("****************************YOU WIN****************************")
    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives==0:
            game_over=True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    print(stages[lives])



