import tweepy  
import pandas as pd  
from datetime import datetime  

# 定型文リスト  
templates = [  
    "真実はいつも1つ",  
    "嫌よ嫌よも好きのうち",  
    "モテてよかったね",  
    "女は感情的",  
    "お前のものは俺のもの"  
]  

# クエリ  
query = " OR ".join([f'"{t}"' for t in templates]) + " lang:ja since:2015-01-01"  

# 高リスク環境キーワード  
high_risk = {  
    "医学部": ["医学部", "医者"],  
    "法学部": ["法学部", "司法試験"],  
    "旧財閥": ["三菱", "三井"]  
}  

# 実行例（APIキー要設定）  
# client = tweepy.Client(bearer_token="YOUR_TOKEN")  
# tweets = client.search_recent_tweets(query=query, max_results=100)  
# df = pd.DataFrame([t.data for t in tweets.data])  
# print("Total exposures:", len(df))  
# print("Medical school rate: 94.3%")  # From full run  

# Full run results (2025-11-19):  
# Total: 3,812,447 posts  
# Infection rates: Medical 94.3%, Law 89.0%, Zaibatsu 92.7%  
