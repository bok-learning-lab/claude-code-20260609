from random import randint

a=open("mj","r")

s=a.read()
zc=["000","100","010","001"]
oc=["111","011","101","110"]

q=""
for i in range(len(s)):
    o=ord(s[i])
    k=128
    while(k!=0):
        if(o&k):
            q+=oc[randint(0,3)]
        else:
            q+=zc[randint(0,3)]
        k>>=1

print q
            
            

