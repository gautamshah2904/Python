import random as rand
rand_no=rand.randint(1,100)
play='y'
while play=='y':
    Try=5
    while Try!=0:
        try:
            guess_no=int(input("Enter your guess in between number:"))
        except ValueError:
            print("Please Enter a number in integer")
            continue
        Try-=1
        if guess_no>rand_no:
            print("The guessed number is grater then actual number \nThe number of attempt left ",Try)
        elif guess_no<rand_no:
            print("The guessed number is less then actual number \nThe number of attempt left ",Try)
        else:
            print("You guessed right number congratulations")
            break
    play=input("You completed all the attempt Do you want to play again?(y/n):")
