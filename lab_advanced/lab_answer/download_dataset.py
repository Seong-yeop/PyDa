import urllib.request

for month in range(1,2):
    urllib.request.urlretrieve("https://s3.amazonaws.com/nyc-tlc/trip+data/"+ \
                               "yellow_tripdata_2019-{0:0=2d}.csv".format(month), 
                               "nyc.2019-{0:0=2d}.csv".format(month))

