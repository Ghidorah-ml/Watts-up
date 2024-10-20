from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

setup(
    name="Watts-up",
    version="0.0.1",
    description="An Open-Source Tool for Machine Learning on Battery "EOL",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ghidorah",
    url="https://github.com/Ghidorah-ml/Watts-up",
    packages=find_packages(exclude=['scripts']),
    install_requires=required_packages,
    # Addressing the Windows usage issue
    # See https://github.com/microsoft/BatteryML/issues/21
    entry_points={
        'console_scripts': [
            'batteryml=bin.batteryml:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
)
