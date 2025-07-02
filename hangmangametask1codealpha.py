import random


wlist = ["heart", "gamer", "lemon", "wheat", "robot"]


sw = random.choice(wlist)
guesser = []
tries = 6


dw = ["_" for _ in sw]

print("welcome to Hangman Game...!")
print("Guess the word, one letter at a time.")
print("You have", tries, "incorrect guesses allowed.")
print("Word: ", " ".join(dw))

while tries > 0 and "_" in dw:
    guess = input("Enter a letter: ")

    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single letter.")
        continue

    if guess in guesser:
        print("you already guessed that letter.")
        continue

    guesser.append(guess)

    if guess in sw:
        print(" Good guess!")
        for i in range(len(sw)):
            if sw[i] == guess:
                dw[i] = guess
    else:
        tries -= 1
        print(" Wrong guess. Tries left:", tries)

    print("Word: ", " ".join(dw))
    print("Guessed letters:", ", ".join(guesser))

if "_" not in dw:
    print("congratulations! You guessed the word:", sw)
else:
    print(" Sorry no more Tries ....Game Over!The word was:", sw)

