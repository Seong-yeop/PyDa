import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')
monthList = df['month_number'].tolist()
facecream = df['facecream'].tolist()
facewash = df['facewash'].tolist()
toothpaste = df['toothpaste'].tolist()
bathingsoap = df['bathingsoap'].tolist()
shampoo = df['shampoo'].tolist()
moisturizer = df['moisturizer'].tolist()

#plt.plot(monthList, facecream,   label = 'Face cream', marker='o', linewidth=2)

plt.plot(df['month_number'], df['facecream'],
         label='Face cream', marker='o', linewidth=2)
plt.plot(monthList, facewash,   label='Face Wash',  marker='o', linewidth=2)
plt.plot(monthList, toothpaste, label='ToothPaste', marker='o', linewidth=2)
plt.plot(monthList, bathingsoap, label='bathingsoap', marker='o', linewidth=2)
plt.plot(monthList, shampoo, label='shampoo', marker='o', linewidth=2)
plt.plot(monthList, moisturizer, label='moisturizer', marker='o', linewidth=2)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales data')

plt.show()
