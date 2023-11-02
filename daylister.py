from datetime import date, timedelta

# Solicita ao usuário o ano mínimo e máximo
ano_minimo = int(input("Digite o ano mínimo: "))
ano_maximo = int(input("Digite o ano máximo: "))

# Solicita ao usuário o nome do arquivo de saída
nome_arquivo_saida = input("Digite o nome do arquivo de saída (ex: datas.txt): ")

# Lista para armazenar as datas
datas = []

# Loop para gerar todas as combinações de dia e mês entre os anos
for ano in range(ano_minimo, ano_maximo + 1):
    for mes in range(1, 13):
        ultimo_dia_mes = (date(ano, mes % 12 + 1, 1) - timedelta(days=1)).day
        for dia in range(1, ultimo_dia_mes + 1):
            data = date(ano, mes, dia)
            # Formato com barra (dd/mm/aaaa)
            data_barra = data.strftime("%d/%m/%Y")
            # Formato sem barra (ddmmyyyy)
            data_sem_barra = data.strftime("%d%m%Y")
            datas.append(data_barra)
            datas.append(data_sem_barra)

# Escreve a lista de datas no arquivo de saída
with open(nome_arquivo_saida, 'w') as arquivo_saida:
    for data in datas:
        arquivo_saida.write(data + '\n')

print(f"As datas foram salvas no arquivo '{nome_arquivo_saida}'.")
