valorFinal = float(input("Digiteo valor final de vneda de um automóvel: "))
ICMS = valorFinal * 0.18
IPI = valorFinal * 0.13
PIS = valorFinal * 0.014
Cofins = valorFinal * 0.076
valorLiquido = valorFinal - ICMS - IPI - PIS - Cofins
print("ICMS:", "{:.2f}".format(ICMS),"\nIPI:","{:.2f}".format(IPI),"\nPIS:","{:.2f}".format(PIS),"\nCofins:","{:.2f}".format(Cofins),"\nValor sem impostos:", valorLiquido)