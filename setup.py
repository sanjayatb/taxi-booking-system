#!/usr/bin/env python3

from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='super-taxi',
    version='0.0.1',
    description='Simple taxi booking api',
    author='Sanjaya Bandara',
    author_email='arstbandara@gmail.com',
    url='https://github.com/sanjayatb/taxi-booking-system',
    packages=find_packages(),
    keywords=['Taxi', 'booking'],
    package_data={'super_taxi': ['testFiles/test1.html']},
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts' : [
            'taxi-booking-api = __main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
        "Topic :: Internet :: WWW/HTTP",
    ],
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
