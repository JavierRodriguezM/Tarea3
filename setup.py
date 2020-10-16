from setuptools import setup, find_packages

setup(
    name='Tarea3',
    version='0.0.1',
    description='Paquete de metodos para la tarea3',
    url='https://github.com/JavierRodriguezM/Tarea3',
    author='Javier Rodriguez',
    author_email='javirodriguez97@gmail.com',
    license='unlicense',
    #package_dir={'':'Tarea3'},
    packages=find_packages(),
    scripts=['imagen'],
    zip_safe=False
)
