import pandas as pd
import os

def obter_nota1():
    while True:
        numero = input("Digite a primeira nota: ")
        try:
            numero = float(numero)
            return numero
        except ValueError:
            print("Erro: Por favor, insira uma nota válida.")

def obter_nota2():
    while True:
        numero = input("Digite a segunda nota: ")
        try:
            numero = float(numero)
            return numero
        except ValueError:
            print("Erro: Por favor, insira uma nota válida.")

def obter_nota3():
    while True:
        numero = input("Digite a terceira nota: ")
        try:
            numero = float(numero)
            return numero
        except ValueError:
            print("Erro: Por favor, insira uma nota válida.")

# Coleta dos dados do aluno
nome = input("Digite o nome do aluno: ")
nota1 = obter_nota1()
nota2 = obter_nota2()
nota3 = obter_nota3()

# Cálculo da média
media = round((nota1 + nota2 + nota3) / 3, 2)

# Determinar status do aluno
status = ""

if media >= 7:
    status = "Aprovado"
    print(f"{nome} está aprovado com média {media}.")
elif media >= 5:
    status = "Exame"
    nota_exame = float(input(f"Informe a nota do exame de {nome}: "))
    media_exame = round((media + nota_exame) / 2, 2)
    if media_exame >= 5:
        status = "Aprovado após exame"
        print(f"{nome} foi aprovado após exame com média {media_exame}.")
    else:
        status = "Reprovado após exame"
        print(f"{nome} foi reprovado após exame com média {media_exame}.")
else:
    status = "Reprovado"
    print(f"{nome} está reprovado com média {media}.")

# Criar um dicionário com as informações do aluno
novo_aluno = {
    "Nome": nome,
    "Nota 1": nota1,
    "Nota 2": nota2,
    "Nota 3": nota3,
    "Média": media,
    "Status": status
}

# Verificar se o arquivo já existe
arquivo_excel = "alunos.xlsx"

if os.path.exists(arquivo_excel):
    # Carregar os dados existentes no arquivo
    df_existente = pd.read_excel(arquivo_excel)
    # Concatenar os dados do novo aluno
    df_atualizado = pd.concat([df_existente, pd.DataFrame([novo_aluno])], ignore_index=True)
else:
    # Criar um novo DataFrame com os dados do novo aluno
    df_atualizado = pd.DataFrame([novo_aluno])

# Salvar os dados atualizados no arquivo Excel
df_atualizado.to_excel(arquivo_excel, index=False, sheet_name="Resultados")

print("Os dados do aluno foram adicionados com sucesso ao arquivo Excel.")
