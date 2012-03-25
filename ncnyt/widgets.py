import urwid

def article_view(title, body):
    content = urwid.SimpleListWalker([
        urwid.Text(title),
        urwid.Text(body) ])
    return urwid.ListBox(content)

def article_list(artlist, button_handler):
    content = urwid.SimpleListWalker(
            [urwid.Button(title, button_handler, url) \
                for (title, url) in artlist])
    return urwid.ListBox(content)

def search_screen_text(sscreen):
    entry = sscreen.original_widget
    return entry.get_text()

def search_screen():
    entry = urwid.Edit('Search: ')
    return urwid.Filler(entry)

def start_screen(button_handler):
    content = urwid.SimpleListWalker(
            [urwid.Button(label, button_handler, action) \
                for (label, action) in [
                    ('Search Article', 'search'),
                    ('Most Popular', 'popular')]])
    return urwid.ListBox(content)

     
        

