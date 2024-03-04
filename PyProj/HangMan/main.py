#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
import hangman_art
import hangman_words
import random

stages = hangman_art.stages
logo = hangman_art.logo
words = hangman_words.word_list
chosen_word = random.choice(words)

print(logo)

n = len(chosen_word)

print(chosen_word)

op_word = []

for letter in chosen_word:
  op_word += '_'

hang = 0

def display(li) :
  for i in li :
    print(i, end = "")
  print()

def checkEqual(chosen_word, op_word) :
  for i in range(n) :
    if chosen_word[i] != op_word[i] :
      return False
  return True

display(op_word)



while (not checkEqual(chosen_word, op_word) and hang < n) :

  count = 0
  guess = input("Choose a letter: ").lower()

  for i in range(0, n) :
    if guess == chosen_word[i] :
      op_word[i] = guess
      count += 1

  if count == 0:
    hang += 1
    print(stages[6 - hang])

  display(op_word)

if hang == n :
  print("You lose!")
else :
  print("You win!")