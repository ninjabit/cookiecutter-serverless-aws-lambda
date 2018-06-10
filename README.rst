================================================
Cookiecutter Python AWS Lambda with Serverless
================================================

Cookiecutter_ template for a Python AWS Lambda with Serverless_, Pipenv_ etc..

It is based on Andrew Elgert's cookiecutter_pipenv_ project.

* GitHub repo: https://github.com/hypoport/cookiecutter-serverless-aws-lambda/

Why Pipenv?
-----------

Packaging in Python can be a pain, but it doesn't need to be. The new Pipenv project
has rapidly improved packaging in Python by tackling two related problems: automatic
package dependency management and virtualenv management. Pipenv uses the new Pipfile_
format that is the endorsed replacement for `requirements.txt`. Pipenv is the future of
Python package management in *application development*, and is even recommended to newcomers in the Python tutorial_.

Features
--------

* Testing setup with ``python setup.py test`` or ``py.test``
* Tox_ testing: Setup to easily test for Python multiple Python versions
* Bumpversion_: Pre-configured version bumping with a single command (e.g. :code:`bumpversion minor`)

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Pipenv: https://docs.pipenv.org/
.. _Serverless: https://serverless.com/framework/docs/
.. _Pipfile: https://github.com/pypa/pipfile
.. _tutorial: https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Install the latest Pipenv::

    pip install -U pipenv

Generate a Python project that uses Pipenv::

    cookiecutter gh:hypoport/cookiecutter-serverless-aws-lambda

Once your project has been created, change directories::

    cd <project-name>


**Then:**

* Create a repo and put it there (e.g. ``git init``).
* Setup the project (``make setup``).
* Deploy your serverless AWS service (``make deploy [STAGE]``).

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This project itself is a fork of Andrew Elgert cookiecutter_pipenv_, which is itself based on Audrey Roy Greenfeld's
cookiecutter-pypackage_. If you have differences in your preferred setup, I encourage you to fork this to create your
own version. Or create your own; it doesn't strictly have to be a fork.

.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
.. _cookiecutter_pipenv: https://github.com/elgertam/cookiecutter-pipenv

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I will consider pull requests as they come in, if they enhance the overall packaging experience.

.. _Tox: http://testrun.org/tox/
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _PyPi: https://pypi.org/
