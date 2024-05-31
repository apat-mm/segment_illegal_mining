# segment_illegal_mining

## Requisitos 

Antes de comenzar asegurate de tener instalados los siguientes componentes:

- Si es posible prepara un entorno virtual.
- Python, lo mas recomendable es que sea la ultima version.

### En caso de corer el despliegue (deploy.py):

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
