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
            mount = os.path.abspath(mount)
            args.append('-v {0}:{0}'.format(mount))
        return ' '.join(args)

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('--oyr-mount',
            metavar='PATH',
            type=str,
            nargs='+',
            help='mount volumes in container')