<<<<<<< HEAD
=======
import pandas as pd

def clean_data(df):
    df = df.dropna()
    df.columns = df.columns.str.strip().str.lower()
    return df
>>>>>>> 9c09285269c4bc97d3d7f6e26f5008d06be67bd1
 
