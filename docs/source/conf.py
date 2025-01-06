# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'uEMEP documentation'
copyright = '2024, metno'
author = 'metno'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'sphinxcontrib.bibtex',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.mathjax'
    ]
bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'plain'
bibtex_reference_style = 'author_year'

templates_path = ['_templates']
exclude_patterns = []

autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
