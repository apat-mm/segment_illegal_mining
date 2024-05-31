# Detección y segmentación de minería ilegal 
###### _Elaborado por:  Kevin Artunduaga Vivas - Angie Manzano Meléndez_


## Contexto

La minería ilegal representa uno de los más grandes desafíos en Colombia, con consecuencias bastante perjudiciales para el medio ambiente, la economía y los ciudadanos. Esta práctica indebida va desde la extracción de minerales hasta la deforestación, arraigando a diversas regiones del país y siendo alimentada principalmente por la ausencia de una supervisión y  regulación efectiva. Como consecuencia a esta problemática surge la necesidad de buscar soluciones innovadoras y eficaces que sean capaces de combatir con la minería ilegal. En este contexto los avances tecnológicos principalmente en el campo de la inteligencia artificial se busca ofrecer una herramienta para abordar este desafío.

El objetivo principal del siguiente proyecto se basa en desarrollar un sistema de detección automatizada de patrones de minería ilegal especialmente en imágenes aéreas. Como resultado este sistema podría ayudar a las autoridades y organizaciones ambientales a identificar las actividades mineras ilegales, aportando a la conservación del medio ambiente y la protección de los derechos humanos.

## Data

El conjunto de imagenes seleccionado para realizar el modelo de detección y segmentación fue el dataset del proyecto [__AmazonCRIME 2022__](https://github.com/jp-geoAI/AmazonCRIME) el cual realiza la creación de un conjunto de datos de Inteligencia Artificial Geoespacial y punto de referencia para la clasificación de áreas potenciales vinculadas a crímenes ambientales transnacionales en la selva amazónica. Tiene datasets para diferentes crimenes como:
- Deforestación
- Cultivos ilícitos
- __Minería ilegal__

El dataset de interes que cumple con el contexto del proyecto es el de minería ilegal, el cual tiene las siguientes caracteristicas:
<div align="center">
   
   | Caracteristicas  | Ejemplo imagenes |
   | ------------- | ------------- |
   | - 5000 imagenes en total<br>- Capturadas entre el años 2017 y 2019<br>- 256 x 256 pixeles<br>- De origen satelital pero procesadas para mejor manejo | ![mina](https://i.postimg.cc/ZCXv9c9Q/illegal-mining-0768.jpg)|
   
</div>

## Requisitos 

Antes de comenzar asegurate de tener instalados los siguientes componentes:

- Si es posible prepara un entorno virtual.
- Python, lo mas recomendable es que sea la ultima version.

### En caso de correr el despliegue (deploy.py):

1. Instala las siguientes librerias
   ```bash
   pip install torch
   pip install ultralytics
   pip install streamlit

2. En caso de querer verificar si se instalo correctamente streamlit y determinar que corra crea un archivo que se llame app.py y pon estas lineas de codigo (sino quieres realizar este paso salta al 4 paso)
   ```bash
   import streamlit as st
   st.write("Hello, World!")

3. Para correr el codigo ejecuta este comando en la terminal
   ```bash
   streamlit run app.py

4. Ya para correr el despliegue solo ejecuta en la terminal este comando
   ```bash
   streamlit run deploy.py
