import requests
import csv
import random

base_url = 'https://jsonplaceholder.typicode.com/todos/5'

response = requests.get(base_url)

data = response.json()

if __name__ == "__main__":
    userId = data["userId"] * random.randint(1, 145266454)
    title = data["title"]
    completed = data["completed"]

    # Criar um dicionário com os dados
    data_dict = {
        "userId": userId,
        "title": title,
        "completed": completed
    }

    # Especificar o nome do arquivo CSV
    csv_filename = "dados_extraidos.csv"

    # Escrever os dados em um arquivo CSV
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = data_dict.keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Se o arquivo CSV ainda não existir, escreva o cabeçalho
        if not csv_file.tell():
            writer.writeheader()

        # Escreva os dados no arquivo CSV
        writer.writerow(data_dict)
