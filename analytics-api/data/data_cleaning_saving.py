import pandas as pd
from pymongo import MongoClient

## Helper funcs & dicts
def helper_func_1(x):
  x=int(x)
  if x>=6 and x<12:
    return 'Morning'
  elif x>=12 and x<18:
    return 'Afternoon'
  elif x>=18 and x<24:
    return 'Evening'
  else:
    return 'Night'
  
def helper_func_2(x):
    x=int(x)
    if x >= 24:
        return '4th Week'
    elif x >= 16:
        return '3rd Week'
    elif x >= 8:
        return '2nd Week'
    else:
        return '1st Week'
  
month_dict={'01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'}

## -------Cleaner and Saver to Mongo Atlas----------
def data_cleaner_saver(file_path):
    df=pd.read_csv(file_path)
    # print(df.iloc[0,11])
    df['Time Slot']=df['Time'].str.split(':').str[0].apply(helper_func_1)
    df['Date'] = pd.to_datetime(df['Date'], format = '%m/%d/%Y')
    df['Month']=df['Date'].dt.strftime('%m')
    df['Date']=df['Date'].dt.strftime('%d')
    df['Month']=df['Month'].map(month_dict)
    df['Week of Month']=df['Date'].apply(helper_func_2)
    df.drop(columns=['Unnamed: 0','Invoice ID','Time','Date'],inplace=True)
    # print(df.head())
    return df