#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='mongo_beaker',
    version='0.2.2',
    description='Beaker backend to write sessions and caches to a MongoDB database.',
    long_description='\n',
    author='Chris Conlin',
    author_email='c.conlin@gmail.com',
    keywords='mongo mongodb beaker cache session',
    license='MIT License',
    url='http://github.com/spongin/mongo_beaker',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    entry_points="""
    [beaker.backends]
    mongo = mongo_beaker:MongoNamespaceManager
    """,
    install_requires = [
        'pymongo>=2.4.1',
        'beaker>=1.4'
    ]
)
