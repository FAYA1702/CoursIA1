import warnings
warnings.filterwarnings('ignore')

import json,requests

from user import user_input_features
#from model import pred_prob
import streamlit as st

url=' http://127.0.0.1:5000/Model'

def main():
    st.set_page_config(page_title="Diagnostique du diabéte",page_icon=":hospital:")
    st.title(":orange[Diagnostique du diabète en ligne :hospital:]")
    st.write("""
    # :red[Application de prédiction du diabète]
    ## Cette application classifie les diabétiques Pos/Neg 

    """   
   )
    st.sidebar.header('Entrer les analyse :')
    analyse=user_input_features()
    #st.write(analyse)
    #pred,proba=pred_prob(analyse)
    requete=json.dumps(analyse)
    reponse_serveur=requests.post(url,requete)
    dic_reponse=reponse_serveur.json()
    pred,proba=dic_reponse['class'],dic_reponse['proba']

    if pred==1:
        st.write("## :red[Positif]:cry:")
    else:
        st.write("## :green[Négatif]:smile:")
    st.write(f"## Proba: {round(proba*100,2)}")

if __name__=='__main__':
    main()

