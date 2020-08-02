from setuptools import setup, Extension, find_packages

URL = 'https://github.com/matham/cython_demo_project'

setup(
    name='cython_demo_project',
    version='0',
    description='A simple Cython demo project with GitHub CI.',
    url=URL,
    author='Matthew Einhorn',
    author_email='moiein2000@gmail.com',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'dev': ['pytest>=3.6', 'wheel'],
    },
    data_files=[],
    entry_points={},
    ext_modules=[Extension(
        'cython_demo_project.numeric',
        sources=['cython_demo_project/numeric.c']
    )],
    project_urls={
        'Bug Reports': URL + '/issues',
        'Source': URL,
    },
)
