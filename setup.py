import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quantum-annealing-sudoku-solver", # Replace with your own username
    version="0.0.1",
    author="Juju Athlete",
    author_email="vimengine@tutanota.com",
    description="A Quantum Annealing Sudoku solver.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ju2ez/quantum_annealing_sudoku",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License NO LICENSE YET",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    tests_require = [
    'pytest >= 3.7.4',
    'pytest-cov'
]
     extras_require={
        'testing': tests_require,
    },


)
