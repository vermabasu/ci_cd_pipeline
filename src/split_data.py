# load data from data/raw
# split into train and test 
# store in data/processed

import os
import pandas as pd
import argparse
from get_data import read_params
from sklearn.model_selection import train_test_split


def train_test_split_data(config_path):
    config = read_params(config_path)
    source_path = config["load_data"]["raw_dataset_csv"]
    train_path = config["split_data"]["train_path"]
    test_path = config["split_data"]["test_path"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]
    
    
    df = pd.read_csv(source_path)
    train,test = train_test_split(df,random_state=random_state,test_size=split_ratio)
    train.to_csv(train_path,index=False)
    test.to_csv(test_path,index=False)


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default = "params.yaml")
    parsed_args = args.parse_args()
    train_test_split_data(parsed_args.config)
    