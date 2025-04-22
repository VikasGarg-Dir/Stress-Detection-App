# Import necessary modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y):
    """This function creates the visualization page"""
    
    # Remove warnings
    warnings.filterwarnings('ignore')

    # Set the page title
    st.title("Visualise the Stress Level")

    # Create a checkbox to show correlation heatmap
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.iloc[:, 1:].corr(), annot=True, ax=ax)
        ax.set_ylim(ax.get_ylim()[0] + 0.5, ax.get_ylim()[1] - 0.5)
        st.pyplot(fig)

    if st.checkbox("Show Scatter Plot"):
        fig, axis = plt.subplots(2, 2, figsize=(15, 10))

        sns.scatterplot(ax=axis[0, 0], data=df, x='t', y='rr')
        axis[0, 0].set_title("Body Temperature vs Respiration Rate")

        sns.scatterplot(ax=axis[0, 1], data=df, x='sr', y='lm')
        axis[0, 1].set_title("Snoring Rate vs Limb Movement")

        sns.scatterplot(ax=axis[1, 0], data=df, x='bo', y='t')
        axis[1, 0].set_title("Blood Oxygen vs Body Temperature")

        sns.scatterplot(ax=axis[1, 1], data=df, x='sh', y='hr')
        axis[1, 1].set_title("Sleeping Hour vs Heart Rate")

        st.pyplot(fig)

    if st.checkbox("Display Boxplot"):
        fig, ax = plt.subplots(figsize=(15, 5))
        df.boxplot(['sr', 'rr', 't', 'rem', 'bo', 'sh'], ax=ax)
        st.pyplot(fig)

    if st.checkbox("Show Sample Results"):
        safe = (df['sl'] == 0).sum()
        low = (df['sl'] == 1).sum()
        med = (df['sl'] == 2).sum()
        high = (df['sl'] == 3).sum()
        vhigh = (df['sl'] == 4).sum()
        data = [safe, low, med, high, vhigh]
        labels = ['Safe', 'Low', 'Medium', 'High', 'Very High']
        colors = sns.color_palette('pastel')[0:5]

        fig, ax = plt.subplots()
        ax.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
        st.pyplot(fig)
