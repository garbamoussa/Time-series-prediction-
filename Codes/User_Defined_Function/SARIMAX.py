import warnings; warnings.simplefilter("ignore")
import numpy as np
import pandas as pd 

data = pd.ExcelFile(r"/Users/moussa.garba/Desktop/DataManager/DataAfine.xlsx")
data = pd.read_excel(r"/Users/moussa.garba/Desktop/DataManager/DataAfine.xlsx",sheetname=0, parse_dates=True, index_col=0)

Disk_Avg = data['Disk_Free_Space_Avg']
Disk_Min = data['Disk_Free_Space_Min']
Disk_Max = data['Disk_Free_Space_Max']
Disk_Avg = pd.DataFrame(data=Disk_Avg)
Disk_Min =  pd.DataFrame(data=Disk_Min)
Disk_Max =  pd.DataFrame(data=Disk_Max)

#Test = Disk_Avg['2017-06-22': '2017-06-23' ]['Disk_Free_Space_Avg']
#Test = pd.DataFrame(data=Test)

Disk_Min.head(5)
Disk_Max.head(5)
import numpy as np
import pandas as pd

from sklearn.model_selection import (train_test_split, GridSearchCV, RandomizedSearchCV, cross_val_score)
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import GradientBoostingClassifier
data = pd.read_excel(r"/Users/moussa.garba/Desktop/DataManager/DataAfine.xlsx",sheetname=0, parse_dates=True)
data.head()


from sklearn.model_selection import ParameterGrid
import itertools
import statsmodels.api as sm

# Set variables to populate
lowest_aic = None
lowest_parm = None
lowest_param_seasonal = None

# GridSearch the hyperparameters of p, d, q and P, D, Q, m

p = d = q = range(0, 3)
param_grid = list(itertools.product(p, d, q))
seasonal_param_grid = [(x[0], x[1], x[2], 96) for x in list(itertools.product(p, d, q))]

for param in param_grid:
    for param_seasonal in seasonal_param_grid:
        try:
            mdl = sm.tsa.statespace.SARIMAX(Test, order=param, seasonal_order=param_seasonal, enforce_stationarity=True, enforce_invertibility=True)

            results = mdl.fit()
            
            # Store results
            current_aic = results.aic

            # Set baseline for aic
            if (lowest_aic == None):
                lowest_aic = np.min.results.aic

            # Compare results
            if (current_aic <= lowest_aic):
                lowest_aic = current_aic
                lowest_parm = param
                lowest_param_seasonal = param_seasonal
                
                print ('SARIMA{}x{} - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue
            
print ('The best model is: SARIMA {}x{} - AIC:{}'.format(lowest_parm, lowest_param_seasonal, lowest_aic))

Test.head(5)


#Test.index = pd.DatetimeIndex(Test.index.values, freq=Test.index.inferred_freq)

Test.head(5)


from statsmodels.tsa.statespace.sarimax import SARIMAX

def Gridsearch(ts):
    # Set variables to populate
    best_aic = np.inf
    #best_aic = None
    lowest_parm = None
    lowest_param_seasonal = None
    import itertools
    import statsmodels.api as sm
    import statsmodels.tsa.api as smt
    # GridSearch the hyperparameters of p, d, q and P, D, Q, m
    p = d = q = range(0, 2)
    param_grid = list(itertools.product(p, d, q))
    seasonal_param_grid = [(x[0], x[1], x[2], 30) for x in list(itertools.product(p, d, q))]
    ts.index = pd.DatetimeIndex(ts.index.values, freq=ts.index.inferred_freq)
    
    for param in param_grid:
        for param_seasonal in seasonal_param_grid:
            try:
                mdl = sm.tsa.statespace.SARIMAX(ts, order=param, seasonal_order=param_seasonal, enforce_stationarity=True, enforce_invertibility=True)
                results = mdl.fit()
                tmp_aic  = results.aic 
                if tmp_aic <= best_aic:
                    best_aic = tmp_aic
                    #best_aic = tmp_aic.index(min(tmp_aic))
                    #best_aic  = [i for i, x in enumerate(tmp_aic) if x ==min(tmp_aic)]
                    lowest_parm = param
                    lowest_param_seasonal = param_seasonal
                    
            except:
                
                continue
            
    return lowest_parm, lowest_param_seasonal, best_aic


Gridsearch(Test)
mdl = sm.tsa.statespace.SARIMAX(Test, order=(1, 1, 0), seasonal_order=(0, 1, 0, 30), enforce_stationarity=True, enforce_invertibility=True)

start_params = []

results = mdl.fit()
tmp_aic  = results.aic 
tmp_aic

def _get_best_model(TS):
    best_aic = np.inf 
    best_order = None
    best_mdl = None
    import statsmodels.tsa.api as smt
    pq_rng = range(10) # [0,1,2,3,4]
    d_rng = range(5) # [0,1]
    for i in pq_rng:
        for d in d_rng:
            for j in pq_rng:
                try:
                    tmp_mdl = smt.ARIMA(TS, order=(i,d,j)).fit(
                        method='mle', trend='nc'
                    )
                    tmp_aic = tmp_mdl.aic
                    if tmp_aic < best_aic:
                        best_aic = tmp_aic
                        best_order = (i, d, j)
                        best_mdl = tmp_mdl
                except: continue
    #p('aic: {:6.5f} | order: {}'.format(best_aic, best_order))                    
    return best_aic, best_order, best_mdl


Test = Disk_Avg['2017-06-22']['Disk_Free_Space_Avg']
Test = pd.DataFrame(data=Test)

Gridsearch(Test)

import statsmodels.api as sm
m = sm.tsa.statespace.SARIMAX(Test, order=(2,2,1), seasonal_order=(0,2,0,30), enforce_stationarity=False, enforce_invertibility=False)
res = m.fit(disp=False)
print(res.summary())



current_aic = res.aic

import itertools
import statsmodels.api as sm
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 30) for x in list(itertools.product(p, d, q))]
print('Les différentes combinaisons de paramètres de saisonnalité')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[4]))

