print('''  
+ ADD
- Substract
* Multiply
/ Divide
'''
      )

num1 = int(input("Enter value1 :"))
num2 = int(input("enter value2:"))
opr = input("Enter the operator(+,-,*,/)")
if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "/":
    print(num1 / num2)
else:
    print("invalid operand")
