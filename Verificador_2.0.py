nome = input("Digite o nome do aluno")
nota1 = float(input("Digite a primeira nota do aluno"))
nota2 = float(input("Digite a segunda nota do aluno"))
nota3 = float(input("Digite a terceira nota do aluno"))

soma_notas = ((nota1) + (nota2) + (nota3))

media = (soma_notas/3)

notas_lim = round(media, 2)

with open ("alunos.txt" , "a") as alunos:
    alunos.write(nome + "," + str(nota1) + "," + str(nota2) + "," + str(nota3) + str(notas_lim) + '\n' )

with open ('alunos.txt', 'r') as alunos:
    notas = alunos.read().split(",")
    print(alunos)

if (media >= 7):
    with open ('aprovados.txt', 'a') as aprovados:
        aprovados.write(nome + ', Parabéns você foi aprovado!' + ',' + str(notas_lim) + "\n" ) 

elif (media >= 5 ):
    with open ('exame.txt', "a") as exame:
         exame.write (nome + ", Você ficou de exame" + ',' + str(notas_lim) + "\n" )
    with open('exame.txt', 'r') as exame:
        alunos = exame.readlines()
        print(alunos)
        for linha in alunos:
            aluno = linha.split(',')
            nome = nome
            nota = notas_lim
            exame = input("Informe a nota do exame do aluno " + nome + ': ')
            media_exame = (float(exame) + float(nota)) /2
        
            if (media > 5):
                with open('aprovados.txt', 'a') as aprovados:
                    aprovados.write(nome + ', ' + str(media) + ', (Aprovado após exame) \n')
            else:
                with open('reprovados.txt', 'a') as reprovados:
                    reprovados.write(nome + ', ' + str(media) + ', (Reprovado após exame) \n')


else:
    with open ("reprovados.txt", "a") as reprovados: 
        reprovados.write(nome + ', Você reprovou' + ',' + str(notas_lim) + "\n" )


