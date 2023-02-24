num = input().split()

a = int(num[0])
b = int(num[1])
c = int(num[2])

maior = ((a+b+abs(a-b)))/2

if maior > c:
    print(f"{maior:.0f} eh o maior")
else:
    print(f"{c} eh o maior")