import warnings; warnings.simplefilter("ignore")
import numpy as np
for param in pdq: 
    for param_seasonal in seasonal_pdq: 
        try: 
            mod = sm.tsa.statespace.SARIMAX(Test, 
                                            order=param, 
                                            seasonal_order=param_seasonal, 
                                            enforce_stationarity=False, 
                                            enforce_invertibility=False)
            results = mod.fit()
            R = []
            R.append(results.aic)
            #results_aic = results.aic
            #best_aic = min(R)
            print('ARIMA{}x{}30 - AIC:{}'.format(param, param_seasonal, min(R)))
        except :
            continue

best_aic  = [i for i, x in enumerate( results.aic) if x == min( results.aic)]

Test = Disk_Avg['2017-06-22']['Disk_Free_Space_Avg']
Test = pd.DataFrame(data=Test)
Test.index = pd.DatetimeIndex(Test.index.values, freq=Test.index.inferred_freq)
Test.head()



def Gridsearch(ts):
    # Set variables to populate
    lowest_aic = None
    lowest_parm = None
    lowest_param_seasonal = None
    import itertools
    import statsmodels.api as sm
    # GridSearch the hyperparameters of p, d, q and P, D, Q, m
    p = d = q = range(0, 2)
    param_grid = list(itertools.product(p, d, q))
    seasonal_param_grid = [(x[0], x[1], x[2], 30) for x in list(itertools.product(p, d, q))]
    ts.index = pd.DatetimeIndex(ts.index.values, freq=ts.index.inferred_freq)
    
    for param in param_grid:
        for param_seasonal in seasonal_param_grid:
            try:
                mdl = sm.tsa.statespace.SARIMAX(ts, order=param, seasonal_order=param_seasonal, enforce_stationarity=True, enforce_invertibility=True)
                results = mdl.fit(maxiter=1000, method='nm')
                
                # Store results
                current_aic = results.aic

                # Set baseline for aic
                
                if (lowest_aic == None):
                    
                    lowest_aic = results.aic
                
                # Compare results
                
                if (current_aic <= lowest_aic):
                    
                    lowest_aic = current_aic
                    lowest_parm = param
                    lowest_param_seasonal = param_seasonal
                    
                #print ('SARIMA{}x{} - AIC:{}'.format(param, param_seasonal, results.aic))
            except:
                
                continue
            
    return lowest_parm,lowest_param_seasonal,lowest_aic




import warnings; warnings.simplefilter("ignore")
import numpy as np
#best_aic = None
#best_param = None
#best_param_seasonal = None
import itertools
import statsmodels.api as sm
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 30) for x in list(itertools.product(p, d, q))]
#print('Les différentes combinaisons de paramètres de saisonnalité')
#print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
#print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
#print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[3]))
#print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[4]))
for param in pdq: 
    for param_seasonal in seasonal_pdq: 
        try:
            mod = sm.tsa.statespace.SARIMAX(Test, order=param, seasonal_order=param_seasonal, enforce_stationarity=False, enforce_invertibility=False).fit()
            R = mod.aic
            results = pd.Series(R[0:4], index=['param', 'param_seasonal', 'AIC', 'BIC'])
            #best_R = min(R)
            #if (bestR <= best_R):
                
               # best_aic = best_R
                #best_param = param
                #best_param_seasonal = param_seasonal 
            print('SARIMA{}x{}30 - AIC:{}'.format(param, param_seasonal, results)
        except:
                  continue






import os
import sys

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas.core.common import is_list_like
import pandas_datareader.data as web
import numpy as np

import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import scipy.stats as scs
from arch import arch_model

import matplotlib.pyplot as plt
import matplotlib as mpl
%matplotlib inline
p = print

#p('Machine: {} {}\n'.format(os.uname().sysname,os.uname().machine))
p(sys.version)




def tsplot(y, lags=None, figsize=(10, 8), style='bmh'):
    if not isinstance(y, pd.DataFrame):
        y = pd.DataFrame(y)
    with plt.style.context(style):    
        fig = plt.figure(figsize=figsize)
        #mpl.rcParams['font.family'] = 'Ubuntu Mono'
        layout = (3, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))
        qq_ax = plt.subplot2grid(layout, (2, 0))
        pp_ax = plt.subplot2grid(layout, (2, 1))
        
        y.plot(ax=ts_ax)
        ts_ax.set_title('Time Series Analysis Plots')
        smt.graphics.plot_acf(y, lags=lags, ax=acf_ax, alpha=0.5)
        smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax, alpha=0.5)
        sm.qqplot(y, line='s', ax=qq_ax)
        qq_ax.set_title('QQ Plot')        
        scs.probplot(y, sparams=(y.mean(), y.std()), plot=pp_ax)

        plt.tight_layout()
    return 



