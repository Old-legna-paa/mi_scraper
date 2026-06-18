import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    citas = soup.find_all('span', class_='text')
    autores = soup.find_all('small', class_='author')

    with open('citas.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['#', 'Cita', 'Autor'])
        for i, (cita, autor) in enumerate(zip(citas, autores), 1):
            texto = cita.text.replace('\u201c', '"').replace('\u201d', '"')
            writer.writerow([i, texto, autor.text])

    print("¡CSV creado correctamente!")
else:
    print(f"Error: {response.status_code}")