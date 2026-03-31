distancia = int(input("Digite a distância entre as cidades: "))
velocidade = int(input("Digite a velocidade média do carro em km/h: "))
tempo = distancia / velocidade
horas = int(tempo)
minutos = int((tempo - horas) * 60)
print(str(horas)+":"+str(minutos))
