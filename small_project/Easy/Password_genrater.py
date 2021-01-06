import string as stri
import random as rand
def Master(Length):
    Symbol=list(stri.punctuation)
    Capital=list(stri.ascii_uppercase)
    Lower=list(stri.ascii_lowercase)
    Digits=list(map(str,stri.digits))
    wish_list=list()
    option=['Symbol','Capital','Lower','Digits']
    option_value=[Symbol,Capital,Lower,Digits]
    if 'y'==input("Do you want customization option in password(y/n):")[0]:
        for i in option:
            if 'y'==input("Do you want {} in you password(y/n):".format(i))[0]:
                wish_list.append(True)
            else:
                wish_list.append(False)
        Password=''
        min=Length//wish_list.count(True)
        wish_dict=dict(zip(option,wish_list))
        wish_combine=list()
        count=0
        for i in option:
            if wish_dict[i]:
                wish_combine+=option_value[count]
                for j in range(min):
                    Password=Password+rand.choice(option_value[count])
            count+=1
        while Length!=len(Password):
            Password=Password+rand.choice(wish_combine)
        return ''.join(rand.sample(Password,len(Password)))
    else:
        Password=''
        ALL=Symbol+Capital+Lower+Digits
        for i in range(Length):
            Password=Password+rand.choice(ALL)
        return Password
try:
    Length=int(input("Enter length of password:"))
    print("Your Password is ",Master(Length))
except:
    print("Something went wrong")
