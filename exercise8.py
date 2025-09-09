# functions reused in a function calculator(a,b) where calculates 2 parameters ints all math operations

def summ(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

def calculator(a,b):
    return {
        summ(a,b),
        sub(a,b),
        mult(a,b),
        div(a,b)
    }

#example
print(calculator(43, 5))
