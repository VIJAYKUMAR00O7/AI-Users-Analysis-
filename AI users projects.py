import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
data = pd.read_csv(r'C:\Users\Vijay\OneDrive\Desktop\Data stream\simulated_ai_user_data.csv')


# Regional Usage Trends
region_counts = data['region'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=region_counts.index, y=region_counts.values)
plt.title('Regional Usage Trends')
plt.xlabel('Region')
plt.ylabel('Number of Interactions')
plt.show()#

 # Peak Interaction Times
data['hour'] = pd.to_datetime(data['timestamp']).dt.hour
plt.figure(figsize=(10, 6))
sns.histplot(data['hour'], bins=24, kde=True)
plt.title('Global Interaction Patterns by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Interactions')
plt.show()#

# User Retention Rates
unique_users_daily = data.groupby(data['timestamp'].str[:10])['user_id'].nunique()
plt.figure(figsize=(10, 6))
unique_users_daily.plot()
plt.title('Daily Unique Users (Retention Analysis)')
plt.xlabel('Date')
plt.ylabel('Number of Unique Users')
plt.show()

# Response Time Analysis
plt.figure(figsize=(10, 6))
sns.boxplot(data['response_time'])
plt.title('Response Time Distribution')
plt.xlabel('Response Time (seconds)')
plt.show()
