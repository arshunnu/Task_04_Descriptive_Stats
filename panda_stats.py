import pandas as pd

def load_dataset_pandas(file_path):
    """Load dataset from a CSV file using pandas."""
    return pd.read_csv(file_path)

def calculate_descriptive_stats_pandas(dataset):
    """Calculate descriptive stats for the dataset using pandas."""
    stats = {}

    numeric_stats = dataset.describe().T  
    
    stats['numeric'] = numeric_stats

    categorical_stats = {}
    for column in dataset.select_dtypes(include=['object']).columns:
        value_counts = dataset[column].value_counts()
        most_common_value = value_counts.idxmax()
        most_common_count = value_counts.max()
        unique_values = dataset[column].nunique() 

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
    
    dataset = load_dataset_pandas(filename)

    stats = calculate_descriptive_stats_pandas(dataset)

    print("Numeric Descriptive Stats:")
    print(stats['numeric'])
    
    print("\nCategorical Descriptive Stats:")
    for column, stat in stats['categorical'].items():
        print(f"Stats for {column}:")
        for key, value in stat.items():
            print(f"  {key}: {value}")
        print("-" * 40)

    print("=" * 80) 
