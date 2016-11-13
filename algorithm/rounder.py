def rounders(value):
    n = 0
    divisor = value
    while divisor//10 > 0:
        mod = divisor%10
        divisor = divisor//10
        print("divisor = ", divisor, 'mod = ', mod)
        if mod > 4:
            divisor = divisor+1
        n += 1
    return divisor*(10**n)
print(rounders(15))