import matplotlib.pyplot as plt
import seaborn as sns


titanic = sns.load_dataset("titanic")


cols = ['survived', 'sex', 'pclass', 'sibsp', 'parch', 'embarked']
nr_rows = 2
nr_cols = 3

fig, axs = plt.subplots(nr_rows, nr_cols, figsize=(nr_cols*3.5,nr_rows*3))

for r in range(0,nr_rows):
    for c in range(0,nr_cols):  
        i = r*nr_cols+c       
        ax = axs[r][c]
        sns.countplot(titanic[cols[i]], hue=titanic["survived"], ax=ax)
        ax.set_title(cols[i], fontsize=14, fontweight='bold')
        ax.legend(title="survived", loc='upper center') 
        
plt.tight_layout()  
plt.show()