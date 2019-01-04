import em
import os
import pkgutil
from rocker.extensions import RockerExtension


class SpaceNav(RockerExtension):

    name = 'oyr_spacenav'

    @classmethod
    def get_name(cls):
        return cls.name

    def precondition_environment(self, cli_args):
        pass

    def get_preamble(self, cli_args):
        return ''

    def get_snippet(self, cli_args):
        snippet = pkgutil.get_data(
            'off_your_rocker',
            'templates/spacenav_snippet.Dockerfile.em').decode('utf-8')
        return em.expand(snippet)

    def get_docker_args(self, cli_args):
        if os.path.exists('/var/run/spnav.sock'):
            return ' -v /var/run/spnav.sock:/var/run/spnav.sock'
        return ''

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('--oyr-spacenav',
            action='store_true',
            help='enable 3Dconnexion SpaceNavigator in container')
