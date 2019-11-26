def factorial(num):
    dividor = 2

    while num != 1:
        num = num / dividor
        dividor += 1

    return dividor-1

print( factorial(120) )
print( factorial(1) )
print( factorial(2) )
print( factorial(6) )
