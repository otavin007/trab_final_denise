import csv
import arff
import os

# Caminho do arquivo CSV de entrada
csv_file = "non_verbal_tourist_data.csv"
# Caminho do arquivo ARFF de saída
arff_file = os.path.splitext(csv_file)[0] + ".arff"

# Lê o CSV
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

# Primeira linha = nomes das colunas
attributes = [(col.strip(), 'STRING') for col in rows[0]]

# Demais linhas = dados
data = rows[1:]

# Cria o dicionário no formato ARFF
arff_data = {
    'description': 'Converted from CSV automatically',
    'relation': 'non_verbal_tourist_data',
    'attributes': attributes,
    'data': data
}

# Salva em arquivo .arff
with open(arff_file, 'w', encoding='utf-8') as f:
    arff.dump(arff_data, f)

print(f"Conversão concluída! Arquivo salvo como: {arff_file}")
