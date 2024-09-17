senha = 12345
senha_digita = int(input("digite a senha: "))
tentativa = 1

while senha_digita != senha and tentativa <3:
    senha_digita = int(input(f"senha errada\n"
                      f"digite novamente: "))
    tentativa+=1
if tentativa == 3 and senha_digita != senha:
    print("bloq")
else:
    print("logado")