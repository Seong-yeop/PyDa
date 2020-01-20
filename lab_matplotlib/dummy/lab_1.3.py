import matplotlib.pyplot as plt
import pandas_datareader.data as web
from mpl_finance import candlestick2_ohlc
import matplotlib.ticker as ticker
import datetime

start = datetime.datetime(2019,6,1)
end = datetime.datetime(2019,12,31)
lg = web.DataReader("066570.KS", "yahoo", start, end)
index = lg.index.astype('str')

ma5 = lg['Close'].rolling(window=5).mean()  
ma20 = lg['Close'].rolling(window=20).mean()

fig = plt.figure(figsize=(12, 8))
top = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
bottom = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)

def mydate(x,pos):
    try:
        return index[int(x-0.5)][:7]
    except IndexError:
        return ''

top.xaxis.set_major_locator(ticker.MaxNLocator(10))
top.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
candlestick2_ohlc(top,lg['Open'],lg['High'],lg['Low'],lg['Close'],width=0.5)
top.plot(index,ma5, label='ma5')
top.plot(index,ma20, label='ma20')
top.legend()
top.set_title('LG Sotck Price')

bottom.plot(index, lg['Volume'])
bottom.xaxis.set_major_locator(ticker.MaxNLocator(10))

top.grid()
bottom.grid()
plt.savefig("fig.png")
plt.show()