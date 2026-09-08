''' 
n=int(input("Enter the Size:"))             #o
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()

    
n = int(input("Enter the Size:"))            #B
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==m:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()


n = int(input("Enter the Size:"))        #E
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==m:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()

    
n = int(input("Enter the Size:"))         #C
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()

n = int(input("Enter the Size:"))           #F
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0  or i==m:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()


n=int(input("Enter the Size:"))               #A
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==m:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()


n = int(input("Enter the Size:"))               #G
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or (j==n-1 and i>=m) or (i==m and j>=m):
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input("Enter the Size:"))         #H
m=n//2
for i in range(n):
    for j in range(n):
        if  j==0 or j==n-1 or i==m:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input("Enter the Size:"))         #I
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==m:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input("Enter the Size:"))         #z
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()



n=int(input("Enter the Size:"))         #y
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or i+j==n-1:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()

    
n=int(input("Enter the Size:"))         #k
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i==m and j<=m) or (i==j and i>=m) or (i+j==n-1 and i<=m):
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()


n=int(input("Enter the Size:"))         #J
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m or (i==0 and j<m) or (j==0 and i<m):
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()


n=int(input("Enter the Size:"))         #R
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (i==m and j<=m) or (i==j and i>=m) or (i+j==n-1 and i<=m):
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()


n=int(input("Enter the Size:"))         #m
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m):
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()

'''
n=int(input("Enter the Size:"))         #w
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i>=m) or (i+j==n-1 and i>=m):
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()

'''
n=int(input("Enter the Size:"))         #v
m=n//2
for i in range(n):
    for j in range(n):
        if  (j==0 and i<=m) or (j==n-1 and i<=m) or (i-j==m) or (i+j==m+n-1):
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input("Enter the Size:"))         #A
m=n//2
for i in range(n):
    for j in range(n):
        if  (i==n-1 and i<=m) or (j==0 and i>=m) or (j==n-1 and i>=m) or i+j==m or (j-i==m and i<=m) or i == m :
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print( )


n=int(input("Enter the Size:"))         #s
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or (j==0 and i<=m) or i==n-1 or (j==n-1 and i>=m) or i==m:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input("Enter the Size:"))         #Q
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j == n-1 or (i==j and i>=m):
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()



n = int(input("Enter the Size:"))         #L
for i in range(n):
    for j in range(n):
        if  j==0 or i==n-1 :
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()

'''