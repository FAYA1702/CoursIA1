from datetime import date
import streamlit as st
from PIL import Image
from pandas import read_csv
import pandas as pd
import scipy  as sc
import seaborn as snb
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix



try:
    fichier = 'pima-indians-diabetes.data.csv'
    col=['NbGrossesse','Glucos','PressArt','AppasPli','Insuline','IMass','Pedigree','Age','Class']
    patient=[f'Patient_{i}' for i in range(1,769)]
    data=read_csv(fichier,names=col)
    data.index=patient
    
    
except:
    print('Erreur de lecture du fichier')

st.sidebar.title('Navigation')
menu=st.sidebar.selectbox('choisir un volet',['Acceuil','Peek at the data','Etude de correlation','Visualisation',"Rapport d'analyse"])

if menu=='Acceuil':
    st.markdown(
        """
        <div style='text-align:center;'>

        <h1> Analyse de donnees sur la diabete </h1>
        </div>

        """, unsafe_allow_html=True
        )
    st.subheader('Affichage des donnees')
    st.dataframe(data)

elif menu=='Peek at the data':
     st.subheader('Peek at the data')
    #---------------------------------
     st.subheader('Affichage des 10 premieres patientes')
     st.dataframe(data.head(10))
    #---------------------------------
     st.subheader('Affichage des 10 dernieres patientes')
     st.dataframe(data.tail(10))
    #---------------------------------
     st.subheader('Statistiques descriptives')
     st.write(data.describe())
    #---------------------------------
     st.subheader('Repetition des classe')
     class_count=data.groupby('Class').size()
     st.write(class_count)
    #---------------------------------
     figure, ax_class = plt.subplots()
     data['Class'].value_counts().plot(kind='bar', color=['green', 'red'], ax=ax_class)
     ax_class.set_xlabel('Class (0=non Diabetique et 1 = Diabetique)')
     ax_class.set_ylabel('Nombre de patientes')
     st.pyplot(figure)

    
elif menu=='Etude de correlation':
     st.subheader('Erreur de correlation')
     st.subheader('Correlation de Pearson')
     st.write(data.corr()) 

     figure_corr, ax_corr = plt.subplots(figsize=(15, 15))  
     snb.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax_corr)
     st.pyplot(figure_corr)

     
elif menu == 'Visualisation':
    st.subheader('Les histogrammes')
    data.hist(figsize=(15,10),bins=20,layout=(3,3),grid=True)
    st.pyplot(plt.gcf())

    st.subheader('Histogrammes pour Insuline')
    figure_hist,ax_his=plt.subplots()
    ax_his.hist(data['Insuline'],bins=20,edgecolor='black')
    ax_his.set_xlabel('Taux insuline')
    ax_his.set_ylabel('frequence')
    st.pyplot(figure_hist)
    
    st.subheader('Graphe de densite')
    data.plot(kind='density',subplots=True,sharex=False,sharey=False,figsize=(15,15),layout=(3,3))
    st.pyplot(plt.gcf())
    
    st.subheader('Boite a Moustache')
    data.plot(kind='box',subplots=True,sharex=False,sharey=False,figsize=(15,15),layout=(3,3))
    st.pyplot(plt.gcf())
   
    st.subheader('Scatter Matrice')
    scatter_matrix(data,figsize=(25,25),c='b')
    st.pyplot(plt.gcf())
    
    st.subheader('Pairplot')
    snb.pairplot(data,hue='Class')
    st.pyplot(plt.gcf())
    
    st.subheader('Pairplot(Insuline/IMass)')
    snb.pairplot(data,hue='Class',vars=['Insuline','IMass'])
    st.pyplot(plt.gcf())
    
else : 
    st.title("Rapport d'analyse de donnees")
