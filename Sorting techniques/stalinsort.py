#made by @athreyas0906 23/03/2026
#if any part of the list isn't in order, half of the list is randomly eliminated until the resulting list is in order
import random
l=eval(input('Enter elements of list in square brackets : '))

poscheck=0
def check(l):
    for i in range(len(l)):
        if i!=0:
            if l[i]<l[i-1]:
                return True
            else:
                continue

while check(l):
    llen=len(l)
    dellist=[]
    delnum=llen//2
    for i in range(delnum):
        pos=random.randint(0,llen-1)
        if pos not in dellist:
            dellist.append(pos)
        else:
            a=random.randint(0,llen-1)
            while a==pos:
                continue
            else:
                dellist.append(a)
    for i in dellist:
        print(l.pop(i))
    print('halfed')
else:
    print(l)
