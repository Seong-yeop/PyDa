import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import answer 

def main():
    #데이터 불러오기 
    df = pd.read_csv(r'C:\Users\yeop\Dropbox\lab\lab_pandas\data.csv') 
    delete_column = 'Unnamed: 0'
    print(df)
    answer.df_drop(df,delete_column)
    print(df)


if __name__ == '__main__':
    main()
