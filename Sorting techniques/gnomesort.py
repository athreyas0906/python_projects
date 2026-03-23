#made by @athreyas0906 on 23/03/2026
#regular sorting algorithm
l=eval(input('Enter elements of list in square brackets : '))
llen=len(l)
poscheck=0
def check(l):
    for i in range(len(l)):
        if i!=0:
            if l[i]<l[i-1]:
                return True
            else:
                continue

while check(l):
    currpos=0
    if poscheck!=0:
        if l[poscheck]<l[poscheck-1]:
            currpos1=poscheck
            poscheck+=1
            while l[currpos1]<l[currpos1-1] and ((currpos1-1)!=-1):
                l[currpos1],l[currpos1-1]=l[currpos1-1],l[currpos1]
                currpos1-=1
            else:
                currpos=0
        else:
            poscheck+=1
    else:
        poscheck+=1
print(l)