def _get_best_model(TS):
    best_aic = np.inf 
    best_order = None
    best_mdl = None
    import itertools
    pq_rng = range(5) # [0,1,2,3,4]
    #p = d = q = range(5)
    #pdq = list(itertools.product(p, d, q))
    d_rng = range(2) # [0,1]
    #seasonal_pdq = [(x[0], x[1], x[2], 30) for x in list(itertools.product(p, d, q))]
    for i in pq_rng:
        for d in d_rng:
            for j in pq_rng:
                try:
                    tmp_mdl = smt.ARIMA(TS, order=(i,d,j)).fit(
                        method='mle', trend='nc'
                    )
                    tmp_aic = tmp_mdl.aic
                    if tmp_aic < best_aic:
                        best_aic = tmp_aic
                        best_order = (i, d, j)
                        best_mdl = tmp_mdl
                except: continue
    p('aic: {:6.5f} | order: {}'.format(best_aic, best_order))                    
    return best_aic, best_order, best_mdl


def _get_best_model(TS):
    best_aic = np.inf 
    best_order = None
    best_mdl = None
    import statsmodels.tsa.api as smt
    pq_rng = range(10) # [0,1,2,3,4]
    d_rng = range(5) # [0,1]
    for i in pq_rng:
        for d in d_rng:
            for j in pq_rng:
                try:
                    tmp_mdl = smt.ARIMA(TS, order=(i,d,j)).fit(
                        method='mle', trend='nc'
                    )
                    tmp_aic = tmp_mdl.aic
                    if tmp_aic < best_aic:
                        best_aic = tmp_aic
                        best_order = (i, d, j)
                        best_mdl = tmp_mdl
                except: continue
    #p('aic: {:6.5f} | order: {}'.format(best_aic, best_order))                    
    return best_aic, best_order, best_mdl



# Set variables to populate
lowest_aic = None
lowest_parm = None
lowest_param_seasonal = None
import itertools
import statsmodels.api as sm
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 30) for x in list(itertools.product(p, d, q))]
# GridSearch the hyperparameters of p, d, q and P, D, Q, m
for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mdl = sm.tsa.statespace.SARIMAX(Test, order=param, seasonal_order=param_seasonal, enforce_stationarity=True, enforce_invertibility=True)

            results = mdl.fit(maxiter=500, method='nm')
            
            # Store results
            current_aic = results.aic

            # Set baseline for aic
            if (lowest_aic == None):
                lowest_aic = results.aic

            # Compare results
            if (current_aic <= lowest_aic):
                lowest_aic = current_aic
                lowest_parm = param
                lowest_param_seasonal = param_seasonal

            print('SARIMA{}x{} - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue
print(results.mle_retvals)           
print('The best model is: SARIMA{}x{} - AIC:{}'.format(lowest_parm, lowest_param_seasonal, lowest_aic))

Test = Disk_Avg['2017-06-20': '2017-06-27' ]['Disk_Free_Space_Avg']
Test = pd.DataFrame(data=Test)


 mdl = sm.tsa.statespace.SARIMAX(Disk_Avg, order=param, seasonal_order=param_seasonal, enforce_stationarity=True, enforce_invertibility=True)

results = mdl.fit()

max_date = data.period.max()
min_date = data.period.min()

num_of_actual_points = data.index.shape[0]
num_of_expected_points = (max_date.year - min_date.year) * 12 + max_date.month - min_date.month + 1

print("Date range: {} - {}".format(min_date.strftime("%d.%m.%Y"), max_date.strftime("%d.%m.%Y")))
print("Number of data points: {} of expected {}".format(num_of_actual_points, num_of_expected_points))


max_date = df.period.max()
min_date = df.period.min()

num_of_actual_points = df.index.shape[0]
num_of_expected_points = (max_date.year - min_date.year) * 12 + max_date.month - min_date.month + 1

print("Date range: {} - {}".format(min_date.strftime("%d.%m.%Y"), max_date.strftime("%d.%m.%Y")))
print("Number of data points: {} of expected {}".format(num_of_actual_points, num_of_expected_points))


from statsmodels.tsa.statespace import sarimax
model = sarimax.SARIMAX()




                  



