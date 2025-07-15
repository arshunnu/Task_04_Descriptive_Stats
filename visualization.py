import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('C:/Users/Arshunnu Bare/Desktop/SEM4/period/2024_fb_ads_president_scored_anon.csv')


plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
sns.histplot(dataset['estimated_spend'], kde=True, color='skyblue', bins=30)
plt.title('Distribution of Estimated Spend')
plt.xlabel('Estimated Spend')
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)
sns.boxplot(x=dataset['estimated_audience_size'], color='lightgreen')
plt.title('Boxplot of Estimated Audience Size')
plt.xlabel('Estimated Audience Size')

plt.subplot(2, 2, 3)
platforms_count = dataset['publisher_platforms'].value_counts()
sns.barplot(x=platforms_count.index, y=platforms_count.values, palette='viridis')
plt.title('Performance by Publisher Platform')
plt.xlabel('Publisher Platform')
plt.ylabel('Number of Ads')
plt.xticks(rotation=45)


plt.tight_layout()
plt.show()
