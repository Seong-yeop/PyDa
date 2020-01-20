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
    
    
    print(df.passenger_count.value_counts())

    '''
    plt.figure(figsize=(16,4))
    sns.barplot(x=num_passengers.index, y=num_passengers.values)
    plt.show()
    '''
if __name__ == '__main__':
    main()