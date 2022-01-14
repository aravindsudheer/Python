num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
oprt = input("Enter a mathematical operation: ")


def calc(num1,num2,oprt):
    if oprt == "+":
        return float(num1) + float(num2)
    elif oprt == "-":
        return float(num1)-float(num2)
    elif oprt == "*":
        return int(num1)*int(num2)
    elif oprt == "/":
        return int(num1)/int(num2)
    else:
        return print("Mathematical operation not supported")

print(calc(num1,num2,oprt))
