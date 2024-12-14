import math
num = int(input("Enter a number: "))

res = math.floor(num)
print("The floor value is", res)
res1 = math.ceil(num)
print("The ceiling value is", res1)

x = int(input("Enter a number: "))
y = int(input("Enter a number"))
res2 = math.copysign(x,y)
print("The value of x after copysign is", res2)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
res3 = math.gcd(a,b)
print("The greatest common factor is", res3)