import random
print("\t\t\tWELCOME TO THE HANGMAN GAME!")
print("\tRULES-"
      "You have 5 chances to guess the right continent in the world")
cont=["North America","South America","Europe","Asia","Africa","Oceania"]
name=random.choice(cont)
gcount=0
print("\t\t\t\tWord: "+"_"*len(name))
while gcount<5:
    guess=input("\nGuess the word:").title()
    gcount += 1
    print("No of guesses left are:"+ str(5-gcount))
    if guess == name:
        print("you won the game!")
        break
    elif guess != name:
        print("wrong guess!")
else:
    print("you have lost the game!")
    print("the word was:"+name)




