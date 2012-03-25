import requests
import json
from bs4 import BeautifulSoup as bs
from bs4.element import NavigableString, Tag

def extract_text(elem):
    if isinstance(elem, NavigableString):
        return unicode(elem)
    if isinstance(elem, Tag):
        return u' '.join([extract_text(subelem) for subelem in elem.contents])
    return u''

def get_page(url, page):
    r = requests.get(url, params={'pagewanted': page})
    if r.status_code != 200:
        r.raise_for_status()

    soup = bs(r.text, 'lxml')

    paragraphs = soup.find_all('p', {'itemprop':'articleBody'})
    
    if paragraphs:
        return u'\n'.join([extract_text(elem).rstrip() for elem in paragraphs])
    return u'Could not extract text for page' + str(page)


def get_text(url):
    """Given the url of a NYTimes article, returns the body text of
    the article."""
    
    r = requests.get(url)
    if r.status_code != 200:
        r.raise_for_status()

    soup = bs(r.text, 'lxml')

    title_elem = soup.find('nyt_headline')
    
    if title_elem:
        title = title_elem.contents[0]
    else:
        title = 'Unknown Article'

    pages = soup.find('ul', {'id': 'pageNumbers'})

    if not pages:
        paragraphs = soup.find_all('p', {'itemprop':'articleBody'})
    
        if paragraphs:
            body =  u'\n'.join([extract_text(elem).rstrip() for elem in paragraphs])
        else:
            body = 'Could not extract Article text.'
    else:
        num_pages = len(pages.find_all('li'))
        paragraphs = soup.find_all('p', {'itemprop':'articleBody'})
    
        if paragraphs:
            body = u'\n'.join([extract_text(elem).rstrip() for elem in paragraphs])
        else:
            body = u'Could not extract text for page 1'
        for x in range(1, num_pages):
            body += u'\n' + get_page(url, x + 1) 

    return title, body
