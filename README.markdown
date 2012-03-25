NCNYT: NCurses-based NYTimes Reader
====================================


#####Because who needs X?

Have you ever been working in the terminal and wanted to read the news, but
didn't want to leave the terminal to do it? Well this might just be the 
application for you! This NCurses-based application allows you to read quality
articles from the New York Times without ever leaving the warm embrace of the
command line.

Dependencies:
 - urwid
 - requests
 - beautifulsoup4
 - lxml
 - python-aalib
 - PIL

Installation:

	pip install ncnyt

or clone the repository and run

	python setup.py install

You must register your own [API keys for the New York
Times](developer.nytimes.com), for the search, popular, and newswire
APIs. Store these in JSON format in ~/.config/nyt/keys.json as
follows:

{
  "search": "search-api-key",
  "popular": "popular-api-key",
  "newswire": "newswire-api-key"
}

Instructions:

Just run the `nyt` executable to start the program. Once inside, press 'q' to
quit, and use the left arrow to go back to the previous screen.
