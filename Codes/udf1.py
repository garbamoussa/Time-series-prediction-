from kapacitor.udf.agent import Agent, Handler
from kapacitor.udf import udf_pb2
import sys
import numpy
import pandas as pd
from scipy import stats
import math
import sys
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
from pandas.tseries.offsets import Second
import warnings; warnings.simplefilter("ignore")
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pprint import pprint
from scipy.optimize import brute

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(name)s: %(message)s')
logger = logging.getLogger()
FIELD_TYPES = ['int', 'double']


class state(object):
       
    def __init__(self):
        self._dates   = []
        self._values  = []
        self._predict = 0
        self._period  = None
        self._order   = None
        self._model   = None
    def update(self, date, value):
        self._dates.append(date)
        self._values.append(value)

    def drop(self):
        self._dates  = []
        self._values = []
        self._order  = None

    def get_series(self):
        return pd.Series(data=self._values, index=pd.to_datetime(self._dates))

    def min(self):
        return min(self._values)

    def max(self):
        return max(self._values)



  
    

    def sarimax(self):
        
        start_date = ts.index[-1] + self._period
        end_date = start_date + (self._predict -1) * self._period
        forecast = self._model.predict(start_date.isoformat(), end_date.isoformat())

        if self._order[1] > 0:
            shift = self.max() - self.min()
            forecast += shift
        logger.debug(forecast)
        return forecast


class ForecastHandler(Handler):
    def __init__(self, agent, state):
        self._agent = agent
        self._state = state
        self._field = None
        self._field_type = None
        self._predict = 0
        self._begin_response = None
        self._point = None

    def info(self):
        response = udf_pb2.Response()
        response.info.wants = udf_pb2.BATCH
        response.info.provides = udf_pb2.BATCH

        response.info.options['predict'].valueTypes.append(udf_pb2.INT)
        response.info.options['field'].valueTypes.append(udf_pb2.STRING)
        response.info.options['type'].valueTypes.append(udf_pb2.STRING)
        logger.info("info")
        return response

    def init(self, init_req):
        success = True
        msg = ''

        for opt in init_req.options:
            if opt.name == 'predict':
                self._predict = opt.values[0].intValue
                self._state._predict = self._predict
            if opt.name == 'field':
                self._field = opt.values[0].stringValue
            if opt.name == 'type':
                self._field_type = opt.values[0].stringValue
        if self._predict < 1:
            succ = False
            msg += ' must supply number of values to be predicted > 0'
        if self._field is None:
            success = False
            msg += ' must supply a field name'
        if self._field_type not in FIELD_TYPES:
            succ = False
            msg += ' field type must be one of {}'.format(FIELD_TYPES)

        response = udf_pb2.Response()
        response.init.success = success
        response.init.error = msg[1:]
        return response

    def snapshot(self):
        response = udf_pb2.Response()
        response.snapshot.snapshot = ''
        return response


    def restore(self, restore_req):
        response = udf_pb2.Response()
        response.restore.success = False
        response.restore.error = 'not implemented'
        return response

    def begin_batch(self, begin_req):
        self._state.drop()
        response = udf_pb2.Response()
        response.begin.CopyFrom(begin_req)
        self._begin_response = response

    def point(self, point):
        value = point.fieldsDouble[self._field]
        self._state.update(pd.to_datetime(point.time), value)
        self._point = point
        #logger.debug(str(point))

    def end_batch(self, end_req):
        forecast  = self._state.sarimax()
        logger.debug("size of forecast %s" %len(forecast))
        self._begin_response.begin.size = self._predict
        self._agent.write_response(self._begin_response)
        response = udf_pb2.Response()
        response.point.CopyFrom(self._point)

        for i in range(0, self._predict):
            response.point.time = forecast.index[i].value
            response.point.fieldsDouble[self._field] = forecast[i]
            self._agent.write_response(response)

        response.end.CopyFrom(end_req)
        self._agent.write_response(response)

if __name__ == '__main__':
    a = Agent()
    h = ForecastHandler(a,state())
    a.handler = h

    logger.info("Starting Agent")
    a.start()
    a.wait()
    logger.info("Agent finished")




