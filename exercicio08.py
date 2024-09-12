#entrada de dados
nota1 = float(input("primeiro numero: "))
nota2= float(input("segundo numero: "))
nota3 = float(input("terceiro numero: "))

#calculando dados
media = (nota1+nota2+nota3)/3

#decisão
if media>= 7:
    print("parabéns você foi aprovado!")
    print(f"{media:.1f}")
else:
    if media >=4:
        print("você foi recuperação!")
        print(f"{media:.1f}")
    else:
        print("você foi reprovado!")

