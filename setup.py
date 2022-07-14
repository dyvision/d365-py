from setuptools import setup

setup(
    name='d365',
    version='0.0.1',    
    description='A python library to make Dynamics 365 authentication easier',
    url='https://github.com/dyvision/d365-py',
    author='Dyvision',
    author_email='the.dyvision@gmail.com',
    license='',
    packages=['d365'],
    install_requires=['requests'],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)