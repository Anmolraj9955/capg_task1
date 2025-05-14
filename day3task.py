# Anmol Raj
# rajanmol588@gmail.com
# Day3 Task

# 1. Discount Calculator
b = int(input())
if b > 1000:
    d = b * 20 // 100
elif b > 500:
    d = b * 10 // 100
else:
    d = 0
print(b - d)

# 2. Grade Categorizer
s = int(input())
if 90 <= s <= 100:
    g = 'A'
elif s >= 70:
    g = 'B'
elif s >= 50:
    g = 'C'
else:
    g = 'Fail'
print(g)

# 3. Age Group Classifier
a = int(input())
if a < 13:
    c = 'Child'
elif a <= 19:
    c = 'Teen'
elif a <= 59:
    c = 'Adult'
else:
    c = 'Senior'
print(c)

# 4. Even/Odd and Multiple of 5
n = int(input())
if n % 2 == 0 and n % 5 == 0:
    r = 'Even & div by 5'
elif n % 2 != 0 and n % 5 == 0:
    r = 'Odd & div by 5'
elif n % 2 == 0:
    r = 'Even & not div by 5'
else:
    r = 'Odd & not div by 5'
print(r)

# 5. Login System
u = input()
if u == 'john' or u == 'amy' or u == 'sita':
    print('Login OK')
else:
    print('Denied')

# 6. Number Comparison Game
x = int(input())
y = int(input())
if x > y:
    print("1st greater")
elif y > x:
    print("2nd greater")
else:
    print("Equal")

# 7. Eligibility for Voting and Driving
a = int(input())
if a >= 21:
    print("Vote & Drive")
elif a >= 18:
    print("Vote only")
else:
    print("Not eligible")

# 8. Leap Year Check
y = int(input())
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("Leap")
else:
    print("Not Leap")

# 9. Login with Role
u = input()
r = input()
if (u == 'john' or u == 'amy' or u == 'sita') and (r == 'admin' or r == 'manager'):
    print("Login OK")
else:
    print("Denied")

# 10. Arithmetic Operations
a = int(input())
b = int(input())
op = input()
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a // b)

# 11. Weather Alert
t = int(input())
if t > 40:
    print("Heat Alert")
elif t > 30:
    print("Warm")
else:
    print("Normal")

# 12. Password Strength
p = input()
c = 0
for i in p:
    c += 1
f = 0
for i in p:
    if i == '@':
        f = 1
if c >= 8 and f == 1:
    print("Strong")
else:
    print("Weak")

# 13. ATM Withdrawal
amt = int(input())
bal = int(input())
if amt <= bal and amt % 100 == 0:
    print("Withdraw OK")
else:
    print("Invalid")

# 14. Divisibility Check
n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print("Div by 3 & 5")
elif n % 3 == 0:
    print("Div by 3")
elif n % 5 == 0:
    print("Div by 5")
else:
    print("Not Div")

# 15. Product Availability
p = input()
if p == 'pen' or p == 'pencil' or p == 'eraser':
    print("Available")
else:
    print("Not Available")

# 16. Triangle Validity
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("Valid")
else:
    print("Invalid")

# 17. Max of Three
a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)

# 18. Marks Validity
m = int(input())
if 0 <= m <= 100:
    print("Valid")
else:
    print("Invalid")

# 19. Login Attempt
u = input()
p = input()
if u == 'admin' and p == '1234':
    print("Login OK")
else:
    print("Denied")

# 20. Electricity Bill
u = int(input())
if u <= 100:
    amt = u * 5
elif u <= 200:
    amt = u * 7
else:
    amt = u * 10
print("Bill:", amt)