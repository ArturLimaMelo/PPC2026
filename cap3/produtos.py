valorProduto = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
DinheiroCliente = float(input("Digite o valor que você tem: "))
aPagar = valorProduto * quantidade
troco = DinheiroCliente - aPagar
print("A pagar:", aPagar,"\nTroco:", troco)