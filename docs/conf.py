# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# our project officially 'begins' in the parent aka root project directory
# since we do not separate source from build we can simply go up one directory
# if we ever separate source from build we'll need to change this to '../..'
sys.path.insert(0, os.path.abspath('..'))

# if we ever have images, we'll be using the supported_image_types
# argument to set the desired formats we wish to support
from sphinx.builders.html import StandaloneHTMLBuilder

# -- Project information -----------------------------------------------------

project = 'ark'
copyright = '2020, Angelo Lab'
author = 'Angelo Lab'

# whether we are on readthedocs or not
on_rtd = os.environ.get('READTHEDOCS') == 'True'

# grab which version we want: needs to be either stable or latest
rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
if rtd_version not in ['stable', 'latest']:
    rtd_version = 'stable'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', # allows you to generate documentation from docstrings (STAR)
              'sphinx.ext.autosectionlabel', # allows you to refer sections aka link to them (STAR)
              'sphinx.ext.coverage', # get coverage statistics (STAR)
              'sphinx.ext.intersphinx', # link to other project's documentation, needed if a cross-reference has no matching target in current documentation
              'sphinx.ext.githubpages', # generates a .nojekyll file on generated HTML directory, allows publishing to GitHub pages
              'sphinx.ext.napoleon', # support for Google style docstrings (STAR)
              'sphinx.ext.todo', # support fo TODO
              'sphinx.ext.viewcode', # support for adding links to highlighted source code, looks at Python object descriptions and tries to find source files where objects are contained
              'm2r2', # allows you to include Markdown files in .rst, use mdinclude for this, choosing this over m2r because m2r is not supported anymore
              'nbsphinx', # support for Jupyter notebooks (STAR)
              'nbsphinx_link'] # include notebook files from outside sphinx src root (STAR)]

# set parameter to read Google docstring and not NumPy
# redundant to add since it's default True but good to know
napoleon_google_docstring = True

# contains list of modules to be marked up
# will ensure 'clean' imports of all the following libraries
# I imagine mibidata will be a problem we'll have to address in the future...
autodoc_mock_imports = ['h5py'
                        'matplotlib',
                        'mibidata',
                        'numpy',
                        'pandas',
                        'skimage',
                        'sklearn',
                        'scipy',
                        'seaborn',
                        'statsmodels',
                        'tables',
                        'umap-learn',
                        'xarray']

# prefix each section label with the name of the document it is in, followed by a colon
# autosection_label_prefix_document = True
autosectionlabel_prefix_document = True

# what role to use for text marked up like `...`, for example this will allow you to parse `filter  ` as a cross-reference to Python function 'filter'
default_role = 'py:obj'

# use recommonmark's CommonMarkParser to parse markdown
# might be unnecessary with m2r2 but we'll see
source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}

# which types of file extensions we want to support
# need .rst for index.rst, and also .md for Markdown
source_suffix = ['.rst', '.md']

# the path to the 'master' document, which in our case, is just index.rst
# not really needed because this is the default value, but still useful to know
master_doc = 'index'

# the language we are writing the documentation in
language = 'en'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# don't allow nbsphinx to run notebooks
nbsphinx_execute = 'never'

# custom 'stuff' we want to ignore in nitpicky mode
# currently empty, I don't think we'll ever run in this
# but if we do we might consider adding
nitpick_ignore = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']