# Import required libraries
import PIL

import streamlit as st
from ultralytics import YOLO

# Ruta de los pesos del modelo
model_path = 'C:/Users/kevin/IA/best.pt'

# Interfaz
st.set_page_config(
    page_title="Illegal mining segmentation",  
    page_icon=":pick:",    
    layout="wide",      
    initial_sidebar_state="expanded",    
    
)

# Barra lateral
with st.sidebar:
    st.header("Image Config")   
    
    source_img = st.file_uploader(
        "Upload an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

    # NIvel de confianza del modelo
    confidence = float(st.slider(
        "Select Model Confidence", 25, 100, 40)) / 100

st.title("Illegal mining segmentation")
st.caption('Updload a photo with some :blue[surface].')
st.caption('Then click the :blue[Segment Objects] button and check the result.')

col1, col2 = st.columns(2)

# Carga de imagen
with col1:
    if source_img:
        
        uploaded_image = PIL.Image.open(source_img)
        
        st.image(source_img,
                 caption="Uploaded Image",
                 use_column_width=True
                 )

try:
    model = YOLO(model_path)
except Exception as ex:
    st.error(
        f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

if st.sidebar.button('Segment Objects'):
    res = model.predict(uploaded_image,
                        conf=confidence
                        )
    boxes = res[0].boxes
    res_plotted = res[0].plot()[:, :, ::-1]
    with col2:
        st.image(res_plotted,
                 caption='Segmented Image',
                 use_column_width=True
                 )
        try:
            with st.expander("Segmentation Results"):
                for box in boxes:
                    st.write(box.xywh)
        except Exception as ex:
            st.write("No image is uploaded yet")