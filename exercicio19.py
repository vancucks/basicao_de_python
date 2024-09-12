n = 1
nota= 0
numeroAluno = int(input("Quantos alunos tem a turma? "))
while n <= numeroAluno:

    notaAluno = float(input(f"qual é a nota do {n} "))
    nota = nota+notaAluno
    n = n+1
media = nota/numeroAluno
print(media)