import urwid
from .widgets import *

def start_transition(button, action):
    if action == 'search':
        top.set_body(sscreen)

def open_article(button, url):
    top.set_body(article_view(button.get_label(), url))

def handle_keypress(key):
    if key == 'enter':
        if top.get_body() is sscreen:
            results = [
                ('Santorum calls gays immoral ... again', 
                'http://nytimes.com/2012/03/25/us/politics/santorum-is-a-douchebag.html'),
                ('''Young wantrepreneur B-School dropout attempting to build
                 next great social app ... thinly-veiled attempt to acquire 
                 your personal data for advertisers''',
                 'http://nytimes.com/2012/03/25/business/bschool-students-are-douchebags.html')
            ]
            top.set_body(article_list(results, open_article))
    if key == 'q':
        raise urwid.ExitMainLoop()

top = urwid.Frame(start_screen(start_transition))
sscreen = search_screen()

def main():
    loop = urwid.MainLoop(top, unhandled_input=handle_keypress)
    loop.run()



