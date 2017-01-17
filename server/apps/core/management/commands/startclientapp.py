import os
from importlib import import_module

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


def try_import_app(app_name):
    try:
        import_module('apps.{}'.format(app_name))
    except ImportError:
        message = "The application '{}' doesn't exist"
        message = message.format(app_name)
        raise CommandError(message)


def check_existence_of_client_dir(app_name):
    app_dir = os.path.join(settings.CLIENT_APPS_DIR, app_name)

    if os.path.exists(app_dir):
        message = "The client directory for '{}' already exists"
        message = message.format(app_name)
        raise CommandError(message)


def get_directories_map(app_name):
    directories_map = {
        app_name: {
            'static': {
                app_name: {
                    'js': '{}.js'.format(app_name),
                    'styles': '{}.scss'.format(app_name),
                    'images': None,
                }
            },
            'templates': {
                app_name: None
            },
        }
    }

    return directories_map


def make_file(path):
    open(path, 'a').close()


def make_directories(directories_map, current_dir='/'):
    client_apps_dir = settings.CLIENT_APPS_DIR + current_dir

    for k, v in directories_map.items():
        if isinstance(v, dict):
            os.makedirs(os.path.join(client_apps_dir, k))
            make_directories(v, os.path.join(current_dir, k))
        else:
            os.makedirs(os.path.join(client_apps_dir, k))

            if directories_map[k]:
                path = os.path.join(os.path.join(client_apps_dir, k), v)
                make_file(path)


def show_final_message(self, app_name):
    message = "Successfully created the client directory for application '{}'"
    message = message.format(app_name)
    self.stdout.write(self.style.SUCCESS(message))


class Command(BaseCommand):
    help = 'Creating client directories for applications'

    def add_arguments(self, parser):
        parser.add_argument('app_name', action='store')

    def handle(self, *args, **options):
        app_name = options['app_name']
        try_import_app(app_name)
        check_existence_of_client_dir(app_name)
        make_directories(get_directories_map(app_name))
        show_final_message(self, app_name)
