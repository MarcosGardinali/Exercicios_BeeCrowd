nome = str(input())
salario = float(input())
vendas = float(input())

bonus = vendas*0.15
salario = salario+bonus

print(f'TOTAL = R$ {salario:.2f}')