valorFinal = float(input("Digiteo valor final de vneda de um automóvel: "))
valorCusto = valorFinal / 1.4
ICMS = valorCusto * 0.18
IPI = valorCusto * 0.13
PIS = valorCusto * 0.014
Cofins = valorCusto * 0.076
valorLiquido = valorFinal - ICMS - IPI - PIS - Cofins
print("ICMS:", "{:.2f}".format(ICMS),"\nIPI:","{:.2f}".format(IPI),"\nPIS:","{:.2f}".format(PIS),"\nCofins:","{:.2f}".format(Cofins),"\nValor sem impostos:", valorLiquido)