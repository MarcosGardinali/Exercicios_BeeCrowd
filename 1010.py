prod1 = input().split()
prod2 = input().split()

cod1 = int(prod1[0])
num1 = int(prod1[1])
valor1 = float(prod1[2])
cod2 = int(prod2[0])
num2 = int(prod2[1])
valor2 = float(prod2[2])

total = (num1*valor1)+(num2*valor2)
print(f'VALOR A PAGAR: R$ {total:.2f}')