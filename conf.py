project = 'Radio Astronomy with Neutral Hydrogen'
copyright = '2022, Daniel Williams'
author = 'Daniel Williams'

import kentigern
release = "0.0.1"

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'numpydoc',
    'nbsphinx'
]

language = 'en'
exclude_patterns = []

html_theme = 'kentigern'

todo_include_todos = True
