from datetime import date
import streamlit as st
from PIL import Image


st.sidebar.title('Cours Streamlit')
menu=st.sidebar.selectbox('Navigation',['Acceuil','Les Objets','IA2'])

if menu=='Acceuil':
    st.header('Titre 1')
    st.subheader('Titre 1.1')
    st.markdown(
        """
        <div style='text-align:center;'>

        <h1> Introduction à streamlit </h1>
        <p style='color:blue'> Ce cours est une introduction à streamlit </p>
       
        </div>

        """, unsafe_allow_html=True
        )

    st.caption('Text.......')
    st.button('OK')

elif menu=='Les Objets':
    # --- Textbox
    nom=st.text_input("Entrer votre Nom:")
    if nom:
        st.write(f'Bonjour : {nom}' )
    #---Comboxbox
    options=['Option1','Option2','Option3']
    choix=st.selectbox("Veuillez choisir une option :",options)
    st.write(f'Vous avez selectionneé : {choix}')

    #------------------------Radio Button
    choix=st.radio('Choisissez votre club préféré:',['FBC','JUV','PSG','MUN'])
    st.write('Votre club préféré est : ',choix)

    #------------------------Multiselect
    choix2=st.multiselect('Choisissez vos clubs préférés:',['FBC','JUV','PSG','MUN'])
    st.write(f'Votre club préféré est : {' , '.join(choix2)}')

    #-----------------------Checkbox
    check=st.checkbox('Accepter-vous les termes du contrat ?')
    if check:
        st.write('Merci')

    # ----------- TextArea
    tex=st.text_area('Votre commentaire svp :')
    if tex:
        st.write(f'Commantaire : {tex}')
        st.write(f'Nb de Caractère : {len(tex)}')
    # -------------Date---------------------
    dateSelec=st.date_input('Choisir une date : ',date.today())
    st.write('La date :',dateSelec)

else :
    #------------- Chargement et affichage d'une image
    # from PIL import Image

    fichier=st.file_uploader('Choisissez une image',type=['jpg','jpeg','png'])

    if fichier is not None:
        img=Image.open(fichier)
        # Affichage dans streamlit
        st.image(img,caption='Image Chargée',use_container_width=True)

    #---------------Slider------------

    Temp=st.slider('Température :',-50.0,50.0,0.0)
    st.write(f'Température est : {Temp}')
'''
st.sidebar.title('Cours Streamlit')
menu=st.sidebar.selectbox('Navigation',['Acceuil','Les Objets','IA2'])

'''