import csv

filenames = [
    'C:/Users/Arshunnu Bare/Desktop/SEM4/period/2024_fb_ads_president_scored_anon.csv',
    'C:/Users/Arshunnu Bare/Desktop/SEM4/period/2024_fb_posts_president_scored_anon.csv',
    'C:/Users/Arshunnu Bare/Desktop/SEM4/period/2024_tw_posts_president_scored_anon.csv'
]

def load_dataset(file_path):
    """Load dataset from a CSV file and return a list of rows as dictionaries."""
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

datasets = {}
for index, filename in enumerate(filenames, 1):
    dataset = load_dataset(filename)
    datasets[filename] = dataset

    print(f"Dataset {index}: {filename}")
    for row in dataset[:5]:
        print(row)
    print("\n" + "-"*80 + "\n")
import math
from collections import Counter
import csv

def load_dataset(file_path):
    """Load dataset from a CSV file and return a list of rows as dictionaries."""
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def calculate_descriptive_stats(dataset):
    """Calculate descriptive stats for the dataset."""
    stats = {}

    columns = dataset[0].keys()

    for column in columns:
        numeric_values = []
        categorical_values = []

        for row in dataset:
            value = row[column]
            if value != '':  
                try:
                    numeric_values.append(float(value))  
                except ValueError:
                    categorical_values.append(value)  

        if numeric_values:
            count = len(numeric_values)
            mean = sum(numeric_values) / count
            min_value = min(numeric_values)
            max_value = max(numeric_values)
            std_dev = math.sqrt(sum((x - mean) ** 2 for x in numeric_values) / count)
            stats[column] = {
                'count': count,
                'mean': mean,
                'min': min_value,
                'max': max_value,
                'std_dev': std_dev
            }

        elif categorical_values:
            unique_values = set(categorical_values)
            most_common_value, most_common_count = Counter(categorical_values).most_common(1)[0]
            stats[column] = {
                'count': len(categorical_values),
                'unique_values': len(unique_values),
                'most_common_value': most_common_value,
                'most_common_count': most_common_count
            }
    
    return stats

filenames = [
    'C:/Users/Arshunnu Bare/Desktop/SEM4/period/2024_fb_ads_president_scored_anon.csv',
    'C:/Users/Arshunnu Bare/Desktop/SEM4/period/2024_fb_posts_president_scored_anon.csv',
    'C:/Users/Arshunnu Bare/Desktop/SEM4/period/2024_tw_posts_president_scored_anon.csv'
]

for index, filename in enumerate(filenames, 1):
    print(f"Processing Dataset {index}: {filename}")
    
    dataset = load_dataset(filename)

    stats = calculate_descriptive_stats(dataset)

    print("Descriptive Stats for the Dataset (Overall):")
    for column, stat in stats.items():
        print(f"Stats for {column}:")
        for key, value in stat.items():
            print(f"  {key}: {value}")
        print("-" * 40)

    print("=" * 80)  
