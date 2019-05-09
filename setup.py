from setuptools import setup, find_packages

long_desc = '''
This package is a sample recipe domain for Sphinx, demonstrating
how to use custom indices.
See https://github.com/ofosos/sphinxrecipes.
'''

requires = ['Sphinx>=0.6',
            'sphinxcontrib-domaintools>=0.1']

setup(
    name='sphinxcontrib-recipes',
    version='0.1',
    url='http://github.com/ofosos/sphinxrecipes',
    download_url='http://pypi.python.org/pypi/sphinxrecipes',
    license='MIT',
    author='Mark Meyer',
    author_email='mark@ofosos.org',
    description='Recipe sample domain for Sphinx',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(exclude=['sample*']),
    include_package_data=False,
    install_requires=requires,
    namespace_packages=['sphinxrecipes']
)
