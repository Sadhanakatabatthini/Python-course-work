'''
username=input("username:")
password=input("password:")
if username == 'admin' and password == 'admin123':
    print("Login Successful")
else:
    print("Invalid Credentials")

product = ["laptop","mouse","bag"]
search = input("enter product:")
if search in product:
    print(f'{search} found')
else:
    print(f'{search} not found')


bill = int(input("enter bill:"))
if bill>99:
    print("Final bill:",bill)
else:
    print("Final bill+del_char:",bill+30)

units = int(input())
is_senior_citizen=eval(input())
if units>100 and units<101 and is_senior_citizen==True:
    amount=units*1.5*0.1
    print(amount)
elif units>=101 and units<=200 and is_senior_citizen==True:
    amount=units*2.5
    print(amount)
elif units>=201 and units<=500 and is_senior_citizen==True:
    amount=units*4-((units*4)*0.1)
    print(amount)
elif units>=500 and is_senior_citizen==True:
    amount=units*6*0.1
    print(amount)
elif units>=800:
    amount=units*6+((units*6)*0.05)
    print(amount)


n = int(input("Enter a number:"))
if n>0:
    print("postive Number")
else:
    print("negative number")

n = int(input("Enter a number:"))
if n%2==0:
    print("even number")
else:
    print("odd number")


n = int(input("Enter a number:"))
if n%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")

n = int(input("Enter a number:"))
if n%3==0 and n%7==0:
    print("divisible by both 3 and 7")
else:
    print("not divisible")

year = int(input("Enter year:"))
if year%400==0:
    print("Leap year")
elif year%100==0:
    print("not a leap year")
elif year%4==0:
    print("leap year")
else:
    print("not a leap year")

n = int(input("enter marks: "))
if n > 35:
    print("Pass")
else:
    print("fail")



n = int(input("Enter a number:"))
s = str(n)
if len(s)==3:
    print("3-digit number")
else:
    print("not a 3-digit number")


n = input("Enter a character:")
v = ['a','e','i','o','u']
if n in v:
    print("Vowel")
else:
    print("consonant")

a =int(input("Enter a: "))
b =int(input("Enter b: "))
if a>b:
    print(f'{a} is greater')
else:
    print(f'{b} is greater')
'''
a =int(input("Enter a: "))
b =int(input("Enter b: "))
if a>b:
    print(f'{b} is smaller')
else:
    print(f'{a} is smaller')
