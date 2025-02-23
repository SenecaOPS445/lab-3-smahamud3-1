#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: 113561229

def operate(number1, number2, operator):
    # Initialize result variable
    result = None

    if operator == 'add':
        result = number1 + number2
    elif operator == 'subtract':
        result = number1 - number2
    elif operator == 'multiply':
        result = number1 * number2
    else:
        result = 'Error: function operator can be "add", "subtract", or "multiply"'
    
    # Return the result (only one return statement)
    return result

if __name__ == '__main__':
    print(operate(10, 5, 'add'))     
    print(operate(10, 5, 'subtract'))  
    print(operate(10, 5, 'multiply'))   
    print(operate(10, 5, 'divide'))     

