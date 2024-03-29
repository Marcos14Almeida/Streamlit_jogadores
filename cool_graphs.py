# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 23:24:07 2022

@author: marcos
"""

import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt


def interactive_plot(df):

    graficos1 = st.container()
    graficos2 = st.container()

    with graficos1:

        st.title("Pode brincar")
        col1, col2 = st.columns(2)

        x_axis_val = col1.selectbox("Select the X-axis", options=df.columns)
        y_axis_val = col2.selectbox("Select the Y-axis", options=df.columns)

        cor = st.color_picker(df, x=x_axis_val, y=y_axis_val)

        plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
        plot.update_traces(marker=dict(color=cor))

        st.plotly_chart(plot, use_container_width=True)

    with graficos2:
        st.title("Agora é minha vez 😈")

        fig, ax = plt.subplots()
        ax.scatter(x=df["Sel. Jogos"], y=df["Jogos"])
        ax.set_xlabel("Eixo X")
        st.pyplot(fig)
