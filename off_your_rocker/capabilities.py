import os
from rocker.extensions import RockerExtension


class CapAdd(RockerExtension):

    name = 'oyr_cap_add'

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
        for cap in cli_args['oyr_cap_add']:
            args.append('--cap-add ' + cap)
        return ' '.join(args)

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('--oyr-cap-add',
            metavar='CAPABILITY',
            type=str,
            nargs=1,
            help='add linux capabilities to container')


class CapDrop(RockerExtension):

    name = 'oyr_cap_drop'

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
        for cap in cli_args['oyr_cap_drop']:
            args.append('--cap-drop ' + cap)
        return ' '.join(args)

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('--oyr-cap-drop',
            metavar='CAPABILITY',
            type=str,
            nargs=1,
            help='remove linux capabilities from container')
