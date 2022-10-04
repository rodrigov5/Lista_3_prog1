gabarito = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a'] 

gabaritoNumerico = []



quantidadeAlunos = int(input('Digite o numero de alunos que iraão utilizar o sistema: '))

alunos = []
notasAlunos = []



for i in range(quantidadeAlunos):
    alunos.append(input('Nome Aluno: '))
    arr = []
    for j in range(len(gabarito)):
        arr.append(input(f'Alternativa marcada: {j + 1}: '))       
    notasAlunos.append(arr)


acertosAlunos = []
for notas in notasAlunos:
    acertos = 0
    for j in range(len(notas)):
        if notas[j] == gabarito[j]:
            acertos += 1
    acertosAlunos.append(acertos)
            
    
print(acertosAlunos)


