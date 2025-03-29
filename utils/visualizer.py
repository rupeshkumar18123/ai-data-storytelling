<<<<<<< HEAD
=======
import seaborn as sns
import matplotlib.pyplot as plt

def plot_revenue_trends(df):
    plt.figure(figsize=(10,5))
    sns.lineplot(x='Date', y='Revenue', data=df)
    plt.title("Revenue Trends Over Time")
    return plt
>>>>>>> 9c09285269c4bc97d3d7f6e26f5008d06be67bd1

