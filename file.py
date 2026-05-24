# Enter operators and numbers

operator = input("Enter Your Operator: ")

num1 = float(input("Enter Your First Number: "))
num2 = float(input("Enter Your Second Number: "))

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    
    if num2 == 0:
        print("Division Error")

    else:
        print(num1 / num2)

else:
    print("Syntax Error, Use valid Operator, Ciao!")