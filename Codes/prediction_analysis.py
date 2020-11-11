import warnings; warnings.simplefilter("ignore")
import matplotlib.pyplot as plt
%matplotlib inline 
import seaborn as sns 
import numpy as np
import pandas as pd 
from datetime import date 
from datetime import time
from datetime import datetime
from matplotlib import pyplot 
import seaborn
from statsmodels.tsa.api import ExponentialSmoothing
from scipy import stats
data = pd.ExcelFile(r"/Users/moussa.garba/Desktop/Disk_2.xlsx")
#data = pd.read_excel(r"/Users/moussa.garba/Desktop/Disk_2.xlsx",index_col="date", sheetname=0)
data = pd.read_excel(r"/Users/moussa.garba/Desktop/Disk_2.xlsx",sheetname=0, )
#data = pd.read_excel(r"/Users/moussa.garba/Desktop/Disk_2.xlsx", sheetname=0)
data = data.rename(columns ={'date': 'Date', 'CPU Load_Avg': 'CPU_Load_Avg', 'CPU Load_Min': 'CPU_Load_Min', 'CPU Load_Max': 'CPU_Load_Max'})
data.index = data['Date']


data.head()


data.CPU_Load_Avg.plot()


#data.CPU_Load_Avg.scaller()
import plotly.plotly as py 
import plotly.graph_objs as go


#data1 = [go.Scatter(x=data.Date, y=data['CPU_Load_Avg'])]
#py.iplot(data1)

data = data.replace(-np.inf, np.nan)
data = data.fillna(data.bfill())


plt.figure(figsize=(50, 15))
plt.plot(data.CPU_Load_Avg)
plt.title('CPU_Load_Avg')

plt.figure(figsize=(50, 15))
plt.plot(data.CPU_Load_Min)
plt.title('CPU_Load_Min')

plt.figure(figsize=(50, 15))
plt.plot(data.CPU_Load_Max)
plt.title('CPU_Load_Max')


df_mean = pd.DataFrame(data.groupby(['Date'])['CPU_Load_Avg'].mean())
df_mean.columns = ['mean']
df_median = pd.DataFrame(data.groupby(['Date'])['CPU_Load_Avg'].median())
df_median.columns = ['median']
data = data.set_index('Date').join(df_mean).join(df_median)
data.reset_index(drop=False,inplace=True)


df_mean_Max = pd.DataFrame(data.groupby(['Date'])['CPU_Load_Max'].mean())
df_mean_Max.columns = ['mean_Max']

df_median_Max = pd.DataFrame(data.groupby(['Date'])['CPU_Load_Max'].median())
df_median_Max.columns = ['median_Max']

data = data.set_index('Date').join(df_mean_Max).join(df_median_Max)
data.reset_index(drop=False,inplace=True)



df_mean_Min = pd.DataFrame(data.groupby(['Date'])['CPU_Load_Min'].mean())
df_mean_Min.columns = ['mean_Min']

df_median_Min = pd.DataFrame(data.groupby(['Date'])['CPU_Load_Min'].median())
df_median_Min.columns = ['median_Min']

data = data.set_index('Date').join(df_mean_Min).join(df_median_Min)
data.reset_index(drop=False,inplace=True)


plt.figure(figsize=(50, 8))
mean_group = data[['Date','CPU_Load_Avg','CPU_Load_Min','CPU_Load_Max']].groupby(['Date'])['CPU_Load_Avg'].mean()
plt.plot(mean_group)
plt.title('Time Series - Average')

data['weekday'] = data['Date'].apply(lambda x: x.weekday())
data['year']=data.Date.dt.year 
data['month']=data.Date.dt.month 
data['day']=data.Date.dt.day

plt.figure(figsize=(50, 10))
mean_group = data[['Date','CPU_Load_Avg']].groupby(['Date'])['CPU_Load_Avg'].mean()
plt.plot(mean_group)
plt.title('CPU_Load_Avg')


plt.figure(figsize=(50, 10))
mean_group = data[['Date','CPU_Load_Max']].groupby(['Date'])['CPU_Load_Max'].mean()
plt.plot(mean_group)
plt.title('CPU_Load_Max')

plt.figure(figsize=(50, 10))
mean_group = data[['Date','CPU_Load_Min']].groupby(['Date'])['CPU_Load_Min'].mean()
plt.plot(mean_group)
plt.title('CPU_Load_Min')

