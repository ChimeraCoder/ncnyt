import requests
import json
import auth

def newest():
    """Returns a list of the newest articles on the nytimes.com 
    as tuples containing the title of the article and the article's url."""

    key = auth.keys()['newswire']
    base_url = 'http://api.nytimes.com/svc/news/v2/content/nyt/all/24.json'

    params = {'api-key': key}
    r = requests.get(base_url, params=params)

    if r.status_code != 200:
        r.raise_for_status()

    response = json.loads(r.text)
    return [(x['headline'], x['url']) for x in response['results']]
