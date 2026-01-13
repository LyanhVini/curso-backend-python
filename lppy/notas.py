lista = [10, 9, 8, 6.7, 5.5, 7.1, 8.9, 7.1, 7.2, 4.2]

media = 6
total_aprovados = 0
total_reprovados = 0
soma_notas = 0

for nota in lista:
    
    soma_notas += nota
    
    if nota >= media:
        print("Aluno APROVADO!")
        total_aprovados += 1
    else:
        print("Aluno REPROVADO!")
        total_reprovados += 1

media_simples = soma_notas / len(lista)

print(f"Total de Aprovados foi {total_aprovados}")
print(f"Total de Reprovados foi {total_reprovados}")
print(f"A média da turma foi {media_simples}")
