import os
import sys
sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = 'Flask-TUI-Editor'
copyright = '2024, <a href="https://mantis.com.tr">Mantis Software Company</a>'
author = 'Furkan Kalkan'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc'
]
autodoc_member_order = 'bysource'
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
master_doc = 'index'
html_theme_options = {
    'description': 'Markdown editor with Toast UI integration for Flask',
    'sidebar_collapse': False,
    'github_user': 'mantis-software-company',
    'github_repo': 'Flask-TUI-Editor',
    'github_button': True,
    'github_type': 'star',
    'sidebar_header': '#3E4349',
    'fixed_sidebar': False,
    'github_banner': True,
    # If available should be in _static/logo.png
    # 'logo': 'logo.png',
    'show_powered_by': True
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_show_sourcelink = False