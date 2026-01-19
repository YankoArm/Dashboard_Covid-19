# Dashboard Científico COVID-19

Proyecto de análisis y visualización de datos desarrollado en Python.  
El objetivo es explorar datos relacionados con la COVID-19 y representarlos gráficamente para facilitar su interpretación.

Este proyecto forma parte de mi portfolio personal y está enfocado al aprendizaje práctico de análisis de datos.

Proyecto final de curso superior de programación con Python (Deusto)

---

## 📊 Funcionalidades

- Lee datos de CSV (RecursoProyecto3.csv)
- Preparación de datos y tratamiento de fechas
- Cálculo de totales agregados por provincia y por día de la semana
- Exportación de resultados a formato JSON
- Análisis exploratorio mediante consola
- Visualización de datos mediante gráficos (barras y circulares)
- Menú interactivo por consola
  
*(El proyecto es fácilmente migrable a pandas para mejorar escalabilidad y limpieza del código)*

---

## 🛠 Tecnologías utilizadas

- csv
- json
- datetime
- matplotlib

---

## 📁 Estructura del proyecto

```text
Dashboard_Covid-19/
│
├── data/
│ └── covid_data.json
│
├── proyecto_final.py
├── requirements.txt
└── README.md 

```

---

## ▶️ Ejecución

A continuación se muestra cómo clonar, instalar las dependencias y ejecutar este proyecto desde la terminal:

```bash
git clone https://github.com/YankoArm/Dashboard_Covid-19.git
cd Dashboard_Covid-19
pip install -r requirements.txt
python proyecto_final.py

```

---

## 🧠 ¿Cómo funciona el dashboard?

- Se agrupan los datos por provincia y por día de la semana para calcular totales agregados.

---

## 🎯 Objetivo del proyecto

Este proyecto ha sido desarrollado con fines formativos, con el objetivo de:

- Aprender a trabajar con datos reales.
- Utilizar librerías de análisis y visualización de datos en Python.
- Comprender el flujo básico de un proyecto de análisis de datos.
- Practicar la creación de visualizaciones claras y útiles.

---

## 📌 Notas

- El proyecto se ejecuta de forma local.
- No requiere conexión a internet.
- Los datos utilizados están incluidos en el repositorio.
