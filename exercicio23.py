pergunta = 1
while pergunta == 1:
    n = int(input("entre com o numero:"))
    while n <= 0:
        n = int(input("entre com o numero novamente:"))
    for y in range (1,n+1):
        print(f"{y}", end=" ")
    pergunta = int(input("\nvai querer novamente?"))
