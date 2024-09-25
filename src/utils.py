import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def summary_statistics(data):
    return data.describe()

def plot_distribution(data, column):
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

def correlation_heatmap(data):
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()
