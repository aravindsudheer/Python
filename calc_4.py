num1 = float(input("enter a num:"))
op= input("enter a operative:")
num2= float(input("enter a num:"))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid Operative")
