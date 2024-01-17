import setuptools
setuptools.setup(
    name="logs_reader",
    version="0.0.1",
    author="Team",
    author_email="something@email.com",
    description="Package to read a log file",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)