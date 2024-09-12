numeroAluno = int(input("Quantos alunos tem a turma? "))
nota= 0
for y in range(numeroAluno,1):
    notaAluno= float(input(f"Entre com a nota do aluno {y+1}: "))
    nota= nota +notaAluno
media = nota/numeroAluno
print(f"A media da turma é: ")