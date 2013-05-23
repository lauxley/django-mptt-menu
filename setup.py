"""Setup script for django_mptt_menu"""
from setuptools import setup
from setuptools import find_packages


setup(
    name='django_mptt_menu',
    version='0.1',
    packages=find_packages(exclude=['test', 'tests',
                                    'example', 'demo']),
    include_package_data=True,
    license='BSD License',
    description='Lightweight and modular menu manager using mptt for the Django framework.',
    long_description=open('README.md').read(),
    author='Djaz Team',
    author_email='devweb@liberation.fr',
    url='http://www.liberation.fr/',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ])
include README.md
include LICENSE.txt
recursive-include docs *
recursive-include build/fixtures *.json
recursive-include build/locale *
recursive-include build/static *
recursive-include build/templates *.txt *.html *.xml *.js
prune docs/build
"""Setup script for django_mptt_menu"""
from setuptools import setup
from setuptools import find_packages


setup(
    name='django_mptt_menu',
    version='0.1',
    packages=find_packages(exclude=['test', 'tests',
                                    'example', 'demo']),
    include_package_data=True,
    license='BSD License',
    description='Lightweight and modular menu manager using mptt for the Django framework.',
    long_description=open('README.md').read(),
    author='Djaz Team',
    author_email='devweb@liberation.fr',
    url='http://www.liberation.fr/',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ])
