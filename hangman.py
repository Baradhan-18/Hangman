import random
words=['ironman','captain america','loki','hulk','thor']
chooseword=random.choice(words)
word_display=['_' for _ in chooseword]
print(word_display)
attempts=7
print("Welcome To Hangman")
while(attempts > 0 and '_' in word_display):
    print("\n"+' '.join(word_display))
    guess=input("Guess a Letter: ").lower()
    if guess in chooseword:
        for index, letter in enumerate(chooseword):
            if letter==guess:
                word_display[index]=guess
    else:
        print("The word is not present!!!")
        attempts-=1
if '_' not in word_display:
    print("you guessed the word")
    print(' '.join(word_display))
    print("you survied")
else:
    print('You ran out of attempts. the word was: '+chooseword)
    print("YOU LOST")