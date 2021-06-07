from setuptools import setup

setup(
    name='cheddar',
    packages=['cheddar'],
    include_package_data=True,
    install_requires=[
        'flask',
        'chess',
        'flask-socketio'
    ],
)
