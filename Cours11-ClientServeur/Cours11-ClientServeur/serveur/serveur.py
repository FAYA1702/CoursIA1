import warnings
warnings.filterwarnings('ignore')

from flask import Flask,request,jsonify
import pandas as pd
from model import pred_prob

# Initialisation du serveur flask

app=Flask(__name__)
@app.route('/Model',methods=['POST'])

def get_res():
    data=request.get_json(force=True)
    new_data=pd.DataFrame(data,index=[0])
    pred,proba=pred_prob(new_data)
    print(f'prediction: {pred} --> Proba: {round(proba*100,2) } %')
    dict_result={'class':pred,'proba':proba}
    return jsonify(dict_result)

# lancement du serveur

if __name__=="__main__":
    app.run(port=5000,debug=True)