data['month_num'] = data['month']
data['month'].replace('01','01 - Janvier',inplace=True)
data['month'].replace('02','02 - Février',inplace=True)
data['month'].replace('03','03 - Mars',inplace=True)
data['month'].replace('04','04 - Avril',inplace=True)
data['month'].replace('05','05 - Mai',inplace=True)
data['month'].replace('06','06 - Juin',inplace=True)
data['month'].replace('07','07 - Juillet',inplace=True)
data['month'].replace('08','08 - Août',inplace=True)
data['month'].replace('09','09 - Septembre',inplace=True)
data['month'].replace('10','10 - Octobre',inplace=True)
data['month'].replace('11','11 - Novembre',inplace=True)
data['month'].replace('12','12 - Décembre',inplace=True)

data['weekday_num'] = data['weekday']
data['weekday'].replace(0,'01 - Lundi',inplace=True)
data['weekday'].replace(1,'02 - Mardi',inplace=True)
data['weekday'].replace(2,'03 - Mercredi',inplace=True)
data['weekday'].replace(3,'04 - Jeudi',inplace=True)
data['weekday'].replace(4,'05 - Vendredi',inplace=True)
data['weekday'].replace(5,'06 - Samedi',inplace=True)
data['weekday'].replace(6,'07 - Dimanche',inplace=True)



data_group_Avg = data.groupby(["month", "weekday"])['CPU_Load_Avg'].mean().reset_index()
data_group_Avg = data.groupby(["month", "weekday"])['CPU_Load_Avg'].mean().reset_index()
data_group_Avg = data_group_Avg.pivot('weekday','month','CPU_Load_Avg')
data_group_Avg.sort_index(inplace=True)

data_group_Max = data.groupby(["month", "weekday"])['CPU_Load_Max'].mean().reset_index()
data_group_Max = data.groupby(["month", "weekday"])['CPU_Load_Max'].mean().reset_index()
data_group_Max = data_group_Max.pivot('weekday','month','CPU_Load_Max')
data_group_Max.sort_index(inplace=True)


data_group_Min = data.groupby(["month", "weekday"])['CPU_Load_Min'].mean().reset_index()
data_group_Min = data.groupby(["month", "weekday"])['CPU_Load_Min'].mean().reset_index()
data_group_Min = data_group_Min.pivot('weekday','month','CPU_Load_Min')
data_group_Min.sort_index(inplace=True)

f, ax = plt.subplots(figsize=(50, 25))
sns.heatmap(data_group_Avg, annot=False, ax=ax, fmt="d",  linewidths=5)
plt.title('CPU_Load_Avg Months cross Weekdays')

f, ax = plt.subplots(figsize=(50, 25))
sns.heatmap(data_group_Max, annot=False, ax=ax, fmt="d",  linewidths=5)
plt.title('CPU_Load_Max Months cross Weekdays')

f, ax = plt.subplots(figsize=(50, 25))
sns.heatmap(data_group_Min, annot=False, ax=ax, fmt="d",  linewidths=5)
plt.title('CPU_Load_Min Months cross Weekdays')

times_series_means = pd.DataFrame(mean_group).reset_index(drop=False)
times_series_means['weekday'] = times_series_means['Date'].apply(lambda x: x.weekday())
times_series_means['Date_str'] = times_series_means['Date'].apply(lambda x: str(x))
times_series_means[['year', 'month', 'day']] = pd.DataFrame(times_series_means['Date_str'].str.split('-', 2).tolist(), columns = ['year', 'month', 'day'])
date_staging = pd.DataFrame(times_series_means['day'].str.split(' ', 2).tolist(), columns = ['day', 'other'])
times_series_means['day'] = date_staging['day']*1
times_series_means.drop('Date_str', axis = 1 , inplace =True)


times_series_means.head()

times_series_mea = pd.DataFrame(mean_group).reset_index(drop=False)
times_series_means['weekday'] = times_series_means['Date'].apply(lambda x: x.weekday())
times_series_means['Date_str'] = times_series_means['Date'].apply(lambda x: str(x))
times_series_means[['year', 'month', 'day']] = pd.DataFrame(times_series_means['Date_str'].str.split('-', 2).tolist(), columns = ['year', 'month', 'day'])
date_staging = pd.DataFrame(times_series_means['day'].str.split(' ', 2).tolist(), columns = ['day', 'other'])
times_series_means['day'] = date_staging['day']*1
times_series_means.drop('Date_str', axis = 1 , inplace =True)











