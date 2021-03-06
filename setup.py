# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='migrate-go2z',
    version='0.9.5',
    url='',
    license='',
    author='Etienne Gille',
    author_email='etienne.gille@ville-acigne.fr',
    description='',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'migratego2z=__main__:main'
        ]
    },
    install_requires=['sqlalchemy', 'vobject']  # ,
    # data_files=[('/etc/migratego2z', ['migratego2z.ini'])]

)
