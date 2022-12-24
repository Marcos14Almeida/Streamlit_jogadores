# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 15:00:26 2022

@author: marcos
"""

#streamlit run streamlit.py

#For automatically install requirements.txt
#pip install pipreqs
#Then in the project folder open the terminal:
#pipreqs ./

#!git pull origin master
#!git add "file.py"
#!git add .
#!git commit -m "My commit"
#!git push origin master

from cool_graphs import interactive_plot
from homepage import home
from modelos import modelos
from testes import testes

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import streamlit as st
import plotly.express as px


st.set_page_config(layout="wide")

firulas = st.container()


st.markdown(
    """
    <style>
    .main(
    background-color: #FA6B6D;
    )
    </style>
    """,
    unsafe_allow_html=True
    )

#streamlit cache for big datasets
@st.cache
def get_data(filename):
    df = pd.read_csv('data/'+filename+'.csv')
    return df


df = get_data('jogadores')


def homes(uploaded_file):
    if uploaded_file:
        st.sidebar.header('Brinks, esse arquivo é só pra enfeitar')
    else:
        st.sidebar.header('To begin please upload a file')
##############################################
##############################################

    
with firulas:    
    optionsList = ['Home','Random Forest','Plot','Teste']
    options = st.sidebar.radio('Titulo',options=optionsList)
    
    upload_file = st.sidebar.file_uploader('Upload a file data')
    #filename = upload_file.name
    homes(upload_file)
    
    # Functions for each of the pages
    if(options == optionsList[0]):
        home(df)
    elif(options == optionsList[1]):
        modelos(df)
    elif(options == optionsList[2]):
        interactive_plot(df)
    else:
        testes(df)








































