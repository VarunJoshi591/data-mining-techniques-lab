#2.Collect a small dataset of 10–15 transactions from your surroundings (e.g., students buying 
#snacks in a canteen).
#Apply the Apriori algorithm to find frequent combinations.
#Interpret rules in simple words (e.g., “If students buy Samosa → they also buy Tea”)

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

transactions = [
    ['Samosa', 'Tea'],
    ['Samosa', 'Tea', 'Vada'],
    ['Samosa', 'Tea'],
    ['Vada', 'Tea'],
    ['Samosa', 'Tea', 'Vada'],
    ['Samosa', 'ColdDrink'],
    ['Vada', 'Tea'],
    ['Samosa', 'Tea'],
    ['Samosa', 'Tea', 'Vada'],
    ['Vada', 'ColdDrink']
]


te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

print("One-Hot Encoded Data:")
print(df)


frequent_itemsets = apriori(
    df,
    min_support=0.5,
    use_colnames=True
)

print("\nFrequent Itemsets:")
print(frequent_itemsets)


rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.6
)

print("\nAssociation Rules:")
print(rules[
    ['antecedents', 'consequents',
     'support', 'confidence', 'lift']
])