salarioAntes = float(input("Digite o salário antes do reajuste: "))
reajuste = float(input("Digite o reajuste: "))
salarioFinal = salarioAntes * (reajuste / 100 + 1)
print("Atual:", salarioAntes,"\nNovo:","{:.2f}".format(salarioFinal))