import urwid

def article_view(art):
    content = urwid.SimpleListWalker([
        urwid.Text(('title', art.title), align='center'),
        urwid.Text(art.img, align='center'),
        urwid.Text(art.byline), 
        urwid.Text(art.dateline),
        urwid.Text(art.body),
        urwid.Text(art.url, align='right')])
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
                    ('Search Articles', 'search'),
                    ('Most Popular Articles', 'popular'),
                    ('NewsWire: Most Recent Articles', 'newest')]])
    return urwid.ListBox(content)

def instruction_text():
    return urwid.Text('q: quit | left: go back | right/enter: select')
        

