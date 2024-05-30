import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce

# Load data
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(url, sep='|')

# Function to select relevant columns
def select_columns(df, columns):
    return df[columns]

# Define the columns we need
columns = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users_cleaned = select_columns(users, columns)

# Function to filter users by age
def filter_by_age(df, min_age, max_age):
    return df[(df['age'] >= min_age) & (df['age'] <= max_age)]

# Filter users between ages 20 and 30
users_filtered = filter_by_age(users_cleaned, 20, 30)

# Function to compute average age
def average_age(df):
    return df['age'].mean()

# Compute average age of filtered users
avg_age = average_age(users_filtered)
print(f'Average age: {avg_age}')

# Function to count occupations
def count_occupations(df):
    return df['occupation'].value_counts()

# Get occupation counts
occupation_counts = count_occupations(users_filtered)

# Plot the results
occupation_counts.plot(kind='bar')
plt.xlabel('Occupation')
plt.ylabel('Count')
plt.title('Occupation Distribution for Users Aged 20-30')
plt.show()
