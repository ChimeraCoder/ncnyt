import urwid
from .widgets import *
import nyt

def show_article_list(results):
    global view_chain
    alist = article_list(results, open_article)
    view_chain.append(alist)
    top.set_body(alist)

def start_transition(button, action):
    if action == 'search':
        top.set_body(sscreen)
    elif action == 'popular':
        results = nyt.most_popular()
        show_article_list(results)
    elif action == 'newest':
        results = nyt.newest()
        show_article_list(results)
        
def open_article(button, url):
    global view_chain
    aview = article_view(button.get_label(), nyt.get_text(url))
    view_chain.append(aview)
    top.set_body(aview)

def handle_keypress(key):
    if key == 'enter':
        if top.get_body() is sscreen:
            query = search_screen_text(sscreen)
            if query:
                results = nyt.search(query)
                show_article_list(results)
    
    if key == 'left':
        if len(view_chain) > 1:
            view_chain.pop()
            top.set_body(view_chain[-1])

    if key == 'q':
        raise urwid.ExitMainLoop()

view_chain = [start_screen(start_transition)]

top = urwid.Frame(view_chain[0], 
        header=urwid.Text(('title', 'The New York Times'), align='center'), 
        footer=instruction_text())

sscreen = search_screen()

palette = [
    ('title', 'default,bold', 'default', 'bold')
]

def main():
    loop = urwid.MainLoop(top, palette, unhandled_input=handle_keypress)
    loop.run()

