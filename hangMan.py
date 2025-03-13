import time
import random as rand

words_list = None
try:
    with open('/usr/share/dict/words', 'r') as f:
        words_list = f.read().splitlines()
except FileNotFoundError:
    print("System dictionary not found.")

hangman = [   " O ",
           "/","|","\\",
            "/", " \\"]

line_counter = {
                 0 : 1,
                 1 : 3,
                 2 : 2
               }

board = ["-------",
         "|/   | ",
         "|   ",
         "|   ",
         "|   ",
         "|   "]

def printBoard(board: []):
    for i in range(len(board)):
        print(board[i])
    print()

def printHiddenWord(word: str, guess: dict):
    for idx in range(len(word)):
        if guess[word[idx]] == True:
            print(word[idx], end="")
        else:
            print(" _ ", end="")
    print()

def guessed(guess: dict) -> bool:
    for letter in guess:
        if guess[letter] == False:
            return False
    return True

def makeDict(words_list: []) -> dict:
    temp = {}
    for i  in range(len(words_list)):
        word = words_list[i].lower()
        if word not in temp:
            temp[word] = { word[letter] : False for letter in range(len(word))}
    return temp

dict_words = makeDict(words_list)
prev_guesses = set()

rand.seed(time.time())
printBoard(board)
# Find a word that does not have '
hiddenWord = "'"
while hiddenWord.find("'") != -1:
    hiddenWord = rand.choice(list(dict_words.keys()))
guess = dict_words[hiddenWord]
printHiddenWord(hiddenWord, guess)
maxCounter = 0
line = 0

while not guessed(guess) and maxCounter < 6:
    letter = input("Guess a letter: ").lower()
    prev_guesses.add(letter)
    if letter in guess:
        guess[letter] = True
    else:
        board[line+2] = board[line+2] + hangman[maxCounter]
        maxCounter += 1
        line_counter[line] -= 1
        if line_counter[line] == 0:
            line += 1
    printBoard(board)
    print("Previous guesses: ", prev_guesses)
    printHiddenWord(hiddenWord, guess)

print()
if maxCounter == 6:
    print("YOU LOSE!")
else:
    print("YOU WON!")
print("Hidden word: ", hiddenWord)
