def hangman(word):
    wrong = 0
    stages = ["",
              "__________    ",
              "|       |     ",
              "|       0     ",
              "|      /|\    ",
              "|      / \    ",
              "|             ",
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print ("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print ("\n")
        guess = input("Guess a letter: ")
        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        print("\n".join(stages[0: wrong + 1]))
        if "__" not in board:
            print ("you win! The word was:")
            print (" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))


hangman("pickle")

