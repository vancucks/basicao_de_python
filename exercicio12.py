mes = int(input("entre com o numero do seu mês: "))
if mes < 12 and mes > 0 :
    if mes == 1:
        print("janeiro!")
    if mes == 2:
        print("fevereiro")
    if mes == 3:
        print("março!")
    if mes == 4:
        print("abril!")
    if mes == 5:
        print("maio!")
    if mes == 6:
        print("junho!")
    if mes == 7:
        print("Julho!")
    if mes == 8:
        print("Agosto!")
    if mes == 9:
        print("Setembro")
    if mes == 10:
        print("Outubro!")
    if mes == 11:
        print("Novembro!")
    if mes == 12:
        print("Dezembro")
else:
    print("valor invalido")