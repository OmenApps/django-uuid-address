import os
import sys

from setuptools import find_packages, setup

version = '0.2.3'

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

setup(
    name='django-uuid-address',
    version=version,
    author='Luke Hodkinson, Jack Linke',
    author_email='furious.luke@gmail.com',
    maintainer='Luke Hodkinson',
    maintainer_email='furious.luke@gmail.com',
    url='https://github.com/OmenApps/django-uuid-address',
    description='A django application for describing addresses. Forked and modified to use UUIDs.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    license='BSD',

    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.txt', '*.js', '*.html', '*.*']},
    install_requires=['setuptools'],
    zip_safe=False,

)
