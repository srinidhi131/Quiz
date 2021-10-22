import random as r
print("Which Animal Are You?")
def fun1():
    def fun(question,a,b,c,d,e):
        su=0
        print(question)
        print(a,b,c,d,e)
        s=input("Enter an option.")
        if s=='a':
         su=su+r.randrange(0,51,10)
        elif s=='b':
         su=su+r.randrange(0,51,10)
        elif s=='c':
         su=su+r.randrange(0,51,10)
        elif s=='d':
         su=su+r.randrange(0,51,10)
        elif s=='e':
         su=su+r.randrange(0,51,10)
        else:
         print("invalid option")
        return su
    a=fun('Which Adventure Activity Would You Choose?',"a)Zip Lining","b)Skiing","c)Sky Diving","d)Surfing","e)Gliding")
    b=fun("What is more important to you?","a)Money","b)Love","c)Family","d)Friends","e)Yourself")
    c=fun("Choose a colour?","a)White","b)Red","c)Purple","d)Black","e)Blue")
    d=fun("What is your soul element?","a)Air","b)Fire","c)Water","d)Earth","e)Metal")
    e=fun("You are....","a)Violent","b)Lazy","c)Stuborn","d)Shy","e)Lonely")
    f=fun("What you want to be?","a)Teacher","b)Writer","c)Politician","d)Soldier","e)Engineer")
    g=fun("Which group fits your personality?","a)Loyal,Curious and Playful","b)Innocent,Confident and Outgoing","c)Brave,Sensitive and Daring","d)Honest, Powerful and Elegant","e)Calm, EMotional and Positive")
    su=a+b+c+d+e+f+g
    print(su)
    if 0<=su<=50:
                print("You are a Cat.You are intelligent,playful,loyal,adventurous,sensitive and kind")
    elif 60<=su<=110:
                print("You are a Bear.You are protective,sensitive,devoted,ethical,strict,attentive and social")
    elif 120<=su<=160:
                print("You are a tiger.You are powerful,fashionable,curious,self confident,brave and elegant")
    elif 170<=su<=220:
                print("You are a wolf. You are intelligent,powerful,independent,desicive,passionate and efficient")
    else:
                print("You are a Panda. You are playful,adorable,introvet,balanced and peace loving")
    a=input("Do you want to continue?(Y/N)")
    if a=="N":
      print("Have a good day")
    else:
      fun1()
fun1()



