import pandas as pd
import matplotlib.pyplot as plt
import json

def load_data(file_path):
    return pd.read_csv(file_path)

def process_data(df):
    return df.describe()

def visualize_data(df):
    df.hist(figsize=(10, 8))
    plt.tight_layout()
    plt.show()

def export_to_json(df, output_path):
    df.to_json(output_path, orient='records', indent=4)

# Main driver
if __name__ == "__main__":
    try:
        data = load_data("data.csv")
        print(process_data(data))
        visualize_data(data)
        export_to_json(data, "output.json")
        print("Exported data to JSON.")
    except Exception as e:
        print("An error occurred:", e)
