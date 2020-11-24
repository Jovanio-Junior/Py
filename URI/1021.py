valor = float(input())
print("NOTAS:")

#notas
n100 = valor/100
print("%d nota(s) de R$ 100.00)" % n100)
valor = valor%100
n50 = valor/50
print("%d nota(s) de R$ 50.00)" % n50)
valor = valor%50
n20 = valor /20
print("%d nota(s) de R$ 20.00)" % n20)
valor = valor%20
n10 = valor/10
print("%d nota(s) de R$ 10.00)" % n10)
valor = valor%10
n5 = valor/5
print("%d nota(s) de R$ 5.00)" % n5)
valor = valor%5
n2 = valor/2
print("%d nota(s) de R$ 2.00)" % n2)
valor = valor%2

print("MOEDAS:")
#moedas
m1 = valor/1
print("%d moeda(s) de R$ 1.00)" % m1)
valor = valor%1
m05 = valor/0.5
print("%d moeda(s) de R$ 1.00)" % m05)
valor = valor%0.5
m025 = valor/0.25
print("%d moeda(s) de R$ 1.00)" % m025)
valor = valor%0.25
m010 = valor/0.10
print("%d moeda(s) de R$ 1.00)" % m010)
valor = valor%0.10
m005 = valor/0.05
print("%d moeda(s) de R$ 1.00)" % m005)
valor = valor%0.05
m001 = valor/0.01
print("%d moeda(s) de R$ 1.00)" % m001)



