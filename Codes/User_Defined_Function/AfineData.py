import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
%matplotlib inline
DataAfine = pd.ExcelFile(r"/Users/moussa.garba/Desktop/DataManager/DataAfine.xlsx")
Data1.head(2)
Data1.plot(x="Date", y=["Disk_Free_Space_Avg", "Disk_Free_Space_Min", "Disk_Free_Space_Max"], figsize=(16,5))
Data1.index = Data1['Date']
Data1['2017-06-22'].head(1)
Data1['Disk_Free_Space_Max'].plot()
data = pd.read_excel('/Users/moussa.garba/Desktop/DataAfine.xlsx', parse_dates=['Date'], index_col='Date')
Disk_Free_Space_Avg = data['Disk_Free_Space_Avg']
Disk_Free_Space_Avg.head(10)
Disk_Free_Space_Avg_2017_06_22 = data['2017-06-22']
Disk_Free_Space_Avg_2017_06_22.head(5)
plt.plot(Disk_Free_Space_Avg_2017_06_22)

Disk_Free_Space_Avg_2017_06_24 = data['2017-06-24']
Disk_Free_Space_Avg_2017_06_24.head(2)
plt.plot(Disk_Free_Space_Avg_2017_06_24)

Disk_Free_Space_Avg_2018_05_20 = data['2018-05-20']
Disk_Free_Space_Avg_2018_05_20.head(2)
plt.plot(Disk_Free_Space_Avg_2018_05_20)


Disk_Free_Space_Avg_2018_06_11 = data['2018-06-11']
Disk_Free_Space_Avg_2018_06_11.head(2)
plt.plot(Disk_Free_Space_Avg_2018_06_11)


Disk_Free_Space_Avg_2018_06_01 = data['2018-06-01']
Disk_Free_Space_Avg_2018_06_01.head(2)
plt.plot(Disk_Free_Space_Avg_2018_06_01)

Disk_Free_Space_Avg_2018_06_02 = data['2018-06-02']
Disk_Free_Space_Avg_2018_06_02.head(2)
plt.plot(Disk_Free_Space_Avg_2018_06_02)


Disk_Free_Space_Avg_2018_06_03 = data['2018-06-03']
Disk_Free_Space_Avg_2018_06_03.head(2)
plt.plot(Disk_Free_Space_Avg_2018_06_03)



Disk_Free_Space_Avg_2018_06_04 = data['2018-06-04']
Disk_Free_Space_Avg_2018_06_04.head(2)
plt.plot(Disk_Free_Space_Avg_2018_06_04)


Disk_Free_Space_Avg_2018_06_05 = data['2018-06-05']
Disk_Free_Space_Avg_2018_06_05.head(2)
plt.plot(Disk_Free_Space_Avg_2018_06_05)

Disk_Free_Space_Avg_2018_06_06 = data['2018-06-06']
Disk_Free_Space_Avg_2018_06_06.head(2)
plt.plot(Disk_Free_Space_Avg_2018_06_06)

Disk_Free_Space_Avg_2018_06_07 = data['2018-06-07']
Disk_Free_Space_Avg_2018_06_07.head(2)
plt.plot(Disk_Free_Space_Avg_2018_06_07)



Disk_Free_Space_Avg_2018_06_08 = data['2018-06-08']
Disk_Free_Space_Avg_2018_06_08.head(2)
plt.plot(Disk_Free_Space_Avg_2018_06_08)


Disk_Free_Space_Avg_2018_06_09 = data['2018-06-09']
Disk_Free_Space_Avg_2018_06_09.head(2)
plt.plot(Disk_Free_Space_Avg_2018_06_09)





import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics 
from sklearn.metrics import accuracy_score
def classification_model(model,data, predictors, outcome):
    model.fit(data[predictors], data[outcome])
    predictions = model.predict(data[predictors])
    accuracy = metrics.accuracy_score(predictions,data[outcome])
    print("Accuracy :{0:.3%}".format(accuracy))
    kf = KFold(data.shape[0], n_folds=5)
    error = []
    for train, test in kf:
        train_predictors = (data[predictors].iloc[train,:])
        train_target = data[outcome].iloc[train]
        model.fit(train_predictors, train_target)
        error.append(model.score(data[preditors].iloc[test,:], data[outcome].iloc[test]))
    print ("Cross-Validation Score :{0: 3%}".format(np.mean(error)))
    model.fit(data[predictors],data[outcome])


data.head(2)
data.plot()
import warnings
import itertools 
import pandas as pd 
import numpy as np 
import statsmodels.api as sm
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')



y = data['Disk_Free_Space_Avg'].resample('MS').mean()

y = y.fillna(y.bfill())
y.plot(figsize=(20, 10))


warnings.filterwarnings("ignore")
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
print('les différentes combinaisons de paramètres de saisonnalité')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[4]))
for param in pdq: 
    for param_seasonal in seasonal_pdq: 
        try: 
            mod = sm.tsa.statespace.SARIMAX(y, order=param, seasonal_order=param_seasonal, enforce_stationarity=False, enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except :
            continue
mod = sm.tsa.statespace.SARIMAX(y, order=(0, 0, 1), seasonal_order=(0, 0, 0, 12), enforce_stationarity=False, enforce_invertibility=False)
results = mod.fit()
print(results.aic)
print(results.summary())
results.plot_diagnostics(figsize=(20, 18))
plt.show()
import pandas as pd
import dateutil 
pred = results.get_prediction(start=pd.to_datetime('2018-06-01'), dynamic=False)
pred_ci = pred.conf_int()
ax = y['2017-06-01':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7)
ax.fill_between(pred_ci.index, pred_ci.iloc[:, 0], pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('Disk_Free_Space_Avg')
plt.legend()
