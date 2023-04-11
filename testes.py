# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 00:17:37 2022

@author: marcos
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st
import plotly.express as px


def testes(df):

    st.header("Gráfico de tamanho ajustável:")

    width = st.sidebar.slider("plot width", 1, 12, 1)
    height = st.sidebar.slider("plot height", 1, 12, 1)
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots(figsize=(width, height))
    ax.hist(arr, bins=20)
    from PIL import Image

    fig.savefig("figure_name.png")
    image = Image.open("figure_name.png")
    st.image(image)

    expander = st.expander("Open")
    expander.write(
        """
                   
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
    
    """
    )
    expander.image("https://static.streamlit.io/examples/dice.jpg", width=350)

    st.header("Exemplo de código:")
    st.code("pip install")
