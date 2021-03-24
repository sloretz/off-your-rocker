import os
from rocker.extensions import RockerExtension


class Mount(RockerExtension):

    name = 'oyr_mount'

    @classmethod
    def get_name(cls):
        return cls.name

    def precondition_environment(self, cli_args):
        pass

    def validate_environment(self, cli_args):
        pass

    def get_preamble(self, cli_args):
        return ''

    def get_snippet(self, cli_args):
        return ''

    def get_docker_args(self, cli_args):
        args = ['']
        for mount in cli_args['oyr_mount']:
            mount_args = mount.split(':')
            if len(mount_args) == 1:
                src_and_dst, = mount_args
                arg = '{0}:{0}'.format(os.path.abspath(src_and_dst))
            elif len(mount_args) == 2:
                src, dst = mount_args
                arg = '{src}:{dst}'.format(src=src, dst=dst)
            elif len(mount_args) == 3:
                src, dst, permissions = mount_args
                arg = '{src}:{dst}:{permissions}'.format(
                    src=src, dst=dst, permissions=permissions)
            else:
                raise ValueError("Invalid mount string: '{0}'".format(mount))
            args.append('-v {0}'.format(arg))
        return ' '.join(args)

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('--oyr-mount',
            metavar='PATH',
            type=str,
            nargs='+',
            help='mount volumes in container')