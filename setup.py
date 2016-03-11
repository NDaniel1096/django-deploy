#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import deployment

setup(
    name='django-deployment',
    version=deployment.get_version(),
    description="Create the correct files to support deployment under apache.",
    long_description=open('README.rst', 'r').read(),
    keywords='django, security, authentication',
    author='Nick Daniel',
    author_email='ndaniel@nimdapro.com',
    url='http://github.com/NDaniel1096/django-deployment/',
    license='MIT',
    package_dir={'deployment': 'deployment'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: Deployment',
    ],
    zip_safe=False,
)
