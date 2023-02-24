sal = float(input())

if sal >= 0 and sal <= 400:
    porcentagem = 15
    novoSal = sal + (sal * 0.15)
    aumento = sal * 0.15
    print(f"Novo salario: {novoSal:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print(f"Em percentual: {porcentagem} %")
    
elif sal >= 400.01 and sal <= 800:
    porcentagem = 12
    novoSal = sal + (sal * 0.12)
    aumento = sal * 0.12
    print(f"Novo salario: {novoSal:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print(f"Em percentual: {porcentagem} %")

elif sal >= 800.01 and sal <= 1200:
    porcentagem = 10
    novoSal = sal + (sal * 0.10)
    aumento = sal * 0.10
    print(f"Novo salario: {novoSal:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print(f"Em percentual: {porcentagem} %")  
    
elif sal >= 1200.01 and sal <= 2000:
    porcentagem = 7
    novoSal = sal + (sal * 0.07)
    aumento = sal * 0.07
    print(f"Novo salario: {novoSal:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print(f"Em percentual: {porcentagem} %") 
    
elif sal > 2000:
    porcentagem = 4
    novoSal = sal + (sal * 0.04)
    aumento = sal * 0.04
    print(f"Novo salario: {novoSal:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print(f"Em percentual: {porcentagem} %")    