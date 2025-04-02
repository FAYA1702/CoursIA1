import pickle

model_name='diabete_RegressionLog.pkl'
model_loaded=pickle.load(open(model_name,'rb'))

def pred_prob(data):
    pred=int(model_loaded.predict(data))
    prob=model_loaded.predict_proba(data)
    prob=prob[0][pred]
    return pred,prob