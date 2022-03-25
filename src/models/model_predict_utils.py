import pandas as pd
from src.features import build_features

def save_output(path,record,header):
   record.to_csv(r''+path, mode='a', header=header,index=False)
   return record                            


def predict_raw_data(model,domain):
    """
    Retuns a list containing the result of the prediction
    The list shows the domain, model, precition score, and confidence score.

    Args:
        model : loaded model from pickle
        domain: A string
        timestamp : A time of the data arrive in.
    Retuns:
        A Dataframe with features, timestamp, prediction_label, confidence_score
    """

    df = ['' + domain]
    df = pd.DataFrame(df, columns=['domain'])

    dataframe = build_features.build_features(df, True,True)
    features =dataframe.drop(['domain','longest_word','sld'], axis=1)

    # Find the prediction score and confidence score of the model
    catboost_pred_score = model.predict(features).tolist()[0]
    catboost_confidence_score = round(model.predict_proba(features)[0][catboost_pred_score], 2)
    dataframe['prediction_label']=catboost_pred_score
    dataframe['confidence_score']=catboost_confidence_score
    return dataframe