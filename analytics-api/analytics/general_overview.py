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

def gen_overview_2(df):
    df=pd.concat([df.groupby(['Product line'])[['Quantity','cogs']].sum().reset_index(),df.groupby(['Product line'])[['gross margin percentage']].mean().reset_index()],axis=1)
    df = df.loc[:, ~df.columns.duplicated(keep='first')]
    df=df.rename(columns={'Product line':'Product','gross margin percentage':'gmp'})
    df['gmp']=df['gmp'].round(2)

    df['cogs']=df['cogs'].astype(int)

    df['cogs']=df['cogs'].apply(lambda x: '{:,.2f}'.format(x))

    return df.to_json(orient='records')

def gen_overview_img(df):
    fig = plt.figure(figsize=(4,6))
    ax=sns.countplot(x='Customer type',hue='Suburb',palette=['#89CFF0', '#6CB4EE', '#002D62'],data=df)
    ax.set(xlabel="Customer Type", ylabel="Count")
    plt.legend(loc=8)
    fig.savefig('.././Main-Project/backend/public/images/general/general_1.png') #Ideally store to AWS s3
    plt.close(fig)
    


    