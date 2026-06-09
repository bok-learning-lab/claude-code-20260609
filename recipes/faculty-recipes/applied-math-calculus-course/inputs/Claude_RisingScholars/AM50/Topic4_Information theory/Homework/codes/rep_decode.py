from random import randint

a=open("code1.txt","r")

dec={"000":0,"001":0,"010":0,"100":0,"110":1,"101":1,"011":1,"111":1}

s=a.read().rstrip()

q=''
i=0
while(i<len(s)):

    k=0
    for l in range(8):
        k<<=1
        k|=dec[s[i:i+3]]
        i+=3

    q+=chr(k)
    
print q
