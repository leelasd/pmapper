import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="pmapper",
    version="0.2",
    author="Pavel Polishchuk",
    author_email="pavel_polishchuk@ukr.net",
    description="pmapper: 3D pharmacophore hashes and fingerprints",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrrDom/pmapper",
    packages=['pmapper'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry"
    ],
    python_requires='>=3.6',
    extras_require={
        'rdkit': ['rdkit>=2017.09'],
        'networkx': ['networkx>=1.11'],
    },
    entry_points={'console_scripts':
                      ['get_pharm_counts = pmapper.get_pharm_counts:entry_point']},
    include_package_data=True
)
