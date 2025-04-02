import streamlit as st
import pandas as pd

def user_input_features():
    with st.sidebar:
        NbGrossesse=st.slider('NbGrossesse',0.00,17.00,10.0)  
        Glucos=st.slider('Glucos',0.00,199.00,80.0)  
        PressArt=st.slider('PressArt',0.00,122.00,80.0)  
        AppasPli=st.slider('AppasPli',0.00,99.00,40.0)    
        Insuline=st.slider('Insuline',0.00,846.00,500.0)      
        IMass=st.slider('IMass',0.00,67.00,40.0)      
        Pedigree=st.slider('Pedigree',0.08,2.42,1.00)        
        age=st.slider('Age',21.00,81.00,50.0)

        data={
            'NbGrossesse':NbGrossesse,  
            'Glucos':Glucos,  
            'PressArt':PressArt,  
            'AppasPli':AppasPli,  
            'Insuline':Insuline,  
            'IMass':IMass,  
            'Pedigree':Pedigree,    
            'age':age
        }
    return data






'''
       NbGrossesse  Glucos  PressArt  AppasPli  Insuline  IMass  Pedigree    age  class

min           0.00    0.00      0.00      0.00      0.00   0.00      0.08  21.00   0.00

max          17.00  199.00    122.00     99.00    846.00  67.10      2.42  81.00   1.00

'''
