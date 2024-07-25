#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

print("HANGMAN\n")

name = input("What is your name? ")
print("Good Luck ! ", name)

words = ['artificial', 'python', 'king', 'india', 'digital', 'language', 'space', 'robot','machine', 'system', 'economy', 'minister']


word = random.choice(words)


print("Guess the characters::")

guessed = ''


turns = 15


while turns > 0:


    failed_attempt = 0

  
    for char in word:

      
        if char in guessed:
            print(char, end=" ")

        else:
            print("_")

          
            failed_attempt += 1

    if failed_attempt == 0:
       
        print("\nYou Win!!")

       
        print("The word is: ", word)
        break

 
    print()
    guess = input("Guess a character:")

  
    guessed += guess

 
    if guess not in word:

        turns -= 1

   
        print("Wrong!")

     
        print("You have", + turns, 'more guesses..')

        if turns == 0:
            print("\nYou Loose!!")


# In[ ]:




