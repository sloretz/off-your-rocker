import os
from rocker.extensions import RockerExtension


class RunArg(RockerExtension):

    name = 'oyr_run_arg'

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
        for arg in cli_args['oyr_run_arg']:
            args.append(arg)
        return ' '.join(args)

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('--oyr-run-arg',
            metavar='DOCKER_RUN_ARG',
            type=str,
            nargs=1,
            help='add docker run arguments to container')
