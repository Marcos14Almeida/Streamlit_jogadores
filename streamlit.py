# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 15:00:26 2022

@author: marcos
"""

#streamlit run streamlit.py

#For automatically install requirements.txt
#pip install pipreqs
#Then in the project folder open the terminal:
#pipreq ./

import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()


st.markdown(
    """
    <style>
    .main(
    background-color: #F5F5F5;
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

with header:
    st.title('Welcome to my awesome project')
    st.text("""
            In this project I look into some
            very cool things I hope you like
            """)
    df = get_data('jogadores')
    st.write(df.head(10))
    
    
    counting = pd.DataFrame(df['PAIS'].value_counts())
    st.subheader('Distribuição de origem dos jogadores')
    st.bar_chart(counting)
   
    counting100 = pd.DataFrame(df['PAIS'].head(100).value_counts())
    st.subheader('Distribuição de origem dos jogadores')
    st.bar_chart(counting100)

with dataset:
    st.header('NY City Taxi dataset')    

with features:  
    st.header('The features I created')
    st.markdown('* **first feature** I created this feature beacause of this...')
    st.markdown('* **second feature** I created this feature beacause of this...')

with model_training:    
    st.header('Time to train the model')
    st.text('Aqui é a descrição do dataset')
    
    sel_col, disp_col = st.columns(2)
    
    max_depth = sel_col.slider('What should be the max_depth of the model?', min_value=10, max_value=100, value=20, step=10)

    st.write(max_depth)

    n_estimators = sel_col.selectbox('How many tress should I use?', options=[100,200,300,'default'], index = 0)
    if n_estimators == 'default':
        n_estimators=100
    
    
    sel_col.text('Here is a list of possible features')
    sel_col.write(df.columns)
    
    input_feature = sel_col.text_input('Which feature should I use?','Jogos')


    regr = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
    
    x = df[[input_feature]]
    y = df[['Gols']]
    
    regr.fit(x,y)
    prediction = regr.predict(y)


    #Outra Coluna
    disp_col.subheader("Mean Absolute Error")
    disp_col.write(mean_absolute_error(y, prediction))
    disp_col.subheader("Mean Squared Error")
    disp_col.write(mean_squared_error(y, prediction))
    disp_col.subheader("R² Score")
    disp_col.write(r2_score(y, prediction))










































