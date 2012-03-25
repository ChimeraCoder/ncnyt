try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='ncnyt',
      version='0.1',
      url='https://github.com/ChimeraCoder/ncnyt',
      packages=['ncnyt', 'nyt'],
      install_requires=['requests', 'urwid', 'BeautifulSoup'],
      entry_points = {
        'console_scripts': ['nyt=ncnyt:main']
      })


