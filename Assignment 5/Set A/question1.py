#Read the dataset (employee.csv) containing employee names and their salaries. Apply 
#K-Means clustering with k=2 to group employees into Low Salary and High Salary 
#categories. Display the cluster centers and the group assignment of each employee.
#Input (employee.csv):
#Name,Salary
#John,40000
#Alice,35000
#Bob,60000
#Eve,90000
#Sam,80000



import pandas as pd
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv(
    r"C:\Users\VARUN-LAP\OneDrive\Dokumen\employee.csv"
)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Check dataset columns
print("Columns:", df.columns.tolist())
print(df.head())

# Select salary column
X = df[['Salary']]

# Apply K-Means clustering
kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
kmeans.fit(X)

# Display cluster centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# Assign clusters
df['Cluster'] = kmeans.labels_

# Identify low and high salary clusters
centers = kmeans.cluster_centers_.flatten()
low_cluster = centers.argmin()
high_cluster = centers.argmax()

df['Category'] = df['Cluster'].map({
    low_cluster: 'Low Salary',
    high_cluster: 'High Salary'
})

# Display employee groups
print("\nEmployee Salary Groups:")
print(df[['Name', 'Salary', 'Category']])
