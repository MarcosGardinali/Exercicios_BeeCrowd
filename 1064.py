positivo = 0
positivos = 0
for i in range (0, 6):
    num = float(input())
    if num >= 0:
        positivo += 1
        positivos += num
        media = positivos/positivo
print(f"{positivo} valores positivos")  
print(f"{media:.1f}")