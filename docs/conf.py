# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import subprocess
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../src/datatable'))


# -- Project information -----------------------------------------------------

project = 'datatable'
copyright = '2018-2020, H2O.ai'
author = 'Pasha Stetsenko'

try:
    import datatable
    version = datatable.__version__

except ImportError:
    verfile = os.path.abspath(os.path.join(os.path.dirname(__file__),
                              "../VERSION.txt"))
    if os.path.isfile(verfile):
        with open(verfile, "rt") as inp:
            version = inp.read().strip()
    else:
        version = ""


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxext.dtframe_directive',
    'sphinxext.xcode',
    'sphinxext.xcontributors',
    'sphinxext.xfunction',
    'sphinxext.dt_changelog',
    'sphinxext.ref_context',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',  # links to external documentation
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',
                    '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'IPython': ('https://ipython.readthedocs.io/en/stable/', None),
}


# -- Options for Changelog extension -----------------------------------------

changelog_issue_url = "https://github.com/h2oai/datatable/issues/{issue}"

changelog_user_url = "https://github.com/{name}"


# -- Options for XFunction extension -----------------------------------------

xf_module_name = "datatable"

xf_project_root = ".."

try:
    _ghcommit = subprocess.check_output(["git", "rev-parse", "master"],
                                        universal_newlines=True).strip()
    xf_permalink_url0 = ("https://github.com/h2oai/datatable/blob/" +
                         _ghcommit + "/{filename}")
    xf_permalink_url2 = xf_permalink_url0 + "#L{line1}-L{line2}"

except subprocess.CalledProcessError:
    pass



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# See: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    "canonical_url": "https://datatable.readthedocs.io/en/latest/",
    "style_external_links": True,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "titles_only": True,
}

html_show_sphinx = False
html_show_copyright = False
html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}



# -- Custom setup ------------------------------------------------------------

def setup(app):
    app.add_css_file("code.css")

