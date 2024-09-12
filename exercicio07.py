#entrada de dados
print("digite numero 1:")
nota1 = int(input("AQUI:"))
print("digite numero 2:")
nota2 = int(input("AQUI:"))

#mostrar dados
print(f"Primeiro: {nota1}\n"
      f"Segundo: {nota2}")

#comparação
if nota1 == nota2:
    print("iguais")
else:
    if nota1 > nota2:
        print(f"{nota2}\n"
              f"{nota1}")
    else:
        print(f"{nota1}\n"
              f"{nota2}")