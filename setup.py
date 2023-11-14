from setuptools import setup, find_packages

setup(
    name='bet_optimizer',  # Name of package
    version='0.0.1',  # Version number
    packages=find_packages(),  # List of all Python modules to be installed
    description='Python script for optimizing bets',  # Short description of library
    long_description=open('README.md').read(),  # Long description read from the the readme file
    long_description_content_type='text/markdown',  # Type of the long description
    url='https://github.com/subodh101/bet_optimizer',  # Link to your github repository or project on another platform
    author='Subodh Pushkar',  # name
    author_email='subodh.pushkar@gmail.com',  # email
    license='Apache License',  # license
    install_requires=[],  # List of dependencies
    python_requires='>=3.6',  # Minimum version requirement of Python
    py_modules=['bet_optimizer'],  # Name of the python file you want to install
    classifiers=[
        # Trove classifiers
        # Full list available at https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
    ],
)
