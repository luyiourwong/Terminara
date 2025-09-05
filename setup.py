from setuptools import setup, find_packages

setup(
    name="terminara",
    version="0.1.0",
    description="Terminal-based adventure game",
    author="Lu Yiou Rwong",
    author_email="35396353+luyiourwong@users.noreply.github.com",
    packages=find_packages(),
    install_requires=[
        "textual",
    ],
    entry_points={
        'console_scripts': [
            'terminara=terminara.main:main',
        ],
    },
    python_requires='>=3.13',
)