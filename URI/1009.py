nome = input()
salario = float(input())
vendas = float(input())

salario += (vendas*15)/100
print("TOTAL = R$ %.2f" % salario)