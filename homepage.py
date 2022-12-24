# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 23:26:35 2022

@author: marcos
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st
import plotly.express as px

def home(df):
    
    
 header = st.container()
 features = st.container()
 dataset = st.container()

##############################################
##############################################
 with header:
    st.title('Welcome to my awesome project')
    st.header('FIFA Best Players dataset')   
    st.text("""
            In this project I look into some
            very cool things I hope you like
            """)
            
    st.markdown('**Olhando os 10 primeiros valores:**')
    st.write(df.head(10))
    
    st.text('Removendo os valores nulos')
    df = df.replace(np.nan, 0)
    st.write(df)
    st.text('Tabela com os melhores jogadores da história')
    

##############################################
##############################################
 with features:  
    st.header('The features I created')
    st.markdown('* **first feature** I created this feature beacause of this...')
    st.markdown('* **second feature** I created this feature beacause of this...')
    
##############################################
##############################################
 with dataset:
    st.header('Distribuição por país')    
    variable_col = 'PAIS'
    
    counting = pd.DataFrame(df[variable_col].value_counts()).sort_values(variable_col,ascending=False)
    st.subheader('Distribuição de origem dos jogadores')
    st.bar_chart(counting)
   
    counting100 = pd.DataFrame(df[variable_col].head(100).value_counts()).sort_values(variable_col,ascending=False)
    st.subheader('Distribuição de origem dos 100 melhores jogadores')
    st.bar_chart(counting100)

