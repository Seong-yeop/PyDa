import pandas_datareader.data as web
import matplotlib.pyplot as plt

lg = web.DataReader("066570.KS", "yahoo")
samsung = web.DataReader("005930.KS", "yahoo")

print(lg)
print(lg.index)
print(lg['Adj Close'])

plt.plot(lg['Adj Close'], label='LG Electronics')
plt.plot(samsung['Adj Close'], label='Samsung Electronics')

plt.legend()
plt.show()
