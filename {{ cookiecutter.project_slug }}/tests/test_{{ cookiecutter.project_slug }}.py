from {{ cookiecutter.project_slug }} import __version__
from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}

import pytest


def test_{{ cookiecutter.project_slug }}():
    assert {{ cookiecutter.project_slug }}() == "Hello World!"

def test__version__():
    assert __version__ == "0.0.1"
