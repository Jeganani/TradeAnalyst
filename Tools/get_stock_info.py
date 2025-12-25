import yfinance as yf
from crewai.tools import tool

@tool('get_stock_price_info')
def get_stock_base_info(Stock:str)->str:
    """
    Retrieves the latest stock price and other relevant info for a given stock symbol using Yahoo Finance.

    Parameters:
        stock_symbol (str): The ticker symbol of the stock (e.g., AAPL, TSLA, MSFT).

    Returns:
        str: A summary of the stock's current price, daily change, and other key data.
    """
    try:
        ticker = yf.Ticker(Stock)
    except Exception as e:
        raise Exception(f"unable to fetch the details from finance app, ensure that stock symbol or stock name is correct ,you can also check the stock name in yfinance website!! {e}")

    Stock_details = ticker.info
    return f"""All time high price:  {Stock_details['allTimeHigh']}
    All time low price :  {Stock_details['allTimeLow']}
    Average analyst rating:  "{Stock_details['averageAnalystRating']}"
    Yfinance Recommendations:  "{Stock_details['recommendationKey']}"
    Market Change for the day as of now (in price):  {Stock_details['regularMarketChange']}
    Market Change for the day as of now (in percentage):  {Stock_details['regularMarketChangePercent']}
    Today's High price as of now:  {Stock_details['regularMarketDayHigh']}
    Today's Low price as of now:  {Stock_details['regularMarketDayLow']}
    Today's Market Open price:  {Stock_details['regularMarketOpen']}
    Last Market Closed price:  {Stock_details['regularMarketPreviousClose']}
    Current or Actual price :  {Stock_details['regularMarketPrice']}"""

# print(get_stock_base_info('GROWW.NS'))


