pergunta = 1

while pergunta == 1:
    nota_aluno1 = float(input("entre com a nota 1: "))
    while nota_aluno1 < 0 or nota_aluno1 > 10:
        nota_aluno1 = float(input(f"tente novamente\n"
                                f"entre com a nota 1: "))
    nota_aluno2 = float(input("entre com a nota 2: "))
    while nota_aluno2 < 0 or nota_aluno2 > 10:
        nota_aluno2 = float(input(f"tente novamente\n"
                                f"entre com a nota 2: "))
    media = (nota_aluno2 + nota_aluno1) / 2
    print(f"sua media foi:"
          f"\n{media}")
    pergunta = int(input("novamente?\n"
                         "1 pra continuar\n"
                         "2 pra sair\n"
                         ""))
