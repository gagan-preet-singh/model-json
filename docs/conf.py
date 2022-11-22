"""Sphinx configuration."""
project = "Model Json"
author = "Gagan Preet Singh"
copyright = "2022, Gagan Preet Singh"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
