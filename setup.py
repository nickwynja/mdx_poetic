from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mdx_poetic',
    author='Nick Wynja',
    description='Formats poetry in Markdown',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nickwynja/mdx_poetic',
    version='0.2',
    py_modules=['mdx_poetic'],
    install_requires = ['markdown>=2.5'],
)
