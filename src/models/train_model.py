import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from src.visualization import visualize
from sklearn.ensemble import RandomForestClassifier
import pickle



def train_model(input_path):
    df = pd.read_csv(r''+input_path)
    df=df.drop(['timestamp','longest_word','sld'], axis = 1)


    X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,:-1], df.iloc[:,-1], test_size=0.3, random_state=42)
    rf_clf=RandomForestClassifier(n_estimators=250)
    rf_clf.fit(X_train,y_train)

    y_pred = rf_clf.predict(X_test)
    visualize.visualize_results(rf_clf,X_test,y_test, y_pred)


    pickle.dump(rf_clf, open(r'C:\Users\alaa\Desktop\assignment2-AalaaNagy88\models\model.sav', 'wb'))



