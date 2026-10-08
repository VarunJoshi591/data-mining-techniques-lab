#1. A supermarket has the following transactions:
#T1: {Milk, Bread, Butter}
#T2: {Bread, Butter, Beer}
#T3: {Milk, Bread, Butter, Beer}
#T4: {Milk, Bread}
#T5: {Bread, Butter}
#Apply the Apriori algorithm with minimum support = 60% and minimum confidence = 70%.
#Find frequent itemsets and generate strong association rules.

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd


transactions = [
    ['Milk', 'Bread', 'Butter'],
    ['Bread', 'Butter', 'Beer'],
    ['Milk', 'Bread', 'Butter', 'Beer'],
    ['Milk', 'Bread'],
    ['Bread', 'Butter']
]

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

print("One-Hot Encoded Data:")
print(df)


frequent_itemsets = apriori(
    df,
    min_support=0.6,
    use_colnames=True
)

print("\nFrequent Itemsets:")
print(frequent_itemsets)


rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.7
)

print("\nStrong Association Rules:")
print(rules[
    ['antecedents', 'consequents',
     'support', 'confidence', 'lift']
])