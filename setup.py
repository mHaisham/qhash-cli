from setuptools import setup

setup(
    name='qhash',
    version='0.1.0',
    packages=['qhash'],
    entry_points={
        'console_scripts': [
            'qhash=qhash.__main__:app'
        ]
    })
