from setuptools import setup

with open("README.rst", "r") as fin:
    long_description = fin.read()

setup(
    name='off-your-rocker',
    version='0.1.0',
    packages=['off_your_rocker'],
    package_data={'off_your_rocker': ['templates/*.em']},
    author='Shane Loretz',
    author_email='shane.loretz@gmail.com',
    description='Extra plugins for rocker',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/sloretz/off-your-rocker",
    license='Apache 2.0',
    install_requires=[
        'rocker',
    ],
    entry_points={
        'rocker.extensions': [
            'oyr_colcon = off_your_rocker.colcon:Colcon',
            'oyr_spacenav = off_your_rocker.spacenav:SpaceNav',
            'oyr_mount = off_your_rocker.mount:Mount',
            'oyr_cap_add = off_your_rocker.capabilities:CapAdd',
            'oyr_cap_drop = off_your_rocker.capabilities:CapDrop',
            'oyr_run_arg = off_your_rocker.run_arg:RunArg',
        ]
    }
)
