#A project I made for CBSE at NPSRNR


import mysql.connector as v
import tabulate
from datetime import datetime
con=v.connect(host='localhost',user='root',password='sql123',database='project')
if con.is_connected:
    print("Connected Successfully")
else:
    print("Not connected")
cur=con.cursor()
q="create table if not exists bank_accounts (Account_No INT primary key,Name varchar(30), Current_Balance int)"
cur.execute(q)
q="create table if not exists acctobeapproved (Account_No INT primary key,Name varchar(30), Current_Balance int)"
cur.execute(q)
q='create table if not exists accpwd (Account_No int primary key, PIN varchar(30))'
cur.execute(q)
q='create table if not exists accpwdtba (Account_No int primary key, PIN varchar(30))'
cur.execute(q)
def create_account():
    print()
    print()
    print('-'*99)
    print('Creating account...')
    print('-'*99)
    print()
    print()
    Name=input("Enter your name : ")
    print('Enter password (8 min ; 30 max): ')
    pwd=input('')
    j=True
    while j:
        if len(pwd)>=8:
            if len(pwd)<=30:
                if pwd.isalnum():
                    print('Password is valid.')
                    j=False
                    print()
            else:
                print('Password is invalid.')
                print('Password must meet the following criteria : ')
                print('1. Must be between 8-30 characters long.')
                print('2. Must be a mix of letters and numbers.')
                print()
                print('Please enter a valid password : ')
                pwd=input()
                j=True
        else:
            print('Password is invalid.')
            print('Password must meet the following criteria : ')
            print('1. Must be between 8-30 characters long.')
            print('2. Must be a mix of letters and numbers.')
            print()
            print('Please enter a valid password : ')
            pwd=input()
            j=True
    CurBalance=int(input("Enter deposit ammount : "))
    while CurBalance<1000:
        print("Error: deposit entered is too low.")
        print("Minimum balance is 1000 Rs.")
        CurBalance=int(input("Enter deposit amount : "))
    Ttype="No transaction"
    Tamount=0
    print()
    q="select max(Account_No) from bank_accounts"
    cur.execute(q)
    k=cur.fetchone()
    q="select max(Account_No) from acctobeapproved"
    cur.execute(q)
    k1=cur.fetchone()
    if k[0]==None and k1[0]==None:
            Acc_no=1000000001
    else:
        if k[0]!=None and k1[0]!=None:
            if k1[0]>k[0]:
                a=k1[0]
                Acc_no=a+1
            else:
                a=k[0]
                Acc_no=a+1
        elif k[0]==None and k1[0]!=None:
            a=k1[0]
            Acc_no=a+1
        elif k[0]!=None and k1[0]==None:
            a=k[0]
            Acc_no=a+1
    print('-'*99)
    print()
    print("Account number : ",Acc_no)
    print("Registered details of account number : ",Acc_no)
    b=[{"Account number":Acc_no,'Name':Name,'Current balance':CurBalance}]
    print(tabulate.tabulate(b,headers='keys',tablefmt='grid'))
    print()
    
    q="insert into acctobeapproved values(%s,%s,%s)"
    cur.execute(q,[Acc_no,Name,CurBalance])
    q='insert into accpwdtba values(%s,%s)'
    cur.execute(q,[Acc_no, pwd])
    con.commit()
    print()
    print('Account pending approval...')
    print()
def approve_account():
    q='select * from acctobeapproved'
    cur.execute(q)
    k=cur.fetchall()
    headings=['Account Number','Name','Current Balance']
    print(tabulate.tabulate(k,headers=headings,tablefmt='grid'))
    print()
    slno=int(input('Account approved (enter account number): '))
    a=[]
    for i in k:
        a+=[i[0]]
    if slno in a:
        for i in k:
            if i[0]==slno:
                q='insert into bank_accounts values(%s,%s,%s)'
                cur.execute(q,[i[0],i[1],i[2]])
                h="ACC"+str(i[0])
                q="create table if not exists "+h+" (Date datetime primary key, Transaction_Type varchar(20), Transaction_Amount int)"
                cur.execute(q)
                q='select PIN from accpwdtba where Account_No=%s'
                cur.execute(q,(slno,))
                Accpwd=(cur.fetchone()[0])
                q='insert into accpwd values(%s,%s)'
                cur.execute(q,[i[0],Accpwd])
                now=datetime.now()
                q="insert into "+h+" values(%s,%s,%s)"
                cur.execute(q,(now,'credit',i[2]))
                q='delete from acctobeapproved where Account_No=%s'
                cur.execute(q,[slno])
                q='delete from accpwdtba where Account_No=%s'
                cur.execute(q,[slno])
                con.commit()
    else:
        print()
        print('No such account exists, exiting now...')
        print()
def check_balance(acc):
    q="select * from bank_accounts where Account_No=%s"%acc
    cur.execute(q)
    k=cur.fetchone()
    if not k:
        print()
        print("Account not found...")
        print()
    else:
        print()
        uptitle=('Account_no','Name','Current Balance')
        accVal=((k[0],k[1],k[2]),)  
        print(tabulate.tabulate(accVal,headers=uptitle,tablefmt='grid'))
        print()
