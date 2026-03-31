dias = int(input("digite o número de dias que se passaram desde o inicio do ano: "))
semanas = dias // 7
diasRestantes = dias % 7
print(str(semanas) + " semana(s)\n" + str(diasRestantes) + " dia(s)")