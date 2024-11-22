from setuptools import find_packages, setup

setup(
    name="metricus",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    description="This Python-based unit converter is a simple and efficient tool for converting measurements between units like meters, kilometers, centimeters, and millimeters. It returns precise results formatted with or without the unit abbreviation for easy readability.",
    author="Guilherme Freschi, Yaron Buchler",
    author_email="guilhermefreschix@gmail.com, buchleryaron@gmail.com",
    url="https://github.com/guifreschi/Metricus",
    project_urls={
        "Yaron Buchler's GitHub": "https://github.com/YaronBuchler",
        "Guilherme Freschi's GitHub": "https://github.com/guifreschi",
        "Project on GitHub": "https://github.com/guifreschi/Metricus",
    },
    license="MIT",
    keywords="conversion, units, temperature, weight, length, distance, energy, volume, mass, pressure, speed, time, metric, imperial, unit converter...",
)
