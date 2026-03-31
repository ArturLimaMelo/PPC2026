hInicial = int(input("Digite a hora inicial: "))
hFinal = int(input("Digite a hora final: "))
duracaoH = (hFinal - hInicial) // 60
duracaoM = (hFinal - hInicial) % 60
print(str(duracaoH)+":"+str(duracaoM))