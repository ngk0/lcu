from setuptools import setup, find_packages

setup(
    name='laporte_cars_utility',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pyqt6',
        'pyodbc',
        'openpyxl'
    ],
    entry_points={
        'console_scripts': [
            'laporte-cars = gui.main_window:main',
        ]
    },
)
