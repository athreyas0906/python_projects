#by athreya s, @athreyas0906 on github, made on 5th march,2026
field={
    1:{
        1:{1:' ',2:' ',3:' '},
        2:{1:' ',2:' ',3:' '},
        3:{1:' ',2:' ',3:' '}},
    2:{
        1:{1:' ',2:' ',3:' '},
        2:{1:' ',2:' ',3:' '},
        3:{1:' ',2:' ',3:' '}},
    3:{
        1:{1:' ',2:' ',3:' '},
        2:{1:' ',2:' ',3:' '},
        3:{1:' ',2:' ',3:' '}},
    4:{
        1:{1:' ',2:' ',3:' '},
        2:{1:' ',2:' ',3:' '},
        3:{1:' ',2:' ',3:' '}},
    5:{
        1:{1:' ',2:' ',3:' '},
        2:{1:' ',2:' ',3:' '},
        3:{1:' ',2:' ',3:' '}},
    6:{
        1:{1:' ',2:' ',3:' '},
        2:{1:' ',2:' ',3:' '},
        3:{1:' ',2:' ',3:' '}},
    7:{
        1:{1:' ',2:' ',3:' '},
        2:{1:' ',2:' ',3:' '},
        3:{1:' ',2:' ',3:' '}},
    8:{
        1:{1:' ',2:' ',3:' '},
        2:{1:' ',2:' ',3:' '},
        3:{1:' ',2:' ',3:' '}},
    9:{
        1:{1:' ',2:' ',3:' '},
        2:{1:' ',2:' ',3:' '},
        3:{1:' ',2:' ',3:' '}}
    }
fieldwins={
    1:' ',
    2:' ',
    3:' ',
    4:' ',
    5:' ',
    6:' ',
    7:' ',
    8:' ',
    9:' '
    }

pturns=[]
pmovelist=[]
pprevchoice=[0]
pchar={1:'x',2:'o'}
pcharinv={'x':1,'o':2}
print('Welcome players!')

def showboard(field):
    for line in range(1,10):
        if line<=3 and line>=0:
            for table in range(1,4):
                for cell in range(1,4):
                    if cell<3:
                            print('',field[table][line][cell],end=' |')
                    elif cell==3 and table==3:
                            print('',field[table][line][cell])
                    elif cell==3 and table!=3:
                            print('',field[table][line][cell],end=' ||')
            print('-'*37)
        if line==3:
            print('-'*37)
        elif line<=6 and line>3:
            line1=line-3
            for table in range(4,7):
                for cell in range(1,4):
                    if cell<3:
                            print('',field[table][line1][cell],end=' |')
                    elif cell==3 and table==6:
                            print('',field[table][line1][cell])
                    elif cell==3 and table!=6:
                            print('',field[table][line1][cell],end=' ||')
            print('-'*37)
        if line==6:
            print('-'*37)
        elif line>6 and line<10:
            line1=line-6
            for table in range(7,10):
                for cell in range(1,4):
                    if cell<3:
                            print('',field[table][line1][cell],end=' |')
                    elif cell==3 and table==9:
                            print('',field[table][line1][cell])
                    elif cell==3 and table!=9:
                            print('',field[table][line1][cell],end=' ||')
            if line!=9:
                print('-'*37)

def occupied(pchfield, pchrow,pchcol,field):
    if field[pchfield][pchrow][pchcol]==' ':
        return False
    else:
        return True

def fieldwon(pchfield,fieldwins):
    if fieldwins[pchfield]==' ':
        return False
    else:
        return True

