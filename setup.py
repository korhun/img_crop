from setuptools import setup

setup(
    name='img_crop',
    version='0.1',
    packages=[''],
    url='https://github.com/korhun/img_crop',
    license='',
    author='Orientis',
    author_email='korhun@gmail.com',
    description='',
    install_requires= [
        "PyYAML~=5.4.1",
        "matplotlib<3.3",  # for PyInstaller
        "opencv-python~=4.3.0.36"
    ]
)
