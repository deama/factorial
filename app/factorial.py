def factorial(num):
    dividor = 2
    
    while num > 1:
        num = num / dividor
        dividor += 1
        if (num.is_integer()) == False:
            return "none"

    return dividor-1

#print(factorial(18))
