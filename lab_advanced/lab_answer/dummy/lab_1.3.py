import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns


def make_trip_duration(df):
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds()/60


def main():
    df = pd.read_csv(r'C:\Users\yeop\Dropbox\lab\lab_pandas\taxi_dataset\nyc.2019-01.csv')
    
    make_trip_duration(df)
    
    df['pickup_day']=df['tpep_pickup_datetime'].dt.day_name()
    df['dropoff_day']=df['tpep_dropoff_datetime'].dt.day_name()
    
    print(df['pickup_day'].value_counts())

if __name__ == '__main__':
    main()