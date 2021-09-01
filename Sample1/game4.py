import random
m=1
n=100
a=random.randint(m,n)
print (' the a is: ', a)
b=input('plz enter your idea between [higher,lower,exact]: ')
while b!= 'exact' :
    if b=='higher':
        m=a
        a=random.randint(m,n)

    
    else :
        n=a
        a=random.randint(m,n)
    print (' the a is: ', a)
    b=input('plz enter your idea between [higher,lower,exact]: ')
print ('haha "b" is :' ,a )
