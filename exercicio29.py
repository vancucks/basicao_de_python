entrada_numero = int(input("entre com o numero:"))
for x in range (0,entrada_numero+1):
    for j in range (x+1):
        print(f"{j}", end=" " )
    print("")