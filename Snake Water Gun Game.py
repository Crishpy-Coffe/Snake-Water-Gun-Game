import random


def result( pc_op, you_op, decision, counter):
    counter = counter+1
    print(f"System choosed {pc_op} and You Choosed {you_op}\n {decision}!")
    print("Your = ", win, "System = ", loss, "Tie = ", tie)
    return counter


attempts = 0
win = 0
loss = 0
tie = 0
print("Welcome to the Snake,Water,Gun Game, \n")
while attempts <= 10:
    lst = ["s", "w", "g"]
    # pc = random.choice(lst)
    pc = "s"
    print("\n*******************************")
    you = input("Let's start \nS for Snake\nW for Water\nG for Gun:  ")
    you = you.lower()
    attempts = attempts+1
    # PC choose snake
    if pc == "s" and you == "s":
        tie = result("Snake", "Snake", "TIE", tie)

    elif pc == "s" and you == "g":
        win = result("Snake", "Gun", "WON", win)

    elif pc == "s" and you == "w":
        loss = result("Snake", "Water", "Won", loss)

# PC choose water
    elif pc == "w" and you == "g":
        loss = result("Water", "Gun", "Won", win)

    elif pc == "w" and you == "w":
        tie = result("Water", "Water", "TIE", tie)

    elif pc == "w" and you == "s":
        win = result("Water", "Sanke", "WON", win)

# PC chose gun
    elif pc == "g" and you == "g":
        tie = result("Gun", "Gun", "TIE", tie)

    elif pc == "g" and you == "w":
        win = result("Gun", "Water", "WON", win)

    elif pc == "g" and you == "s":
        loss = result("Gun", "Snake", "LOSS", loss)

    else:
        print("Invalid input")
        attempts = attempts-1

    if attempts < 11:
        print("Attempts left : ", 10-int(attempts))
    else:
        print("Game Over")
if loss > win:
    print("\nComputer won and you lost!\n")
elif loss < win:
    print("\nYou won and computer lost!\n")
else:
    print("It was a tie!")
    # print("Invalid")

