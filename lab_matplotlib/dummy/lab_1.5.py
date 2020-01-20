import matplotlib.pyplot as plt
import seaborn as sns

# Load data
titanic = sns.load_dataset("titanic")

sns.barplot(x="class", y="survived", hue="sex", data=titanic)
#sns.countplot(x="class", hue="survived", data=titanic)

plt.title("survived percent by class, sex")

print(titanic)

plt.show()