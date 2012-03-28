try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='ncnyt',
    version='0.2.0',
    url='https://github.com/ChimeraCoder/ncnyt',
    packages=['ncnyt', 'nyt'],
    install_requires=[
        'requests', 
        'urwid', 
        'beautifulsoup4', 
        'lxml',
        'python-aalib',
        'PIL'],
    entry_points = {
        'console_scripts': ['nyt=ncnyt:main']})


