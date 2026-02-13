import sys
import requests
from bs4 import BeautifulSoup
import feedparser
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def get_google_trends():
    # Google Trends Daily Search Trends RSS for US
    url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
    try:
        feed = feedparser.parse(url)
        hot_items = []
        for entry in feed.entries:
            hot_items.append(entry.title)
            if len(hot_items) >= 10:
                break
        return hot_items
    except Exception as e:
        logging.error(f"Error fetching Google Trends: {e}")
        return []

def get_daily_news():
    now = datetime.datetime.now()
    current_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    google_hot = get_google_trends()
    
    greeting = f"Bugün: {current_time_str} (UTC). Küresel gündem başlıkları:"
    news_list = ""
    for i, item in enumerate(google_hot, 1):
        news_list += f"{i}. {item}\n"
        
    return f"{greeting}\n{news_list}"

if __name__ == "__main__":
    print(get_daily_news())
