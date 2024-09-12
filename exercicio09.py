#entrada de dados
time1 = input("time 1: ")
golst1 = int(input(f"quantos gols o {time1} fez: "))
time2 = input("time 2: ")
golst2 = int(input(f"quantos gols o {time2} fez: "))
#decisão de dados
if golst1==golst2:
    print("Empate")
else:
    if golst1>golst2:
        print(f"{time1} Ganhou!")
    else:
        print(f"{time2} Ganhou!")
