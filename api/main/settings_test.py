# -*- coding: utf-8 -*-
from main.settings import *

INSTALLED_APPS += (
    'django_jenkins',
)

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.run_flake8',
)

# Application definition
PROJECT_APPS = [
]

JENKINS_TEST_RUNNER = 'django_jenkins.runner.CITestSuiteRunner'
