# daylister
gera arquivo de senhas mas com datas (tem input de ano mínimo e máximo e nome de arquivo de saída

# Gerador de Lista de Datas em Python

Este é um script Python simples que gera uma lista de datas no formato com ou sem barras, com base nos anos mínimo e máximo fornecidos pelo usuário.

## Requisitos

- Python 3.x

## Como Usar

1. Clone o repositório ou faça o download do arquivo `gerador_datas.py`.

2. Execute o script em seu ambiente Python. Isso pode ser feito abrindo um terminal ou prompt de comando e navegando até o diretório onde o arquivo `gerador_datas.py` está localizado e, em seguida, digitando o seguinte comando:

   ```shell
   python gerador_datas.py
O script solicitará ao usuário os seguintes inputs:

Ano mínimo
Ano máximo
Nome do arquivo de saída (opcional)
Após fornecer essas informações, o script gerará uma lista de datas com e sem barras, no intervalo de anos especificado.

Se você fornecer um nome de arquivo de saída, o script salvará a lista de datas geradas nesse arquivo.

Exemplo de Uso

Digite o ano mínimo: 2020
Digite o ano máximo: 2023
Digite o nome do arquivo de saída (ex: datas.txt): lista_datas.txt
As datas foram salvas no arquivo 'lista_datas.txt'.
Formato das Datas
O script gera as datas no formato "dd/mm/aaaa" (com barra) e "ddmmyyyy" (sem barra).
