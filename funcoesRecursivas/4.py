def conta_algarismos(n):
    if n > 0 and n < 10:
        return 1
    else:
        return 1 + conta_algarismos(n // 10)
    
