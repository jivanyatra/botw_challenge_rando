from setuptools import setup

setup(
    name='botw_rando_gen',
    version='0.2.0',
    py_modules=['botw_rando_gen'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'botw_rando_gen = botw_rando_gen:botw_rando_gen',
        ],
    },
)