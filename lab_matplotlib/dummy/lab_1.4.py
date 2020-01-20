import matplotlib.pyplot as plt
import seaborn as sns

# Load data
titanic = sns.load_dataset("titanic")

sns.countplot(x="class", data=titanic)
plt.title("number of people by class")

#sns.barplot(x="class", y="survived", hue="sex", data=titanic)
#plt.title("survived percent by class, sex")

plt.show()