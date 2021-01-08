#Rock paper Scissors
#Rock can loss against paper
#Paper can loss against scissors
#Scissor can loss against Rock
import random as rand
def RPS(User_name):
    option='Rock paper Scissor'.split(' ')
    points={'computer':0,User_name:0}
    while 5 not in list(points.values()):
        score_board(points)
        u_option=user_option_select()
        user_option=option[u_option-1]
        computer_option=rand.choice(option)
        if (computer_option=='paper' and user_option=='Rock') or (computer_option=='Scissor' and user_option=='paper') or (computer_option=='Rock' and user_option=='Scissor'):
            points['computer']+=1
        elif (computer_option=='Rock' and user_option=='paper') or (computer_option=='paper' and user_option=='Scissor') or (computer_option=='Scissor' and user_option=='Rock'):
            points[User_name]+=1
    for i in points:
        if points[i]==5:
            print(i,' is the winner of the game')
    return True
def user_input():
    print("This is Rock Paper Scissor game this game will be of 5 points against computer")
    return input("Please Enter your name:")
def score_board(points):
    print("\nScore board\n--------------")
    for i in points:
        print(i,':',points[i])
def user_option_select():
    user_input=int(input("\nSelct your option \n1.Rock \n2.Paper \n3.Scissor \nEnter your option:"))
    if user_input not in range(1,4):
        print("\nYou entered wrong option please enter again")
        return user_option_select()
    else:
        return user_input
while True:
    if RPS(user_input()):
        select=input('Do you want to play again(y/n):')
        if 'y'==select[0]:
            RPS(user_input())
        else:
            break
