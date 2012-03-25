import auth
import json
import requests

def search(query):
    """Searches for an article in the NYTimes database.

    Keyword arguments: 
    query -- the search query, in NYTimes format

    Returns a list of tuples containing article titles and article
    urls (as strings)"""
    
    key = auth.keys()['search']
    base_url = 'http://api.nytimes.com/svc/search/v1/article'
    params = {'query': query, 'api-key': key}
    r = requests.get(base_url, params=params)
    
    if r.status_code != 200:
        r.raise_for_status()

    response = json.loads(r.text)
    return [(x['title'], x['url']) for x in response['results']]
