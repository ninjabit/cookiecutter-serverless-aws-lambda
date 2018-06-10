"""Tests for `{{ cookiecutter.project_slug }}` package."""

from {{ cookiecutter.lambda_name }}.main import say_hello

def test_say_hello():
    """Test something."""
    assert say_hello() == "Hello World!"

def test_something_else():
    """Test something."""
    assert 1 == 1
