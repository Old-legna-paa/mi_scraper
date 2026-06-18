# 🕷️ Web Scraper de Citas

Scraper desarrollado en Python que extrae citas y autores del sitio 
[quotes.toscrape.com](https://quotes.toscrape.com) y las guarda 
automáticamente en un archivo CSV.

## 🛠️ Tecnologías utilizadas

- Python 3
- Requests
- BeautifulSoup4
- CSV

## ⚙️ Instalación

1. Clona el repositorio:
   git clone https://github.com/TU_USUARIO/mi_scraper.git

2. Crea el entorno virtual:
   python -m venv .venv

3. Actívalo:
   .venv\Scripts\activate

4. Instala las dependencias:
   pip install requests beautifulsoup4

## 🚀 Uso

   python scraper.py

El script generará un archivo `citas.csv` con las columnas:
| # | Cita | Autor |

## 📁 Estructura del proyecto

   mi_scraper/
   ├── scraper.py
   ├── .gitignore
   └── README.md