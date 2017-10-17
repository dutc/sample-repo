from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from os.path import join, dirname
from sys import version_info, exit
from pip.req import parse_requirements

if version_info.major < 3 or version_info.minor < 6:
    exit("Sorry, Python 3.6 or above only")

requires = [str(x.req) for x in parse_requirements('requirements.txt', session='hack')]

class Test(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        super().initialize_options()
        self.pytest_args = []

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        exit(errno)

setup(
    name='sample-repo',
    version='0.0.1',
    description='Sample Repo',
    long_description=''.join(open(join(dirname(__file__),'README.md'))),
    author='James Powell',
    author_email='james@dontusethiscode.com',
    url='https://github.com/dutc/sample-repo',
    packages=find_packages(exclude=['*demos*']),
    install_requires=requires,
    cmdclass={'test': Test},
)
