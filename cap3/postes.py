distRua = int(input("Distância da rua em km: ")) * 1000
distPostes = int(input("Distância entre dois postes em m: "))
qntPostes = int(distRua / distPostes + 1.9)
distUltimoPoste = distRua % distPostes
print(str(qntPostes)+" poste(s)\n"+str(distUltimoPoste)+" metro(s)")