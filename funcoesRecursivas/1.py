def conta_divisores_r(n, d):
    if d == 1:
        return 1
    else:
        if n % d == 0:
            return 1 + conta_divisores_r(n, d - 1)
        else:
            return 0 + conta_divisores_r(n, d - 1)

def conta_divisores(n):
    return conta_divisores_r(n, n)

print(conta_divisores(4))