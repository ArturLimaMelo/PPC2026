def conta_bits_r(n, b):
    if 1 >= n:
        return 1
    else:
        b += 1
        return 1 + conta_bits_r(n - 2 ** b, b)
    
def conta_bits(n):
    return conta_bits_r(n, 0)

print(conta_bits(int(input())))
    