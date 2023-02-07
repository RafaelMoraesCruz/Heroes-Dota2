import pandas as pd
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from utils import create_static_graph1

df = pd.read_csv('./data/heroes_data_limpo.csv',sep=',')

list_primary_attr = df['primary_attr'].unique()
list_main_role = df['main_role'].unique()
image = Image.open('./data/img/dota2.jpg')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


header = st.container()
data_frame = st.container()
static_graph1 = st.container()
dinamic_graph = st.container()

with header:
    st.header('Estudo analítico Herois do Dota 2')
    st.image(image, caption='Herois Dota2')

with data_frame:
    st.title('Visão inicial dos dados')
    values = st.slider(
    'Selecione a quantidade de dados',
    0, df.shape[0], (0, 20))
    st.dataframe(df.iloc[values[0] : values[1],:])
    
with static_graph1:
    st.title('Gráficos estáticos')
    graph1 = create_static_graph1(df)
    st.pyplot(graph1)
    
with dinamic_graph:
    st.title('Gráficos dinâmicos')