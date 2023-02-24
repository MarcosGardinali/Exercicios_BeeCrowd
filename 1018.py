N = int(input())

nota100 = N//100
nota50 = (N%100)//50
nota20 = ((N%100)%50)//20
nota10 = (((N%100)%50)%20)//10
nota5 = ((((N%100)%50)%20)%10)//5
nota2 = (((((N%100)%50)%20)%10)%5)//2
nota1 = ((((((N%100)%50)%20)%10)%5)%2)//1

print(N)
print(f'{nota100} nota(s) de R$ 100,00')
print(f'{nota50} nota(s) de R$ 50,00')
print(f'{nota20} nota(s) de R$ 20,00')
print(f'{nota10} nota(s) de R$ 10,00')
print(f'{nota5} nota(s) de R$ 5,00')
print(f'{nota2} nota(s) de R$ 2,00')
print(f'{nota1} nota(s) de R$ 1,00')