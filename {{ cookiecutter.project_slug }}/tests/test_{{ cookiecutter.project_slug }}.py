from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}

import pytest


def test_{{ cookiecutter.project_slug }}():
    assert {{ cookiecutter.project_slug }}() == "Hello World!"
