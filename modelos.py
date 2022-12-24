# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 23:35:30 2022

@author: marcos
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import streamlit as st
import plotly.express as px

def modelos(df):
    model_training = st.container()
    ##############################################
    ##############################################
    with model_training:    
        st.header('Hora de treinar o modelo')
        st.text('Aqui é a descrição do dataset')
        
        sel_col, disp_col = st.columns(2)
        
        max_depth = sel_col.slider('What should be the max_depth of the model?', min_value=10, max_value=100, value=20, step=10)

        st.write(max_depth)

        n_estimators = sel_col.selectbox('How many trees should I use?', options=[100,200,300,'default'], index = 0)
        if n_estimators == 'default':
            n_estimators=100
        
        
        sel_col.text('Nomes de features possíveis')
        sel_col.write(df.columns)
        
        input_feature = sel_col.text_input('Que feature eu devo usar?','Jogos')

        input_cols = [col for col in df.columns if input_feature in col]
        if(len(input_cols) == 0 or isinstance(df[input_feature][0],str)):
            input_feature = "Jogos"
            st.write("Coluna não numérica, ou coluna inexistente")
            st.write("Aviso a coluna usada é:",str(input_feature))
        regr = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
        
        x = df[[input_feature]]
        y = df[['Gols']]
        
        regr.fit(x,y.values.ravel())
        y.columns = ['Gols']
        prediction = regr.predict(x)

        #Outra Coluna
        disp_col.subheader("Mean Absolute Error")
        disp_col.write(mean_absolute_error(y, prediction))
        disp_col.subheader("Mean Squared Error")
        disp_col.write(mean_squared_error(y, prediction))
        disp_col.subheader("R² Score")
        disp_col.write(r2_score(y, prediction))