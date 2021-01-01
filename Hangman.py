import random
dictionary = ["hello", "anime", "memes", "poggers", "establishment"]
word = dictionary[(random.randint(0, len(dictionary)))]
operable_word = []
guessing_word = []
guessed_letters = []
score = 5
won = False
for letter in word:
    operable_word.append(letter)

for letter in word:
    guessing_word.append("_")

def guessing(guess):
    global score
    if guess in guessed_letters:
        print("You have already guessed this letter.")
    if guess not in guessed_letters:
        for letter in operable_word:
            if guess in operable_word:
                pos = int(operable_word.index(guess))
                guessing_word[pos] = str(guess)
                operable_word[pos] = '_'
                if guess not in guessed_letters:
                    guessed_letters.append(guess)
        if guess not in word:
            guessed_letters.append(guess)
            score -= 1
            
print("Welcome to Hangman! You have 5 lives. \n")

while score > 0  and "_" in guessing_word:
    print(str(guessing_word) + "\n")
    print(str(guessed_letters))
    guess = input(str("Guess a letter: \n"))
    guessing(guess)
    print("You have " + str(score) + "/5 lives left. \n")
    
if score == 0:
    print("You have ran out of lives! The word was " + word)
    
if "_" not in guessing_word:
    print("Congratulations! You got the word with " + str(score) + "/5 lives remaining!\n The word was: " + str(word))