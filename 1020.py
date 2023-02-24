idadeDias = int(input())

ano = idadeDias//365
mes = (idadeDias%365)//30
dias = ((idadeDias%365)%30)//1

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")