import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def gen_overview_1(df):
    df = pd.concat([df.groupby('Suburb')[['Total amount with Tax','Tax 5%', 'net profit']].sum().reset_index(), df.groupby('Suburb')['Customer Rating'].mean().reset_index()], axis=1)
    df = df.loc[:, ~df.columns.duplicated(keep='first')]
    df=df.rename(columns={'Total amount with Tax':'TotalAmountWithTax','Tax 5%':'Tax','net profit':'NetProfit','Customer Rating':'CustomerRating'})
    df['CustomerRating'] = df['CustomerRating'].round(2)
    
    df['TotalAmountWithTax']=df['TotalAmountWithTax'].astype(int)
    df['Tax']=df['Tax'].astype(int)
    df['NetProfit']=df['NetProfit'].astype(int)

    df['TotalAmountWithTax']=df['TotalAmountWithTax'].apply(lambda x: '{:,.2f}'.format(x))
    df['Tax']=df['Tax'].apply(lambda x: '{:,.2f}'.format(x))
    df['NetProfit']=df['NetProfit'].apply(lambda x: '{:,.2f}'.format(x))
    
    return df.to_json(orient='records')
    


    