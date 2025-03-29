import seaborn as sns
import matplotlib.pyplot as plt

def plot_revenue_trends(df):
    plt.figure(figsize=(10,5))
    sns.lineplot(x='Date', y='Revenue', data=df)
    plt.title("Revenue Trends Over Time")
    return plt

