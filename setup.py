
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
    install_requires = ['argparse'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
