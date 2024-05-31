# Detección y segmentación de minería ilegal 
###### _Elaborado por:  Kevin Artunduaga Vivas - Angie Manzano Meléndez_


## Contexto

La minería ilegal representa uno de los más grandes desafíos en Colombia, con consecuencias bastante perjudiciales para el medio ambiente, la economía y los ciudadanos. Esta práctica indebida va desde la extracción de minerales hasta la deforestación, arraigando a diversas regiones del país y siendo alimentada principalmente por la ausencia de una supervisión y  regulación efectiva. Como consecuencia a esta problemática surge la necesidad de buscar soluciones innovadoras y eficaces que sean capaces de combatir con la minería ilegal. En este contexto los avances tecnológicos principalmente en el campo de la inteligencia artificial se busca ofrecer una herramienta para abordar este desafío.

El objetivo principal del siguiente proyecto se basa en desarrollar un sistema de detección automatizada de patrones de minería ilegal especialmente en imágenes aéreas. Como resultado este sistema podría ayudar a las autoridades y organizaciones ambientales a identificar las actividades mineras ilegales, aportando a la conservación del medio ambiente y la protección de los derechos humanos.

## Data

El conjunto de imagenes seleccionado para realizar el modelo de detección y segmentación fue el dataset del proyecto [__AmazonCRIME 2022__](https://github.com/jp-geoAI/AmazonCRIME) el cual realiza la creación de un conjunto de datos de Inteligencia Artificial Geoespacial y punto de referencia para la clasificación de áreas potenciales vinculadas a crímenes ambientales transnacionales en la selva amazónica. Tiene datasets para diferentes crimenes como:
- Pistas de aterrizaje
- Deforestación
- Forestación
- __Mineria ilegal__
- Cultivos ilicitos
- Agua

<br>

Este dataset contaba con 5000 imagenes a partir de la mineria ilegal, sin embargo al contar con demasiadas imagenes se hizo la anotacion o labeling de 1053 imagenes de 256 x 256 pixeles para realizar el debido etiquetado de las clases, las cuales son:

<br>

<div align="center">
   
   | Clase  | Descripción |
   | ------------- | ------------- |
   | illegal-mining | Área donde se realizan actividades de minería ilegal. |
   | toxic-pool | Una piscina tóxica es el agua contaminada con productos químicos o desechos industriales por la mineria. |
   | river | Avistamientos de rios o lagos cercas. |
   
</div>
<br>

Teniendo como datos de entrenamiento las siguientes imagenes:

<div align="center">
   
   | Imagen original  | Imagen para entrenamiento |
   | ------------- | ------------- |
   | [![illegal-mining-0665.jpg](https://i.postimg.cc/sgzfc1CW/illegal-mining-0665.jpg)](https://postimg.cc/PP6kfXxf) | <img src="https://i.postimg.cc/8zjRD1Cj/Captura.jpg" alt="Perro" width="256" height="256"/> |
   
</div>
<br>

## Arquitectura YoloV8

La principal ventaja de las arquitecturas Yolo (You Only Look Once) es la velocidad ya que no necesitan una arquitectura o estructura compleja a diferencia de otras.

__FPN:__ Feature Pyramid Network (Red de piramide de caracteristicas)

La red se divide en las siguientes partes:
- Backbone --> Extractor de caracteristicas
- ¿Neck? --> Operaciones de fusión y concatenación
- Head --> Generación de bounding boxes

![arq](https://miro.medium.com/v2/resize:fit:1400/1*YkkGwFBksWVbm4GmZfSDsg.jpeg)

## Entrenamiento

Si desea realizar el entrenamieno del modelo por su cuenta, ejecute los comando que se encuentran en el notebook llamado [segmentation_illegalMining.ipynb](https://github.com/apat-mm/segment_illegal_mining/blob/main/segmentation_illegalMining.ipynb). Siga todos los pasos en el orden que se encuentran.

>[!Tip]
>Para realizar el entrenamiento es necesario utilizar la T4 GPU que ofrece Google Colab. Para ello dirjase a `Entorno de ejecución` despues a `Cambiar tipo de entorno de ejecución` y seleccione la opción de `T4 GPU`



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
