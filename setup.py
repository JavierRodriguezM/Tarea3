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
    packages=['Tarea3'],
    #scripts=['Tarea3/imagen.py', 'Tarea3/audio.py','Tarea3/texto.py'],
    entry_points = {
        'console_scripts': ['imagen = Tarea3.imagen:main'],
        #'console_scripts': ['audio = Tarea3.audio:main'],
        #'console_scripts': ['texto = Tarea3.texto:main'],
    },
    zip_safe=False
)
