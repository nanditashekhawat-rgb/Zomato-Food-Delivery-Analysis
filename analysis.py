import pandas as pd

df = pd.read_csv("zomato.csv", encoding="latin-1")

# -------- CLEANING --------

# Remove "/5" from rate column
df['rate'] = df['rate'].astype(str).str.replace('/5', '', regex=False)

# Replace 'NEW' and '-' with NaN
df['rate'] = df['rate'].replace(['NEW', '-'], None)

# Convert to numeric
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

# Drop rows where rating is not available
df = df.dropna(subset=['rate'])

print("Cleaned Data Sample:")
print(df.head())


# ------------ BASIC EDA -------------

print("\n1️⃣ TOP 10 CUISINES")
top_cuisines = df['cuisines'].value_counts().head(10)
print(top_cuisines)

print("\n2️⃣ TOP 10 RESTAURANT TYPES")
top_rest_types = df['rest_type'].value_counts().head(10)
print(top_rest_types)

print("\n3️⃣ AVERAGE RATING BY LOCATION (Top 10)")
location_rating = df.groupby('location')['rate'].mean().sort_values(ascending=False).head(10)
print(location_rating)

print("\n4️⃣ DOES ONLINE ORDERING AFFECT RATINGS?")
online_rating = df.groupby('online_order')['rate'].mean()
print(online_rating)

print("\n5️⃣ AVERAGE COST FOR TWO PEOPLE")
avg_cost = df['approx_cost(for two people)'].replace(',', '', regex=True).astype(float).mean()
print("Average cost for two people:", avg_cost)


import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# 1️⃣ TOP 10 CUISINES BAR CHART
plt.figure(figsize=(10,5))
top_cuisines.plot(kind='bar')
plt.title("Top 10 Cuisines")
plt.ylabel("Count of Restaurants")
plt.xlabel("Cuisine")
plt.xticks(rotation=45)
plt.show()

# 2️⃣ TOP 10 RESTAURANT TYPES BAR CHART
plt.figure(figsize=(10,5))
top_rest_types.plot(kind='bar', color='orange')
plt.title("Top 10 Restaurant Types")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 3️⃣ AVERAGE RATING BY LOCATION (TOP 10)
plt.figure(figsize=(10,5))
location_rating.plot(kind='bar', color='green')
plt.title("Top Rated Locations")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.show()

# 4️⃣ ONLINE ORDER VS RATING
plt.figure(figsize=(5,5))
online_rating.plot(kind='bar', color=['red', 'blue'])
plt.title("Online Order vs Average Rating")
plt.ylabel("Average Rating")
plt.xticks(rotation=0)
plt.show()

# 5️⃣ PRICE DISTRIBUTION
plt.figure(figsize=(7,5))
sns.histplot(df['approx_cost(for two people)'].replace(',', '', regex=True).astype(float),
             bins=30, kde=True)
plt.title("Distribution of Cost for Two People")
plt.xlabel("Cost for Two")
plt.ylabel("Frequency")
plt.show()


print("\n================ BUSINESS INSIGHTS ================\n")

print("1. North Indian and Chinese cuisines dominate the Bengaluru market.")
print("- 'North Indian' alone has 2158 restaurants.")
print("- Fusion cuisines (North Indian + Chinese) are extremely popular.")

print("\n2. Quick Bites and Casual Dining are the most successful restaurant formats.")
print("- Quick Bites: 13,944 restaurants")
print("- Casual Dining: 9,659 restaurants")
print("This suggests a preference for affordable and fast options.")

print("\n3. Lavelle Road and Koramangala are the highest-rated locations.")
print("- Lavelle Road has an average rating of 4.14")
print("- These areas may have better quality restaurants.")

print("\n4. Customers prefer restaurants that offer online ordering.")
print("- Average rating (online_order=Yes): 3.72")
print("- Average rating (online_order=No): 3.65")
print("This means offering online delivery improves customer satisfaction.")

print("\n5. Average cost for two is around ₹600.")
print("This indicates Bengaluru has a mid-range food pricing structure.")

print("\n====================================================\n")
