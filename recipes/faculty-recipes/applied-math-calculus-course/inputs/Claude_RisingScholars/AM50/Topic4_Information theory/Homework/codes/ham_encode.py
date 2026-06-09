from random import randint
f=open("regina","r")

s=f.read()

q="On ne voit bien qu'avec le coeur. L'essentiel est invisible pour les yeux."

no=''
for i in range(len(q)):
    no+="{0:08b}".format(ord(q[i]))

while(len(no)<6*len(s)):
    no+=str(randint(0,1))

m=""
for i in range(len(s)):
    a=ord(s[i])
    for j in [0,1]:
        b=(a&240)>>1
        if(b&64):
            b^=5
        if(b&32):
            b^=6
        if(b&16):
            b^=7
        if(b&8):
            b^=3

        c=int(no[6*i+3*j:6*i+3*j+3],2)
        if(c!=0):
            b^=1<<(7-c)

        m+="{0:07b}".format(b)
        a<<=4

print m
