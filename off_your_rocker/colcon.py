import em
import pkgutil
from rocker.extensions import RockerExtension


class Colcon(RockerExtension):

    name = 'oyr_colcon'

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
        snippet = pkgutil.get_data(
            'off_your_rocker',
            'templates/colcon_snippet.Dockerfile.em').decode('utf-8')
        return em.expand(snippet)

    def get_docker_args(self, cli_args):
        return ''

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('--oyr-colcon',
            action='store_true',
            help='install colcon with some useful extensions')