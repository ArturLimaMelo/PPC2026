def primo_r(n, d): 
    if d == 1:
        return 1
    else:
        if n % d == 0:
            return 1 + primo_r(n, d-1)
        else:
            return 0 + primo_r(n, d-1)

def primo(n):
    if primo_r(n, n) == 2:
        return 1
    else:
        return 0

print(primo(5))