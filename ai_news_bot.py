import requests

API_KEY = '740091e7f8d94098844dd4c3042996f2'  
NEWS_URL = 'https://newsapi.org/v2/everything'
QUERY = 'artificial intelligence OR AI OR machine learning OR deep learning OR generative AI OR neural network'

params = {
    'q': QUERY,
    'sortBy': 'publishedAt',
    'language': 'en',
    'apiKey': API_KEY,
    'pageSize': 20, 
    'category': 'technology' 
}

def fetch_ai_news():
    response = requests.get(NEWS_URL, params=params)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        print(f"Latest AI News Headlines:\n")
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   URL: {article['url']}\n")
    else:
        print(f"Error fetching news: {response.status_code}")

if __name__ == "__main__":
    fetch_ai_news()
