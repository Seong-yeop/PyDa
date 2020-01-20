import numpy as np
import pandas as pd


def get_ratings_numpy(df):
    # ============================================
    # TODO : datafame을 인자로 받지만, numpy를 이용해서 각 영화별 평점(평균)을 구한다.
    #      [input] : dataframe of pandas 
    #       
    #      [output] : 영화 id별 평점 평균이 담겨있는 data
    arr = np.array(df)      # Hint
    # ================ EDIT HERE =================
    ratings = {}
    for i in np.unique(arr[:,1]):
        tmp = arr[np.where(arr[:,1] == i)]
        ratings[i] = np.mean(tmp[:,2])
    # ============================================
    return ratings

def get_ratings_pandas(df):
    # ============================================
    # TODO : pandas를 이용해서 get_ratings_numpy와 같은 기능을 하는 함수를 만든다.
    #        즉, 영화별 평점 평균을 반환한다.
    #      [input] : dataframe of pandas 
    #       
    #      [output] : 영화 id별 평점 평균이 담겨있는 data
    # ================ EDIT HERE =================
    id_group = df.groupby('movieId').mean()
    ratings = id_group.rating
    # ============================================
    return ratings

def get_genres_cloumns(df):
    # ============================================
    # TODO : datafame의 영화 genres column에 있는 genre들을 unique하게 반환하는 함수
    #      [input] : dataframe of pandas 
    #       
    #      [output] : list 형태, genres 안에 있는 genre들을 담은 list
    # ================ EDIT HERE =================
    df.genres = df.genres.str.split('|')
    genre_columns = list(set([j for i in df.genres.tolist() for j in i]))
    '''
    [j for i in arguments for j in i] 
    equals
    for i in arguments
        for j in i
            list.append(j)
    '''
    # ============================================
    return genre_columns

def make_df_to_oneshot(df,genre_columns):
    # ============================================
    # TODO : datafame에 있는 genres column을 one shot encoding을 해서, 각 genre별 column을 만들어서 
    #        해당 영화의 장르인 경우에 1로 표시한다. (앞에서 lab에서 했던 결과와 동일)
    #      [input] : (dataframe of pandas, genre의 column들의 list)
    #       
    #      [output] : None or 필요없어진 genres의 column을 제거한 dataframe
    # ================ EDIT HERE =================
    for j in genre_columns:
        df[j] = 0
    for i in range(df.shape[0]):
        for j in genre_columns:
            if(j in df['genres'].iloc[i]):
                df.loc[i,j] = 1
    df.drop('genres', axis=1, inplace=True)
    # ============================================
    return None

if __name__ == '__main__':
    ratings_path = '/Users/yeop/Dropbox/lab/lab_pandas/lab_5_1/ratings.csv'
    movies_path = '/Users/yeop/Dropbox/lab/lab_pandas/lab_5_1/movies.csv'
    ratings = pd.read_csv(ratings_path)
    movies = pd.read_csv(movies_path)

    # =============== 영화 평점 평균 ================
    ratings_n = get_ratings_numpy(ratings)
    ratings_p = get_ratings_pandas(ratings)
    # ============================================

    # ============ one shot encoding =============
    genre_columns = get_genres_cloumns(movies)
    make_df_to_oneshot(movies,genre_columns)
    # ============================================
    
    print(movies)