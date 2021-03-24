===============
Off Your Rocker
===============

This adds extensions for `tfoote/rocker <https://github.com/tfoote/rocker>`_.

Extensions
^^^^^^^^^^

Mount
:::::

This mounts paths as docker volumes.
Multiple paths may be passed.
The last path must be terminated with two slashes -- before the image name.
You can either pass a path directly (without colons) and the path used inside the container is the same as the path outside the container.
For example:

::

    rocker --oyr-mount ~/.vimrc ~/.bashrc -- ubuntu:18.04

Or use the colon syntax for ``Docker volumes <https://docs.docker.com/storage/volumes/#choose-the--v-or---mount-flag>``_.
This includes the ability to specify comma separated options, such as ``ro`` for readonly.
This syntax supports the use of named volumes, which must first be created (for example, with ``docker volume create``)

::

    # docker volume create my_volume
    rocker --oyr-mount ~/.bashrc:/root/.bashrc ~/.vimrc:/root/.vimrc:ro my_volume:/root/my_volume -- ubuntu:18.04

Colcon
::::::

This adds `colcon <https://colcon.readthedocs.io>`_ to the docker image.

::

    rocker --oyr-colcon ubuntu:18.04

Spacenav
::::::::
This adds support for a 3Dconnexion SpaceNavigator and allows the docker container to use it.

::

    rocker --oyr-spacenav ubuntu:18.04

Capabilities
::::::::::::
Two plugins add support for adding or droping runtime linux capabilities.
For more information see [docker run --cap-add and --cap-drop documentation](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities).

::

    rocker --oyr-cap-add SYS_PTRACE --ory-cap-drop ALL ubuntu:18.04

Docker Run args
:::::::::::::::
This allows adding arbitray arguments to docker run.

::

    rocker --oyr-run-arg " --label foo=bar" ubuntu:18.04