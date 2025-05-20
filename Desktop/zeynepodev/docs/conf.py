import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'ShortestPath2220674052'
copyright = '2024, Zeynep Oğulcan'
author = 'Zeynep Oğulcan'
release = '0.1.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

# Add the source directory as the current directory
source_dir = '.'
templates_path = ['_templates']
exclude_patterns = ['_build', 'build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static'] 