def firstmove(ppref,pchar):
    psym=pchar[ppref]
    pfmove=ppref
    print('Choose field to begin : (1-9)')
    pchfield=int(input(''))
    print('Choose square : (type row_number*10+column_number)')
    pchoice=int(input(''))
    pchrow=int(pchoice//10)
    pchcol=int(pchoice%10)
    return (psym,pchfield,pchrow,pchcol)

def makemove(pchar,ptomove,pprevchoice):
    psym=pchar[ptomove]
    print('Player',ptomove,'has to move')
    pchfield=int(pprevchoice[0])
    print('Now playing in field',pchfield)
    print('Choose square to occupy : (type row_number*10+column_number)')
    pchoice=int(input(''))
    pchrow=int(pchoice//10)
    pchcol=int(pchoice%10)
    return (psym,pchfield,pchrow,pchcol)

def choosenext(pchrow,pchcol):
    fieldnum=0
    if pchrow==1:
        fieldnum=pchcol
    elif pchrow==2:
        fieldnum=pchcol+3
    elif pchrow==3:
        fieldnum=pchcol+6
    return fieldnum

def pmove(pturns,pchar,pmovelist,field,fieldwins,pprevchoice):
    if len(pmovelist)==0:
        print('Choose player to make first move : (1 or 2)')
        ppref=int(input(''))       
        psym,pchfield,pchrow,pchcol=firstmove(ppref,pchar)
        field[pchfield][pchrow][pchcol]=psym
        pmovelist+=[int(ppref)]
        pprevchoice[0]=choosenext(pchrow,pchcol)
    else:
        if len(pmovelist)%2!=0:
            ptomove=0
            for i in pchar:
                if i!=pmovelist[0]:
                    ptomove=int(i)
            
            psym,pchfield,pchrow,pchcol=makemove(pchar,ptomove,pprevchoice)
            if not(occupied(pchfield, pchrow,pchcol,field)) and not(fieldwon(pchfield,fieldwins)):
                field[pchfield][pchrow][pchcol]=psym
                pmovelist+=[int(ptomove)]
                pprevchoice[0]=choosenext(pchrow,pchcol)
            
            while (occupied(pchfield, pchrow,pchcol,field) or fieldwon(pchfield,fieldwins)) and pmovelist[len(pmovelist)-1]!=ptomove:
                print('Invalid move')
                if occupied(pchfield, pchrow,pchcol,field):
                    print('This square has already been occupied, please select a new square')
                    psym,pchfield,pchrow,pchcol=makemove(pchar,ptomove,pprevchoice)
                if fieldwon(pchfield,fieldwins):
                    print('This field is won, please select new field to play in : (1-9)')
                    pprevchoice[0]=int(input(''))
                    psym,pchfield,pchrow,pchcol=makemove(pchar,ptomove,pprevchoice)
            else:
                field[pchfield][pchrow][pchcol]=psym
                if pmovelist[len(pmovelist)-1]!=ptomove:
                    pmovelist+=[int(ptomove)]
                pprevchoice[0]=choosenext(pchrow,pchcol)
                checkfieldwin(pchfield,field,fieldwins,pchar)
        else:
            ptomove=pmovelist[0]
            psym,pchfield,pchrow,pchcol=makemove(pchar,ptomove,pprevchoice)
            if not(occupied(pchfield, pchrow,pchcol,field)) and not(fieldwon(pchfield,fieldwins)):
                field[pchfield][pchrow][pchcol]=psym
                pmovelist+=[int(ptomove)]
                pprevchoice[0]=choosenext(pchrow,pchcol)
            
            while (occupied(pchfield, pchrow,pchcol,field) or fieldwon(pchfield,fieldwins)) and pmovelist[len(pmovelist)-1]!=ptomove:
                print('Invalid move')
                if occupied(pchfield, pchrow,pchcol,field):
                    print('This square has already been occupied, please select a new square')
                    psym,pchfield,pchrow,pchcol=makemove(pchar,ptomove,pprevchoice)
                if fieldwon(pchfield,fieldwins):
                    print('This field is won, please select new field to play in : (1-9)')
                    pprevchoice[0]=int(input(''))
                    psym,pchfield,pchrow,pchcol=makemove(pchar,ptomove,pprevchoice)
            else:
                field[pchfield][pchrow][pchcol]=psym
                if pmovelist[len(pmovelist)-1]!=ptomove:
                    pmovelist+=[int(ptomove)]
                pprevchoice[0]=choosenext(pchrow,pchcol)
                checkfieldwin(pchfield,field,fieldwins,pchar)

def checkfieldwin(pchfield,field,fieldwins,pchar):
    winner1,fieldwon1=anyrowiswon(field,pcharinv,pchfield)
    winner2,fieldwon2=anycoliswon(field,pcharinv,pchfield)
    winner3,fieldwon3=anydiagiswon(field,pcharinv,pchfield)
    winner=winner1+winner2+winner3
    fieldwon=fieldwon1 or fieldwon2 or fieldwon3
    if fieldwon:
        print('Player',winner,'has won field',pchfield,'!')
        fieldwins[pchfield]=pchar[int(winner)]

def anyrowiswon(field,pcharinv,pchfield):
    for i in range(1,4):
        if field[pchfield][i][1]==field[pchfield][i][2]!=' ' and field[pchfield][i][2]==field[pchfield][i][3]!=' ':
            pwon=pcharinv[field[pchfield][i][1]]
            return (pwon,True)
    else:
        return (0,False)
def anycoliswon(field,pcharinv,pchfield):
    for i in range(1,4):
        if field[pchfield][1][i]==field[pchfield][2][i]!=' ' and field[pchfield][2][i]==field[pchfield][3][i]!=' ':
            pwon=pcharinv[field[pchfield][1][i]]
            return (pwon,True)
    else:
        return (0,False)
def anydiagiswon(field,pcharinv,pchfield):
    if (field[pchfield][1][1]==field[pchfield][2][2]!=' ' and field[pchfield][2][2]==field[pchfield][3][3]!=' '):
        pwon=pcharinv[field[pchfield][1][1]]
        return (pwon,True)
    elif (field[pchfield][1][3]==field[pchfield][2][2]!=' ' and field[pchfield][2][2]==field[pchfield][3][1]!=' '):
        pwon=pcharinv[field[pchfield][3][1]]
        return (pwon,True)
    else:
        return (0,False)
def checkgamewin(fieldwins):
    if fieldwins[1]==fieldwins[2]!=' ' and fieldwins[2]==fieldwins[3]!=' ':
        pwon=pcharinv[fieldwins[1]]
        return (pwon,True)
    if fieldwins[4]==fieldwins[5]!=' ' and fieldwins[5]==fieldwins[6]!=' ':
        pwon=pcharinv[fieldwins[4]]
        return (pwon,True)
    if fieldwins[7]==fieldwins[8]!=' ' and fieldwins[8]==fieldwins[9]!=' ':
        pwon=pcharinv[fieldwins[9]]
        return (pwon,True)
    if fieldwins[1]==fieldwins[4]!=' ' and fieldwins[4]==fieldwins[7]!=' ':
        pwon=pcharinv[fieldwins[1]]
        return (pwon,True)
    if fieldwins[2]==fieldwins[5]!=' ' and fieldwins[5]==fieldwins[8]!=' ':
        pwon=pcharinv[fieldwins[1]]
        return (pwon,True) 
    if fieldwins[3]==fieldwins[6]!=' ' and fieldwins[6]==fieldwins[9]!=' ':
        pwon=pcharinv[fieldwins[1]]
        return (pwon,True) 
    if (fieldwins[1]==fieldwins[5]!=' ' and fieldwins[5]==fieldwins[9]!=' '):
        pwon=pcharinv[fieldwins[1]]
        return (pwon,True)
    if (fieldwins[3]==fieldwins[5]!=' ' and fieldwins[5]==fieldwins[7]!=' '):
        pwon=pcharinv[fieldwins[7]]
        return (pwon,True)
    else:
        return (0,False)

chk=True
while chk:
    gamewinner,checker=checkgamewin(fieldwins)
    if checker:
        print('Player',gamewinner,'has won the game!')
        chk=False
    else:
        print()
        pmove(pturns,pchar,pmovelist,field,fieldwins,pprevchoice)
        print()
        showboard(field)
