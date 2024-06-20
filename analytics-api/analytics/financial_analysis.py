import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_finance_img_1(df):
    fig = plt.figure(figsize=(5,7))
    ax = sns.barplot(x="Suburb", y="Total amount with Tax", color='green',saturation=0.5, data=df, errorbar=None, estimator=sum, label='Total Revenue')
    ax = sns.barplot(x="Suburb", y="cogs", color='black', saturation=0.2, data=df, errorbar=None, estimator=sum, label='Cost of goods')
    ax = sns.barplot(x="Suburb", y="gross profit", color='lime', saturation=0.5, data=df, errorbar=None, estimator=sum, label='Gross Profit')
    ax.set(xlabel="Suburbs", ylabel="Financial Parameters")
    plt.legend(loc=1)
    fig.savefig('.././Main-Project/backend/public/images/financials/financials.png') #Ideally store to AWS s3
    plt.close(fig)