from setuptools import setup, find_packages

setup(
    name='Bosa-bot',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'discord.py'
    ],
    entry_points={
        'console_scripts': [
            'bosa = cliweather.main:cli',
        ],
    },
)
