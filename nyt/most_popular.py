import requests
import json
import auth

def most_popular():
    """Returns a list of the most popular articles on nytimes.com as
    tuples containing the title and url."""

    key = auth.keys()['popular']
    base_url = 'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/30.json'
    params = {'api-key': key}
    r = requests.get(base_url, params=params)
    

    if r.status_code != 200:
        r.raise_for_status()


    response = json.loads(r.text)    
    return [(x['title'], x['url']) for x in response['results']]

