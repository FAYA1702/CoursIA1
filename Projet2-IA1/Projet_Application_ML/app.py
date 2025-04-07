import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.impute import SimpleImputer

# Title of the app
st.title('Application Web pour Modèles d\'Apprentissage Automatique')

# Function to load the data
def load_data(file):
    data = pd.read_csv(file)
    st.write("Aperçu des données", data.head())
    return data

# Function to handle classification task
def classification_model(data, target):
    X = data.drop(columns=[target])
    y = data[target]
    
    # Handling missing values
    imputer = SimpleImputer(strategy='most_frequent')
    X = imputer.fit_transform(X)
    y = imputer.fit_transform(y.values.reshape(-1, 1)).ravel()

    # Convert y to pandas Series to use unique() method
    y = pd.Series(y)

    # Check if the target is binary or multicalss (classification task)
    unique_values = len(y.unique())
    if unique_values == 2:
        st.write("C'est un problème de classification binaire.")
    elif unique_values > 2:
        st.write("C'est un problème de classification multiclasse.")
    else:
        st.write("Ce problème semble être un problème de régression, pas de classification.")
        return
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train the models
    models = {
        'Random Forest': RandomForestClassifier(),
        'SVM': SVC(),
        'Decision Tree': DecisionTreeClassifier()
    }
    
    best_model = None
    best_accuracy = 0
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model

    st.write(f'Modèle choisi : {best_model.__class__.__name__}')
    st.write(f'Précision : {best_accuracy * 100:.2f}%')

# Function to handle regression task
def regression_model(data, target):
    X = data.drop(columns=[target])
    y = data[target]
    
    # Handling missing values
    imputer = SimpleImputer(strategy='mean')
    X = imputer.fit_transform(X)
    y = imputer.fit_transform(y.values.reshape(-1, 1)).ravel()

    # Convert y to pandas Series to use unique() method
    y = pd.Series(y)
    
    # Check if the target is numeric or categorical
    if y.dtype in ['int64', 'float64'] and len(y.unique()) > 2:  # Check if numeric and continuous
        st.write("C'est un problème de régression.")
    else:
        st.write("Ce problème semble être un problème de classification, pas de régression.")
        return
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train the models
    models = {
        'Random Forest': RandomForestRegressor(),
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor()
    }
    
    best_model = None
    best_mse = float('inf')
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        if mse < best_mse:
            best_mse = mse
            best_model = model

    st.write(f'Modèle choisi : {best_model.__class__.__name__}')
    st.write(f'Erreur Quadratique Moyenne : {best_mse:.2f}')

# Uploading the file
uploaded_file = st.file_uploader("Téléchargez votre fichier CSV", type="csv")

if uploaded_file is not None:
    data = load_data(uploaded_file)
    
    # Selecting task type (classification or regression)
    task_type = st.selectbox("Sélectionnez le type de tâche", ["Classification", "Régression"])
    
    # Selecting target variable
    target = st.selectbox("Sélectionnez la variable cible", data.columns)
    
    if task_type == "Classification":
        classification_model(data, target)
    elif task_type == "Régression":
        regression_model(data, target)
