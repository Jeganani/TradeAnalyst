import yfinance as yf
from datetime import datetime,timedelta
import pprint

def get_stock_news_yfin(stock_symbol:str)->dict:
    """
    Helps to retreive the Latest Stock news from yahoo finance api, Helps to understand the coming trend and valuable insights that can be applied on Stock Decision.

    Parameters:
    stock_symbol (str): The ticker symbol of the stock (e.g., AAPL, TSLA, MSFT).

    Returns:
    dict: Latest news on the particular stock from yfinance app.
    dictionary elements:
    title: title for the particular article.
    news: Actual news for the specific article.
    """
    ticker=yf.Ticker(stock_symbol)
    news=ticker.news
    updated_dict=[]
    for i in news:
        published_date=datetime.fromisoformat(i['content']['pubDate'].replace('Z', '+00:00')).date()
        if published_date>=datetime.now().date()- timedelta(days=100):
            print(i['content']['summary'])
            new={
                "title":i['content']['title'],
                "news":i['content']['summary']
                }
            updated_dict.append(new)
    return updated_dict


print(get_stock_news_yfin('MEESHO.NS'))