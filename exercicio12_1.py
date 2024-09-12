mes = int(input("entre com o numero do seu mês: "))
match mes:
    case 1:
        print("janeiro!")
    case 2:
        print("fevereiro")
    case 3:
        print("março!")
    case 4:
        print("abril!")
    case 5:
        print("maio!")
    case 6:
        print("junho!")
    case 7:
        print("Julho!")
    case 8:
        print("Agosto!")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro!")
    case 11:
        print("Novembro!")
    case 12:
        print("Dezembro")
    case _:
        print("valor invalido")