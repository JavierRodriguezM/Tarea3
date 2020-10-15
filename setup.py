import setuptools

setuptools.setup(
    name="Tarea3",
    version="0.0.1",

    # Packages and executables
    # All python packages will be located under the lib folder
    # This is not a requirement but allows a better order
    package_dir={'': 'lib'},
    packages=setuptools.find_packages('lib'),

    # Scripts are located under the bin directory
    scripts=['bin/Tarea3'],

    # Dependencies
    #install_requires=find_requirements('requirements.txt'),

    # Metadata
    #author="Rodolfo Piedra Camacho",
    #author_email="rjpiedra@itcr.ac.cr",
    #description="Image Creator package",
    #long_description=long_description,

    url="https://github.com/JavierRodriguezM/Tarea3",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers'
    ],
    python_requires='>=3.5',
)
