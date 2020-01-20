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


def main():
    df = pd.read_csv(r'C:\Users\yeop\Dropbox\lab\lab_matplotlib\data.csv')

    px, py = lat_lng_to_pixels(df['pickup_latitude'],df['pickup_longitude'])
  
    plt.figure(figsize=(8,6))
    plt.scatter(px,py, s=.1,alpha=.03)
    plt.axis('equal')
    plt.xlim(29.40,29.55)
    plt.ylim(-37.64, -37.54)
    plt.show()
    

if __name__ == '__main__':
    main()