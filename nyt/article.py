import json
from BeautifulSoup import BeautifulSoup

def get_text(url):
    """Given the url of a NYTimes article, returns the body text of
    the article."""

    return """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris quis ultricies est. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Mauris lobortis libero velit. Ut at justo sed leo gravida feugiat. Donec cursus porta lectus ac consectetur. Suspendisse vel mi at nulla aliquam varius vitae at nibh. Sed vehicula, nisi non blandit aliquet, lorem metus suscipit eros, et pharetra metus ipsum at nibh. Fusce iaculis sollicitudin justo et bibendum. In hac habitasse platea dictumst. Vestibulum eu nulla elit, venenatis accumsan velit.

Etiam pretium mi sit amet magna ultrices sit amet ullamcorper mauris blandit. Nulla eu nibh in purus ullamcorper semper ac ac diam. Quisque vulputate congue elit sit amet dignissim. Mauris placerat tristique tellus sed tincidunt. Vivamus blandit iaculis enim in congue. Nulla at ipsum sed arcu tincidunt faucibus eu a quam. Nunc non ligula a odio tempus laoreet et vitae est. Vivamus nisl leo, auctor ac dignissim non, semper ac tellus. Praesent mauris nunc, blandit eu feugiat in, condimentum imperdiet eros. Nunc purus leo, vehicula sed placerat sit amet, vestibulum ut dolor.

Mauris lorem sem, pretium vel imperdiet viverra, malesuada ac quam. Phasellus dictum auctor nunc, in scelerisque sapien elementum ac. Suspendisse lectus est, consectetur in semper et, dapibus nec orci. Quisque viverra, erat non ullamcorper mattis, massa purus dictum nisl, ac blandit risus justo vitae mauris. Fusce consectetur fringilla dui, id sodales turpis ultricies nec. Donec porttitor, mauris vulputate laoreet semper, est ipsum fringilla nibh, quis vulputate tortor mauris id lacus. Sed elementum nibh at magna interdum molestie. Nulla facilisi. Sed eleifend consectetur cursus.

Aliquam volutpat risus non massa gravida ut sodales sapien aliquam. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean commodo turpis sed lacus consequat eu facilisis elit condimentum. Nunc pretium mattis fermentum. Vivamus consectetur varius fermentum. Integer cursus volutpat augue, viverra varius est tincidunt at. Phasellus sit amet sapien et diam feugiat interdum. In at eros placerat ipsum blandit lobortis. Pellentesque congue diam nec arcu rhoncus sagittis. Etiam placerat feugiat quam posuere ullamcorper.

Morbi magna dolor, consequat sit amet aliquam sed, fringilla sed nulla. In nibh mauris, rutrum sed interdum congue, feugiat sed ante. Nunc condimentum lectus et diam venenatis malesuada. Proin consequat accumsan augue molestie aliquam. Aliquam posuere dapibus consequat. Proin magna purus, rutrum non sollicitudin ac, imperdiet sit amet diam. Pellentesque ac justo et orci varius consequat sed sit amet enim. Pellentesque a venenatis mauris. Vivamus interdum nibh quis mi congue rhoncus. Duis porttitor pellentesque purus ac facilisis. Duis at sapien est, vitae interdum erat. Nullam pharetra euismod nisi, laoreet volutpat elit suscipit in. Proin lacinia, risus vel tempus luctus, velit leo venenatis augue, et commodo nisi neque sodales mauris. In hac habitasse platea dictumst."""
