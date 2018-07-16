{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
[![](https://img.shields.io/pypi/v/{{ cookiecutter.project_directory }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_directory }})

[![](https://img.shields.io/travis/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.project_directory }}.svg)](https://travis-ci.org/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.project_directory }})

[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_directory | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_directory | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest)
{%- endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_directory | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
-------

This software was created with [Cookiecutter] and the [`hypoport/cookiecutter-serverless-aws-lambda`], based on 
[`elgertam/cookiecutter-pipenv`] and [`audreyr/cookiecutter-pypackage`].

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[`hypoport/cookiecutter-serverless-aws-lambda`]: https://github.com/hypoport/cookiecutter-serverless-aws-lambda
[`elgertam/cookiecutter-pipenv`]: https://github.com/elgertam/cookiecutter-pipenv
[`audreyr/cookiecutter-pypackage`]: https://github.com/audreyr/cookiecutter-pypackage
