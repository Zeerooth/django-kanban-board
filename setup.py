
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='django-kanban-board',
    version='0.0.1',
    description='Package providing models and views for displaying customizable kanban-like boards',
    python_requires='==3.*,>=3.6.0',
    project_urls={"homepage": "https://github.com/Zeerooth/django-kanban-board", "repository": "https://github.com/Zeerooth/django-kanban-board"},
    author='Radosław Stępień',
    author_email='rstepien@protonmail.com',
    license='BSD',
    keywords='django',
    packages=['kanban_board', 'kanban_board.migrations'],
    package_dir={"": "."},
    package_data={"kanban_board": ["static/kanban_board/css/*.css", "static/kanban_board/js/*.js", "templates/kanban_board/*.html"]},
    install_requires=['django<3.2,>=2.0', 'django-gm2m==1.*,>=1.0.0', 'django-model-utils==4.*,>=4.0.0', 'django-ordered-model==3.*,>=3.4.1', 'django-simple-history==2.*,>=2.11.0', 'toml==0.*,>=0.9.0'],
    extras_require={"dev": ["bandit==1.*,>=1.6.2", "dephell==0.*,>=0.8.3", "mypy==0.*,>=0.782.0", "pylint==2.*,>=2.5.3", "pytest==3.*,>=3.0.0", "pytest-cov==2.*,>=2.4.0"]},
)
