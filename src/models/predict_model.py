import pickle
from src.models.model_predict_utils import save_output,predict_raw_data


def predict_model(consumer,output_path):
# Load the model
    with open(r'C:\Users\alaa\Desktop\assignment2-AalaaNagy88\models\model.sav', 'rb') as pickle_file:
        model = pickle.load(pickle_file)

    # Ingesting data from input topic
    for i,message in enumerate(consumer):
        if i==0:
            header=True
        else:
            header=False
        if i<=100000:
            domain = message.value.decode("utf-8")
            dataframe = predict_raw_data(model,domain)
            print(save_output(output_path,dataframe,header))
        else:
            break
