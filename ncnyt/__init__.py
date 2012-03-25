import urwid
from .widgets import *
import nyt

def start_transition(button, action):
    if action == 'search':
        top.set_body(sscreen)

def open_article(button, url):
    top.set_body(article_view(button.get_label(), nyt.get_text(url)))

def handle_keypress(key):
    if key == 'enter':
        if top.get_body() is sscreen:
            query = search_screen_text(sscreen)
            results = nyt.search(query)
            top.set_body(article_list(results, open_article))
    if key == 'q':
        raise urwid.ExitMainLoop()

top = urwid.Frame(start_screen(start_transition))
sscreen = search_screen()

def main():
    loop = urwid.MainLoop(top, unhandled_input=handle_keypress)
    loop.run()



