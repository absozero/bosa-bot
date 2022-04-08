from setuptools import setup, find_packages

setup(
    name='Bosa-bot',
    version='0.1.0',
    packages=find_packages(include=['bosa_bot', 'bosa_bot.*']),
    include_package_data=True,
    install_requires=[
        'typer',
        'discord.py'
    ],
    entry_points={
        'console_scripts': [
            'bosa = bosa_bot.main:main',
        ],
    },
)
