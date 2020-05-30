
import random


def hangman():
    
    list2 = ["Dream", "Cup", "Fountain"]
    ra = random.randint(0,2)
    word = list2[ra]
    
    
    
    wrong = 0 #keep track of letters they guessed wrong
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
            
              
    rletters = list(word) #keeps track of characters in the word
    board = ["__"] * len(word)  #track of letters they have yet to solve
    win = False #starts as false to keep track if Player Two has one yet
    print("Welcome to Hangman")


#2nd part of program

    while wrong < len(stages) -1:
      print("\n")
      msg = "Guess a letter:"
      char = input(msg)
      if char in rletters:
         cind = rletters.index(char)
         board[cind] = char
         rletters[cind] = '$'
      else:
         wrong+=1
      print((" ".join(board)))
      e = wrong + 1
      print("\n".join(stages[0:e]))
      if "__" not in board:
         print("You win!")
         print(" ".join(board))
         win = True
         break
    if not win:
      print("\n".join(stages[0:wrong]))
      print("You lose! It was {}.".format(word))




hangman()