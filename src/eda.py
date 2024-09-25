from utils import load_data, summary_statistics, plot_distribution, correlation_heatmap

data = load_data('data/dataset.csv')
print(summary_statistics(data))
plot_distribution(data, 'feature_column')
correlation_heatmap(data)
