import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt


def lat_lng_to_pixels(lat,lng):
    lat_rad = lat * np.pi / 180.0
    lat_rad = np.log(np.tan((lat_rad + np.pi / 2.0)/2.0))
    x = 100 * (lng + 180.0)/ 360.0
    y = 100 * (lat_rad - np.pi) / (2.0 * np.pi)
    return (x,y)


def df_drop(df, column_name):
    ## EDIT HERE ##
    df.drop(column_name, axis = 1, inplace = True)


def make_trip_duration(df):
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime']) #problem 2
    df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])
    df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds()/60
    