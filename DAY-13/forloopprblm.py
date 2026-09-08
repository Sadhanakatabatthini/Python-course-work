''''
n = int(input("enter the input: "))
result = [ ]
for i in range(1,n+1):
    if n%i==0:
        result.append(i)
print(f'Factors of {n} = {result}')

s = 'python programming'
d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

s = input("enter a string: ")
count = 1
res = ''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        res+=s[i]+str(count)
        count=1
print(res+s[i]+str(count))


list = list(map(int,input().split()))
s = sum(list)
print(s)

password = input("Enter password: ")
upper = 0
lower = 0
digits = 0
special_char = 0

for ch in password:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        digits+=1
    else:
        special_char+=1
print(f'Uppercase:{upper}')
print(f'Lowercase:{lower}')
print(f'Digits:{digits}')
print(f'Special Characters: {special_char}')


Movies_list = list(map(str,input("enter movies:").split()))
for i,item in enumerate(Movies_list,1):
    print(i,item)


n = int(input("enter number: "))
data = { }
for i in range(n):
    name=input("enter name:")
    salary = int(input("enter salary: "))
    data[name]=salary
salaries = data.values()

h = max(salaries)
l = min(salaries)
avg = int(sum(salaries)/len(salaries))

print(f'highest salary: {h}')
print(f'Lowest Salary: {l}')
print(f'average Salary: {avg}')


n = list(map(int,input("Enter the innings:").split()))
t=0
b=0
d=0
for i in n:
    if i==4 or i==6:
        b+=1
    elif i==0:
        d+=1
t = sum(n)
print(f'Total Runs: {t}')
print(f'Boundaries: {b}')
print(f'Dot Balls: {d}')


e = input("Enter Emails:")
emails = [ ]
for i in e:
    email = input("enter email: ")
    emails.append(email)
for email in emails:
    domain = email.split("@")[1]
    print(domain)

n = int(input("Enter number of email addresses: "))

emails = []

for i in range(n):
    email = input("Enter email: ")
    emails.append(email)

for email in emails:
    domain = email.split("@")[1]
    print(domain)
'''