def transaction(acc):
    curb=0
    q="select * from bank_accounts where Account_No=%s"%acc
    cur.execute(q)
    k=cur.fetchone()
    if not k:
        print("Account not found...")
    else:
        Ttype=input("Enter transcation type (credit or debit) : ")
        Tamount=int(input("Enter transcation amount : "))
        if Ttype.lower()=="credit":
            curb=k[2]+Tamount
            q="UPDATE bank_accounts SET Current_Balance=%s where Account_No=%s"
            cur.execute(q,(curb,acc))
            now=datetime.now()
            h="ACC"+str(acc)
            q="insert into "+h+" values(%s,%s,%s)"
            cur.execute(q,(now,Ttype,Tamount))
            print()
            print()
            print('-'*99)
            print('')
            print('Bankinator 400')
            print()
            print('Bill')
            print()
            print('Date and time : ',now)
            print('Account Details :- ')
            print('Account Number : ',k[0])
            print('Name : ',k[1])
            print()
            print('Transaction Type : ',Ttype.capitalize())
            print('Transaction Amount : ',Tamount)
            print('Balance : ',curb)
            print()
            print()
            print('-'*99)
        elif Ttype.lower()=="debit":
            if k[2]<1000 or k[2]<Tamount or k[2]-Tamount<1000:
                print("Current balance is not enough...")
            else:
                curb=k[2]-Tamount
                q="UPDATE bank_accounts SET Current_Balance=%s where Account_No=%s"
                cur.execute(q,(curb,acc))
                now=datetime.now()
                h="ACC"+str(acc)
                q="insert into "+h+" values(%s,%s,%s)"
                cur.execute(q,(now,Ttype,Tamount))
                print()
                print()
                print('-'*99)
                print()
                print('Bankinator 400 Bill')
                print()
                print('Date and time : ',now)
                print('Account Details :- ')
                print('Account Number : ',k[0])
                print('Name : ',k[1])
                print()
                print('Transaction Type : ',Ttype.capitalize())
                print('Transaction Amount : ',Tamount)
                print('Balance : ',curb)
                print()
                print()
                print('-'*99)     
    con.commit()
def delete_account():
    print('This will automatically exit if bank account number entered isn\'t in the database...')
    print()
    print()
    acc=int(input("Enter account number : "))
    q="delete from bank_accounts where Account_No=%s"%acc
    cur.execute(q)
    q='delete from accpwd where Account_No=%s'%acc
    cur.execute(q)
    h="ACC"+str(acc)
    q='drop table '+h
    cur.execute(q)
    con.commit()
def check_transaction(acc):
    acc=int(input("Enter account number : "))
    h="ACC"+str(acc)
    q="select * from bank_accounts where Account_No=%s"%acc
    cur.execute(q)
    k=cur.fetchone()
    if not k:
        print("Account not found...")
    else:
        q='select * from '+h+' order by DATE desc'
        cur.execute(q)
        k=cur.fetchmany(5)
        heading=['Date and time of transaction','Transaction Type','Transaction Amount']
        print(tabulate.tabulate(k,headers=heading,tablefmt='grid'))
def display_all():
    q='select Account_No,Name,Current_Balance from bank_accounts'
    cur.execute(q)
    k=cur.fetchall()
    uptitle=('Account_no','Name','Current Balance')
    print()  
    print(tabulate.tabulate(k,headers=uptitle,tablefmt='grid'))
    print()
def user_login_acc(acc):
    h="ACC"+str(acc)
    q="select * from bank_accounts where Account_No=%s"%acc
    cur.execute(q)
    k=cur.fetchone()
    if not k:
        print("Account not found...")
        return False
    else:
        pwd=input('Enter password : ')
        q='select PIN from accpwd where Account_No=%s'
        cur.execute(q,(acc,))
        pwdchk=cur.fetchone()
        if pwd==pwdchk[0]:
            return True
        else:
            print('Incorrect PIN...')
chk=True
while chk:
    print('-'*99)
    print()
    print('''Enter -
1 to login as user
2 to login as admin
3 to create new account : ''')
    print()
    print()
    j=int(input())
    print()
    print()
    if j==1:
        chk1=True
        acc=int(input('Enter account number : '))
        acccheck=user_login_acc(acc)
        while chk1 and acccheck:
            print()
            print('-'*99)
            print()
            print('Welcome to')
            print('''
█████████████████████████████████████████████████████████████████████████████
█▄─▄─▀██▀▄─██▄─▀█▄─▄█▄─█─▄█▄─▄█▄─▀█▄─▄██▀▄─██─▄─▄─█─▄▄─█▄─▄▄▀█░█░██─▄▄─█─▄▄─█
██─▄─▀██─▀─███─█▄▀─███─▄▀███─███─█▄▀─███─▀─████─███─██─██─▄─▄█▄▄░██─██─█─██─█
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▄▄▄▄▀▄▄▄▄▀''')
            print()
            print('-'*99)
            print()
            print("""Enter-
1 to check bank account status,
2 to make a transaction
3 to check recent transactions : """)
            print()
            print('-'*99)
            print()
            g=int(input())
            print()
            print()
            if g==1:
                check_balance(acc)
            elif g==2:
                transaction(acc)
            elif g==3:
                check_transaction(acc)
            print()
            print('-'*99)
            print()
            chk1c=(input("Enter \'Logout\' to leave or any key to stay : "))
            if chk1c.lower()=='logout':
                chk1=False
                acccheck=False
            else:
                chk1=True
    elif j==2:
        chk2=True
        pwdchkadmin=input('Enter admin password : ')
        while chk2 and pwdchkadmin=='adminpass123':
            print('-'*99)
            print()
            print('Welcome to BANKINATOR4000')
            print()
            print('-'*99)
            print()
            print("""Enter-
1 to display all accounts,
2 to approve pending accounts,
3 to delete account : """)
            print()
            print('-'*99)
            print()
            g=int(input())
            print()
            print()
            if g==1:
                display_all()
            elif g==2:
                approve_account()
            elif g==3:
                delete_account()
            print()
            print('-'*99)
            print()
            chk2=bool(input("Press enter to exit or any key to stay : "))
    elif j==3:
        create_account()
        chk=True
    chk=bool(input('Press enter to exit or any key to stay : '))
