"""Sphinx configuration."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join('..', '..')))

# -- General configuration ---------------------------------------------
extensions = [
	'sphinx.ext.autodoc',
	'sphinx_autodoc_typehints',
	'sphinx.ext.doctest',
	'sphinx.ext.intersphinx',
	'sphinx.ext.todo',
	'sphinx.ext.coverage',
	'sphinx.ext.viewcode',
	'myst_parser',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = 'e-lims-cookiecutter-template'
package = 'e_lims_cookiecutter_template'
author = 'Fabien Meyer'
copyright = '2024, {}'.format(author)
version = '0.3.0'
release = '{ cookiecutter.version }}'
language = 'en'
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True


# -- Options for HTML output -------------------------------------------
html_theme = 'sphinx_rtd_theme'

# -- Options for HTMLHelp output ---------------------------------------
htmlhelp_basename = 'e_lims_cookiecutter_templatedoc'

# -- Options for LaTeX output ------------------------------------------
latex_elements = {}

latex_documents = [
    (master_doc, 'e_lims_cookiecutter_template.tex',
     '{} Documentation'.format(project),
     author, 'manual'),
]


# -- Options for manual page output ------------------------------------
man_pages = [
    (master_doc, 'e_lims_cookiecutter_template',
     '{} Documentation'.format(project),
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------
texinfo_documents = [
    (master_doc, 'e_lims_cookiecutter_template',
     '{} Documentation'.format(project),
     author,
     'e_lims_cookiecutter_template',
     """E-lims Cookiecutter Template.""",
     'Miscellaneous'),
]

intersphinx_mapping = {'python': ('https://docs.python.org/3/', None)}
set_type_checking_flag = True
always_document_param_types = True
