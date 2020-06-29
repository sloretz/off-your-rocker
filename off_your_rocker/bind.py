import os
from rocker.extensions import RockerExtension


class Bind(RockerExtension):

    name = 'oyr_bind'

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
        print(cli_args)
        for mount in cli_args['oyr_bind']:
            for d in mount.split(" "):
                if ":" in d:
                    src,dst = d.split(":")
                else:
                    src = d
                    dst = d
                src = os.path.abspath(src)
                args.append(f'--mount type=bind,source={src},target={dst}')
        return ' '.join(args)

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('--oyr-bind',
            metavar='PATH',
            type=str,
            nargs='+',
            help='mount local foldrs to arbitrary folders in container. Sintax: /host_path[:/container_path]. If container path is not given, same path will be used. Multiple directories can be separated by space.')
