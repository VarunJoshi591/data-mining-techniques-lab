#.A supermarket provides Groceries_dataset.csv containing customer transactions 
#(Member_number and itemDescription).
#(Member_number and itemDescription).
#2. Apply Apriori with min support = 0.05 to find frequent itemsets.
#3. Generate association rules with min confidence = 0.6.
#4. Display the top 5 rules with antecedents, consequents, support, confidence, and lift

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_csv("d:\Users\VARUN-LAP\Downloads\groceries - groceries.csv")

print("Dataset:")
print(df.head())

transactions = df.groupby('Member_number')['itemDescription'].apply(list).values

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_onehot = pd.DataFrame(te_ary, columns=te.columns_)

print("\nOne-Hot Encoded Data:")
print(df_onehot.head())

frequent_itemsets = apriori(
    df_onehot,
    min_support=0.05,
    use_colnames=True
)

print("\nFrequent Itemsets:")
print(frequent_itemsets)


rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.6
)


rules = rules.sort_values(
    'confidence',
    ascending=False
)


print("\nTop 5 Association Rules:")

print(
    rules[
        ['antecedents',
         'consequents',
         'support',
         'confidence',
         'lift']
    ].head(5)
)