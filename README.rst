===============
Off Your Rocker
===============

This adds extensions for `tfoote/rocker<https://github.com/tfoote/rocker>`_.

Extensions
^^^^^^^^^^

Mount
:::::

This mounts paths as docker volumes.
The path used inside the container is the same as the path outside the container.
Multiple paths may be passed.
The last path must be terminated with two slashes -- before the image name.

::

    rocker --oyr-mount ~/.vimrc ~/.bashrc -- ubuntu:18.04

Colcon
::::::

This adds `colcon<https://colcon.readthedocs.io>`_ to the docker image.

::

    rocker --oyr-colcon -- ubuntu:18.04

Spacenav
::::::::
This adds support for a 3Dconnexion SpaceNavigator and allows the docker container to use it.

::

    rocker --oyr-spacenav -- ubuntu:18.04
