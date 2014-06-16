try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'AshleyUy',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ashleyuy@hotmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['lexicon'],
    'scripts': [],
    'name': 'lexicon'
}

setup(**config)