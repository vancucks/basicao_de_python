pergunta = 1
negativo = 0
tentativas = 0
while pergunta == 1 and tentativas <= 3:
    for x in range (1,11):
        n = int(input(f"entre com numero {x}: "))
        if n < 0:
            negativo = negativo+1
    print(negativo)
    pergunta = int(input("novamente?\n"
                         "1 pra continuar\n"
                         "2 pra sair\n"
                         ""))
    tentativas = tentativas + 1