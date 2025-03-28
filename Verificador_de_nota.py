#Exercício 1 (Verificador de notas 2.0)

import pandas as pd

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))    
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

with open ('notas.txt','a')as notas:
    notas.write(nome + ',' + str(nota1) + "," + str(nota2) + "," + str(nota3) + '\n')

with open ('notas.txt', 'r') as notas:
    notas = notas.read().split(",")
    print(notas)


soma_notas = (float(notas[1]) + float(notas[2]) + float(notas[3]))

media = soma_notas / 3
media_limitada = round(media, 1)

print(media_limitada)

if (media >= 7):
    with open ('aprovados.txt', 'a') as aprovados:
        aprovados.write(nome + ', Parabéns você foi aprovado!' + ',' + str(media_limitada) ) 

elif (media >= 5 ):
     with open ('exame.txt', "a") as exame:
         exame.write (nome + ", Você ficou de exame" + ',' + str(media_limitada) )

if (media < 5):
    with open ("reprovados.txt", "a") as reprovados: 
        reprovados.write(nome + ', Você reprovou' + ',' + str(media_limitada) )

