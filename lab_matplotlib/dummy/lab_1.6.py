import matplotlib.pyplot as plt
import seaborn as sns

# Load data
titanic = sns.load_dataset("titanic")

f, ax = plt.subplots(1,2,figsize=(12,8))
sns.violinplot(x='pclass', y='age', hue='survived',scale='count',split=True,data=titanic,ax=ax[0])
ax[0].set_yticks(range(0,110,10))

sns.violinplot(x='sex', y='age', hue='survived',scale='count',split=True, data=titanic, ax=ax[1])
ax[1].set_yticks(range(0,110,10))

plt.show()