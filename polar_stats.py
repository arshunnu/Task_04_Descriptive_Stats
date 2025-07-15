import polars as pl
import math
from collections import Counter

def load_dataset_polars(file_path):
    """Load dataset from a CSV file using Polars."""
    return pl.read_csv(file_path)

def calculate_descriptive_stats_polars(dataset):
    """Calculate descriptive stats for the dataset using Polars."""
    stats = {}

    numeric_columns = dataset.select(pl.col(pl.Float64)).columns
    for column in numeric_columns:
        numeric_values = dataset[column].drop_nulls().to_list() 

        count = len(numeric_values)
        if count > 0:
            mean = sum(numeric_values) / count
            min_value = min(numeric_values)
            max_value = max(numeric_values)
            std_dev = math.sqrt(sum((x - mean) ** 2 for x in numeric_values) / count)
        else:
            mean = min_value = max_value = std_dev = None

        stats[column] = {
            'count': count,
            'mean': mean,
            'min': min_value,
            'max': max_value,
            'std_dev': std_dev
        }

    categorical_columns = dataset.select(pl.col(pl.Utf8)).columns
    categorical_stats = {}
    for column in categorical_columns:
        value_counts = dataset[column].value_counts()
        most_common_value = value_counts[0, 'count']
        most_common_count = value_counts[0, 'count']
        unique_values = len(value_counts)

        categorical_stats[column] = {
            'count': dataset[column].count(),
            'unique_values': unique_values,
            'most_common_value': most_common_value,
            'most_common_count': most_common_count
        }

    stats['categorical'] = categorical_stats
    return stats

filenames = [
    'C:/Users/Arshunnu Bare/Desktop/SEM4/period/2024_fb_ads_president_scored_anon.csv',
    'C:/Users/Arshunnu Bare/Desktop/SEM4/period/2024_fb_posts_president_scored_anon.csv',
    'C:/Users/Arshunnu Bare/Desktop/SEM4/period/2024_tw_posts_president_scored_anon.csv'
]

for index, filename in enumerate(filenames, 1):
    print(f"Processing Dataset {index}: {filename}")
    
    dataset = load_dataset_polars(filename)

    stats = calculate_descriptive_stats_polars(dataset)

    print("Numeric Descriptive Stats:")
    for column, stat in stats.items():
        if column != 'categorical':
            print(f"Stats for {column}:")
            for key, value in stat.items():
                print(f"  {key}: {value}")
            print("-" * 40)
    
    print("\nCategorical Descriptive Stats:")
    for column, stat in stats['categorical'].items():
        print(f"Stats for {column}:")
        for key, value in stat.items():
            print(f"  {key}: {value}")
        print("-" * 40)

    print("=" * 80)  
