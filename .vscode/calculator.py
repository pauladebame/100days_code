#develop funtions that does basic arithmetics

# add
def add(n1, n2):
    """takes in two numbers and returns their sum """
    return n1 + n2
#subtraction
def subtract(n1, n2):
    """Returns the difference bettween two numbers n1-n2"""
    return n1 - n2
#division
def divide(n1, n2):
    """divides n1/n2"""
    return n1/n2
#multiplication
def multiply(n1, n2):
    """multiply n1*n2"""
    return n1*n2
 
#dictionary
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}



def Calculator():
    should_continue = True
    num1 = float(input("what is the first number?: "))
    for symbols in operations:
        print (symbols)

    
    while should_continue:
        operation_symbol = input("pick an operation: ")
        num2 = float(input("what is the next number?: "))
        function = operations[operation_symbol]
        answer = function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        Continue = input(f"type y to continue calculatin with {answer} type n to exit: ")
        if Continue=='y':
            num1 = answer
        else:
            Calculator()
            should_continue = False 
Calculator()