"""Tests for `{{ cookiecutter.project_slug }}` package."""

from unittest import TestCase

from {{ cookiecutter.lambda_name }} import {{ cookiecutter.lambda_name }}


class Test{{ cookiecutter.project_slug|title }}(TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
        self.fail()
