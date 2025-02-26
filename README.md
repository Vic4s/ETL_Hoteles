# 🏨 Proyecto ETL - Análisis de Reservas Hoteleras en Madrid

## 📖 Descripción
Este proyecto implementa un proceso **ETL (Extract, Transform, Load)** para gestionar y analizar datos de reservas hoteleras en Madrid. Se extrajeron datos de diferentes fuentes, incluyendo un archivo **Parquet**, **Web Scraping** y una **API pública**, con el objetivo de comprender patrones de reserva, evaluar la competencia y optimizar estrategias comerciales.

## 📂 Estructura del Proyecto

Proyecto_ETL │ ├── data/ # Datos crudos y transformados │ ├── api/ # Datos obtenidos de la API del Ayuntamiento de Madrid │ ├── limpieza/ # Datos limpios después de la transformación │ ├── web_scrapping/ # Datos extraídos por Web Scraping │ ├── reservas_hoteles.parquet # Datos iniciales proporcionados │ ├── notebooks/ # Notebooks de Jupyter con el desarrollo del proyecto │ ├── api.ipynb # Extracción de datos de la API │ ├── carga_BBDD.ipynb # Inserción de datos en la base de datos │ ├── consultas_BBDD.ipynb # Consultas SQL de análisis │ ├── final.ipynb # Resumen del análisis final │ ├── inicial.ipynb # Exploración y transformación inicial │ ├── web_scrapping.ipynb # Extracción de datos de la competencia │ ├── src/ # Scripts de procesamiento y ETL │ ├── etl_pipeline.py # Pipeline completo del ETL │ ├── data_cleaning.py # Funciones de limpieza y transformación │ ├── database_loader.py # Funciones para la carga de datos en SQL │ ├── web_scraping.py # Código de Web Scraping │ ├── venv/ # Entorno virtual ├── .gitignore # Archivo para ignorar archivos innecesarios en el repositorio ├── README.md # Documentación del proyecto


