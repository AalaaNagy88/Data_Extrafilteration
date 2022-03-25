# -*- coding: utf-8 -*-
# import click
import logging
from pathlib import Path
# from dotenv import find_dotenv, load_dotenv
from src.models.train_model import train_model
from src.models.predict_model import predict_model
from kafka import KafkaConsumer





def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    train_model(input_filepath)
    consumer = KafkaConsumer('ml-raw-dns', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    predict_model(consumer,output_filepath)



if __name__ == '__main__':
    # log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    # logging.basicConfig(level=logging.INFO, format=log_fmt)

    # # not used in this stub but often useful for finding various files
    # project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    # load_dotenv(find_dotenv())

    main(r"C:\Users\alaa\Desktop\assignment2-AalaaNagy88\data\raw\training_dataset.csv",r"C:\Users\alaa\Desktop\assignment2-AalaaNagy88\data\processed\output.csv")
