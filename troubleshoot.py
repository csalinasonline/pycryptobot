import numpy as np
import matplotlib.pyplot as plt

from models.PyCryptoBot import PyCryptoBot
from models.Trading import TechnicalAnalysis
from models.Binance import AuthAPI as BAuthAPI, PublicAPI as BPublicAPI
from models.CoinbasePro import AuthAPI as CBAuthAPI, PublicAPI as CBPublicAPI
from views.TradingGraphs import TradingGraphs

app = PyCryptoBot()
trading_data = app.getHistoricalData(app.getMarket(), app.getGranularity())

ta = TechnicalAnalysis(trading_data)
ta.addAll()
ta.saveCSV(filename='tradingdata_050921.csv')

df_data = ta.getDataFrame()
#df_fib = ta.getFibonacciRetracementLevels()
#df_sr = ta.getSupportResistanceLevels()

print (df_data)
print(len(df_data))
#print (df_fib)
#print(len(df_fib))
#print (df_sr)
#print(len(df_sr))

graphs = TradingGraphs(ta)
# graphs.renderBuySellSignalEMA1226(saveOnly=False)
# graphs.renderBuySellSignalEMA1226MACD(saveOnly=False)
# graphs.renderPriceEMA12EMA26(saveOnly=False)
# graphs.renderEMAandMACD(saveOnly=False)
# graphs.renderSeasonalARIMAModel(saveOnly=False)
# graphs.renderSMAandMACD(saveOnly=False)
# graphs.renderSeasonalARIMAModelPrediction(saveOnly=False)
# graphs.renderCandlestickAstralPattern(saveOnly=False)
# graphs.renderCandlesticks(saveOnly=False)
# graphs.renderSupportResistance(saveOnly=False)
# #graphs = TradingGraphs(ta)
# graphs.renderPercentageChangeHistogram()
# graphs.renderCumulativeReturn()
# graphs.renderPercentageChangeScatterMatrix()
# graphs.renderFibonacciBollingerBands(period=24)