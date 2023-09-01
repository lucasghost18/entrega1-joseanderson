import requests
import csv

base_url = 'https://jsonplaceholder.typicode.com/todos/2'

response = requests.get(base_url)

data = response.json()

with open('dados.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(data)

    