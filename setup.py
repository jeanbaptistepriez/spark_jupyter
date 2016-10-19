from setuptools import setup, find_packages


setup(
    name='Spark-Jupyter',
    version='1.0.0',
    author_email='jbp@kerios.fr',
    long_description=open('README.md').read(),
    packages=find_packages(),
    scripts = [],
    description = 'This library customizes some DataFrame output',
    install_requires=[]
)