
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    df = pd.read_csv(r'C:\Users\yeop\Dropbox\lab\lab_matplotlib\data.csv')
    df.drop('Unnamed: 0', axis = 1, inplace = True)

    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime']) 
    df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])
    df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds()/60


    sns.distplot(df['passenger_count'],kde=False)
    plt.title('Distribution of Passenger Count')
    plt.show()
    


if __name__ == '__main__':
    main()