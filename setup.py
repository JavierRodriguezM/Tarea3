<<<<<<< Updated upstream

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Tarea3", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="Paquete de metodos para la tarea3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JavierRodriguezM/Tarea3.git",
    packages=setuptools.find_packages(),
    license='MIT'
    install_requires=['argparse', 'cv2', 'playsound', 'tabulate'],
    scripts=['imagen.py', 'audio.py', 'texto.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
=======
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
>>>>>>> Stashed changes
)
