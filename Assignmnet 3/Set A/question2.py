#2. A bookstore records these transactions:
#T1: {Book, Pen, Notebook}
#T2: {Book, Pen}
#T3: {Book, Notebook}
#T4: {Pen, Notebook}
#T5: {Book, Pen, Notebook}
#Find frequent itemsets with support ≥ 50%.
#Generate at least three association rules with confidence ≥ 60%.

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd


transactions = [
    ['Book', 'Pen', 'Notebook'],
    ['Book', 'Pen'],
    ['Book', 'Notebook'],
    ['Pen', 'Notebook'],
    ['Book', 'Pen', 'Notebook']
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