from calculator_art import logo

print(logo)

def operation(num1,num2,operator):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2

def calculator():
    more = True
    current = float(input("What's the first number?: "))
    while more:
      operator = input("Pick an operation (+,-,*,/): ")
      second = float(input("What's the next number?: "))

      ans = operation(float(current),float(second),operator)
      print(f"{current} {operator} {second} = {ans}")
      current = ans

      ask = input("Do you want to continue? ('y' or 'n'): ")
      if ask == 'n':
          more = False

calculator()
