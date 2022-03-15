from setuptools import setup

setup(
    name = "aitime",
    version = "0.1.0",
    description = "Prints current time",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/aitime",
    packages = ["ukraine"],
    entry_points = {
        'console_scripts': [
            'aitime = aitime.__main__:main'
        ]
    },
)
