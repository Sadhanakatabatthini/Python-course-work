'''
for i in range(5):
    for j in range(5):
        if (i+j)%2==0:
            print('0' ,end=' ')
        else:
            print('1',end=' ')
    print( )


n = 1
for i in range(5):
    for j in range(5):
        print(n,end=' ')
        n+=1
    print( )

for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print( )

n=5
for i in range(5):
    for j in range(n-i):
        print('*',end=' ')
    print( )

n=5
for i in range(5):
    for s in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()


n=int(input("Enter a number: "))
for i in range(n):
    for s in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()


n=int(input("Enter a number: "))
m=n//2
for i in range(n):
    if i<=m:
        for j in range(i+1):
            print('*',end=' ')
    else:
        for k in range(n-i):
            print('*',end=' ')
    print()


n=int(input("Enter a number: "))
m=n//2
for i in range(n):
    if i<=m:
         print('* '*(i+1),end=' ')
    else:
        print('* '*(n-i),end=' ')
    print()

n=int(input("Enter a number: "))
m=n//2
for i in range(n):
    if i<=m:
         print(' '*(m-i),'* '*(i+1),end=' ')
    else:
        print(' '*(i-m),'* '*(n-i),end=' ')
    print()




for i in range(5):
    for j in range(5):
        print(i+j,end=' ')
    print( )

'''
n = int(input("Enter a number: "))
m = int(input("Enter other number:  "))
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(m,end=' ')
            m += 1
    else:
        m += n
        for j in range(n):
            m-=1
            print(m,end=' ')
        m += n+1
    print( )