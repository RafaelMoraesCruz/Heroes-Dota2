import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv('./data/heroes_data_limpo.csv',sep=',')

def create_static_graph1(df):
    
    area = plt.figure(figsize=(12,8))
    fig1 = area.add_subplot(2,2,1)
    fig2 = area.add_subplot(2,2,2)
    fig3 = area.add_subplot(2,2,(3,4))

    fig1.bar(data=df, x=df['attack_type'].unique(), height=df['attack_type'].value_counts())
    fig1.set_title('Quantidade de herois por tipo de ataque',fontweight="bold")
    fig1.set_ylabel('Quantidade de herois',fontweight="bold")
    fig1.set_xlabel('Tipo do ataque',fontweight="bold")

    fig2.bar(data=df, x=df['primary_attr'].unique(), height=df['primary_attr'].value_counts())
    fig2.set_title('Quantidade de herois por atributo',fontweight="bold")
    fig2.set_ylabel('Quantidade de herois',fontweight="bold")
    fig2.set_xlabel('Atributo primário',fontweight="bold")

    fig3.bar(data=df, x=df['main_role'].unique(), height=df['main_role'].value_counts())
    fig3.set_title('Quantidade de herois por função principal',fontweight="bold")
    fig3.set_ylabel('Quantidade de herois',fontweight="bold")
    fig3.set_xlabel('Função principal',fontweight="bold")
    area.tight_layout(pad=2.0)
    return area

def create_dinamic_graph1(df,eixo_x='main_role',eixo_y='winrate'):
    fig = px.scatter(data_frame=df, 
                 x=eixo_x, 
                 y=eixo_y, 
                 color='primary_attr',
                 marginal_y="box",
                 hover_data=['main_role','winrate','primary_attr','localized_name'],
                 title=f"<b> {eixo_y} por {eixo_x} dos herois </b>",
                 width=1000, 
                 height=600)
    return fig