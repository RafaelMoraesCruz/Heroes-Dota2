import pandas as pd
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from utils import create_static_graph1,create_dinamic_graph1

df = pd.read_csv('./data/heroes_data_limpo.csv',sep=',')
df_to_show = df[['localized_name', 'primary_attr','attack_type','move_speed','winrate', 'main_role','quantidade_vezes_escolhido']]

image = Image.open('./data/img/dota2.jpg')

st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

header = st.container()
data_frame, static_graph = st.columns(2)
dinamic_graph_title = st.container()
legenda,dinamic_graph = st.columns([1,3])

with header:
    st.header('Estudo analítico Herois do Dota 2')
    st.image(image, caption='Herois Dota2')

with data_frame:
    st.title('Visão inicial dos dados')
    values = st.slider(
    'Selecione a quantidade de dados',
    0, df.shape[0], (0, 120))
    st.dataframe(df_to_show.iloc[values[0] : values[1],:])
    
with static_graph:
    st.title('Gráficos estáticos')
    static_graph1 = create_static_graph1(df)
    st.pyplot(static_graph1)
    
with dinamic_graph_title:
    st.title('Gráficos dinâmicos')
    
with legenda:
    st.write('Filtros')
    eixo_x = st.selectbox(
    'Selecione a variável para o eixo x',
    ('primary_attr', 'attack_type', 'main_role'))
    eixo_y = st.selectbox(
    'Selecione a variável para o eixo y',
    ('winrate', 'quantidade_vezes_escolhido','1_pick','8_pick'))
    
with dinamic_graph:
    dinamic_graph1 = create_dinamic_graph1(df,eixo_x=eixo_x, eixo_y=eixo_y)
    st.plotly_chart(dinamic_graph1)