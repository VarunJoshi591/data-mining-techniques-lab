#1. File: bookstore.csv
#TransactionID,Items
#1,"Book,Pen,Notebook"
#2,"Book,Pen"
#3,"Book,Notebook"
#4,"Pen,Notebook"
#5,"Book,Pen,Notebook"
#Import this CSV file into Python.
#Apply Apriori with minimum support = 40%, confidence = 60%.
#Generate at least 3 strong rules.

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules 

df = pd.read_csv("C:\\Users\\VARUN-LAP\\OneDrive\\Dokumen\\bookstore.csv")

transaction = df['Items'].apply(lambda x: x.split(','))

te = TransactionEncoder()
te_ary = te.fit(transaction).transform(transaction)
df_onhot = pd.DataFrame(te_ary, columns=te.columns_)

print("One-Hot Encoded Data:")
print(df_onhot)

frequent_itemsets = apriori(
    df_onhot,
    min_support=0.4,
    use_colnames=True
)

print("\nFrequent Itemsets:")
print(frequent_itemsets)

rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.6
)

strong_rules = rules.sort_values(
    'confidence',
    ascending=False
)

print("\nStrong Association Rules:")
print(strong_rules[
    ['antecedents', 'consequents',
     'support', 'confidence', 'lift']
].head(3))
