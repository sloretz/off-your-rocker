from setuptools import setup

setup(
    name='off-your-rocker',
    version='0.1.0',
    packages=['off_your_rocker'],
    package_data={'off_your_rocker': ['templates/*.em']},
    author='Shane Loretz',
    author_email='shane.loretz@gmail.com',
    description='Plugins for rocker that I find useful',
    license='Apache 2.0',
    install_requires=[
        # 'git+https://github.com/tfoote/rocker.git',
    ],
    entry_points={
        'rocker.extensions': [
            'oyr_colcon = off_your_rocker.colcon:Colcon',
            'oyr_spacenav = off_your_rocker.spacenav:SpaceNav',
            'oyr_mount = off_your_rocker.mount:Mount',
            'oyr_cap_add = off_your_rocker.capabilities:CapAdd',
            'oyr_cap_drop = off_your_rocker.capabilities:CapDrop',
        ]
    }
)
