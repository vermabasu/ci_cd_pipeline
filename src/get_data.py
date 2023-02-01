# read the data from s3_source
# convert that into dataframe
# store it in data/raw

import os
import yaml
import argparse
import pandas as pd


def read_params(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config

def read_data(config_path):
    config = read_params(config_path)
    source_path = config["data_source"]["s3_source"]
    dest_path = config["load_data"]["raw_dataset_csv"]
    df = pd.read_csv(source_path)
    new_col = [col.replace(" ","_") for col in df.columns]
    df.to_csv(dest_path,index=False,header=new_col)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    read_data(parsed_args.config)