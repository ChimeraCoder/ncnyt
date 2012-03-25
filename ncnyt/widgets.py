import urwid

def article_view(title, body):
    content = urwid.SimpleListWalker([
        urwid.Text(('bold', title)),
        urwid.Text(body) ])
    return urwid.ListBox(content)

def article_list(artlist, button_handler):
    content = urwid.SimpleListWalker(
            [urwid.Button(title, button_handler, url) \
                for (title, url) in artlist])
    return urwid.ListBox(content)

def search_screen_text(sscreen):
    entry = sscreen.original_widget
    return entry.get_edit_text()

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

def instruction_text():
    return urwid.Text('q: quit | left: go back')
        

