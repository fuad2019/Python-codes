print('''  
+ ADD
- Substract
* Multiply
/ Divide
'''
      )

num1 = int(input("Enter number1:-"))
num2 = int(input("Enter number2:-"))
operator1 = input("Enter operator(+, -, *, /): ")

match operator1:
    case "+":
        print(num1 + num2)

    case "-":
        print(num1 - num2)

    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)

    case _:
        print("Invalid operator.")
