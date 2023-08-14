def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,b2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
    
operations_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("Whats the first number? "))
num2 = int(input("Whats the secound number? "))
for symbol in operations_dict:
    print(symbol)
operation = input("What operation would you like to use? ")

calculation_symbol = operations_dict[operation]
answer = calculation_symbol(num1,num2)

print(f"{num1} {operation} {num2} = {answer}")