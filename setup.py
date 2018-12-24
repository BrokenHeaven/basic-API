from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='elex',
    version='0.1.0',
    description='To be added',
    long_description_content_type='text/markdown',
    url='noURL',
    author='Mirko Muscará',
    author_email='mrkmuscara@gmail.com',
    classifiers=[
        'Development status :: 1 - Alpha',
        'Intended audience :: Private',
        'Programming language :: Python :: 3.6'
    ],
    keywords='elex',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests', 'request_kerberos', 'winkerberos', 'pandas', 'pytz']
)
