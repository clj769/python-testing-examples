from setuptools import setup, find_packages

import agecalc


install_requires = []


setup(
    name='agecalc',
    version=agecalc.__version__,
    description=agecalc.__doc__.strip(),
    license=agecalc.__licence__,
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[ 
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)