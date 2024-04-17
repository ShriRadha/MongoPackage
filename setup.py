from setuptools import setup, find_packages

setup(
    name='mongodb_package',
    version='0.1.0',
    author='Shriharran',
    author_email='shriharran.radhakrishnan@digit7.ai',
    packages=find_packages(),
    install_requires=[
        'pymongo>=3.10',
        'dnspython>=1.16.0',
    ],
    python_requires='>=3.6',
    description='A MongoDB client package for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)