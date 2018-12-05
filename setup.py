from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='mdx_poetic',
    author='Nick Wynja',
    description='Formats poetry in Markdown',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/nickwynja/mdx_poetic',
    version='0.6',
    py_modules=['mdx_poetic'],
    install_requires = ['markdown>=2.5'],
)
