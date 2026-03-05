
field={
    1:{1:' ',2:' ',3:' '},
    2:{1:' ',2:' ',3:' '},
    3:{1:' ',2:' ',3:' '}
    }
pturns=[]
pmovenum=1
pmovelist=[]
pchar={1:'x',2:'o'}
pcharinv={'x':1,'o':2}
print('Welcome players!')

def showboard(field):
    for i in range(1,4):
        for j in range(1,4):
            if j!=3:
                print(' '+field[i][j],end=' |')
            else:
                print(field[i][j])
        if i!=3:
            print('-'*11)

def notoccupied(pchrow,pchcol,field):
    if field[pchrow][pchcol]==' ':
        return True
    else:
        return False

def firstmove(ppref,pchar):
    psym=pchar[ppref]
    pfmove=ppref
    print('Choose square to begin : (type row_number*10+column_number)')
    pchoice=int(input(''))
    pchrow=int(pchoice//10)
    pchcol=int(pchoice%10)
    return (psym,pfmove,pchrow,pchcol)

def makemove(pchar,ptomove):
    psym=pchar[ptomove]
    print('Player',ptomove,'has to move')
    print('Choose square to occupy : (type row_number*10+column_number)')
    pchoice=int(input(''))
    pchrow=int(pchoice//10)
    pchcol=int(pchoice%10)
    return (psym,pchrow,pchcol)

def pmove(pturns,pchar,pmovelist,field):
    if len(pmovelist)==0:
        print('Choose player to make first move : (1 or 2)')
        ppref=int(input(''))
        pmnum=int(pmovenum)       
        psym,pfmove,pchrow,pchcol=firstmove(ppref,pchar)
        field[pchrow][pchcol]=psym
        pmovelist+=[int(pfmove)]
        
    else:
        if len(pmovelist)%2!=0:
            ptomove=0
            for i in pchar:
                if i!=pmovelist[0]:
                    ptomove=int(i)
            
            psym,pchrow,pchcol=makemove(pchar,ptomove)
            
            while not notoccupied(pchrow,pchcol,field):
                print('Invalid move, square already occupied')
                psym,pchrow,pchcol=makemove(pchar,ptomove)
            else:
                field[pchrow][pchcol]=psym
                pmovelist+=[int(ptomove)]
        else:
            ptomove=pmovelist[0]
            psym,pchrow,pchcol=makemove(pchar,ptomove)
            if notoccupied(pchrow,pchcol,field):
                field[pchrow][pchcol]=psym
                pmovelist+=[int(ptomove)]
            
            while not notoccupied(pchrow,pchcol,field):
                print('Invalid move, square already occupied')
                psym,pchrow,pchcol=makemove(pchar,ptomove)
            else:
                field[pchrow][pchcol]=psym
                pmovelist+=[int(ptomove)]

def anyrowiswon(field,pcharinv):
    for i in range(1,4):
        if field[i][1]==field[i][2]!=' ' and field[i][2]==field[i][3]!=' ':
            pwon=pcharinv[field[i][1]]
            return (pwon,True)
    else:
        return (0,False)
def anycoliswon(field,pcharinv):
    for i in range(1,4):
        if field[1][i]==field[2][i]!=' ' and field[2][i]==field[3][i]!=' ':
            pwon=pcharinv[field[1][i]]
            return (pwon,True)
    else:
        return (0,False)
def anydiagiswon(field,pcharinv):
    if (field[1][1]==field[2][2]!=' ' and field[2][2]==field[3][3]!=' '):
        pwon=pcharinv[field[1][1]]
        return (pwon,True)
    elif (field[1][3]==field[2][2]!=' ' and field[2][2]==field[3][1]!=' '):
        pwon=pcharinv[field[3][1]]
        return (pwon,True)
    else:
        return (0,False)


chk=True
while chk:
    winner1,gamewon1=anyrowiswon(field,pcharinv)
    winner2,gamewon2=anycoliswon(field,pcharinv)
    winner3,gamewon3=anydiagiswon(field,pcharinv)
    winner=winner1+winner2+winner3
    
    gamewon=gamewon1 or gamewon2 or gamewon3
    if gamewon:
        print('Player',winner,'has won the game!')
        chk=False
    else:
        pmove(pturns,pchar,pmovelist,field)
        showboard(field)
    
        
        
